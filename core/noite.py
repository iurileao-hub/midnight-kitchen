"""
Noite — Orquestrador de uma noite no Midnight Kitchen.

Coordena diálogo, tempo, cozinha e UI para criar
a experiência completa de uma noite com um cliente.
"""

from dataclasses import dataclass
from typing import Optional

from contracts import TipoInteracao, ResultadoNoite
from core.tempo import SistemaTempo
from core.game import Game
from sistemas.dialogo import SistemaDialogo, ResultadoDialogo
from sistemas.cozinha import SistemaCozinha
from ui.renderer import Renderer


@dataclass
class ResultadoNoiteCompleto:
    """Resultado completo de uma noite."""
    resultado: ResultadoNoite
    memoria: Optional[str] = None
    cliente_nome: str = ""
    prato_servido: Optional[str] = None


class Noite:
    """
    Orquestra uma noite completa com um cliente.

    Gerencia o fluxo entre diálogo, tempo, cozinha,
    e a interface visual.
    """

    def __init__(
        self,
        game: Game,
        renderer: Renderer,
        cliente_id: str,
    ):
        self.game = game
        self.renderer = renderer
        self.cliente_id = cliente_id

        # Inicializa sistemas
        self.dialogo = SistemaDialogo()
        self.cozinha = SistemaCozinha()
        self.tempo: Optional[SistemaTempo] = None

        # Estado da noite
        self._prato_revelado: Optional[str] = None
        self._prato_servido: bool = False
        self._memoria_revelada: Optional[str] = None
        self._encerrado: bool = False
        self._resultado_cozinha: Optional[ResultadoNoiteCompleto] = None

    def iniciar(self) -> bool:
        """
        Inicia a noite.

        Returns:
            True se iniciou com sucesso.
        """
        # Carrega dados do cliente
        if not self.dialogo.carregar_cliente(self.cliente_id):
            return False

        # Inicia noite no game (avança dia e cria sistema de tempo)
        self.game.iniciar_noite(self.cliente_id)
        self.tempo = self.game.tempo

        return True

    def executar(self) -> ResultadoNoiteCompleto:
        """
        Executa o loop principal da noite.

        Returns:
            Resultado completo da noite.
        """
        # Limpa tela e mostra chegada
        self.renderer.limpar()
        self._mostrar_chegada()

        # Loop principal
        while not self._encerrado:
            # Verifica tempo
            if self.tempo and self.tempo.tempo_esgotado():
                return self._encerrar_por_tempo()

            # Mostra status e opções
            self._mostrar_status()
            resultado = self._processar_turno()

            if resultado:
                return resultado

        # Não deveria chegar aqui
        return ResultadoNoiteCompleto(
            resultado=ResultadoNoite.FALHA_CONFIANCA,
            cliente_nome=self.dialogo.cliente_dados.get("nome", ""),
        )

    def _mostrar_chegada(self) -> None:
        """Mostra a cena de chegada do cliente."""
        noite = self.game.noite_atual
        tempo_str = self.tempo.formatar() if self.tempo else ""

        self.renderer.mostrar_narrativa(
            self.dialogo.obter_descricao_chegada(),
            noite=noite,
            tempo=tempo_str,
            digitar=True,
        )
        self.renderer.pausar()

    def _mostrar_status(self) -> None:
        """Mostra o diálogo atual do cliente."""
        self.renderer.limpar()

        nome = self.dialogo.cliente_dados.get("nome", "Cliente")
        nome_japones = self.dialogo.cliente_dados.get("nome_japones", "")
        estado = self.dialogo.obter_estado_emocional().value
        tempo_str = self.tempo.formatar() if self.tempo else ""

        # Contexto do momento (se houver)
        contexto = self.dialogo.obter_contexto()
        if contexto:
            self.renderer.console.print(f"[sutil]{contexto}[/sutil]")
            self.renderer.espaco()

        # Diálogo do cliente (com nome + kanji e cor sutil da borda)
        texto = self.dialogo.obter_texto()
        if texto:
            self.renderer.mostrar_dialogo_cliente(
                nome, texto, estado, tempo_str, nome_japones
            )

    def _processar_turno(self) -> Optional[ResultadoNoiteCompleto]:
        """
        Processa um turno de diálogo.

        Returns:
            Resultado se a noite encerrou, None se continua.
        """
        # Obtém opções
        opcoes = self.dialogo.obter_opcoes()

        if not opcoes:
            # Sem opções = fim do diálogo
            return self._encerrar_dialogo()

        # Prepara opções para menu
        opcoes_menu = [
            (op.texto, op.dica if op.disponivel else "indisponível")
            for op in opcoes
        ]

        # Mostra menu
        self.renderer.espaco()
        escolha = self.renderer.mostrar_menu(
            "O que você diz?",
            opcoes_menu,
            permitir_cancelar=False,
        )

        # Processa escolha
        if escolha == 0:
            return None  # Continua

        # Processa escolha de diálogo
        resultado = self.dialogo.processar_escolha(escolha)
        if resultado:
            self._processar_resultado_dialogo(resultado)

        # Retorna resultado de cozinha se houve (via tipo_cena)
        if self._resultado_cozinha:
            return self._resultado_cozinha

        return None

    def _processar_resultado_dialogo(self, resultado: ResultadoDialogo) -> None:
        """Processa o resultado de uma escolha de diálogo."""
        # Avança tempo
        if self.tempo:
            self.tempo.avancar(resultado.tipo_interacao)

        # Mostra pensamento de Master se houver
        if resultado.pensamento_master:
            self.renderer.mostrar_pensamento(resultado.pensamento_master)

        # Verifica se revelou prato
        if resultado.revelacao_prato:
            self._prato_revelado = resultado.revelacao_prato
            nome_prato = self._obter_nome_prato(resultado.revelacao_prato)
            self.renderer.console.print(
                f"\n[destaque]Você percebe que {nome_prato} seria perfeito agora.[/destaque]"
            )
            self.renderer.pausar()  # Garante que jogador veja a dica antes de continuar

        # Verifica se é cena de cozinha
        if resultado.tipo_cena == "cozinha":
            self._resultado_cozinha = self._executar_cozinha()

    def _executar_cozinha(self) -> Optional[ResultadoNoiteCompleto]:
        """Executa a cena de cozinha."""
        if not self._prato_revelado:
            return None

        prato_id = self._prato_revelado
        nome = self.dialogo.cliente_dados.get("nome", "Cliente")

        # Mostra menu de pratos com descrições culturais
        self.renderer.limpar()
        pratos = self.cozinha.listar_pratos()

        escolha = self.renderer.mostrar_menu_pratos(
            "Qual prato preparar?",
            pratos,
        )

        prato_escolhido = pratos[escolha - 1][0]  # ID do prato

        # Avança tempo para preparação
        if self.tempo:
            tempo_preparo = self.cozinha.obter_tempo_preparo(prato_escolhido)
            self.tempo.avancar(TipoInteracao.COZINHA)

        # Mostra preparação
        self.renderer.transicao()
        narrativa_preparo = self.cozinha.preparar_prato(prato_escolhido)
        if narrativa_preparo:
            self.renderer.mostrar_narrativa(
                narrativa_preparo,
                titulo="Preparação",
                tempo=self.tempo.formatar() if self.tempo else "",
            )
            self.renderer.pausar()

        # Serve o prato
        resultado = self.cozinha.servir_prato(prato_escolhido, self.cliente_id)

        # Mostra narrativa de servir
        self.renderer.transicao()
        self.renderer.mostrar_narrativa(
            resultado.narrativa_servir,
            tempo=self.tempo.formatar() if self.tempo else "",
        )
        self.renderer.pausar()

        # Mostra reação
        self.renderer.mostrar_narrativa(
            resultado.reacao,
            digitar=True,
        )
        self.renderer.pausar()

        self._prato_servido = True

        if resultado.sucesso:
            # Sucesso! Memória revelada
            self._memoria_revelada = resultado.memoria_revelada

            # Mostra despedida de sucesso
            self.renderer.transicao()
            self.renderer.mostrar_narrativa(
                self.dialogo.obter_despedida("sucesso"),
                titulo="Despedida",
            )
            self.renderer.pausar()

            return ResultadoNoiteCompleto(
                resultado=ResultadoNoite.SUCESSO,
                memoria=self._memoria_revelada,
                cliente_nome=nome,
                prato_servido=prato_escolhido,
            )
        else:
            # Prato errado - continua mas dificulta
            return None

    def _encerrar_por_tempo(self) -> ResultadoNoiteCompleto:
        """Encerra a noite porque o tempo esgotou."""
        nome = self.dialogo.cliente_dados.get("nome", "Cliente")

        self.renderer.transicao()
        self.renderer.mostrar_narrativa(
            self.dialogo.obter_despedida("tempo"),
            titulo="O tempo passa...",
        )
        self.renderer.pausar()

        return ResultadoNoiteCompleto(
            resultado=ResultadoNoite.FALHA_TEMPO,
            cliente_nome=nome,
        )

    def _encerrar_dialogo(self) -> ResultadoNoiteCompleto:
        """Encerra quando não há mais opções de diálogo."""
        nome = self.dialogo.cliente_dados.get("nome", "Cliente")

        # Determina tipo de despedida
        if self._memoria_revelada:
            tipo = "sucesso"
            resultado = ResultadoNoite.SUCESSO
        elif self.dialogo.confianca < 20:
            tipo = "falha"
            resultado = ResultadoNoite.FALHA_CONFIANCA
        else:
            tipo = "tempo"
            resultado = ResultadoNoite.PARCIAL

        self.renderer.transicao()
        self.renderer.mostrar_narrativa(
            self.dialogo.obter_despedida(tipo),
            titulo="Despedida",
        )
        self.renderer.pausar()

        return ResultadoNoiteCompleto(
            resultado=resultado,
            memoria=self._memoria_revelada,
            cliente_nome=nome,
        )

    def _obter_nome_prato(self, prato_id: str) -> str:
        """Obtém o nome de um prato pelo ID."""
        prato = self.cozinha.obter_prato(prato_id)
        return prato.nome if prato else prato_id
