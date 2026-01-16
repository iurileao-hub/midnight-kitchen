"""
Renderer — Sistema Central de Renderização.

Coordena todos os componentes de UI para criar
uma experiência visual coesa.
"""

from typing import Optional

from rich.console import Console
from rich.align import Align

from config import LARGURA_PAINEL
from ui.styles import Tema
from ui.components import Componentes
from ui.effects import Efeitos
from ui.ascii_art import AsciiArt


class Renderer:
    """
    Sistema central de renderização do Midnight Kitchen.

    Coordena estilos, componentes e efeitos para criar
    uma experiência visual consistente e imersiva.
    """

    def __init__(self):
        """Inicializa o renderer com console configurado."""
        self.console = Console(
            theme=Tema.get_rich_theme(),
            width=LARGURA_PAINEL + 10,  # Margem extra
            highlight=False,
        )
        self.componentes = Componentes(self.console)
        self.efeitos = Efeitos(self.console)

    def limpar(self) -> None:
        """Limpa a tela."""
        self.console.clear()

    def mostrar_logo(self) -> None:
        """Exibe o logo do jogo."""
        self.limpar()
        self.console.print(AsciiArt.LOGO)

    def mostrar_titulo(
        self,
        titulo: str,
        subtitulo: Optional[str] = None
    ) -> None:
        """Exibe um título centralizado."""
        self.console.print()
        self.componentes.centralizar(f"[titulo]{titulo}[/titulo]")
        if subtitulo:
            self.componentes.centralizar(f"[subtitulo]{subtitulo}[/subtitulo]")
        self.console.print()

    def mostrar_narrativa(
        self,
        texto: str,
        titulo: Optional[str] = None,
        tempo: Optional[str] = None,
        noite: Optional[int] = None,
        digitar: bool = True,
    ) -> None:
        """
        Exibe texto narrativo com formatação apropriada.

        Args:
            texto: O texto narrativo
            titulo: Título opcional do painel
            tempo: Hora atual (ex: "2:15")
            noite: Número da noite
            digitar: Se usa efeito de digitação
        """
        if digitar:
            # Exibe o frame primeiro
            self._exibir_frame_noite(noite, tempo)

            # Digita o conteúdo
            self.console.print()
            paragrafos = texto.strip().split("\n\n")
            for paragrafo in paragrafos:
                for linha in paragrafo.split("\n"):
                    self.efeitos.digitar(f"  {linha.strip()}")
                self.efeitos.pausar()
            self.console.print()
        else:
            painel = self.componentes.painel_narrativa(
                texto,
                titulo=titulo,
                tempo=tempo,
                noite=noite,
            )
            self.console.print(painel)

    def _exibir_frame_noite(
        self,
        noite: Optional[int],
        tempo: Optional[str]
    ) -> None:
        """Exibe o frame decorativo de uma noite."""
        if noite is None:
            return

        # Monta header com noite e tempo
        titulo_noite = f"NOITE {noite}"
        tempo_str = f"{AsciiArt.RELOGIO} {tempo}" if tempo else ""

        # Calcula espaçamento
        espacos = 60 - len(titulo_noite) - len(tempo_str.replace("[", "").replace("]", ""))

        self.console.print(AsciiArt.DIVISOR)
        self.console.print(
            f"  [titulo]{titulo_noite}[/titulo]"
            f"{' ' * espacos}"
            f"[relogio]{tempo_str}[/relogio]"
        )
        self.console.print(AsciiArt.DIVISOR)

    def mostrar_pensamento(self, texto: str) -> None:
        """Exibe um pensamento interno de Master com destaque visual."""
        # Pausa antes para criar separação
        self.efeitos.pausar(0.5)
        self.console.print()

        # Usa painel visual para destacar o pensamento
        painel = self.componentes.painel_pensamento(texto)
        self.console.print(Align.center(painel))

        # Pausa mais longa depois para o jogador absorver
        self.efeitos.pausar(2.0)

    def mostrar_dialogo_cliente(
        self,
        nome: str,
        texto: str,
        estado: Optional[str] = None,
        tempo: Optional[str] = None,
        nome_japones: Optional[str] = None,
    ) -> None:
        """Exibe fala de um cliente."""
        painel = self.componentes.painel_dialogo(
            nome, texto, estado, tempo, nome_japones
        )
        self.console.print(painel)

    def mostrar_menu(
        self,
        titulo: str,
        opcoes: list[tuple[str, str]],
        permitir_cancelar: bool = True,
    ) -> int:
        """
        Exibe menu e retorna escolha do jogador.

        Returns:
            Índice da opção escolhida (0 = cancelar)
        """
        menu = self.componentes.menu_opcoes(titulo, opcoes, permitir_cancelar)
        self.console.print(menu)

        while True:
            escolha = self.componentes.prompt_escolha("Escolha")
            try:
                num = int(escolha)
                if 0 <= num <= len(opcoes):
                    return num
                self.console.print("[erro]Opção inválida.[/erro]")
            except ValueError:
                self.console.print("[erro]Digite um número.[/erro]")

    def mostrar_menu_pratos(
        self,
        titulo: str,
        pratos: list[tuple[str, str, str, str]],  # id, nome, nome_japones, descricao
    ) -> int:
        """
        Exibe menu especializado de pratos com descrições culturais.

        Returns:
            Índice do prato escolhido (0 = cancelar)
        """
        from rich.panel import Panel
        from rich.text import Text

        linhas = []

        for i, (_, nome, nome_jp, desc) in enumerate(pratos, 1):
            # Nome do prato com nome japonês
            linha_nome = Text()
            linha_nome.append(f"{i}. ", style="menu.numero")
            linha_nome.append(f"{nome}", style="bold white")
            linha_nome.append(f"  {nome_jp}", style="grey50")
            linhas.append(linha_nome)

            # Descrição cultural (com wrap automático)
            linhas.append(Text(f"   {desc}", style="grey62"))
            linhas.append(Text())  # Espaço entre pratos

        linhas.append(Text("0. [Voltar]", style="grey50"))

        # Monta painel
        conteudo = Text()
        for i, linha in enumerate(linhas):
            if isinstance(linha, Text):
                conteudo.append_text(linha)
            else:
                conteudo.append(str(linha))
            if i < len(linhas) - 1:
                conteudo.append("\n")

        painel = Panel(
            conteudo,
            title=f"[titulo]{titulo}[/titulo]",
            border_style="grey35",
            padding=(1, 2),
        )
        self.console.print(painel)

        while True:
            escolha = self.componentes.prompt_escolha("Escolha")
            try:
                num = int(escolha)
                if 0 <= num <= len(pratos):
                    return num
                self.console.print("[erro]Opção inválida.[/erro]")
            except ValueError:
                self.console.print("[erro]Digite um número.[/erro]")

    def mostrar_status(
        self,
        nome: str,
        estado: str,
        confianca: int,
        tempo: str,
    ) -> None:
        """Exibe painel de status do cliente."""
        status = self.componentes.status_cliente(nome, estado, confianca, tempo)
        self.console.print(status)

    def mostrar_memoria(self, titulo: str, texto: str) -> None:
        """Exibe revelação de memória."""
        self.efeitos.transicao_cena()
        painel = self.componentes.painel_memoria(titulo, texto)
        self.console.print(painel)
        self.componentes.prompt_continuar()

    def transicao(self) -> None:
        """Executa transição entre cenas."""
        self.efeitos.transicao_cena()

    def pausar(self) -> None:
        """Pausa esperando input do jogador."""
        self.componentes.prompt_continuar()

    def mostrar_erro(self, mensagem: str) -> None:
        """Exibe mensagem de erro."""
        self.console.print(f"[erro]{mensagem}[/erro]")

    def mostrar_sucesso(self, mensagem: str) -> None:
        """Exibe mensagem de sucesso."""
        self.console.print(f"[sucesso]{mensagem}[/sucesso]")

    def input(self, prompt: str = "") -> str:
        """Obtém input do jogador."""
        return self.componentes.prompt_escolha(prompt)

    def divisor(self, estilo: str = "normal") -> None:
        """Exibe divisor."""
        self.componentes.divisor(estilo)

    def espaco(self, linhas: int = 1) -> None:
        """Adiciona espaço vertical."""
        self.componentes.espaco(linhas)
