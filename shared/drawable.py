"""Módulo que contiene la clase Drawable"""

from abc import ABC, abstractmethod


class Drawable(ABC):
    """Clase abstracta que representa un objeto que se puede dibujar"""

    @abstractmethod
    def draw(self, screen):
        """Dibuja el objeto en la pantalla"""
