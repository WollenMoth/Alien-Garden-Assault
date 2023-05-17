"""Módulo que contiene la clase Alien"""

import random

from shared import Animated, Coordinate, load_sounds

from .stats import Stats


class Alien(Animated):
    """Clase que representa un alien"""

    def __init__(
        self,
        center: Coordinate,
        stats: Stats,
        directory,
        size: Coordinate,
        scale: int = 3,
    ):
        """Inicializa la clase Alien"""
        super().__init__(center, directory, size, fps=8, scale=scale)

        self.sprite = random.choice(list(self.sprites.keys()))
        self.health = stats.health
        self.speed = stats.speed
        self.sounds = load_sounds("alien")

    def move(self) -> None:
        """Mueve el alien a la izquierda"""
        self.rect.x -= int(self.speed)

    def receive_damage(self) -> None:
        """Recibe daño"""
        self.health -= 1
        self.sounds["hit" if self.health > 0 else "death"].play()
