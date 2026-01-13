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
            {"texto": "Boa noite. O que posso servir?", "efeito": +1},
            {"texto": "Parece cansado. Dia dificil?", "efeito": +1},
            {"texto": "Primeira vez aqui?", "efeito": 0},
        ],
        "cauteloso": [
            {"texto": "Tem algo em mente para comer?", "efeito": +1},
            {"texto": "Esse lugar e tranquilo, pode relaxar.", "efeito": +1},
            {"texto": "De onde voce vem?", "efeito": 0},
        ],
        "aberto": [
            {"texto": "Parece que tem algo te preocupando.", "efeito": +1},
            {"texto": "Qual seu prato favorito?", "efeito": 0},
            {"texto": "Quer conversar sobre isso?", "efeito": +1},
        ],
        "vulneravel": [
            {"texto": "Estou ouvindo.", "efeito": 0},
            {"texto": "Deve ter sido dificil.", "efeito": 0},
            {"texto": "Obrigado por compartilhar.", "efeito": 0},
        ],
    }

    RESPOSTAS = {
        "fechado": "O cliente acena levemente.",
        "cauteloso": "O cliente parece mais relaxado.",
        "aberto": "O cliente suspira e comeca a se abrir.",
        "vulneravel": "O cliente olha para voce com gratidao.",
    }

    def __init__(self, cliente: Cliente):
        """Inicializa o sistema com um cliente."""
        self.cliente = cliente

    def obter_opcoes(self) -> list:
        """Retorna as opcoes de dialogo disponiveis."""
        estado = self.cliente.estado
        return self.OPCOES.get(estado, [])

    def escolher_opcao(self, indice: int) -> str:
        """Processa a escolha do jogador."""
        opcoes = self.obter_opcoes()
        if indice < 0 or indice >= len(opcoes):
            return "Opcao invalida."

        opcao = opcoes[indice]
        efeito = opcao["efeito"]

        if efeito != 0:
            self.cliente.mudar_estado(efeito)

        return self.RESPOSTAS.get(self.cliente.estado, "")

    def tentar_descobrir_prato(self) -> str:
        """Tenta descobrir o prato favorito do cliente."""
        return self.cliente.descobrir_prato()

    def obter_estado_cliente(self) -> str:
        """Retorna o estado emocional atual do cliente."""
        return self.cliente.estado


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

    dialogo = SistemaDialogo(yuki)

    print(f"\n1. Estado inicial: {dialogo.obter_estado_cliente()}")
    print(f"2. Opcoes disponiveis: {dialogo.obter_opcoes()}")

    resposta = dialogo.escolher_opcao(0)
    print(f"3. Resposta: {resposta}")
    print(f"4. Novo estado: {dialogo.obter_estado_cliente()}")

    # Continuar ate aberto
    dialogo.escolher_opcao(0)  # cauteloso -> aberto

    prato = dialogo.tentar_descobrir_prato()
    print(f"5. Prato descoberto: {prato}")

    print("\n" + "=" * 50)
