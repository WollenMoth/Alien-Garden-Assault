"""Módulo que contiene la clase HealthBar"""

from typing import overload

import pygame

from shared.colors import GREEN, RED, YELLOW
from shared.types import Coordinate


class HealthBar:
    """Clase que representa la barra de vida de un objeto"""

    def __init__(self, obj, rect: pygame.Rect):
        """Inicializa la barra de vida"""
        self.obj = obj
        self.max_health = obj.health
        self.rect = rect
        self.width = rect.width

    @overload
    def update(self) -> None:
        ...

    @overload
    def update(self, topleft: Coordinate) -> None:
        ...

    def update(self, topleft: Coordinate | None = None) -> None:
        """Actualiza la barra de vida"""
        if topleft:
            self.rect.topleft = topleft

        self.rect.width = (self.width * self.obj.health) // self.max_health

    def draw(self, screen: pygame.Surface, always_draw: bool = False):
        """Dibuja la barra de vida"""
        if always_draw or self.obj.health != self.max_health:
            if self.obj.health > 0.5 * self.max_health:
                color = GREEN
            elif self.obj.health > 0.2 * self.max_health:
                color = YELLOW
            else:
                color = RED

            pygame.draw.rect(screen, color, self.rect)
