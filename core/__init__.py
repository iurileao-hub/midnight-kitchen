"""
Core — Núcleo do Midnight Kitchen.

Contém o loop principal, gerenciamento de estado,
sistema de tempo e persistência.
"""

from .tempo import SistemaTempo
from .save import SistemaSave
from .game import Game
from .scene import GerenciadorCenas

__all__ = ["SistemaTempo", "SistemaSave", "Game", "GerenciadorCenas"]
