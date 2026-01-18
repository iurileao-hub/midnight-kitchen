"""
Sistema de Reflexao v2.0 — Dia 7 do Midnight Kitchen.

O dia final onde Master revisita todas as memorias,
abre o envelope de Yuki (se existir) e descobre a verdade
sobre o incendio que mudou sua vida.

Quatro finais possiveis:
- Perfeito: 0 falhas, 6 memorias, envelope
- Bom: max 1 falha, envelope
- Neutro: max 2 falhas
- Ruim: 3+ falhas
"""

from dataclasses import dataclass
from typing import Optional
from rich.console import Console
from rich.panel import Panel
from rich.align import Align

from config import LARGURA_PAINEL, CORES
from ui.renderer import Renderer
from ui.ascii_art import AsciiArt


# ============================================================
# NARRATIVAS DO DIA 7
# ============================================================

ABERTURA_DIA7 = """O restaurante esta vazio.

Pela primeira vez em sete noites, ninguem empurra a cortina de noren.
Nenhum passo hesitante no beco de pedra. Nenhuma historia esperando
para ser contada.

Apenas voce. E as memorias da semana.

O relogio acima do balcao marca 2:47 da manha.
O mesmo horario em que tudo comecou. Dez anos atras.

Seus olhos percorrem o restaurante — as cadeiras vazias,
o balcao de madeira gasta pelo tempo, o reflexo tremulo
da lampada no caldo de dashi.

E entao voce olha para as suas maos.
As mesmas maos que carregaram aquela crianca para fora do fogo."""


ABERTURA_MEMORIAS = """As vozes da semana ecoam na sua mente.

Fragmentos de conversas. Confissoes sussurradas no silencio
da madrugada. Cada cliente trouxe uma peca do quebra-cabeca
que voce tentou esquecer por dez anos."""


TRANSICAO_ENVELOPE = """Esta manha, quando voce abriu a porta do restaurante,
havia um envelope no chao. Pardo, amarelado pelo tempo.

Nenhum selo. Nenhum endereco. Apenas seu nome,
escrito em letra feminina que voce reconheceu.

Yuki.

Ela deve ter vindo de madrugada, enquanto a cidade dormia.
Deixou o envelope e foi embora, sem acordar ninguem.

Suas maos tremem ao pega-lo.
Ela disse que iria ver as fotos. Que precisava entender.
Agora, parece que ela quer que voce entenda tambem."""


CONTEUDO_ENVELOPE = """Um bilhete cai primeiro. Letra de Yuki.

"Eu finalmente olhei.

Dez anos carregando essas fotos sem coragem de ver.
Naquela noite no seu restaurante, algo mudou.
Voce me deu forca para encarar.

E eu vi. Vi voce. Jovem. Entrando no fogo.
Vi a crianca nos seus bracos.
Vi o heroi que nunca soube que era.

Mas vi outra coisa tambem.

Uma foto que eu tinha esquecido de olhar.
O quadro de energia do lado de fora. Faiscas.
O fogo comecou ali. Nao dentro. Fora.

Pesquisei nos arquivos do jornal onde trabalho."

Voce tira o recorte de jornal. Amarelado. Datado de dez anos atras.

PERICIA CONFIRMA: CURTO-CIRCUITO CAUSOU INCENDIO
Investigacao descarta negligencia. Fiacao antiga
do predio foi a causa do acidente que matou
o renomado chef Takeshi Yamamoto.

A voz dentro de voce — aquela que sussurrava que foi
sua culpa, que voce deveria ter feito mais, que Takeshi
morreu por sua causa — finalmente silencia.

O bilhete continua:

"Voce nao causou o incendio. Ninguem causou.
Foi um acidente. Uma fiacao velha. Nada mais.

Takeshi voltou para salvar voce nao por culpa —
por escolha. Como voce escolheu salvar aquela crianca.

Obrigada. Por me ajudar a ver.
Espero que isso ajude voce tambem.

— Yuki"

Suas maos param de tremer.
Pela primeira vez em dez anos, param de tremer."""


SEM_ENVELOPE = """Voce pensa em Yuki. A fotografa da primeira noite.

Ela carregava algo. Um envelope. Fotos de uma noite antiga.
Mas foi embora ainda fechada, ainda carregando seu peso.

Voce se pergunta se ela encontrou coragem para olhar.
Se descobriu algo nas fotos que a libertou.
Se pensou em voce.

Algumas respostas se perdem assim.
Na noite. No silencio. Na distancia entre estranhos
que quase se conheceram."""


# ============================================================
# FINAIS
# ============================================================

FINAIS = {
    "perfeito": {
        "titulo": "REDENÇÃO",
        "texto": """Voce olha para a cicatriz no espelho do banheiro.

Pela primeira vez em dez anos, ela nao doi.
Pela primeira vez, voce entende.

Takeshi nao morreu por sua causa.
Ele morreu fazendo uma escolha — a mesma escolha
que voce fez quando carregou aquela crianca para fora do fogo.

A mesma escolha que voce faz toda noite,
quando abre as portas do Midnight Kitchen
para os perdidos, os solitarios, os quebrados.

Voce caminha ate a porta e vira a placa.

"ABERTO"

O Midnight Kitchen continua.
Nao como penitencia — como proposito.

O proposito que Takeshi sempre viu em voce,
mesmo quando voce nao conseguia ver.

A cortina de noren balanca suavemente.
Em algum lugar la fora, alguem precisa de um lugar para parar.

E voce estara aqui.
Como sempre esteve.
Como sempre estara.""",
        "cor": CORES["vulneravel"],
    },

    "bom": {
        "titulo": "AMANHECER",
        "texto": """A primeira luz da manha entra pela janela.

Voce segura a foto de dez anos atras. O rosto jovem,
determinado, carregando uma crianca para a seguranca.

Nao era um covarde. Nunca foi.
A culpa que carregou por tanto tempo...
era um fardo que nunca lhe pertenceu.

Takeshi fez sua escolha. Voce fez a sua.
E as duas escolhas salvaram vidas.

O Midnight Kitchen continua aberto.
Agora, com um peso a menos nos ombros.
A cicatriz ainda esta la — sempre estara.
Mas talvez cicatrizes nao sejam apenas lembretes de dor.
Talvez sejam lembretes de sobrevivencia.

Voce limpa o balcao e prepara o caldo do dia.
O ritual de sempre.
Mas hoje, os movimentos parecem mais leves.

Amanha, a cortina de noren balancara novamente.
E voce estara pronto para ouvir.""",
        "cor": CORES["aberto"],
    },

    "neutro": {
        "titulo": "PERGUNTAS SEM RESPOSTA",
        "texto": """O sol nasce sobre Shinjuku.

Voce ainda tem perguntas. Muitas perguntas.
A semana trouxe fragmentos, mas nao o quadro completo.

Takeshi. O incendio. A crianca que voce salvou.
Os rostos que vieram e foram durante essas sete noites.

Alguns revelaram verdades. Outros levaram
seus segredos embora.

O Midnight Kitchen continua aberto.
Como sempre continuou, noite apos noite,
por dez anos.

Talvez as respostas ainda venham.
Talvez outras almas perdidas cruzem aquela porta
carregando pecas do quebra-cabeca.

Ou talvez algumas perguntas nao tenham resposta.

Voce pega o pano e comeca a limpar o balcao.
O movimento familiar. O ritual que da sentido
aos dias sem resposta.

A vida continua.
O Midnight Kitchen continua.
A espera.""",
        "cor": CORES["cauteloso"],
    },

    "ruim": {
        "titulo": "CINZAS",
        "texto": """A manha chega cinzenta.

Muitas noites falharam.
Muitas historias ficaram pela metade.
Muitas memorias se perderam antes de serem contadas.

Voce olha para a cicatriz.
Ela ainda arde. Ainda pesa.
O fardo de dez anos continua la, intocado.

O Midnight Kitchen esta quieto demais.
As cadeiras vazias parecem mais vazias hoje.
O silencio, mais pesado.

Voce se pergunta por quanto tempo ainda consegue fazer isso.
Abrir as portas. Preparar o caldo. Esperar.

Esperar por que?

A cortina de noren balanca no vento.
Ninguem entra.

Voce continua limpando o balcao.
E o que sabe fazer.
E o unico ritual que restou.

Mas a pergunta permanece:
Por quanto tempo?""",
        "cor": CORES["fechado"],
    },
}


# ============================================================
# CLASSE PRINCIPAL
# ============================================================

class SistemaReflexao:
    """
    Sistema que gerencia o Dia 7 — a reflexao final.

    Compila memorias, revela verdades e determina o final
    baseado nas escolhas do jogador ao longo das 6 noites.
    """

    def __init__(self, renderer: Renderer):
        """
        Inicializa o sistema.

        Args:
            renderer: Sistema de renderizacao para output
        """
        self.renderer = renderer
        self.console = renderer.console

    def _digitar_texto(self, texto: str, pausar_paragrafos: bool = False) -> None:
        """
        Digita texto linha por linha com efeito typewriter.

        Args:
            texto: Texto a ser digitado
            pausar_paragrafos: Se True, pausa entre paragrafos
        """
        if pausar_paragrafos:
            for paragrafo in texto.strip().split("\n\n"):
                for linha in paragrafo.split("\n"):
                    self.renderer.efeitos.digitar(f"  {linha.strip()}")
                self.renderer.efeitos.pausar()
        else:
            for linha in texto.strip().split("\n"):
                self.renderer.efeitos.digitar(f"  {linha.strip()}")

    def executar(
        self,
        memorias: list[tuple[str, str]],
        tem_envelope: bool,
        tipo_final: str,
    ) -> None:
        """
        Executa a sequencia completa do Dia 7.

        Args:
            memorias: Lista de (nome_cliente, memoria) coletadas
            tem_envelope: Se o jogador tem o envelope de Yuki
            tipo_final: "perfeito", "bom", "neutro" ou "ruim"
        """
        # 1. Abertura atmosferica
        self._mostrar_abertura()

        # 2. Compilacao das memorias
        self._mostrar_memorias(memorias)

        # 3. Revelacao da verdade (baseada nas memorias)
        self._revelar_verdade(memorias)

        # 4. Envelope de Yuki (se existir)
        self._processar_envelope(tem_envelope)

        # 5. Final
        self._mostrar_final(tipo_final)

    def _mostrar_abertura(self) -> None:
        """Exibe a abertura atmosferica do Dia 7."""
        self.renderer.limpar()

        # Cabecalho especial
        self.console.print(AsciiArt.DIVISOR)
        self.renderer.componentes.centralizar("[titulo]DIA 7 — NOITE DE REFLEXAO[/titulo]")
        self.console.print(AsciiArt.DIVISOR)
        self.console.print()

        # Narrativa de abertura com digitacao
        self._digitar_texto(ABERTURA_DIA7, pausar_paragrafos=True)

        self.renderer.pausar()

    def _mostrar_memorias(self, memorias: list[tuple[str, str]]) -> None:
        """Exibe as memorias coletadas durante a semana."""
        self.renderer.transicao()

        if not memorias:
            self.console.print()
            self.renderer.efeitos.digitar("  Nenhuma memoria foi coletada.")
            self.renderer.efeitos.digitar("  O passado permanece obscuro.")
            self.renderer.pausar()
            return

        # Transicao para memorias
        self._digitar_texto(ABERTURA_MEMORIAS)
        self.renderer.efeitos.pausar()

        self.console.print()

        # Cada memoria como um painel
        for nome, memoria in memorias:
            painel = Panel(
                f"[memoria]{memoria}[/memoria]",
                title=f"[grey70]{nome}[/grey70]",
                border_style=CORES["memoria"],
                width=LARGURA_PAINEL - 10,
                padding=(0, 2),
            )
            self.console.print(Align.center(painel))
            self.renderer.efeitos.pausa_dramatica()

        self.renderer.pausar()

    def _revelar_verdade(self, memorias: list[tuple[str, str]]) -> None:
        """Revela insights sobre o incendio baseado nas memorias."""
        self.renderer.transicao()

        qtd = len(memorias)

        self.console.print()
        self.renderer.componentes.centralizar("[titulo]O que as memorias revelam[/titulo]")
        self.console.print()

        if qtd >= 5:
            texto = """As pecas se encaixam lentamente.

Tanaka tentou salvar Takeshi — voce nao foi o unico
que fez o que podia naquela noite.

Ryo fugiu, carregando culpa por dez anos —
assim como voce.

Midori viu algo estranho na origem do fogo —
talvez nunca tenha sido culpa de ninguem.

E a crianca que voce salvou... cresceu.
Veio ate aqui, sem saber quem voce era.

A verdade emerge das sombras:
Voce nao causou o incendio.
Voce salvou vidas.
Takeshi morreu te protegendo — por escolha, nao por sua culpa."""

        elif qtd >= 3:
            texto = """Algumas pecas ainda faltam.
Mas uma verdade comeca a emergir.

As historias se cruzam — o bombeiro, o taxista,
a fotografa. Todos conectados por uma noite.
Todos carregando fragmentos da mesma historia.

Voce fez o que podia naquela noite.
A culpa que carrega... pode nao ser sua."""

        else:
            texto = """Poucas memorias. Poucas respostas.

Os rostos que vieram esta semana
levaram seus segredos embora.

O passado continua nebuloso.
A verdade permanece enterrada
sob dez anos de silencio."""

        self._digitar_texto(texto, pausar_paragrafos=True)
        self.renderer.pausar()

    def _processar_envelope(self, tem_envelope: bool) -> None:
        """Processa o envelope de Yuki."""
        self.renderer.transicao()

        if tem_envelope:
            # Transicao para o envelope
            self._digitar_texto(TRANSICAO_ENVELOPE)

            self.renderer.pausar()
            self.renderer.transicao()

            # Conteudo do envelope
            painel = Panel(
                f"[memoria]{CONTEUDO_ENVELOPE.strip()}[/memoria]",
                title="[memoria]O Envelope de Yuki[/memoria]",
                border_style=CORES["memoria"],
                width=LARGURA_PAINEL,
                padding=(1, 2),
            )
            self.console.print(painel)
        else:
            # Sem envelope
            self._digitar_texto(SEM_ENVELOPE)

        self.renderer.pausar()

    def _mostrar_final(self, tipo: str) -> None:
        """Exibe o final correspondente."""
        self.renderer.transicao()

        final = FINAIS.get(tipo, FINAIS["neutro"])

        # Titulo do final
        self.console.print()
        self.console.print(AsciiArt.DIVISOR)
        self.renderer.componentes.centralizar(
            f"[{final['cor']}]FINAL: {final['titulo']}[/{final['cor']}]"
        )
        self.console.print(AsciiArt.DIVISOR)
        self.console.print()

        # Texto do final com digitacao
        self._digitar_texto(final["texto"], pausar_paragrafos=True)

        self.renderer.pausar()

        # Creditos finais
        self._mostrar_creditos(tipo)

    def _mostrar_creditos(self, tipo_final: str) -> None:
        """Exibe os creditos finais."""
        self.renderer.transicao()

        self.console.print()
        self.renderer.componentes.centralizar("[titulo]M I D N I G H T   K I T C H E N[/titulo]")
        self.console.print()
        self.renderer.componentes.centralizar("[grey70]Uma historia sobre culpa, perdao e conexao[/grey70]")
        self.console.print()
        self.console.print()

        self.renderer.componentes.centralizar("[grey50]Inspirado em Shinya Shokudo (Midnight Diner)[/grey50]")
        self.renderer.componentes.centralizar("[grey50]de Yaro Abe[/grey50]")

        self.console.print()
        self.console.print()

        # Estatisticas da partida
        finais_bonitos = {
            "perfeito": "[vulneravel]Perfeito[/vulneravel]",
            "bom": "[aberto]Bom[/aberto]",
            "neutro": "[cauteloso]Neutro[/cauteloso]",
            "ruim": "[fechado]Ruim[/fechado]",
        }

        self.renderer.componentes.centralizar(
            f"Seu final: {finais_bonitos.get(tipo_final, tipo_final)}"
        )

        self.console.print()
        self.console.print()
        self.renderer.componentes.centralizar("[grey50]Obrigado por jogar.[/grey50]")
        self.console.print()

        self.renderer.pausar()


# ============================================================
# TESTE
# ============================================================

if __name__ == "__main__":
    from ui.renderer import Renderer

    print("=== TESTE SISTEMA REFLEXAO v2.0 ===\n")

    renderer = Renderer()
    reflexao = SistemaReflexao(renderer)

    # Simula memorias coletadas
    memorias_teste = [
        ("Yuki", "Fotografou o incendio. Guarda fotos e um envelope misterioso."),
        ("Tanaka", "Bombeiro que tentou salvar Takeshi. O teto desabou entre eles."),
        ("Ryo", "Fugiu do incendio enquanto outros ficaram para ajudar."),
        ("Midori", "Vizinha que viu faiscas estranhas vindo de fora do restaurante."),
        ("Sachiko", "Filha de Takeshi. O pai deixou uma carta falando de um 'jovem promissor'."),
        ("Hiroto", "A crianca que Master salvou do fogo, agora adulto."),
    ]

    # Executa reflexao com final perfeito
    reflexao.executar(
        memorias=memorias_teste,
        tem_envelope=True,
        tipo_final="perfeito",
    )
