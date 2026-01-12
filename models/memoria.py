"""
Memoria - Uma peca do quebra-cabeca do passado.

Cada memoria e revelada por um cliente durante uma noite bem sucedida.
"""


class Memoria:
    """Uma peca do quebra-cabeca revelada por um cliente."""

    def __init__(self, dia: int, cliente_nome: str, conteudo: str):
        """Inicializa a memoria com seus dados."""
        self.dia = dia
        self.cliente_nome = cliente_nome
        self.conteudo = conteudo

    def exibir(self) -> str:
        """Retorna a memoria formatada para exibicao."""
        return f'Dia {self.dia} - Cliente: {self.cliente_nome}\nMemoria: {self.conteudo}'

    def __str__(self) -> str:
        return f'Memoria de {self.cliente_nome}'


# Testes
if __name__ == "__main__":
    print("=" * 50)
    print("TESTE - MEMORIA")
    print("=" * 50)

    mem = Memoria(
        dia=1,
        cliente_nome="Yuki Tanabe",
        conteudo="Fotos de um incendio que ela nunca conseguiu olhar"
    )

    print(f"\n1. Str: {mem}")
    print(f"\n2. Exibir:\n{mem.exibir()}")

    print("\n" + "=" * 50)
