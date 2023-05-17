"""Módulo que contiene la clase Stats"""


class Stats:
    """Clase que contiene las estadísticas de un Alien"""

    def __init__(self, health: float, speed: float, prob: float):
        """Inicializa la clase Stats"""
        self.health = health
        self.speed = speed
        self.prob = prob
