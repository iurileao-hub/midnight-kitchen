"""
Jogo - Estado central do Midnight Kitchen.

Controla os dias, memorias coletadas, e determina o final.
O envelope de Yuki so existe se a primeira noite foi sucesso.
"""

from memoria import Memoria


class Jogo:
    """Estado central do jogo Midnight Kitchen."""

    TOTAL_DIAS = 7
    MAX_FALHAS_FINAL_BOM = 1

    def __init__(self):
        """Inicializa um novo jogo."""
        # TODO: dia_atual comeca em 0
        # TODO: memorias e uma lista vazia
        # TODO: tem_envelope comeca False
        # TODO: noites_resultados e uma lista vazia
        pass

    def iniciar_dia(self) -> int:
        """Avanca para o proximo dia e retorna o numero."""
        # TODO: Incrementar dia_atual
        # TODO: Retornar dia_atual
        pass

    def registrar_sucesso(self, cliente_nome: str, memoria_conteudo: str):
        """Registra uma noite bem sucedida."""
        # TODO: Criar Memoria e adicionar a lista
        # TODO: Adicionar True a noites_resultados
        # TODO: Se dia 1, tem_envelope = True
        pass

    def registrar_falha(self):
        """Registra uma noite mal sucedida."""
        # TODO: Adicionar False a noites_resultados
        pass

    def contar_memorias(self) -> int:
        """Retorna quantas memorias foram coletadas."""
        # TODO: Retornar tamanho da lista
        pass

    def contar_falhas(self) -> int:
        """Retorna quantas noites falharam."""
        # TODO: Contar False em noites_resultados
        pass

    def pode_final_bom(self) -> bool:
        """Verifica se o jogador pode ter o final bom."""
        # TODO: Verificar se falhas <= MAX_FALHAS_FINAL_BOM
        pass

    def e_dia_reflexao(self) -> bool:
        """Verifica se e o dia 7 (reflexao)."""
        # TODO: Verificar se dia_atual == TOTAL_DIAS
        pass

    def obter_memorias(self) -> list:
        """Retorna todas as memorias coletadas."""
        # TODO: Retornar lista de memorias
        pass

    def abrir_envelope(self) -> str:
        """
        Abre o envelope de Yuki no dia 7.
        So funciona se tiver o envelope e for dia 7.
        """
        # TODO: Verificar condicoes
        # TODO: Retornar conteudo ou None
        pass


# Testes
if __name__ == "__main__":
    print("=" * 50)
    print("TESTE - JOGO")
    print("=" * 50)

    jogo = Jogo()

    # Simular algumas noites
    jogo.iniciar_dia()  # Dia 1
    jogo.registrar_sucesso("Yuki", "Fotos do incendio")
    print(f"Dia {jogo.dia_atual}: Yuki - Envelope: {jogo.tem_envelope}")

    jogo.iniciar_dia()  # Dia 2
    jogo.registrar_falha()
    print(f"Dia {jogo.dia_atual}: FALHA")

    jogo.iniciar_dia()  # Dia 3
    jogo.registrar_sucesso("Ryo", "Fragmentos de memoria")
    print(f"Dia {jogo.dia_atual}: Ryo")

    print(f"\nMemorias: {jogo.contar_memorias()}")
    print(f"Falhas: {jogo.contar_falhas()}")
    print(f"Final bom possivel: {jogo.pode_final_bom()}")

    print("\n" + "=" * 50)
