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
        self.nome = nome
        self.ingredientes = ingredientes
        self.tempo_preparo = tempo_preparo
        self.descricao_preparo = descricao_preparo

    def preparar(self) -> str:
        """Retorna a narrativa do preparo do prato."""
        return f"Preparando {self.nome}...\n{self.descricao_preparo}\nTempo de preparo: {self.tempo_preparo} minutos."

    def listar_ingredientes(self) -> str:
        """Retorna os ingredientes formatados."""
        return "\n".join(f"- {ingrediente}" for ingrediente in self.ingredientes)

    def __str__(self) -> str:
        """Representacao em texto do prato."""
        return self.nome


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
