"""
Styles — Sistema de Estilos do Midnight Kitchen.

Define cores, temas e estilos consistentes usando rich.
"""

from rich.style import Style
from rich.theme import Theme as RichTheme

from config import CORES


class Tema:
    """
    Gerencia os estilos visuais do jogo.

    Usa a biblioteca rich para criar estilos consistentes
    que evocam a atmosfera de um restaurante noturno em Tóquio.
    """

    # Estilos base
    TEXTO = Style(color=CORES["texto"])
    TEXTO_SUTIL = Style(color=CORES["texto_sutil"])
    DESTAQUE = Style(color=CORES["destaque"], bold=True)

    # Estados emocionais dos clientes
    FECHADO = Style(color=CORES["fechado"])
    CAUTELOSO = Style(color=CORES["cauteloso"])
    CURIOSO = Style(color=CORES["curioso"])
    ABERTO = Style(color=CORES["aberto"])
    VULNERAVEL = Style(color=CORES["vulneravel"], bold=True)

    # UI
    BORDA = Style(color=CORES["borda"])
    BORDA_ATIVA = Style(color=CORES["borda_ativa"])
    TITULO = Style(color=CORES["primaria"], bold=True)
    SUBTITULO = Style(color=CORES["secundaria"])

    # Menu
    MENU_ITEM = Style(color=CORES["menu_item"])
    MENU_SELECIONADO = Style(color=CORES["menu_selecionado"], bold=True)
    MENU_NUMERO = Style(color=CORES["primaria"], bold=True)
    MENU_DICA = Style(color=CORES["texto_sutil"], italic=True)

    # Tempo
    RELOGIO = Style(color=CORES["relogio"])
    RELOGIO_URGENTE = Style(color=CORES["relogio_urgente"], bold=True)

    # Especiais
    PENSAMENTO = Style(color="grey62", italic=True)
    MEMORIA = Style(color=CORES["memoria"])
    DIALOGO_CLIENTE = Style(color=CORES["texto"])
    DIALOGO_MASTER = Style(color=CORES["destaque"])

    # Feedback
    ERRO = Style(color=CORES["erro"])
    SUCESSO = Style(color=CORES["sucesso"])

    @classmethod
    def get_rich_theme(cls) -> RichTheme:
        """
        Retorna um tema rich para uso com Console.

        Permite usar markup como [titulo]Texto[/titulo].
        """
        return RichTheme({
            "texto": cls.TEXTO,
            "sutil": cls.TEXTO_SUTIL,
            "destaque": cls.DESTAQUE,
            "titulo": cls.TITULO,
            "subtitulo": cls.SUBTITULO,
            "borda": cls.BORDA,
            "menu.item": cls.MENU_ITEM,
            "menu.numero": cls.MENU_NUMERO,
            "menu.dica": cls.MENU_DICA,
            "relogio": cls.RELOGIO,
            "relogio.urgente": cls.RELOGIO_URGENTE,
            "pensamento": cls.PENSAMENTO,
            "memoria": cls.MEMORIA,
            "cliente": cls.DIALOGO_CLIENTE,
            "master": cls.DIALOGO_MASTER,
            "erro": cls.ERRO,
            "sucesso": cls.SUCESSO,
            # Estados
            "estado.fechado": cls.FECHADO,
            "estado.cauteloso": cls.CAUTELOSO,
            "estado.curioso": cls.CURIOSO,
            "estado.aberto": cls.ABERTO,
            "estado.vulneravel": cls.VULNERAVEL,
        })

    @classmethod
    def estilo_por_estado(cls, estado: str) -> Style:
        """Retorna o estilo correspondente a um estado emocional."""
        estilos = {
            "fechado": cls.FECHADO,
            "cauteloso": cls.CAUTELOSO,
            "curioso": cls.CURIOSO,
            "aberto": cls.ABERTO,
            "vulneravel": cls.VULNERAVEL,
        }
        return estilos.get(estado, cls.TEXTO)

    @classmethod
    def cor_por_estado(cls, estado: str) -> str:
        """Retorna a cor correspondente a um estado emocional."""
        return CORES.get(estado, CORES["texto"])
