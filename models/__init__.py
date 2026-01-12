"""
Models - Classes base do Midnight Kitchen.

Classes:
    - Cliente: Um visitante do restaurante
    - Prato: Uma receita que pode ser preparada
    - Memoria: Uma peca do quebra-cabeca
    - Jogo: Estado central do jogo
"""

from .cliente import Cliente
from .prato import Prato
from .memoria import Memoria
from .jogo import Jogo

__all__ = ["Cliente", "Prato", "Memoria", "Jogo"]
