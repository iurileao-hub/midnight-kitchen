"""
SistemaCozinha - Gerencia a preparacao de pratos.

O jogador pode preparar pratos e servi-los aos clientes.
Servir o prato favorito desbloqueia a memoria do cliente.
"""
import sys
from pathlib import Path

# Adiciona o diretorio raiz do projeto ao path
# Isso permite importar 'models' mesmo rodando de dentro de 'sistemas/'

sys.path.insert(0, str(Path(__file__).parent.parent))
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
      "Katsudon": Prato(
          nome="Katsudon",
          ingredientes=["arroz", "porco empanado", "ovo", "cebola", "dashi"],
          tempo_preparo=15,
          descricao_preparo="O tonkatsu crepita no oleo. O ovo abraca a carne. Comida de vitoria, ou de consolo."
      ),
      "Nikujaga": Prato(
          nome="Nikujaga",
          ingredientes=["carne", "batata", "cenoura", "shoyu", "acucar"],
          tempo_preparo=25,
          descricao_preparo="A carne cozinha lentamente com os legumes. O cheiro preenche o restaurante como um abraco."
      ),
      "Omurice": Prato(
          nome="Omurice",
          ingredientes=["arroz", "frango", "ketchup", "ovos", "manteiga"],
          tempo_preparo=12,
          descricao_preparo="O arroz frito e coberto pelo manto dourado do ovo. Com ketchup, desenha-se uma mensagem."
      ),
  }

    def listar_pratos(self) -> list:
        """Retorna os nomes dos pratos disponiveis."""
        return list(self.pratos.keys())
        
    def obter_prato(self, nome: str) -> Prato:
        """Retorna um prato pelo nome, ou None se nao existir."""
        return self.pratos.get(nome, None)

    def preparar_prato(self, nome: str) -> str:
        """
        Prepara um prato e retorna a narrativa do preparo.
        Retorna None se o prato nao existir.
        """
        return self.pratos[nome].preparar() if nome in self.pratos else None

    def servir_prato(self, nome: str, cliente: Cliente) -> str:
        """
        Serve um prato ao cliente.
        Se for o prato favorito, retorna a memoria revelada.
        Caso contrario, retorna uma reacao generica.
        """
        if nome in self.pratos:
            return cliente.receber_prato(nome)
        else:
            return "Prato nao disponivel."


# Testes
if __name__ == "__main__":
    print("=" * 50)
    print("TESTE - SISTEMA COZINHA")
    print("=" * 50)

    cozinha = SistemaCozinha()

    # Listar pratos
    print(f"\n1. Pratos disponiveis: {cozinha.listar_pratos()}")

    # Preparar um prato
    narrativa = cozinha.preparar_prato("Tamago Gohan")
    print(f"\n2. Preparo:\n{narrativa}")

    # Criar cliente para teste
    yuki = Cliente(
        nome="Yuki Tanabe",
        idade=28,
        profissao="Fotografa",
        descricao="Uma jovem com camera antiga",
        genero_masculino=False,
        prato_favorito="Tamago Gohan",
        memoria="Fotos do incendio"
    )

    # Simular descoberta do prato (necessario para servir funcionar)
    yuki.mudar_estado(+1)  # cauteloso
    yuki.mudar_estado(+1)  # aberto
    yuki.descobrir_prato()

    # Servir prato
    resultado = cozinha.servir_prato("Tamago Gohan", yuki)
    print(f"\n3. Resultado ao servir: {resultado}")

    print("\n" + "=" * 50)
