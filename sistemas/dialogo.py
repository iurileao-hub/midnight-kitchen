"""
Sistema de Diálogo v2 — Midnight Kitchen.

Gerencia a navegação pela árvore de diálogos,
sistema de confiança, e detecção de pistas.
"""

import json
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional

from config import (
    DIALOGOS_DIR,
    CLIENTES_DIR,
    CONFIANCA_INICIAL,
)
from contracts import (
    TipoInteracao,
    EstadoEmocional,
    DadosCliente,
    NoDialogo,
    OpcaoDialogo,
)


@dataclass
class OpcaoFormatada:
    """Uma opção de diálogo formatada para exibição."""
    indice: int
    texto: str
    dica: str
    disponivel: bool = True


@dataclass
class ResultadoDialogo:
    """Resultado de uma escolha de diálogo."""
    texto_resposta: str
    impacto_confianca: int
    tipo_interacao: TipoInteracao
    proximo_no: Optional[str]
    e_pista: bool = False
    pista_id: Optional[str] = None
    pensamento_master: Optional[str] = None
    gatilho_prato: bool = False
    revelacao_prato: Optional[str] = None
    tipo_cena: Optional[str] = None


class SistemaDialogo:
    """
    Sistema de diálogo baseado em árvore JSON.

    Cada cliente tem sua própria árvore de diálogos,
    com nós, opções, e consequências únicas.
    """

    def __init__(self):
        self._dados_dialogos: dict = {}
        self._dados_clientes: dict = {}
        self._no_atual: Optional[str] = None
        self._cliente_atual: Optional[str] = None
        self._confianca: int = CONFIANCA_INICIAL
        self._pistas_captadas: list[str] = []
        self._historico: list[str] = []

    def carregar_cliente(self, cliente_id: str) -> bool:
        """
        Carrega os dados de diálogo de um cliente.

        Returns:
            True se carregou com sucesso.
        """
        try:
            # Carrega diálogos
            dialogo_path = DIALOGOS_DIR / f"{cliente_id}.json"
            with open(dialogo_path, "r", encoding="utf-8") as f:
                self._dados_dialogos = json.load(f)

            # Carrega dados do cliente
            cliente_path = CLIENTES_DIR / f"{cliente_id}.json"
            with open(cliente_path, "r", encoding="utf-8") as f:
                self._dados_clientes = json.load(f)

            # Inicializa estado
            self._cliente_atual = cliente_id
            self._no_atual = self._dados_dialogos.get("no_inicial", "chegada")
            self._confianca = CONFIANCA_INICIAL
            self._pistas_captadas = []
            self._historico = []

            return True

        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Erro ao carregar cliente {cliente_id}: {e}")
            return False

    def obter_no_atual(self) -> Optional[dict]:
        """Retorna os dados do nó atual."""
        if not self._dados_dialogos or not self._no_atual:
            return None

        nos = self._dados_dialogos.get("nos", {})
        return nos.get(self._no_atual)

    def obter_contexto(self) -> str:
        """Retorna o contexto narrativo do nó atual."""
        no = self.obter_no_atual()
        if no:
            return no.get("contexto", "")
        return ""

    def obter_texto(self) -> str:
        """Retorna o texto de diálogo do nó atual (o que o cliente diz)."""
        no = self.obter_no_atual()
        if no:
            return no.get("texto", "")
        return ""

    def obter_opcoes(self) -> list[OpcaoFormatada]:
        """
        Retorna as opções disponíveis no nó atual.

        Filtra opções que requerem confiança mínima ou pistas específicas.
        """
        no = self.obter_no_atual()
        if not no:
            return []

        opcoes = no.get("opcoes", [])
        resultado = []

        for i, opcao in enumerate(opcoes, 1):
            # Verifica confiança mínima
            confianca_min = opcao.get("confianca_minima", 0)
            disponivel = self._confianca >= confianca_min

            # Verifica se requer pista
            pista_requerida = opcao.get("requer_pista")
            if pista_requerida and pista_requerida not in self._pistas_captadas:
                disponivel = False

            resultado.append(OpcaoFormatada(
                indice=i,
                texto=opcao.get("texto", ""),
                dica=opcao.get("dica", ""),
                disponivel=disponivel,
            ))

        return resultado

    def processar_escolha(self, indice: int) -> Optional[ResultadoDialogo]:
        """
        Processa a escolha do jogador.

        Args:
            indice: Índice da opção escolhida (1-based)

        Returns:
            ResultadoDialogo com os efeitos da escolha.
        """
        no = self.obter_no_atual()
        if not no:
            return None

        opcoes = no.get("opcoes", [])
        if indice < 1 or indice > len(opcoes):
            return None

        opcao = opcoes[indice - 1]

        # Aplica impacto de confiança
        impacto = opcao.get("impacto", 0)
        self._confianca = max(0, min(100, self._confianca + impacto))

        # Registra pista se o nó atual é uma pista
        if no.get("e_pista"):
            pista_id = no.get("pista_id", self._no_atual)
            if pista_id not in self._pistas_captadas:
                self._pistas_captadas.append(pista_id)

        # Determina tipo de interação
        tipo_str = opcao.get("tipo", "dialogo_medio")
        try:
            tipo = TipoInteracao(tipo_str)
        except ValueError:
            tipo = TipoInteracao.DIALOGO_MEDIO

        # Obtém próximo nó
        proximo = opcao.get("proximo")
        proximo_no = self._dados_dialogos.get("nos", {}).get(proximo, {})

        # Adiciona ao histórico
        self._historico.append(self._no_atual)

        # Atualiza nó atual
        if proximo:
            self._no_atual = proximo

        return ResultadoDialogo(
            texto_resposta=proximo_no.get("texto", ""),
            impacto_confianca=impacto,
            tipo_interacao=tipo,
            proximo_no=proximo,
            e_pista=proximo_no.get("e_pista", False),
            pista_id=proximo_no.get("pista_id"),
            pensamento_master=proximo_no.get("pensamento_master"),
            gatilho_prato=proximo_no.get("gatilho_prato", False),
            revelacao_prato=proximo_no.get("revelacao_prato"),
            tipo_cena=proximo_no.get("tipo_cena"),
        )

    def obter_estado_emocional(self) -> EstadoEmocional:
        """Retorna o estado emocional baseado na confiança."""
        if self._confianca <= 20:
            return EstadoEmocional.FECHADO
        elif self._confianca <= 40:
            return EstadoEmocional.CAUTELOSO
        elif self._confianca <= 60:
            return EstadoEmocional.CURIOSO
        elif self._confianca <= 80:
            return EstadoEmocional.ABERTO
        else:
            return EstadoEmocional.VULNERAVEL

    @property
    def confianca(self) -> int:
        """Retorna o nível atual de confiança."""
        return self._confianca

    @property
    def pistas_captadas(self) -> list[str]:
        """Retorna as pistas captadas."""
        return self._pistas_captadas.copy()

    @property
    def cliente_dados(self) -> dict:
        """Retorna os dados do cliente atual."""
        return self._dados_clientes

    def obter_descricao_chegada(self) -> str:
        """Retorna a descrição de chegada do cliente."""
        return self._dados_clientes.get("descricao_chegada", "")

    def obter_despedida(self, tipo: str) -> str:
        """
        Retorna o texto de despedida apropriado.

        Args:
            tipo: "sucesso", "tempo" ou "falha"
        """
        chaves = {
            "sucesso": "despedida_sucesso",
            "tempo": "despedida_tempo",
            "falha": "despedida_falha",
        }
        chave = chaves.get(tipo, "despedida_falha")
        return self._dados_clientes.get(chave, "O cliente vai embora.")

    def prato_foi_revelado(self) -> bool:
        """Verifica se o prato ideal foi revelado."""
        no = self.obter_no_atual()
        return no.get("revelacao_prato") is not None if no else False

    def obter_prato_revelado(self) -> Optional[str]:
        """Retorna o ID do prato revelado, se houver."""
        no = self.obter_no_atual()
        return no.get("revelacao_prato") if no else None


# Teste rápido
if __name__ == "__main__":
    print("=== TESTE SISTEMA DIÁLOGO V2 ===\n")

    sistema = SistemaDialogo()

    if sistema.carregar_cliente("yuki"):
        print(f"Cliente carregado: Yuki")
        print(f"Confiança inicial: {sistema.confianca}")
        print(f"Estado: {sistema.obter_estado_emocional().value}")
        print(f"\n--- Descrição de chegada ---")
        print(sistema.obter_descricao_chegada()[:200] + "...")

        print(f"\n--- Contexto ---")
        print(sistema.obter_contexto())

        print(f"\n--- Opções ---")
        for opcao in sistema.obter_opcoes():
            status = "✓" if opcao.disponivel else "✗"
            print(f"  {status} {opcao.indice}. {opcao.texto} [{opcao.dica}]")

        # Simula uma escolha
        print(f"\n--- Escolhendo opção 2 ---")
        resultado = sistema.processar_escolha(2)
        if resultado:
            print(f"Impacto: {resultado.impacto_confianca:+d}")
            print(f"Tipo: {resultado.tipo_interacao.value}")
            print(f"Resposta: {resultado.texto_resposta[:150]}...")
            print(f"\nNova confiança: {sistema.confianca}")
            print(f"Estado: {sistema.obter_estado_emocional().value}")
    else:
        print("Erro ao carregar cliente")
