import json
from pathlib import Path

from models.cliente import Cliente
from models.jogo import Jogo
from sistemas.dialogo import SistemaDialogo
from sistemas.cozinha import SistemaCozinha
from sistemas.reflexao import SistemaReflexao


# ============================================================
# ARTE ASCII
# ============================================================

LOGO = """
                            ░░░░░░░░░░░░░░░░░░░░░
                        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                      ░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░
                     ░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░
                    ░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░
                   ░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░
                  ░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░
                  ░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░
                 ░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░
                 ░░░▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓░░░
                 ░░░▓▓▓▓▓░░░░  深 夜 キッチン  ░░░░▓▓▓▓▓░░░
                 ░░░▓▓▓▓▓░░░░                  ░░░░▓▓▓▓▓░░░
                 ░░░▓▓▓▓▓░░░░  MIDNIGHT        ░░░░▓▓▓▓▓░░░
                 ░░░▓▓▓▓▓░░░░    KITCHEN       ░░░░▓▓▓▓▓░░░
                 ░░░▓▓▓▓▓░░░░                  ░░░░▓▓▓▓▓░░░
                 ░░░▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓░░░
                 ░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░
                  ░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░
                   ░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░
                    ░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░
                      ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                            ░░░░░░░░░░░░░░░░░░░░░
                                   ║║║║║
                                   ║║║║║
                                   ║║║║║
                              ═════╩╩╩╩╩═════

        ╔═══════════════════════════════════════════════════════╗
        ║                                                       ║
        ║   "O que voce quer comer? Se eu tiver os              ║
        ║    ingredientes, eu faco."                            ║
        ║                                                       ║
        ║   Uma historia de culpa, memoria e perdao.            ║
        ║                                                       ║
        ║   Este jogo se passa 10 anos antes dos eventos        ║
        ║   de "Midnight Diner" (Shinya Shokudo).               ║
        ║                                                       ║
        ╚═══════════════════════════════════════════════════════╝
"""

ABERTURA = """
═══════════════════════════════════════════════════════════════

    Toquio, 2:00 da manha.

    Um beco silencioso no bairro de Shinjuku.
    Uma cortina de noren balanca suavemente.

    Atras dela, um pequeno restaurante.
    Apenas seis lugares no balcao.
    Um homem trabalha sozinho na cozinha.

    Ele tem uma cicatriz no rosto.
    Nunca fala sobre ela.

    Ha dez anos, algo aconteceu.
    Algo que ele tenta esquecer toda noite.
    Mas esta semana... sera diferente.

═══════════════════════════════════════════════════════════════
"""


def limpar_tela():
    """Limpa a tela do terminal."""
    print("\033[H\033[J", end="")


def pausar():
    """Aguarda o jogador pressionar ENTER."""
    input("\n[Pressione ENTER para continuar...]")


def carregar_clientes() -> list:
    """
    Carrega os clientes do arquivo JSON.
    Retorna uma lista de objetos Cliente.
    """
    caminho = Path(__file__).parent / "dados" / "clientes.json"

    with open(caminho, "r", encoding="utf-8") as f:
        dados = json.load(f)

    clientes = []
    for c in dados["clientes"]:
        cliente = Cliente(
            nome=c["nome"],
            idade=c["idade"],
            profissao=c["profissao"],
            descricao=c["descricao"],
            genero_masculino=c["genero_masculino"],
            prato_favorito=c["prato_favorito"],
            memoria=c["memoria"]
        )
        clientes.append(cliente)

    return clientes


def mostrar_menu_pratos(cozinha: SistemaCozinha) -> str:
    """
    Mostra o menu de pratos e retorna a escolha do jogador.
    """
    pratos = cozinha.listar_pratos()

    print("\n=== CARDAPIO ===")
    for i, prato in enumerate(pratos, 1):
        print(f"  {i}. {prato}")

    while True:
        try:
            escolha = int(input("\nQual prato preparar? "))
            if 1 <= escolha <= len(pratos):
                return pratos[escolha - 1]
            print("Opcao invalida.")
        except ValueError:
            print("Digite um numero.")


def executar_noite(
    jogo: Jogo,
    cliente: Cliente,
    dialogo: SistemaDialogo,
    cozinha: SistemaCozinha
) -> bool:
    """
    Executa uma noite completa com um cliente.
    Retorna True se a memoria foi revelada, False caso contrario.
    """
    limpar_tela()

    print("=" * 50)
    print(f"NOITE {jogo.dia_atual}")
    print("=" * 50)

    print(f"\n{cliente.apresentar()}")
    pausar()

    # Loop de dialogo
    while True:
        limpar_tela()

        print(f"\n[{cliente.nome} - Estado: {cliente.estado}]")
        print("-" * 40)

        # Mostrar opcoes de dialogo
        opcoes = dialogo.obter_opcoes(cliente)
        for i, opcao in enumerate(opcoes, 1):
            print(f"  {i}. {opcao}")
        print(f"  0. [Encerrar noite]")

        try:
            escolha = int(input("\nO que dizer? "))
        except ValueError:
            continue

        if escolha == 0:
            break

        if 1 <= escolha <= len(opcoes):
            resposta = dialogo.processar_escolha(cliente, escolha - 1)
            print(f"\n{resposta}")
            pausar()

            # Verificar se pode descobrir prato
            if cliente.esta_aberto() and not cliente.prato_descoberto:
                prato = cliente.descobrir_prato()
                if prato:
                    print(f"\n[Voce percebe que {cliente.nome} gostaria de {prato}]")
                    pausar()

            # Se prato foi descoberto, oferecer menu
            if cliente.prato_descoberto and not cliente.memoria_revelada:
                print("\n[O cliente parece esperar algo...]")
                prato_escolhido = mostrar_menu_pratos(cozinha)

                # Preparar prato
                narrativa = cozinha.preparar_prato(prato_escolhido)
                print(f"\n{narrativa}")
                pausar()

                # Servir prato
                resultado = cozinha.servir_prato(prato_escolhido, cliente)
                if resultado:
                    print(f"\n{cliente.nome} olha para o prato...")
                    pausar()
                    print(f"\n\"{resultado}\"")
                    pausar()
                    return True
                else:
                    print(f"\n{cliente.nome} agradece educadamente.")
                    pausar()

    return cliente.foi_sucesso()


def executar_jogo():
    """
    Loop principal do jogo.
    Coordena as 7 noites e os sistemas.
    """
    limpar_tela()
    print(LOGO)
    pausar()

    limpar_tela()
    print(ABERTURA)
    pausar()

    # Criar instancias
    jogo = Jogo()
    dialogo = SistemaDialogo()
    cozinha = SistemaCozinha()
    clientes = carregar_clientes()

    # Loop das 6 noites
    for cliente in clientes:
        jogo.iniciar_dia()

        sucesso = executar_noite(jogo, cliente, dialogo, cozinha)

        if sucesso:
            jogo.registrar_sucesso(cliente.nome, cliente.memoria)
            print(f"\n[{cliente.nome} deixa o restaurante em paz.]")
        else:
            jogo.registrar_falha()
            print(f"\n[{cliente.nome} vai embora... algo ficou por dizer.]")

        pausar()

    # Dia 7 - Reflexao
    jogo.iniciar_dia()
    reflexao = SistemaReflexao(jogo)

    limpar_tela()
    resultado_final = reflexao.executar_dia_reflexao()
    print(resultado_final)
    pausar()

    print("\n\nObrigado por jogar Midnight Kitchen.")
    print("深夜キッチン\n")


# ============================================================
# PONTO DE ENTRADA
# ============================================================

if __name__ == "__main__":
    try:
        executar_jogo()
    except KeyboardInterrupt:
        print("\n\nO restaurante fecha por hoje...")
        print("Volte quando quiser.\n")
