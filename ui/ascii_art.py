"""
ASCII Art — Arte Visual do Midnight Kitchen.

Artes ASCII que dão personalidade visual ao jogo.
"""


class AsciiArt:
    """Coleção de arte ASCII para o jogo."""

    # Logo principal do jogo - Noite chuvosa em Shinjuku
    LOGO = """
[grey15]     ╱ [/grey15][grey23]╱[/grey23]    [grey19]╱[/grey19]   [magenta]▄▀▀▀▄[/magenta]   [grey19]╱[/grey19]  [cyan]▄▀▀▄[/cyan] [grey15]╱[/grey15]   [hot_pink]▄▀▀▀▀▄[/hot_pink]  [grey19]╱[/grey19]  [grey15]╱[/grey15]
[grey19]   ╱[/grey19]   [grey15]╱[/grey15]  [grey23]╱[/grey23]   [magenta]█ 酒 █[/magenta]  [grey15]╱[/grey15]   [cyan]█▀▀█[/cyan]   [grey19]╱[/grey19]  [hot_pink]█ 24H █[/hot_pink] [grey15]╱[/grey15]   [grey19]╱[/grey19]
[grey23]  ╱[/grey23] [grey19]╱[/grey19]    [grey15]╱[/grey15]   [magenta]▀▄▄▄▀[/magenta] [grey19]╱[/grey19]    [cyan]▀▄▄▀[/cyan] [grey15]╱[/grey15]    [hot_pink]▀▄▄▄▄▀[/hot_pink]   [grey23]╱[/grey23]   [grey15]╱[/grey15]
[grey23] ╱[/grey23]    [grey15]╱[/grey15]   [grey19]╱[/grey19]    [blue]║[/blue] [grey19]╱[/grey19]  [green]▄▄▄▄▄[/green] [grey15]╱[/grey15] [blue]║[/blue]   [grey23]╱[/grey23] [deep_pink4]║[/deep_pink4]   [grey15]╱[/grey15]  [grey19]╱[/grey19]    [grey23]╱[/grey23]
[grey27]╱[/grey27]  [grey23]╱[/grey23]    [grey15]╱[/grey15]  [grey19]╱[/grey19] [blue]║[/blue][grey23]╱[/grey23]   [green]█カラオケ█[/green]  [blue]║[/blue] [grey19]╱[/grey19]  [deep_pink4]║[/deep_pink4] [grey15]╱[/grey15]   [grey23]╱[/grey23]    [grey15]╱[/grey15]  [grey19]╱[/grey19]
[grey30]▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔[/grey30]
[grey35]                     [dark_orange]┌─────────────────────┐[/dark_orange]
[grey35]                     [dark_orange]│[/dark_orange]   [orange1]░░░░░░░░░░░░░░░[/orange1]   [dark_orange]│[/dark_orange]
[grey35]      [red]░[/red]              [dark_orange]│[/dark_orange]  [orange1]░[/orange1][yellow1] 深 夜 食 堂 [/yellow1][orange1]░[/orange1]  [dark_orange]│[/dark_orange]              [red]░[/red]
[grey39]     [red]░▓░[/red]             [dark_orange]│[/dark_orange]   [orange1]░░░░░░░░░░░░░░░[/orange1]   [dark_orange]│[/dark_orange]             [red]░▓░[/red]
[grey39]     [red]░▓░[/red]             [dark_orange]├─────────────────────┤[/dark_orange]             [red]░▓░[/red]
[grey42]     [dark_red]║║║[/dark_red]             [grey62]│[/grey62][wheat1]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/wheat1][grey62]│[/grey62]             [dark_red]║║║[/dark_red]
[grey42]                     [grey62]│[/grey62][orange1]┃  ┃  ┃[/orange1] [yellow1]░▓▓░[/yellow1] [orange1]┃  ┃  ┃[/orange1][grey62]│[/grey62]
[grey46]                     [grey62]│[/grey62][orange1] ╲╱ ╲╱ [/orange1] [yellow1]░▓▓░[/yellow1] [orange1] ╲╱ ╲╱ [/orange1][grey62]│[/grey62]
[grey46]                     [grey62]│[/grey62][wheat1]▓▓▓▓▓▓▓[/wheat1][yellow3]▓▓▓▓▓▓▓[/yellow3][wheat1]▓▓▓▓▓▓▓[/wheat1][grey62]│[/grey62]
[grey50]  [grey35]▄[/grey35]                  [grey62]│[/grey62][grey19]▄[/grey19][yellow4]░░░░░░░░░░░░░░░░░░░[/yellow4][grey19]▄[/grey19][grey62]│[/grey62]                  [grey35]▄[/grey35]
[grey50]▄███▄[/grey50]          [grey30]▄▄[/grey30]   [grey19]▀[/grey19][yellow4]░░░░░░░░░░░░░░░░░░░░░[/yellow4][grey19]▀[/grey19]   [grey30]▄▄[/grey30]          [grey50]▄███▄[/grey50]
[grey54]█████[/grey54]   [grey35]▄▄▄[/grey35]  [grey39]████[/grey39]  [yellow3]░░░░░░░░░░░░░░░░░░░░░░░[/yellow3]  [grey39]████[/grey39]  [grey35]▄▄▄[/grey35]   [grey54]█████[/grey54]
[grey58]━━━━━━━━━━━━━━━━━[/grey58][yellow4]░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░[/yellow4][grey58]━━━━━━━━━━━━━━━━━[/grey58]
[grey27]▓[/grey27] [magenta dim]~[/magenta dim] [grey30]▓[/grey30] [cyan dim]~[/cyan dim] [grey23]▓[/grey23]  [yellow3]~░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░~[/yellow3]  [grey27]▓[/grey27] [hot_pink dim]~[/hot_pink dim] [grey30]▓[/grey30] [green dim]~[/green dim] [grey23]▓[/grey23]
[grey19]▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔[/grey19]

[white bold]                   M I D N I G H T   K I T C H E N[/white bold]"""

    # Lanterna japonesa (menor, para headers)
    LANTERNA_PEQUENA = """[dark_orange]
    ░░░░░░░
   ░░▓▓▓▓▓░░
   ░▓▓▓▓▓▓▓░
   ░▓░░░░░▓░
   ░▓░░░░░▓░
   ░▓▓▓▓▓▓▓░
   ░░▓▓▓▓▓░░
    ░░░░░░░
      ║║║
    ══╩╩══
[/dark_orange]"""

    # Noren (cortina de entrada)
    NOREN = """[grey50]
╭─────────────────────────────────╮
│  ┃   ┃   ┃   ┃   ┃   ┃   ┃   ┃  │
│  ┃   ┃   ┃   ┃   ┃   ┃   ┃   ┃  │
│   ╲ ╱     ╲ ╱     ╲ ╱     ╲ ╱   │
│    ╳       ╳       ╳       ╳    │
│   ╱ ╲     ╱ ╲     ╱ ╲     ╱ ╲   │
╰─────────────────────────────────╯
[/grey50]"""

    # Divisor decorativo estilo japonês
    DIVISOR = "[grey35]═══════════════════════════════════════════════════════════════════[/grey35]"

    DIVISOR_LEVE = "[grey35]───────────────────────────────────────────────────────────────────[/grey35]"

    DIVISOR_DECORATIVO = "[grey35]─────────── ◆ ─────────── ◆ ─────────── ◆ ───────────[/grey35]"

    # Ícone de relógio para o tempo
    RELOGIO = "[grey50]◷[/grey50]"

    # Indicadores de estado
    INDICADOR_FECHADO = "[grey50]◯[/grey50]"
    INDICADOR_CAUTELOSO = "[dark_khaki]◐[/dark_khaki]"
    INDICADOR_CURIOSO = "[khaki1]◑[/khaki1]"
    INDICADOR_ABERTO = "[pale_green1]◕[/pale_green1]"
    INDICADOR_VULNERAVEL = "[light_coral]●[/light_coral]"

    # Frame para cenas de noite
    FRAME_NOITE_TOP = """[dark_orange]╔══════════════════════════════════════════════════════════════════╗[/dark_orange]"""
    FRAME_NOITE_BOTTOM = """[dark_orange]╚══════════════════════════════════════════════════════════════════╝[/dark_orange]"""

    # Chama (para momentos de memória do incêndio)
    CHAMA = """[orange1]
     (
    )\\)
   ((_)
    /|
   / |
[/orange1]"""

    @classmethod
    def indicador_estado(cls, estado: str) -> str:
        """Retorna o indicador visual para um estado emocional."""
        indicadores = {
            "fechado": cls.INDICADOR_FECHADO,
            "cauteloso": cls.INDICADOR_CAUTELOSO,
            "curioso": cls.INDICADOR_CURIOSO,
            "aberto": cls.INDICADOR_ABERTO,
            "vulneravel": cls.INDICADOR_VULNERAVEL,
        }
        return indicadores.get(estado, cls.INDICADOR_FECHADO)
