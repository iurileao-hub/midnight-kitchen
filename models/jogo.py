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
        self.dia_atual = 0
        self.memorias = []
        self.tem_envelope = False
        self.noites_resultados = []

    def iniciar_dia(self) -> int:
        """Avanca para o proximo dia e retorna o numero."""
        self.dia_atual += 1
        return self.dia_atual

    def registrar_sucesso(self, cliente_nome: str, memoria_conteudo: str):
        """Registra uma noite bem sucedida."""
        self.memorias.append([cliente_nome, memoria_conteudo])
        self.noites_resultados.append(True)
        if self.dia_atual == 1:
            self.tem_envelope = True

    def registrar_falha(self):
        """Registra uma noite mal sucedida."""
        self.noites_resultados.append(False)

    def contar_memorias(self) -> int:
        """Retorna quantas memorias foram coletadas."""
        return len(self.memorias)

    def contar_falhas(self) -> int:
        """Retorna quantas noites falharam."""
        return self.noites_resultados.count(False)

    def pode_final_bom(self) -> bool:
        """Verifica se o jogador pode ter o final bom."""
        return self.contar_falhas() <= self.MAX_FALHAS_FINAL_BOM

    def e_dia_reflexao(self) -> bool:
        """Verifica se e o dia 7 (reflexao)."""
        return self.dia_atual == self.TOTAL_DIAS

    def obter_memorias(self) -> list:
        """Retorna todas as memorias coletadas."""
        return self.memorias

    def abrir_envelope(self) -> str:
        """
        Abre o envelope de Yuki no dia 7.
        So funciona se tiver o envelope e for dia 7.
        """
        if self.tem_envelope and self.e_dia_reflexao():
            return "Conteudo do envelope de Yuki"
        return None


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
