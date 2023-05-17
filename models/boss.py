"""Módulo que contiene la clase Boss"""

from shared import Coordinate

from .alien import Alien

SPRITE_SIZE = (32, 32)


class Boss(Alien):
    """Clase que representa un Boss"""

    def __init__(self, center: Coordinate, health: int):
        """Inicializa la clase Boss"""
        super().__init__(center, health, "bosses", SPRITE_SIZE)
