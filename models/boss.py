"""Módulo que contiene la clase Boss"""

import random
from shared import Animated, Coordinate

SPRITE_SIZE = (32, 32)


class Boss(Animated):
    """Clase que representa un Boss"""

    def __init__(self, center: Coordinate):
        """Inicializa la clase Boss"""
        super().__init__(center, "bosses", SPRITE_SIZE, fps=8, scale=3)

        self.sprite = random.choice(list(self.sprites.keys()))
