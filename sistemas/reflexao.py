"""
SistemaReflexao - Gerencia o dia 7 (reflexao final).

Master revisita todas as memorias coletadas e descobre a verdade.
O envelope de Yuki (se existir) contem a peca final do quebra-cabeca.
"""
import sys
from pathlib import Path

# Adiciona o diretorio raiz do projeto ao path
# Isso permite importar 'models' mesmo rodando de dentro de 'sistemas/'
sys.path.insert(0, str(Path(__file__).parent.parent))

from models.jogo import Jogo

class SistemaReflexao:
    """Sistema que gerencia a reflexao final do dia 7."""

    CONTEUDO_ENVELOPE = """Uma foto antiga cai do envelope.
Nela, voce ve a si mesmo, jovem, carregando uma crianca para fora do fogo.
Atras da foto, uma anotacao: "O heroi que nunca soube que era."

Yuki escreveu: "Encontrei isso nos arquivos do jornal.
Voce nao causou o incendio. Voce salvou vidas.
A pericia confirmou: curto-circuito na cozinha.
Takeshi sabia. Ele voltou para salvar voce."
"""

    def __init__(self, jogo: Jogo):
        """Inicializa com o estado do jogo."""
        self.jogo = jogo

    def compilar_memorias(self) -> str:
        """Compila todas as memorias em uma narrativa."""
        memorias = self.jogo.obter_memorias()
        if not memorias:
            return "Nenhuma memoria foi coletada. O passado permanece obscuro."

        texto = "=== Memorias Coletadas ===\n\n"
        for i, mem in enumerate(memorias, 1):
            cliente_nome, conteudo = mem
            texto += f"[{cliente_nome}]\n{conteudo}\n\n"
        return texto.strip()

    def revelar_verdade(self) -> str:
        """Revela a verdade sobre o incendio baseado nas memorias."""
        qtd = self.jogo.contar_memorias()

        if qtd >= 5:
            return """As pecas se encaixam.
O incendio nao foi sua culpa.
Voce tentou salvar todos que podia.
Takeshi morreu te protegendo, nao por sua causa."""
        elif qtd >= 3:
            return """Algumas pecas ainda faltam, mas uma verdade emerge:
Voce fez o que podia naquela noite.
A culpa que carrega pode nao ser sua."""
        else:
            return """Poucas memorias. Poucas respostas.
O passado continua nebuloso.
Talvez algumas verdades permanecam enterradas."""

    def processar_envelope(self) -> str:
        """Processa o envelope de Yuki, se existir."""
        conteudo = self.jogo.abrir_envelope()
        if conteudo:
            return f"=== O Envelope de Yuki ===\n\n{self.CONTEUDO_ENVELOPE}"
        return "Yuki nunca deixou o envelope. Algumas respostas se perderam."

    def determinar_final(self) -> str:
        """Determina e retorna o final do jogo."""
        pode_bom = self.jogo.pode_final_bom()
        tem_envelope = self.jogo.tem_envelope

        if pode_bom and tem_envelope:
            return """=== FINAL BOM ===

Voce olha para a cicatriz no espelho.
Pela primeira vez em dez anos, ela nao doi.

Takeshi nao morreu por sua causa.
Ele morreu te salvando.
E voce salvou outros.

O Midnight Kitchen continua aberto.
Agora, com um proposito renovado:
Ser o lugar onde as pessoas encontram paz.

Como Takeshi queria."""

        elif pode_bom and not tem_envelope:
            return """=== FINAL NEUTRO ===

As memorias trouxeram alguma paz.
Mas sem o envelope de Yuki, a verdade completa escapou.

Voce ainda carrega a cicatriz.
Ainda carrega a duvida.
Mas talvez, um dia, a resposta venha.

O Midnight Kitchen continua aberto.
A espera."""

        else:
            return """=== FINAL INCOMPLETO ===

Muitas noites falharam.
Muitas memorias se perderam.

O passado permanece um peso.
A cicatriz ainda arde.

O Midnight Kitchen continua aberto.
Mas voce se pergunta: por quanto tempo?"""

    def executar_dia_reflexao(self) -> str:
        """Executa a sequencia completa do dia 7."""
        partes = []

        partes.append("=" * 50)
        partes.append("DIA 7 - NOITE DE REFLEXAO")
        partes.append("=" * 50)
        partes.append("")
        partes.append("O restaurante esta vazio.")
        partes.append("Apenas voce e as memorias da semana.")
        partes.append("")

        partes.append(self.compilar_memorias())
        partes.append("")
        partes.append(self.revelar_verdade())
        partes.append("")
        partes.append(self.processar_envelope())
        partes.append("")
        partes.append(self.determinar_final())

        return "\n".join(partes)


# Testes
if __name__ == "__main__":
    print("=" * 50)
    print("TESTE DO GABARITO - SISTEMA REFLEXAO")
    print("=" * 50)

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

    jogo.iniciar_dia()  # Dia 7

    reflexao = SistemaReflexao(jogo)

    print(reflexao.executar_dia_reflexao())

    print("\n" + "=" * 50)