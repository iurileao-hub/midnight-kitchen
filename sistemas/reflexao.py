"""
SistemaReflexao - Gerencia o dia 7 (reflexao final).

Master revisita todas as memorias coletadas e descobre a verdade.
O envelope de Yuki (se existir) contem a peca final do quebra-cabeca.
"""

from models.jogo import Jogo


class SistemaReflexao:
    """Sistema que gerencia a reflexao final do dia 7."""

    def __init__(self, jogo: Jogo):
        """Inicializa com o estado do jogo."""
        # TODO: armazenar referencia ao jogo
        pass

    def compilar_memorias(self) -> str:
        """
        Compila todas as memorias em uma narrativa.
        Retorna texto formatado com todas as memorias coletadas.
        """
        # TODO: obter memorias do jogo
        # TODO: formatar em texto narrativo
        pass

    def revelar_verdade(self) -> str:
        """
        Revela a verdade sobre o incendio baseado nas memorias.
        O conteudo depende de quantas memorias foram coletadas.
        """
        # TODO: analisar memorias coletadas
        # TODO: retornar narrativa apropriada
        pass

    def processar_envelope(self) -> str:
        """
        Processa o envelope de Yuki, se existir.
        Retorna o conteudo ou mensagem de que nao ha envelope.
        """
        # TODO: verificar se jogo tem envelope
        # TODO: abrir envelope e retornar conteudo
        pass

    def determinar_final(self) -> str:
        """
        Determina e retorna o final do jogo.
        Final bom: <= 1 falha e tem envelope.
        Final neutro: <= 1 falha mas sem envelope.
        Final ruim: > 1 falha.
        """
        # TODO: verificar condicoes
        # TODO: retornar narrativa do final apropriado
        pass

    def executar_dia_reflexao(self) -> str:
        """
        Executa a sequencia completa do dia 7.
        Retorna a narrativa completa da reflexao.
        """
        # TODO: compilar memorias
        # TODO: revelar verdade
        # TODO: processar envelope (se houver)
        # TODO: determinar final
        # TODO: combinar tudo em narrativa
        pass


# Testes
if __name__ == "__main__":
    print("=" * 50)
    print("TESTE - SISTEMA REFLEXAO")
    print("=" * 50)

    # Criar jogo simulado
    jogo = Jogo()

    # Simular 6 noites
    jogo.iniciar_dia()
    jogo.registrar_sucesso("Yuki", "Fotos do incendio")

    jogo.iniciar_dia()
    jogo.registrar_sucesso("Tanaka", "Tentou salvar Takeshi")

    jogo.iniciar_dia()
    jogo.registrar_falha()

    jogo.iniciar_dia()
    jogo.registrar_sucesso("Midori", "Viu faiscas estranhas")

    jogo.iniciar_dia()
    jogo.registrar_sucesso("Sachiko", "Carta do pai")

    jogo.iniciar_dia()
    jogo.registrar_sucesso("Hiroto", "Foi salvo por Master")

    # Dia 7 - Reflexao
    jogo.iniciar_dia()

    reflexao = SistemaReflexao(jogo)

    print(f"\n1. Memorias compiladas:\n{reflexao.compilar_memorias()}")
    print(f"\n2. Verdade revelada:\n{reflexao.revelar_verdade()}")
    print(f"\n3. Envelope:\n{reflexao.processar_envelope()}")
    print(f"\n4. Final:\n{reflexao.determinar_final()}")

    print("\n" + "=" * 50)
