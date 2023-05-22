"""Módulo que contiene la clase Alien"""

import math
import random

import pygame

from shared import Animated, Coordinate, load_sounds

from .alien_stats import AlienStats
from .health_bar import HealthBar


class Alien(Animated):
    """Clase que representa un alien"""

    def __init__(
        self,
        center: Coordinate,
        stats: AlienStats,
        directory,
        size: Coordinate,
        scale: int = 3,
    ):
        """Inicializa la clase Alien"""
        super().__init__(center, directory, size, fps=8, scale=scale)

        self.sprite = random.choice(list(self.sprites.keys()))
        self.health = math.ceil(stats.health)
        self.health_bar = HealthBar(
            self, pygame.Rect(self.rect.x, self.rect.y - 10, self.rect.width, 5)
        )
        self.speed = stats.speed
        self.sounds = load_sounds("alien")

    def draw(self, screen: pygame.Surface) -> None:
        """Dibuja el alien en la pantalla"""
        super().draw(screen)
        self.health_bar.draw(screen)

    def move(self) -> None:
        """Mueve el alien a la izquierda"""
        self.rect.x -= int(self.speed)
        self.health_bar.update((self.rect.x, self.rect.y - 10))

    def receive_damage(self) -> None:
        """Recibe daño"""
        self.health -= 1
        self.sounds["hit" if self.health > 0 else "death"].play()
