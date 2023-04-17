"""Módulo que contiene la clase Pawn"""

import random
from shared import Animated, Coordinate

SPRITE_SIZE = (16, 16)


class Pawn(Animated):
    """Clase que representa un Pawn"""

    def __init__(self, center: Coordinate):
        """Inicializa la clase Pawn"""
        super().__init__(center, "pawns", SPRITE_SIZE, fps=8, scale=3)

        self.sprite = random.choice(list(self.sprites.keys()))
