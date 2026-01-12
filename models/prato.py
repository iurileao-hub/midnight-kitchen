"""
Prato - Uma receita que pode ser preparada no Midnight Kitchen.

Cada prato tem ingredientes e uma narrativa de preparo.
"""


class Prato:
    """Representa um prato que pode ser preparado."""

    def __init__(
        self,
        nome: str,
        ingredientes: list,
        tempo_preparo: int,
        descricao_preparo: str
    ):
        """Inicializa o prato com seus dados."""
        # TODO: Inicializar atributos
        pass

    def preparar(self) -> str:
        """Retorna a narrativa do preparo do prato."""
        # TODO: Formatar e retornar nome + descricao + tempo
        pass

    def listar_ingredientes(self) -> str:
        """Retorna os ingredientes formatados."""
        # TODO: Formatar lista de ingredientes
        pass

    def __str__(self) -> str:
        """Representacao em texto do prato."""
        # TODO: Retornar o nome
        pass


# Testes
if __name__ == "__main__":
    print("=" * 50)
    print("TESTE - PRATO")
    print("=" * 50)

    tamago = Prato(
        nome="Tamago Gohan",
        ingredientes=["arroz", "ovo", "shoyu"],
        tempo_preparo=5,
        descricao_preparo="O ovo cru e quebrado sobre o arroz quente. O shoyu escorre devagar."
    )

    print(f"\n1. Nome: {tamago}")
    print(f"\n2. Ingredientes:\n{tamago.listar_ingredientes()}")
    print(f"\n3. Preparo:\n{tamago.preparar()}")

    print("\n" + "=" * 50)
