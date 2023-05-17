"""Módulo que contiene la clase Boss"""

from shared import Coordinate

from .alien import Alien
from .alien_stats import AlienStats

SPRITE_SIZE = (32, 32)


class Boss(Alien):
    """Clase que representa un Boss"""

    def __init__(self, center: Coordinate, stats: AlienStats):
        """Inicializa la clase Boss"""
        super().__init__(center, stats, "bosses", SPRITE_SIZE)
