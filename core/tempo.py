"""
Sistema de Tempo Atmosférico — Midnight Kitchen.

O tempo avança discretamente a cada interação, criando
pressão sutil sem punir o jogador. Quando o tempo se esgota,
o cliente se despede melancolicamente.
"""

import random
from dataclasses import dataclass, field
from typing import Optional

from config import (
    TEMPO_POR_INTERACAO,
    DURACAO_MAXIMA_NOITE,
    DURACAO_POR_CLIENTE,
    HORARIOS_CLIENTES,
)
from contracts import TipoInteracao


@dataclass
class SistemaTempo:
    """
    Gerencia o tempo durante uma noite.

    O tempo avança a cada interação do jogador.
    Cria atmosfera e tensão sutil.
    """

    hora: int = 0
    minuto: int = 0
    minutos_passados: int = 0
    duracao_maxima: int = DURACAO_MAXIMA_NOITE

    # Histórico para debug/análise
    _historico: list[tuple[str, int]] = field(default_factory=list)

    @classmethod
    def para_cliente(cls, cliente_id: str) -> "SistemaTempo":
        """
        Cria um sistema de tempo configurado para um cliente específico.

        Cada cliente chega em um horário diferente e pode ter
        duração diferente (primeira noite é mais generosa).
        """
        hora, minuto = HORARIOS_CLIENTES.get(cliente_id, (2, 0))
        duracao = DURACAO_POR_CLIENTE.get(cliente_id, DURACAO_MAXIMA_NOITE)
        return cls(hora=hora, minuto=minuto, duracao_maxima=duracao)

    def avancar(self, tipo: TipoInteracao) -> int:
        """
        Avança o tempo baseado no tipo de interação.

        Args:
            tipo: O tipo de interação que ocorreu

        Returns:
            Quantos minutos passaram
        """
        # Obtém o range de tempo para este tipo
        min_tempo, max_tempo = TEMPO_POR_INTERACAO.get(
            tipo.value,
            (5, 10)  # Fallback
        )

        # Calcula tempo aleatório dentro do range
        minutos = random.randint(min_tempo, max_tempo)

        # Atualiza estado
        self.minutos_passados += minutos
        total_minutos = self.hora * 60 + self.minuto + minutos
        self.hora = (total_minutos // 60) % 24
        self.minuto = total_minutos % 60

        # Registra histórico
        self._historico.append((tipo.value, minutos))

        return minutos

    def formatar(self) -> str:
        """
        Retorna a hora formatada para exibição.

        Ex: "2:15", "23:47"
        """
        return f"{self.hora}:{self.minuto:02d}"

    def tempo_restante(self) -> int:
        """Retorna quantos minutos restam antes do cliente ir embora."""
        return max(0, self.duracao_maxima - self.minutos_passados)

    def tempo_esgotado(self) -> bool:
        """Verifica se o tempo se esgotou."""
        return self.minutos_passados >= self.duracao_maxima

    def porcentagem_passada(self) -> float:
        """Retorna a porcentagem do tempo que já passou."""
        return min(100.0, (self.minutos_passados / self.duracao_maxima) * 100)

    def esta_urgente(self, limite: float = 80.0) -> bool:
        """
        Verifica se está nos minutos finais.

        Usado para mudar a cor do relógio.
        """
        return self.porcentagem_passada() >= limite

    def obter_historico(self) -> list[tuple[str, int]]:
        """Retorna o histórico de passagem de tempo."""
        return self._historico.copy()

    def resetar(self, cliente_id: str) -> None:
        """Reseta o tempo para um novo cliente."""
        hora, minuto = HORARIOS_CLIENTES.get(cliente_id, (2, 0))
        self.hora = hora
        self.minuto = minuto
        self.minutos_passados = 0
        self._historico.clear()


# Teste rápido
if __name__ == "__main__":
    print("=== TESTE SISTEMA DE TEMPO ===\n")

    tempo = SistemaTempo.para_cliente("yuki")
    print(f"Hora inicial: {tempo.formatar()}")
    print(f"Tempo restante: {tempo.tempo_restante()} min\n")

    interacoes = [
        TipoInteracao.DIALOGO_CURTO,
        TipoInteracao.DIALOGO_MEDIO,
        TipoInteracao.SILENCIO,
        TipoInteracao.DIALOGO_LONGO,
        TipoInteracao.COZINHA,
        TipoInteracao.SERVIR,
    ]

    for tipo in interacoes:
        minutos = tempo.avancar(tipo)
        print(f"{tipo.value}: +{minutos} min -> {tempo.formatar()}")
        print(f"  Restante: {tempo.tempo_restante()} min ({tempo.porcentagem_passada():.0f}%)")

        if tempo.tempo_esgotado():
            print("\n⚠️  TEMPO ESGOTADO!")
            break

    print(f"\n=== Histórico ===")
    for tipo, mins in tempo.obter_historico():
        print(f"  {tipo}: {mins} min")
