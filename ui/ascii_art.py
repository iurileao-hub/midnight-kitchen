"""
ASCII Art — Arte Visual do Midnight Kitchen.

Artes ASCII que dão personalidade visual ao jogo.
"""


class AsciiArt:
    """Coleção de arte ASCII para o jogo."""

    # Logo principal do jogo - Beco de Shinjuku com restaurante ao fundo
    LOGO = """
[grey30]                                  _[/grey30]
[grey30]                             ___/[/grey30]   [grey30]\\___[/grey30]
[grey30]                        ____/[/grey30]   [grey42]∥ ∥[/grey42]   [grey30]\\____[/grey30]
[grey50]             ~~~~~~~~/~~~~~∥~∥~∥~~~~~\\~~~~~~~~[/grey50]
[grey30]            ____/[/grey30]         [grey42]∥ ∥ ∥[/grey42]         [grey30]\\____[/grey30]
[grey30]       ____/[/grey30]     [dark_orange]░░░░░[/dark_orange]   [grey42]∥ ∥ ∥[/grey42]   [dark_orange]░░░░░[/dark_orange]     [grey30]\\____[/grey30]
[grey30]  ____/[/grey30]         [dark_orange]░▓▓▓▓░[/dark_orange]  [grey42]∥ ∥ ∥[/grey42]  [dark_orange]░▓▓▓▓░[/dark_orange]         [grey30]\\____[/grey30]
[grey27] |▒▒|[/grey27]  [grey50]▪───▪[/grey50]   [orange1]░▓▓▓░[/orange1]              [orange1]░▓▓▓░[/orange1]   [grey50]▪───▪[/grey50]  [grey27]|▒▒|[/grey27]
[grey27] |▒▒|[/grey27]  [grey50]│[/grey50][yellow3]▓▓▓[/yellow3][grey50]│[/grey50]    [dark_orange]║║║[/dark_orange]                [dark_orange]║║║[/dark_orange]    [grey50]│[/grey50][yellow3]▓▓▓[/yellow3][grey50]│[/grey50]  [grey27]|▒▒|[/grey27]
[grey27] |▒▒|[/grey27]  [grey50]▪───▪[/grey50]       [grey62]┌──────────────────┐[/grey62]       [grey50]▪───▪[/grey50]  [grey27]|▒▒|[/grey27]
[grey27] |▒▒|[/grey27]  [grey50]▪───▪[/grey50]       [grey62]│[/grey62] [dark_orange]深  夜  食  堂[/dark_orange] [grey62]│[/grey62]       [grey50]▪───▪[/grey50]  [grey27]|▒▒|[/grey27]
[grey27] |▒▒|[/grey27]  [grey50]│[/grey50][wheat1]░░░[/wheat1][grey50]│[/grey50]       [grey62]├──────────────────┤[/grey62]       [grey50]│[/grey50][wheat1]░░░[/wheat1][grey50]│[/grey50]  [grey27]|▒▒|[/grey27]
[grey27] |▒▒|[/grey27]  [grey50]▪───▪[/grey50]       [grey62]│[/grey62][grey70]┃ ┃ ┃[/grey70] [orange1]▒▒[/orange1] [grey70]┃ ┃ ┃[/grey70][grey62]│[/grey62]       [grey50]▪───▪[/grey50]  [grey27]|▒▒|[/grey27]
[grey27] |▒▒|[/grey27]              [grey62]│[/grey62] [grey70]╲╱╲╱[/grey70] [orange1]▒▒[/orange1] [grey70]╲╱╲╱[/grey70] [grey62]│[/grey62]              [grey27]|▒▒|[/grey27]
[grey27] |▒▒|[/grey27][grey19]_____________[/grey19][grey62]│[/grey62][grey19]____[/grey19][yellow4]▒▒▒▒▒▒[/yellow4][grey19]____[/grey19][grey62]│[/grey62][grey19]_____________[/grey19][grey27]|▒▒|[/grey27]
[grey23] |[/grey23][grey30]░░░    ░░[/grey30]       [yellow4]░░░░░░░░░░[/yellow4]       [grey30]░░    ░░░[/grey30][grey23]|[/grey23]
[grey19] |___________________[/grey19][grey30]░░░░░░[/grey30][grey19]___________________|[/grey19]

[white bold]                M I D N I G H T   K I T C H E N[/white bold]"""

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
