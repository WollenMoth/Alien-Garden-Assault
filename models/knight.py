"""Módulo que contiene la clase Knight"""

from shared import Coordinate

from .alien import Alien
from .alien_stats import AlienStats

SPRITE_SIZE = (16, 16)


class Knight(Alien):
    """Clase que representa un Knight"""

    def __init__(self, center: Coordinate, stats: AlienStats):
        """Inicializa la clase Knight"""
        super().__init__(center, stats, "knights", SPRITE_SIZE, scale=4)
