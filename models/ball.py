"""Módulo que contiene la clase Ball."""

import math

import pygame

from shared import Coordinate, Drawable, WHITE

BALL_COLOR = WHITE
BALL_RADIUS = 10
BALL_VELOCITY = 10


class Ball(Drawable):
    """Representa una bola disparada por el cañón."""

    def __init__(self, center: Coordinate, angle: float) -> None:
        """Inicializa los atributos del objeto bola.

        Args:
            center (Coordinate): Coordenadas (x, y) del centro de la bola.
            angle (float): Ángulo de disparo de la bola en radianes.
        """
        self.center = [*center]
        self.angle = angle
        self.color = BALL_COLOR
        self.radius = BALL_RADIUS
        self.velocity_x = BALL_VELOCITY
        self.velocity_y = BALL_VELOCITY
        surface = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(surface, self.color, (self.radius, self.radius), self.radius)
        self.mask = pygame.mask.from_surface(surface)

    def draw(self, screen: pygame.Surface) -> None:
        """Dibuja la bola en la pantalla."""
        pygame.draw.circle(screen, self.color, self.center, self.radius)

    def move(self) -> None:
        """Mueve la bola en función del ángulo y la velocidad de la misma."""
        self.center[0] += int(self.velocity_x * math.cos(self.angle))
        self.center[1] += int(self.velocity_y * math.sin(self.angle))
