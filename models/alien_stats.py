"""Módulo que contiene la clase AlienStats"""


class AlienStats:
    """Clase que contiene las estadísticas de un Alien"""

    def __init__(self, health: float, speed: float, prob: float):
        """Inicializa la clase AlienStats"""
        self.health = health
        self.speed = speed
        self.prob = prob
