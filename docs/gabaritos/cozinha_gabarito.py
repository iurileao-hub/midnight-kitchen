"""
GABARITO - SistemaCozinha
NAO MOSTRAR AO APRENDIZ
"""

from models.prato import Prato
from models.cliente import Cliente


class SistemaCozinha:
    """Sistema que gerencia a cozinha do restaurante."""

    def __init__(self):
        """Inicializa a cozinha com os pratos disponiveis."""
        self.pratos = {
            "Tamago Gohan": Prato(
                nome="Tamago Gohan",
                ingredientes=["arroz", "ovo", "shoyu"],
                tempo_preparo=5,
                descricao_preparo="O ovo cru e quebrado sobre o arroz quente. O shoyu escorre devagar."
            ),
            "Ochazuke": Prato(
                nome="Ochazuke",
                ingredientes=["arroz", "cha verde", "umeboshi", "nori"],
                tempo_preparo=3,
                descricao_preparo="O cha quente e despejado sobre o arroz. O aroma sobe suavemente."
            ),
            "Onigiri": Prato(
                nome="Onigiri",
                ingredientes=["arroz", "sal", "nori", "atum"],
                tempo_preparo=10,
                descricao_preparo="O arroz e moldado com cuidado. Cada bolinho carrega dedicacao."
            ),
            "Miso Shiru": Prato(
                nome="Miso Shiru",
                ingredientes=["miso", "tofu", "wakame", "cebolinha"],
                tempo_preparo=8,
                descricao_preparo="O miso se dissolve lentamente. O tofu flutua em silencio."
            ),
            "Yakisoba": Prato(
                nome="Yakisoba",
                ingredientes=["macarrao", "repolho", "carne", "molho"],
                tempo_preparo=12,
                descricao_preparo="O macarrao estala na chapa quente. O aroma invade o restaurante."
            ),
            "Tamagoyaki": Prato(
                nome="Tamagoyaki",
                ingredientes=["ovos", "acucar", "shoyu", "dashi"],
                tempo_preparo=7,
                descricao_preparo="Camada por camada, a omelete se forma. Doce e delicada."
            ),
        }

    def listar_pratos(self) -> list:
        """Retorna os nomes dos pratos disponiveis."""
        return list(self.pratos.keys())

    def obter_prato(self, nome: str) -> Prato:
        """Retorna um prato pelo nome, ou None se nao existir."""
        return self.pratos.get(nome)

    def preparar_prato(self, nome: str) -> str:
        """Prepara um prato e retorna a narrativa do preparo."""
        prato = self.obter_prato(nome)
        if prato:
            return prato.preparar()
        return None

    def servir_prato(self, nome: str, cliente: Cliente) -> str:
        """Serve um prato ao cliente."""
        prato = self.obter_prato(nome)
        if not prato:
            return "Esse prato nao existe no cardapio."

        memoria = cliente.receber_prato(nome)
        if memoria:
            return f"{cliente.nome} olha para o prato com lagrimas nos olhos.\n\n\"{memoria}\""
        return f"{cliente.nome} agradece educadamente pelo {nome}."


# Testes
if __name__ == "__main__":
    print("=" * 50)
    print("TESTE DO GABARITO - SISTEMA COZINHA")
    print("=" * 50)

    cozinha = SistemaCozinha()

    print(f"\n1. Pratos disponiveis: {cozinha.listar_pratos()}")

    narrativa = cozinha.preparar_prato("Tamago Gohan")
    print(f"\n2. Preparo:\n{narrativa}")

    yuki = Cliente(
        nome="Yuki Tanabe",
        idade=28,
        profissao="Fotografa",
        descricao="Uma jovem com camera antiga",
        genero_masculino=False,
        prato_favorito="Tamago Gohan",
        memoria="Fotos do incendio"
    )

    yuki.mudar_estado(+1)
    yuki.mudar_estado(+1)
    yuki.descobrir_prato()

    resultado = cozinha.servir_prato("Tamago Gohan", yuki)
    print(f"\n3. Resultado ao servir:\n{resultado}")

    print("\n" + "=" * 50)
