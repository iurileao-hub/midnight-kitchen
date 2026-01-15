"""
Scene — Gerenciador de Cenas do Midnight Kitchen.

Coordena o fluxo entre diferentes telas e estados do jogo:
título, menu, noites, diálogo, cozinha, reflexão, finais.
"""

from enum import Enum, auto
from dataclasses import dataclass, field
from typing import Optional, Callable, Any

from contracts import TipoCena


@dataclass
class Cena:
    """
    Representa uma cena do jogo.

    Cada cena tem um tipo, dados opcionais, e pode
    transicionar para outras cenas.
    """

    tipo: TipoCena
    dados: dict = field(default_factory=dict)
    origem: Optional["Cena"] = None

    def com_dados(self, **kwargs) -> "Cena":
        """Retorna uma nova cena com dados adicionais."""
        novos_dados = {**self.dados, **kwargs}
        return Cena(tipo=self.tipo, dados=novos_dados, origem=self.origem)


class GerenciadorCenas:
    """
    Gerencia o fluxo de cenas do jogo.

    Controla transições, histórico, e estado atual.
    Permite voltar para cenas anteriores quando apropriado.
    """

    def __init__(self):
        self._cena_atual: Optional[Cena] = None
        self._historico: list[Cena] = []
        self._handlers: dict[TipoCena, Callable] = {}

    @property
    def cena_atual(self) -> Optional[Cena]:
        """Retorna a cena atual."""
        return self._cena_atual

    @property
    def tipo_atual(self) -> Optional[TipoCena]:
        """Retorna o tipo da cena atual."""
        return self._cena_atual.tipo if self._cena_atual else None

    def registrar_handler(
        self,
        tipo: TipoCena,
        handler: Callable[[Cena], Optional[Cena]]
    ) -> None:
        """
        Registra um handler para um tipo de cena.

        O handler recebe a cena atual e retorna a próxima cena
        (ou None para permanecer na mesma).
        """
        self._handlers[tipo] = handler

    def ir_para(self, tipo: TipoCena, **dados) -> None:
        """
        Transiciona para uma nova cena.

        Args:
            tipo: O tipo de cena para ir
            **dados: Dados a passar para a cena
        """
        nova_cena = Cena(
            tipo=tipo,
            dados=dados,
            origem=self._cena_atual,
        )

        # Adiciona cena atual ao histórico
        if self._cena_atual:
            self._historico.append(self._cena_atual)

        self._cena_atual = nova_cena

    def voltar(self) -> bool:
        """
        Volta para a cena anterior.

        Returns:
            True se conseguiu voltar, False se não há histórico.
        """
        if not self._historico:
            return False

        self._cena_atual = self._historico.pop()
        return True

    def executar_cena_atual(self) -> Optional[Cena]:
        """
        Executa o handler da cena atual.

        Returns:
            A próxima cena, se houver transição.
        """
        if not self._cena_atual:
            return None

        handler = self._handlers.get(self._cena_atual.tipo)
        if handler:
            return handler(self._cena_atual)

        return None

    def loop_principal(self, cena_inicial: TipoCena = TipoCena.TITULO) -> None:
        """
        Executa o loop principal de cenas.

        Continua até chegar em uma cena terminal ou sem handler.
        """
        self.ir_para(cena_inicial)

        while self._cena_atual:
            proxima = self.executar_cena_atual()

            if proxima:
                # Adiciona atual ao histórico
                if self._cena_atual:
                    self._historico.append(self._cena_atual)
                self._cena_atual = proxima
            elif self._cena_atual.tipo == TipoCena.FINAL:
                # Cena terminal
                break

    def limpar_historico(self) -> None:
        """Limpa o histórico de cenas."""
        self._historico.clear()

    def obter_dado(self, chave: str, padrao: Any = None) -> Any:
        """Obtém um dado da cena atual."""
        if self._cena_atual:
            return self._cena_atual.dados.get(chave, padrao)
        return padrao

    def definir_dado(self, chave: str, valor: Any) -> None:
        """Define um dado na cena atual."""
        if self._cena_atual:
            self._cena_atual.dados[chave] = valor


# Teste rápido
if __name__ == "__main__":
    print("=== TESTE GERENCIADOR DE CENAS ===\n")

    gerenciador = GerenciadorCenas()

    # Simula fluxo de cenas
    gerenciador.ir_para(TipoCena.TITULO)
    print(f"Cena: {gerenciador.tipo_atual}")

    gerenciador.ir_para(TipoCena.MENU)
    print(f"Cena: {gerenciador.tipo_atual}")

    gerenciador.ir_para(TipoCena.NOITE, noite=1, cliente="yuki")
    print(f"Cena: {gerenciador.tipo_atual}, Dados: {gerenciador.cena_atual.dados}")

    gerenciador.ir_para(TipoCena.DIALOGO, cliente="yuki", no="intro")
    print(f"Cena: {gerenciador.tipo_atual}, Dados: {gerenciador.cena_atual.dados}")

    # Volta
    gerenciador.voltar()
    print(f"Voltou para: {gerenciador.tipo_atual}")

    gerenciador.voltar()
    print(f"Voltou para: {gerenciador.tipo_atual}")
