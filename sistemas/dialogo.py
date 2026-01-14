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

    def __init__(self, cliente: Cliente):
        """
        Inicializa o sistema com um cliente.

        O sistema precisa guardar uma referencia ao cliente para:
        - Consultar seu estado atual
        - Mudar seu estado com mudar_estado()
        - Descobrir seu prato com descobrir_prato()
        """
        self.cliente = cliente

    def obter_opcoes(self) -> list:
        """
        Retorna as opcoes de dialogo disponiveis para o estado ATUAL do cliente.

        Exemplo de retorno quando cliente esta "fechado":
        [
            {"texto": "Boa noite. O que posso servir?", "efeito": +1},
            {"texto": "Parece cansado. Dia dificil?", "efeito": +1},
            {"texto": "Primeira vez aqui?", "efeito": 0},
        ]

        Passos:
        1. Obter o estado atual do cliente (self.cliente.estado)
        2. Buscar as opcoes desse estado no dicionario OPCOES
        3. Retornar a lista de opcoes
        """
        return self.OPCOES.get(self.cliente.estado, [])

    def escolher_opcao(self, indice: int) -> str:
        """
        Processa a escolha do jogador e retorna a resposta do cliente.

        Parametros:
            indice: qual opcao o jogador escolheu (0, 1, 2, ...)

        Retorna:
            A resposta do cliente (string do dicionario RESPOSTAS)

        Passos:
        1. Obter a lista de opcoes atuais (use obter_opcoes())
        2. Validar se o indice e valido (0 <= indice < len(opcoes))
        3. Pegar a opcao escolhida: opcoes[indice]
        4. Extrair o efeito: opcao["efeito"]
        5. Se efeito != 0, chamar self.cliente.mudar_estado(efeito)
        6. Retornar a resposta apropriada do dicionario RESPOSTAS
        """
        opcoes = self.obter_opcoes()
        if 0 <= indice < len(opcoes):
            opcao = opcoes[indice]
            efeito = opcao["efeito"]
            if efeito != 0:
                self.cliente.mudar_estado(efeito)
            return self.RESPOSTAS[self.cliente.estado]
        else:
            return "Opcao invalida."

    def tentar_descobrir_prato(self) -> str:
        """
        Tenta descobrir o prato favorito do cliente.

        Esta funcao so deve funcionar se o cliente estiver "aberto".
        E basicamente um wrapper para self.cliente.descobrir_prato()

        Retorna:
            Nome do prato (str) se cliente esta aberto
            None se cliente ainda nao esta pronto
        """
        return self.cliente.descobrir_prato()

    def obter_estado_cliente(self) -> str:
        """
        Retorna o estado emocional atual do cliente.

        Simplesmente retorna self.cliente.estado
        """
        return self.cliente.estado


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

    dialogo = SistemaDialogo(yuki)

    # Teste 1: Estado inicial
    print(f"\n1. Estado inicial: {dialogo.obter_estado_cliente()}")

    # Teste 2: Ver opcoes disponiveis
    opcoes = dialogo.obter_opcoes()
    print(f"2. Opcoes disponiveis:")
    if opcoes:
        for i, op in enumerate(opcoes):
            print(f"   [{i}] {op['texto']} (efeito: {op['efeito']})")

    # Teste 3: Escolher uma opcao
    resposta = dialogo.escolher_opcao(0)
    print(f"\n3. Resposta do cliente: {resposta}")
    print(f"4. Novo estado: {dialogo.obter_estado_cliente()}")

    # Teste 4: Continuar conversando ate "aberto"
    dialogo.escolher_opcao(0)  # Mais uma opcao positiva
    print(f"\n5. Estado apos mais conversa: {dialogo.obter_estado_cliente()}")

    # Teste 5: Tentar descobrir prato
    prato = dialogo.tentar_descobrir_prato()
    print(f"6. Prato descoberto: {prato}")

    print("\n" + "=" * 50)
