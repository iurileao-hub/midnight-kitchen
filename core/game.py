"""
Game — Estado Central do Midnight Kitchen.

Coordena o estado global do jogo, incluindo:
- Noite atual
- Memórias coletadas
- Sistema de tempo
- Resultados das noites
"""

from dataclasses import dataclass, field
from typing import Optional

from config import TOTAL_NOITES, MAX_FALHAS_FINAL_BOM
from contracts import (
    EstadoJogo,
    SaveData,
    ResultadoNoite,
    EstadoTempo,
)
from core.tempo import SistemaTempo
from core.save import SistemaSave


@dataclass
class Game:
    """
    Estado central do jogo.

    Gerencia todo o progresso do jogador através
    das 7 noites do Midnight Kitchen.
    """

    # Estado interno
    _estado: EstadoJogo = field(default_factory=EstadoJogo)

    # Sistemas
    _save_sistema: SistemaSave = field(default_factory=SistemaSave)
    _tempo: Optional[SistemaTempo] = None

    # Configuração
    total_noites: int = TOTAL_NOITES
    max_falhas: int = MAX_FALHAS_FINAL_BOM

    def __post_init__(self):
        """Inicialização após criação."""
        pass

    # ========================================
    # PROPRIEDADES
    # ========================================

    @property
    def noite_atual(self) -> int:
        """Retorna a noite atual."""
        return self._estado.noite_atual

    @property
    def memorias(self) -> list[tuple[str, str]]:
        """Retorna as memórias coletadas."""
        return self._estado.memorias

    @property
    def tem_envelope(self) -> bool:
        """Verifica se tem o envelope de Yuki."""
        return self._estado.tem_envelope

    @property
    def tempo(self) -> Optional[SistemaTempo]:
        """Retorna o sistema de tempo atual."""
        return self._tempo

    # ========================================
    # FLUXO DO JOGO
    # ========================================

    def iniciar_noite(self, cliente_id: str) -> int:
        """
        Inicia uma nova noite.

        Args:
            cliente_id: ID do cliente desta noite

        Returns:
            Número da noite iniciada
        """
        self._estado.noite_atual += 1
        self._tempo = SistemaTempo.para_cliente(cliente_id)
        return self._estado.noite_atual

    def registrar_sucesso(self, cliente_nome: str, memoria: str) -> None:
        """
        Registra uma noite bem sucedida.

        Args:
            cliente_nome: Nome do cliente
            memoria: A memória revelada
        """
        self._estado.memorias.append((cliente_nome, memoria))
        self._estado.resultados_noites.append(ResultadoNoite.SUCESSO)

        # Envelope só existe se Yuki (noite 1) foi sucesso
        if self._estado.noite_atual == 1:
            self._estado.tem_envelope = True

    def registrar_falha(self, motivo: ResultadoNoite = ResultadoNoite.FALHA_CONFIANCA) -> None:
        """
        Registra uma noite que falhou.

        Args:
            motivo: O motivo da falha
        """
        self._estado.resultados_noites.append(motivo)

    def registrar_parcial(self) -> None:
        """Registra uma noite com resultado parcial."""
        self._estado.resultados_noites.append(ResultadoNoite.PARCIAL)

    # ========================================
    # CONSULTAS
    # ========================================

    def contar_memorias(self) -> int:
        """Retorna quantas memórias foram coletadas."""
        return len(self._estado.memorias)

    def contar_falhas(self) -> int:
        """Retorna quantas noites falharam."""
        return self._estado.contar_falhas()

    def pode_final_bom(self) -> bool:
        """Verifica se o final bom ainda é possível."""
        return self._estado.pode_final_bom()

    def e_ultima_noite(self) -> bool:
        """Verifica se é a noite de reflexão."""
        return self._estado.noite_atual >= self.total_noites - 1

    def e_dia_reflexao(self) -> bool:
        """Verifica se é o dia 7 (reflexão)."""
        return self._estado.noite_atual == self.total_noites

    def obter_resultado_noite(self, noite: int) -> Optional[ResultadoNoite]:
        """Retorna o resultado de uma noite específica."""
        if 0 < noite <= len(self._estado.resultados_noites):
            return self._estado.resultados_noites[noite - 1]
        return None

    # ========================================
    # SAVE / LOAD
    # ========================================

    def salvar(self) -> bool:
        """
        Salva o progresso atual.

        Returns:
            True se salvou com sucesso.
        """
        save_data = self._save_sistema.criar_save_de_jogo(
            noite_atual=self._estado.noite_atual,
            memorias=self._estado.memorias,
            tem_envelope=self._estado.tem_envelope,
            resultados=self._estado.resultados_noites,
        )
        return self._save_sistema.salvar(save_data)

    def carregar(self) -> bool:
        """
        Carrega o progresso salvo.

        Returns:
            True se carregou com sucesso.
        """
        save = self._save_sistema.carregar()
        if not save:
            return False

        self._estado.noite_atual = save.noite_atual
        self._estado.memorias = save.memorias
        self._estado.tem_envelope = save.tem_envelope
        self._estado.resultados_noites = [
            ResultadoNoite(r) for r in save.resultados_noites
        ]

        return True

    def existe_save(self) -> bool:
        """Verifica se existe um save."""
        return self._save_sistema.existe_save()

    def obter_resumo_save(self) -> Optional[dict]:
        """Retorna resumo do save para o menu."""
        return self._save_sistema.obter_resumo()

    def apagar_save(self) -> bool:
        """Apaga o save existente."""
        return self._save_sistema.apagar_save()

    def novo_jogo(self) -> None:
        """Inicia um novo jogo do zero."""
        self._estado = EstadoJogo()
        self._tempo = None

    # ========================================
    # FINAIS
    # ========================================

    def determinar_final(self) -> str:
        """
        Determina qual final o jogador recebe.

        Returns:
            "bom", "neutro" ou "ruim"
        """
        falhas = self.contar_falhas()
        memorias = self.contar_memorias()

        if falhas == 0 and memorias == 6 and self.tem_envelope:
            return "perfeito"
        elif falhas <= self.max_falhas and self.tem_envelope:
            return "bom"
        elif falhas <= 2:
            return "neutro"
        else:
            return "ruim"


# Teste rápido
if __name__ == "__main__":
    print("=== TESTE GAME ===\n")

    game = Game()

    # Simula algumas noites
    clientes = ["yuki", "tanaka", "ryo"]

    for cliente in clientes:
        noite = game.iniciar_noite(cliente)
        print(f"Noite {noite}: {cliente}")
        print(f"  Tempo: {game.tempo.formatar()}")

        # Simula resultado
        if cliente == "tanaka":
            game.registrar_falha(ResultadoNoite.FALHA_TEMPO)
            print("  Resultado: FALHA")
        else:
            game.registrar_sucesso(cliente.capitalize(), f"Memória de {cliente}")
            print("  Resultado: SUCESSO")

    print(f"\n=== Estado Final ===")
    print(f"Noite: {game.noite_atual}")
    print(f"Memórias: {game.contar_memorias()}")
    print(f"Falhas: {game.contar_falhas()}")
    print(f"Envelope: {game.tem_envelope}")
    print(f"Final bom possível: {game.pode_final_bom()}")

    # Teste save/load
    print(f"\n=== Save/Load ===")
    game.salvar()
    print("Salvo!")

    game2 = Game()
    game2.carregar()
    print(f"Carregado: Noite {game2.noite_atual}, {game2.contar_memorias()} memórias")

    # Limpa
    game.apagar_save()
