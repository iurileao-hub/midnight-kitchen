"""
UI — Interface Visual do Midnight Kitchen.

Sistema de renderização usando a biblioteca rich
para criar uma experiência visual elegante no terminal.
"""

from .styles import Tema
from .components import Componentes
from .effects import Efeitos
from .renderer import Renderer

__all__ = ["Tema", "Componentes", "Efeitos", "Renderer"]
