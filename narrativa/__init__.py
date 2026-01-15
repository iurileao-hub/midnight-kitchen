"""
Narrativa — Conteúdo Textual do Midnight Kitchen.

Toda a prosa, descrições, diálogos e ambientação
que dão vida ao jogo.
"""

from .abertura import Abertura, TextosMenu
from .onboarding import Onboarding

__all__ = ["Abertura", "TextosMenu", "Onboarding"]
