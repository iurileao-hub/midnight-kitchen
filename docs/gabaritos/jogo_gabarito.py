"""
GABARITO - Jogo
NAO MOSTRAR AO APRENDIZ
"""

from memoria_gabarito import Memoria


class Jogo:
    """Estado central do jogo Midnight Kitchen."""

    TOTAL_DIAS = 7
    MAX_FALHAS_FINAL_BOM = 1

    def __init__(self):
        self.dia_atual = 0
        self.memorias = []
        self.tem_envelope = False
        self.noites_resultados = []  # Lista de bool: True = sucesso

    def iniciar_dia(self) -> int:
        """Avanca para o proximo dia e retorna o numero."""
        self.dia_atual += 1
        return self.dia_atual

    def registrar_sucesso(self, cliente_nome: str, memoria_conteudo: str):
        """Registra uma noite bem sucedida."""
        memoria = Memoria(self.dia_atual, cliente_nome, memoria_conteudo)
        self.memorias.append(memoria)
        self.noites_resultados.append(True)

        # Yuki (dia 1) entrega o envelope
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
        if self.e_dia_reflexao() and self.tem_envelope:
            return "As fotos mostram claramente: o fogo comecou no quadro eletrico, nao na cozinha."
        return None


# Testes
if __name__ == "__main__":
    print("=" * 50)
    print("TESTE DO GABARITO - JOGO")
    print("=" * 50)

    jogo = Jogo()

    # Simular 6 noites
    print("\n--- Simulando 6 noites ---")

    jogo.iniciar_dia()  # Dia 1 - Yuki
    jogo.registrar_sucesso("Yuki", "Fotos do incendio")
    print(f"Dia {jogo.dia_atual}: Sucesso com Yuki. Envelope: {jogo.tem_envelope}")

    jogo.iniciar_dia()  # Dia 2 - Tanaka
    jogo.registrar_sucesso("Tanaka", "O fogo nao parecia vir da cozinha")
    print(f"Dia {jogo.dia_atual}: Sucesso com Tanaka")

    jogo.iniciar_dia()  # Dia 3 - Ryo
    jogo.registrar_falha()  # Falhou!
    print(f"Dia {jogo.dia_atual}: FALHA com Ryo")

    jogo.iniciar_dia()  # Dia 4 - Midori
    jogo.registrar_sucesso("Midori", "Vi faiscas no quadro eletrico")
    print(f"Dia {jogo.dia_atual}: Sucesso com Midori")

    jogo.iniciar_dia()  # Dia 5 - Sachiko
    jogo.registrar_sucesso("Sachiko", "Meu pai sabia do problema eletrico")
    print(f"Dia {jogo.dia_atual}: Sucesso com Sachiko")

    jogo.iniciar_dia()  # Dia 6 - Hiroto
    jogo.registrar_sucesso("Hiroto", "Voce me salvou naquela noite")
    print(f"Dia {jogo.dia_atual}: Sucesso com Hiroto")

    # Dia 7 - Reflexao
    jogo.iniciar_dia()
    print(f"\n--- Dia {jogo.dia_atual}: Reflexao ---")
    print(f"Memorias: {jogo.contar_memorias()}")
    print(f"Falhas: {jogo.contar_falhas()}")
    print(f"Final bom possivel: {jogo.pode_final_bom()}")
    print(f"E dia de reflexao: {jogo.e_dia_reflexao()}")

    print(f"\nMemorias coletadas:")
    for mem in jogo.obter_memorias():
        print(f"  {mem.exibir()}")

    envelope = jogo.abrir_envelope()
    print(f"\nEnvelope: {envelope}")

    print("\n" + "=" * 50)
