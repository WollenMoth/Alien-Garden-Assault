"""Módulo que contiene la clase Cannon."""

import math

import pygame

from shared import Coordinate, Drawable, YELLOW, ORANGE
from .ball import Ball

CANNON_COLOR = YELLOW
LINE_COLOR = ORANGE
CANNON_RADIUS = 50
CANNON_WIDTH = 20
CANNON_HEIGHT = 80


class Cannon(Drawable):
    """Representa el cañón que dispara bolas."""

    def __init__(self, center: Coordinate, angle: float) -> None:
        """Inicializa los atributos del objeto cañón.

        Args:
            center (Coordinate): Coordenadas (x, y) del centro del cañón.
            angle (float): Ángulo inicial del cañón en radianes.
        """
        self.center = center
        self.angle = angle
        self.color = CANNON_COLOR
        self.radius = CANNON_RADIUS
        self.width = CANNON_WIDTH
        self.height = CANNON_HEIGHT
        self.line_color = LINE_COLOR

    def get_end(self) -> Coordinate:
        """Calcula el extremo del cañón en función del ángulo actual.

        Returns:
            Coordinate: Coordenadas (x, y) del extremo del cañón.
        """
        return (int(self.center[0] + self.height * math.cos(self.angle)),
                int(self.center[1] + self.height * math.sin(self.angle)))

    def draw(self, screen: pygame.Surface) -> None:
        """Dibuja el cañón en la pantalla."""
        end = self.get_end()
        pygame.draw.line(screen, self.line_color, self.center, end, self.width)
        pygame.draw.circle(screen, self.color, self.center, self.radius)

    def move(self, angle: float) -> None:
        """Mueve el cañón a una nueva posición en función del ángulo dado.

        Args:
            angle (float): Nuevo ángulo del cañón en radianes.
        """
        self.angle = angle

    def shoot(self) -> Ball:
        """Crea una nueva bola y la devuelve si hay bolas disponibles."""
        return Ball(self.get_end(), self.angle)
