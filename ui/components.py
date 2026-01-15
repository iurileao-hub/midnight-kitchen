"""
Components — Componentes de UI do Midnight Kitchen.

Painéis, menus, caixas de diálogo e outros elementos
reutilizáveis da interface.
"""

from typing import Optional

from rich.console import Console, Group
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich.columns import Columns
from rich.table import Table

from config import LARGURA_PAINEL, CORES
from ui.styles import Tema
from ui.ascii_art import AsciiArt


class Componentes:
    """
    Biblioteca de componentes visuais reutilizáveis.

    Todos os componentes seguem o tema visual do jogo:
    elegante, minimalista, atmosférico.
    """

    def __init__(self, console: Console):
        self.console = console

    def painel_narrativa(
        self,
        texto: str,
        titulo: Optional[str] = None,
        subtitulo: Optional[str] = None,
        tempo: Optional[str] = None,
        noite: Optional[int] = None,
    ) -> Panel:
        """
        Cria um painel para texto narrativo.

        O componente principal do jogo - usado para ambientação,
        descrições e momentos narrativos.
        """
        # Monta o título com noite e tempo
        titulo_completo = ""
        if noite is not None:
            titulo_completo = f"NOITE {noite}"
        if titulo:
            titulo_completo = titulo

        # Subtítulo no canto direito (tempo)
        if tempo:
            # O tempo vai no subtitle do painel
            subtitulo_painel = f"[relogio]{AsciiArt.RELOGIO} {tempo}[/relogio]"
        else:
            subtitulo_painel = subtitulo

        return Panel(
            texto,
            title=f"[titulo]{titulo_completo}[/titulo]" if titulo_completo else None,
            subtitle=subtitulo_painel,
            subtitle_align="right",
            border_style=CORES["borda"],
            width=LARGURA_PAINEL,
            padding=(1, 2),
        )

    def painel_dialogo(
        self,
        personagem: str,
        texto: str,
        estado: Optional[str] = None,
        tempo: Optional[str] = None,
    ) -> Panel:
        """
        Cria um painel para diálogo de um personagem.
        """
        # Indicador de estado emocional
        indicador = AsciiArt.indicador_estado(estado) if estado else ""

        titulo = f"{indicador} {personagem}" if indicador else personagem

        return Panel(
            f'"{texto}"',
            title=f"[grey70]{titulo}[/grey70]",
            subtitle=f"[relogio]{AsciiArt.RELOGIO} {tempo}[/relogio]" if tempo else None,
            subtitle_align="right",
            border_style=Tema.cor_por_estado(estado) if estado else CORES["borda"],
            width=LARGURA_PAINEL,
            padding=(0, 2),
        )

    def menu_opcoes(
        self,
        titulo: str,
        opcoes: list[tuple[str, str]],  # Lista de (texto, dica)
        permitir_cancelar: bool = True,
    ) -> Panel:
        """
        Cria um menu de opções para o jogador escolher.

        Args:
            titulo: Título do menu
            opcoes: Lista de tuplas (texto_opcao, dica_opcional)
            permitir_cancelar: Se mostra opção 0 para cancelar
        """
        linhas = []

        for i, (texto, dica) in enumerate(opcoes, 1):
            linha = f"[menu.numero]{i}.[/menu.numero] [menu.item]{texto}[/menu.item]"
            if dica:
                linha += f" [menu.dica][{dica}][/menu.dica]"
            linhas.append(linha)

        if permitir_cancelar:
            linhas.append("")
            linhas.append("[grey50]0. [Voltar][/grey50]")

        conteudo = "\n".join(linhas)

        return Panel(
            conteudo,
            title=f"[titulo]{titulo}[/titulo]",
            border_style=CORES["borda_ativa"],
            width=LARGURA_PAINEL,
            padding=(1, 2),
        )

    def painel_pensamento(self, texto: str) -> Panel:
        """
        Cria um painel para pensamentos internos de Master.

        Estilo diferenciado - itálico, mais escuro.
        """
        linhas = texto.strip().split("\n")
        formatado = "\n".join(f"[pensamento]{linha}[/pensamento]" for linha in linhas)

        return Panel(
            formatado,
            border_style="grey30",
            width=LARGURA_PAINEL - 8,
            padding=(0, 2),
        )

    def painel_memoria(self, titulo: str, texto: str) -> Panel:
        """
        Cria um painel para revelação de memória.

        Estilo especial - cores diferenciadas para momentos importantes.
        """
        return Panel(
            f"[memoria]{texto}[/memoria]",
            title=f"[memoria]✦ {titulo} ✦[/memoria]",
            border_style=CORES["memoria"],
            width=LARGURA_PAINEL,
            padding=(1, 2),
        )

    def cabecalho_noite(self, noite: int, tempo: str) -> None:
        """
        Exibe o cabeçalho de uma noite.

        Mostra número da noite e relógio no topo.
        """
        esquerda = f"[titulo]NOITE {noite}[/titulo]"
        direita = f"[relogio]{AsciiArt.RELOGIO} {tempo}[/relogio]"

        # Calcula espaçamento
        espacos = LARGURA_PAINEL - 20  # Ajuste para markup

        self.console.print(AsciiArt.DIVISOR)
        self.console.print(f"  {esquerda}{' ' * espacos}{direita}")
        self.console.print(AsciiArt.DIVISOR)

    def barra_confianca(self, nivel: int, largura: int = 20) -> str:
        """
        Cria uma barra visual de confiança.

        Args:
            nivel: Nível de confiança (0-100)
            largura: Largura da barra em caracteres
        """
        preenchido = int((nivel / 100) * largura)
        vazio = largura - preenchido

        # Cor baseada no nível
        if nivel <= 20:
            cor = CORES["fechado"]
        elif nivel <= 40:
            cor = CORES["cauteloso"]
        elif nivel <= 60:
            cor = CORES["curioso"]
        elif nivel <= 80:
            cor = CORES["aberto"]
        else:
            cor = CORES["vulneravel"]

        barra = f"[{cor}]{'█' * preenchido}[/{cor}][grey30]{'░' * vazio}[/grey30]"
        return f"[{barra}] {nivel}%"

    def status_cliente(
        self,
        nome: str,
        estado: str,
        confianca: int,
        tempo: str,
    ) -> Panel:
        """
        Painel de status do cliente atual.

        Mostra nome, estado emocional, confiança e tempo.
        """
        indicador = AsciiArt.indicador_estado(estado)
        estado_formatado = f"[estado.{estado}]{estado.capitalize()}[/estado.{estado}]"
        barra = self.barra_confianca(confianca)

        conteudo = f"{indicador} {nome} — {estado_formatado}\n\nConfiança: {barra}"

        return Panel(
            conteudo,
            subtitle=f"[relogio]{AsciiArt.RELOGIO} {tempo}[/relogio]",
            subtitle_align="right",
            border_style=CORES["borda"],
            width=LARGURA_PAINEL,
            padding=(0, 2),
        )

    def divisor(self, estilo: str = "normal") -> None:
        """Exibe um divisor decorativo."""
        if estilo == "decorativo":
            self.console.print(AsciiArt.DIVISOR_DECORATIVO)
        elif estilo == "leve":
            self.console.print(AsciiArt.DIVISOR_LEVE)
        else:
            self.console.print(AsciiArt.DIVISOR)

    def espaco(self, linhas: int = 1) -> None:
        """Adiciona espaço vertical."""
        self.console.print("\n" * (linhas - 1))

    def centralizar(self, texto: str) -> None:
        """Exibe texto centralizado."""
        self.console.print(Align.center(texto))

    def prompt_continuar(self) -> None:
        """Exibe prompt para continuar."""
        self.console.print(
            "\n[grey50][Pressione ENTER para continuar...][/grey50]",
            justify="center"
        )
        input()

    def prompt_escolha(self, texto: str = "Escolha") -> str:
        """Exibe prompt para entrada do jogador."""
        self.console.print(f"\n[grey70]{texto}:[/grey70] ", end="")
        return input()
