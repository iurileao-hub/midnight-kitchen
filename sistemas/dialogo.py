"""
SistemaDialogo - Gerencia as conversas com clientes.

CONCEITO:
- O jogador ve opcoes de dialogo na tela (ex: "Boa noite", "Dia dificil?")
- Cada opcao tem um EFEITO: +1 (abre), 0 (neutro), -1 (fecha)
- Conforme o cliente muda de estado, as opcoes mudam tambem
- Quando o cliente esta "aberto", o jogador pode descobrir o prato favorito

FLUXO DO JOGO:
1. Cliente entra (estado: "fechado")
2. Jogador escolhe opcoes de dialogo
3. Cliente muda de estado: fechado -> cauteloso -> aberto -> vulneravel
4. Quando "aberto", jogador pode perguntar sobre o prato favorito
5. Sistema retorna o nome do prato para a cozinha preparar

ESTRUTURA DE DADOS:
- Opcoes sao dicionarios: {"texto": "Boa noite!", "efeito": +1}
- Cada estado tem suas proprias opcoes
- Use um dicionario OPCOES onde a chave e o estado
"""

import sys
from pathlib import Path

# Adiciona o diretorio raiz do projeto ao path
# Isso permite importar 'models' mesmo rodando de dentro de 'sistemas/'
sys.path.insert(0, str(Path(__file__).parent.parent))

from models.cliente import Cliente


class SistemaDialogo:
    """Sistema que gerencia conversas com clientes."""

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

        Exemplo de retorno quando cliente esta "fechado":
        [
            "Boa noite. O que posso servir?",
            "Parece cansado. Dia dificil?",
            "Primeira vez aqui?",
        ]

        Retorna apenas os textos das opcoes (para exibir ao jogador).
        """
        opcoes = self.OPCOES.get(cliente.estado, [])
        return [op["texto"] for op in opcoes]

    def processar_escolha(self, cliente: Cliente, indice: int) -> str:
        """
        Processa a escolha do jogador e retorna a resposta do cliente.

        Parametros:
            cliente: o cliente com quem estamos conversando
            indice: qual opcao o jogador escolheu (0, 1, 2, ...)

        Retorna:
            A resposta do cliente (string do dicionario RESPOSTAS)
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
        """
        Tenta descobrir o prato favorito do cliente.

        Esta funcao so deve funcionar se o cliente estiver "aberto".

        Retorna:
            Nome do prato (str) se cliente esta aberto
            None se cliente ainda nao esta pronto
        """
        return cliente.descobrir_prato()

    def obter_estado_cliente(self, cliente: Cliente) -> str:
        """
        Retorna o estado emocional atual do cliente.
        """
        return cliente.estado


# =============================================================================
# TESTES
# =============================================================================
if __name__ == "__main__":
    print("=" * 50)
    print("TESTE - SISTEMA DIALOGO")
    print("=" * 50)

    # Criar cliente de teste
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

    # Teste 1: Estado inicial
    print(f"\n1. Estado inicial: {dialogo.obter_estado_cliente(yuki)}")

    # Teste 2: Ver opcoes disponiveis
    opcoes = dialogo.obter_opcoes(yuki)
    print(f"2. Opcoes disponiveis:")
    for i, texto in enumerate(opcoes):
        print(f"   [{i}] {texto}")

    # Teste 3: Escolher uma opcao positiva
    resposta = dialogo.processar_escolha(yuki, 1)  # "Parece cansado. Dia dificil?" (+1)
    print(f"\n3. Resposta do cliente: {resposta}")
    print(f"4. Novo estado: {dialogo.obter_estado_cliente(yuki)}")

    # Teste 4: Continuar conversando ate "aberto"
    dialogo.processar_escolha(yuki, 0)  # Mais uma opcao positiva
    print(f"\n5. Estado apos mais conversa: {dialogo.obter_estado_cliente(yuki)}")

    # Teste 5: Tentar descobrir prato
    prato = dialogo.tentar_descobrir_prato(yuki)
    print(f"6. Prato descoberto: {prato}")

    print("\n" + "=" * 50)
