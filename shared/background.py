"""Módulo que contiene la clase Background"""

import pygame

from .drawable import Drawable
from .types import Coordinate


class Background(Drawable):
    """Clase que representa el fondo del juego"""

    def __init__(self, tile_size: Coordinate):
        """Inicializa la clase Background"""
        image = pygame.image.load("images/background/tile.png").convert_alpha()
        self.tile = pygame.transform.scale(image, tile_size)

    def draw(self, screen: pygame.Surface):
        """Dibuja el fondo del juego"""

        s_width, s_height = screen.get_size()
        t_width, t_height = self.tile.get_size()

        for x in range(0, s_width, t_width):
            for y in range(0, s_height, t_height):
                screen.blit(self.tile, (x, y))
