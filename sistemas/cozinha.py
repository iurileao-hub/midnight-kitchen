"""
SistemaCozinha - Gerencia a preparacao de pratos.

O jogador pode preparar pratos e servi-los aos clientes.
Servir o prato favorito desbloqueia a memoria do cliente.
"""

from models.prato import Prato
from models.cliente import Cliente


class SistemaCozinha:
    """Sistema que gerencia a cozinha do restaurante."""

    def __init__(self):
        """Inicializa a cozinha com os pratos disponiveis."""
        # TODO: criar dicionario de pratos disponiveis
        # Exemplo: {"Tamago Gohan": Prato(...), "Ochazuke": Prato(...)}
        pass

    def listar_pratos(self) -> list:
        """Retorna os nomes dos pratos disponiveis."""
        # TODO: retornar lista de nomes
        pass

    def obter_prato(self, nome: str) -> Prato:
        """Retorna um prato pelo nome, ou None se nao existir."""
        # TODO: buscar prato no dicionario
        pass

    def preparar_prato(self, nome: str) -> str:
        """
        Prepara um prato e retorna a narrativa do preparo.
        Retorna None se o prato nao existir.
        """
        # TODO: obter prato
        # TODO: chamar metodo preparar() do prato
        pass

    def servir_prato(self, nome: str, cliente: Cliente) -> str:
        """
        Serve um prato ao cliente.
        Se for o prato favorito, retorna a memoria revelada.
        Caso contrario, retorna uma reacao generica.
        """
        # TODO: verificar se prato existe
        # TODO: chamar receber_prato() do cliente
        # TODO: retornar memoria ou reacao generica
        pass


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
