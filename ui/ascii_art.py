"""
ASCII Art — Arte Visual do Midnight Kitchen.

Artes ASCII que dão personalidade visual ao jogo.
"""


class AsciiArt:
    """Coleção de arte ASCII para o jogo."""

    # Logo principal do jogo - Design limpo e centralizado
    LOGO = """
[grey23]╔═══════════════════════════════════════════════════════════╗[/grey23]
[grey23]║[/grey23]                                                           [grey23]║[/grey23]
[grey23]║[/grey23]     [dark_orange]░░░░░░░[/dark_orange]                                               [grey23]║[/grey23]
[grey23]║[/grey23]    [dark_orange]░░░░░░░░░[/dark_orange]      [white]M I D N I G H T   K I T C H E N[/white]        [grey23]║[/grey23]
[grey23]║[/grey23]   [dark_orange]░░░░░░░░░░░[/dark_orange]                                             [grey23]║[/grey23]
[grey23]║[/grey23]    [dark_orange]░░░░░░░░░[/dark_orange]                                              [grey23]║[/grey23]
[grey23]║[/grey23]     [dark_orange]░░░░░░░[/dark_orange]                                               [grey23]║[/grey23]
[grey23]║[/grey23]       [dark_orange]║║║[/dark_orange]                                                 [grey23]║[/grey23]
[grey23]║[/grey23]       [dark_orange]║║║[/dark_orange]         [grey50]Uma historia de culpa,[/grey50]                  [grey23]║[/grey23]
[grey23]║[/grey23]    [dark_orange]═══╩╩╩═══[/dark_orange]          [grey50]memoria e perdao.[/grey50]                   [grey23]║[/grey23]
[grey23]║[/grey23]                                                           [grey23]║[/grey23]
[grey23]╚═══════════════════════════════════════════════════════════╝[/grey23]"""

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
