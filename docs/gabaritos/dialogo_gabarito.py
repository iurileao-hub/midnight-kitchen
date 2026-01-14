"""
GABARITO - SistemaDialogo
NAO MOSTRAR AO APRENDIZ
"""

from models.cliente import Cliente


class SistemaDialogo:
    """Sistema que gerencia conversas com clientes."""

    # Opcoes de dialogo por estado
    OPCOES = {
        "fechado": [
            {"texto": "Boa noite. O que posso servir?", "efeito": 0},
            {"texto": "Parece cansado. Dia difícil?", "efeito": +1},
            {"texto": "Primeira vez aqui?", "efeito": 0},
            {"texto": "Apenas sorri e serve um chá fresco", "efeito": +1},
        ],
        "cauteloso": [
            {"texto": "O que gosta de fazer nas horas vagas?", "efeito": +1},
            {"texto": "Ja visitou outros restaurantes por aqui?", "efeito": 0},
            {"texto": "Prefere ficar sozinho?", "efeito": -1},
            {"texto": "Conte-me sobre seu trabalho.", "efeito": +1},
        ],
        "aberto": [
            {"texto": "Qual seu prato favorito?", "efeito": +1},
            {"texto": "Gostaria de ouvir mais sobre voce.", "efeito": 0},
            {"texto": "Nao confia em estranhos?", "efeito": -1},
        ],
        "vulneravel": [
            {"texto": "Posso ajudar em algo?", "efeito": 0},
            {"texto": "Quer conversar sobre o que aconteceu?", "efeito": -1},
            {"texto": "Fique a vontade para pedir o que quiser.", "efeito": 0},
        ],
    }

    RESPOSTAS = {
        "fechado": "O cliente permanece em silêncio.",
        "cauteloso": "O cliente parece mais relaxado.",
        "aberto": "O cliente sorri e começa a conversar.",
        "vulneravel": "O cliente parece confiar em você agora.",
    }

    def __init__(self):
        """
        Inicializa o sistema de dialogo.

        Este sistema e reutilizavel para multiplos clientes.
        O cliente e passado como parametro nos metodos.
        """
        pass

    def obter_opcoes(self, cliente: Cliente) -> list:
        """
        Retorna as opcoes de dialogo disponiveis para o estado ATUAL do cliente.
        Retorna apenas os textos das opcoes (para exibir ao jogador).
        """
        opcoes = self.OPCOES.get(cliente.estado, [])
        return [op["texto"] for op in opcoes]

    def processar_escolha(self, cliente: Cliente, indice: int) -> str:
        """
        Processa a escolha do jogador e retorna a resposta do cliente.
        """
        opcoes = self.OPCOES.get(cliente.estado, [])
        if 0 <= indice < len(opcoes):
            opcao = opcoes[indice]
            efeito = opcao["efeito"]
            if efeito != 0:
                cliente.mudar_estado(efeito)
            return self.RESPOSTAS[cliente.estado]
        else:
            return "Opcao invalida."

    def tentar_descobrir_prato(self, cliente: Cliente) -> str:
        """Tenta descobrir o prato favorito do cliente."""
        return cliente.descobrir_prato()

    def obter_estado_cliente(self, cliente: Cliente) -> str:
        """Retorna o estado emocional atual do cliente."""
        return cliente.estado


# Testes
if __name__ == "__main__":
    print("=" * 50)
    print("TESTE DO GABARITO - SISTEMA DIALOGO")
    print("=" * 50)

    yuki = Cliente(
        nome="Yuki Tanabe",
        idade=28,
        profissao="Fotografa",
        descricao="Uma jovem com camera antiga",
        genero_masculino=False,
        prato_favorito="Tamago Gohan",
        memoria="Fotos do incendio"
    )

    dialogo = SistemaDialogo()

    print(f"\n1. Estado inicial: {dialogo.obter_estado_cliente(yuki)}")
    print(f"2. Opcoes disponiveis: {dialogo.obter_opcoes(yuki)}")

    resposta = dialogo.processar_escolha(yuki, 1)  # +1
    print(f"3. Resposta: {resposta}")
    print(f"4. Novo estado: {dialogo.obter_estado_cliente(yuki)}")

    # Continuar ate aberto
    dialogo.processar_escolha(yuki, 0)  # cauteloso -> aberto

    prato = dialogo.tentar_descobrir_prato(yuki)
    print(f"5. Prato descoberto: {prato}")

    print("\n" + "=" * 50)
