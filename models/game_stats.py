"""Módulo que contiene la clase GameStats"""

from typing import Type

from .alien_stats import AlienStats
from .boss import Boss
from .knight import Knight
from .pawn import Pawn

AlienTypes = dict[Type[Pawn] | Type[Knight] | Type[Boss], AlienStats]


class GameStats:
    """Clase que contiene las estadísticas del juego"""

    def __init__(
        self, spawn_delay: int, spawn_number: int, spawn_prob: float, types: AlienTypes
    ):
        self.spawn_delay = spawn_delay
        self.spawn_number = spawn_number
        self.spawn_prob = spawn_prob
        self.types = types
