"""Módulo que contiene la clase Pawn"""

from shared import Coordinate

from .alien import Alien
from .stats import Stats

SPRITE_SIZE = (16, 16)


class Pawn(Alien):
    """Clase que representa un Pawn"""

    def __init__(self, center: Coordinate, stats: Stats):
        """Inicializa la clase Pawn"""
        super().__init__(center, stats, "pawns", SPRITE_SIZE)
