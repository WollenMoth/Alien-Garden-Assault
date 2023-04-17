"""Módulo que contiene la clase Knight"""

import random
from shared import Animated, Coordinate

SPRITE_SIZE = (16, 16)


class Knight(Animated):
    """Clase que representa un Knight"""

    def __init__(self, center: Coordinate):
        """Inicializa la clase Knight"""
        super().__init__(center, "knights", SPRITE_SIZE, fps=8, scale=4)

        self.sprite = random.choice(list(self.sprites.keys()))
