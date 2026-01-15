"""
Effects — Efeitos Visuais do Midnight Kitchen.

Efeitos de digitação, transições e animações
que criam imersão e atmosfera.
"""

import time
from typing import Optional

from rich.console import Console
from rich.live import Live
from rich.text import Text

from config import (
    VELOCIDADE_DIGITACAO,
    VELOCIDADE_DIGITACAO_RAPIDA,
    VELOCIDADE_DIGITACAO_DRAMATICA,
    PAUSA_PARAGRAFO,
    PAUSA_DRAMATICA,
    SKIP_ANIMACOES,
)


class Efeitos:
    """
    Gerencia efeitos visuais do jogo.

    Inclui efeito de máquina de escrever, pausas dramáticas,
    e transições suaves.
    """

    def __init__(self, console: Console):
        self.console = console

    def digitar(
        self,
        texto: str,
        velocidade: Optional[float] = None,
        estilo: str = "",
        nova_linha: bool = True
    ) -> None:
        """
        Exibe texto com efeito de digitação (máquina de escrever).

        Args:
            texto: O texto a ser exibido
            velocidade: Segundos entre cada caractere (None = padrão)
            estilo: Estilo rich para aplicar ao texto
            nova_linha: Se deve adicionar nova linha ao final
        """
        if SKIP_ANIMACOES:
            if estilo:
                self.console.print(f"[{estilo}]{texto}[/{estilo}]", end="\n" if nova_linha else "")
            else:
                self.console.print(texto, end="\n" if nova_linha else "")
            return

        velocidade = velocidade or VELOCIDADE_DIGITACAO

        # Processa markup rich para manter cores durante digitação
        texto_formatado = Text.from_markup(texto) if "[" in texto else Text(texto)

        if estilo:
            texto_formatado.stylize(estilo)

        # Usa Live para atualização suave - digita caractere por caractere
        texto_exibido = Text(style=estilo if estilo else None)

        with Live(texto_exibido, console=self.console, refresh_per_second=60, transient=True) as live:
            for char in texto_formatado.plain:
                texto_exibido.append(char)
                live.update(texto_exibido)
                time.sleep(velocidade)

        # Imprime versão final com formatação completa
        self.console.print(texto_formatado, end="\n" if nova_linha else "")

    def digitar_rapido(self, texto: str, estilo: str = "") -> None:
        """Digita texto mais rapidamente."""
        self.digitar(texto, velocidade=VELOCIDADE_DIGITACAO_RAPIDA, estilo=estilo)

    def digitar_dramatico(self, texto: str, estilo: str = "") -> None:
        """Digita texto lentamente para efeito dramático."""
        self.digitar(texto, velocidade=VELOCIDADE_DIGITACAO_DRAMATICA, estilo=estilo)

    def pausar(self, segundos: Optional[float] = None) -> None:
        """
        Pausa a execução por um tempo.

        Args:
            segundos: Tempo de pausa (None = pausa padrão)
        """
        if SKIP_ANIMACOES:
            return

        time.sleep(segundos or PAUSA_PARAGRAFO)

    def pausa_dramatica(self) -> None:
        """Pausa mais longa para momentos dramáticos."""
        if SKIP_ANIMACOES:
            return

        time.sleep(PAUSA_DRAMATICA)

    def fade_in_texto(self, texto: str, estilo: str = "") -> None:
        """
        Efeito de fade-in simulado com caracteres.

        O texto aparece gradualmente do escuro.
        """
        if SKIP_ANIMACOES:
            if estilo:
                self.console.print(f"[{estilo}]{texto}[/{estilo}]")
            else:
                self.console.print(texto)
            return

        # Simula fade com níveis de cinza
        niveis = ["grey15", "grey30", "grey50", "grey70", "grey85"]

        for nivel in niveis:
            self.console.print(f"[{nivel}]{texto}[/{nivel}]", end="\r")
            time.sleep(0.1)

        # Versão final
        if estilo:
            self.console.print(f"[{estilo}]{texto}[/{estilo}]")
        else:
            self.console.print(texto)

    def transicao_cena(self) -> None:
        """Efeito de transição entre cenas."""
        if SKIP_ANIMACOES:
            self.console.clear()
            return

        # Fade out simulado
        self.console.print("\n" * 2)
        self.pausar(0.3)
        self.console.clear()
        self.pausar(0.3)

    def piscar_cursor(self, segundos: float = 1.0) -> None:
        """
        Exibe um cursor piscando (para esperar input).

        Útil para indicar que o jogo está esperando o jogador.
        """
        if SKIP_ANIMACOES:
            return

        cursor_on = "█"
        cursor_off = " "
        ciclos = int(segundos / 0.5)

        for _ in range(ciclos):
            self.console.print(cursor_on, end="\r")
            time.sleep(0.25)
            self.console.print(cursor_off, end="\r")
            time.sleep(0.25)

    def digitar_pensamento(self, texto: str) -> None:
        """
        Exibe um pensamento interno de Master.

        Usa estilo itálico e indentação.
        """
        linhas = texto.strip().split("\n")
        for linha in linhas:
            self.digitar(f"    [italic grey62]{linha}[/italic grey62]")
            self.pausar(0.2)

    def digitar_dialogo(self, personagem: str, texto: str, e_master: bool = False) -> None:
        """
        Exibe uma linha de diálogo.

        Args:
            personagem: Nome do personagem
            texto: O que o personagem diz
            e_master: Se é fala do Master (jogador)
        """
        if e_master:
            self.console.print(f"[grey50]Você:[/grey50]", end=" ")
            self.digitar(f"[wheat1]\"{texto}\"[/wheat1]")
        else:
            self.console.print(f"[grey70]{personagem}:[/grey70]", end=" ")
            self.digitar(f"\"{texto}\"")

    def exibir_paragrafo(self, texto: str, estilo: str = "") -> None:
        """
        Exibe um parágrafo com pausas naturais.

        Quebra o texto em frases e adiciona pausas.
        """
        # Divide por pontuação
        import re
        frases = re.split(r'([.!?]+\s*)', texto)

        for i in range(0, len(frases) - 1, 2):
            frase = frases[i] + frases[i + 1] if i + 1 < len(frases) else frases[i]
            self.digitar(frase.strip(), estilo=estilo, nova_linha=False)
            self.pausar(0.3)

        self.console.print()  # Nova linha final
