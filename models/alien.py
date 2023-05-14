"""Módulo que contiene la clase Alien"""

import random
from shared import Animated, Coordinate

class Alien(Animated):
    """Clase que representa un alien"""

    def __init__(self, center: Coordinate, directory, size: Coordinate, scale: int = 3):
        """Inicializa la clase Alien"""
        super().__init__(center, directory, size, fps=8, scale=scale)

        self.sprite = random.choice(list(self.sprites.keys()))

    def move(self, speed) -> None:
        """Mueve el alien a la izquierda"""
        self.rect.x -= speed
