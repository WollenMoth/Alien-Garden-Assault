"""Módulo que contiene la clase Pawn"""

from shared import Coordinate
from .alien import Alien

SPRITE_SIZE = (16, 16)


class Pawn(Alien):
    """Clase que representa un Pawn"""

    def __init__(self, center: Coordinate, health: int):
        """Inicializa la clase Pawn"""
        super().__init__(center, health, "pawns", SPRITE_SIZE)
