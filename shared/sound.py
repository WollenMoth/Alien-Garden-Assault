"""Módulo que contiene funciones para reproducir sonidos"""

from os import listdir
from os.path import isfile, join

import pygame


def load_sounds(directory: str = "default") -> dict[str, pygame.mixer.Sound]:
    """Carga los sonidos de un directorio"""
    path = join("sounds", directory)
    sounds = [f for f in listdir(path) if isfile(join(path, f))]

    return {s.replace(".mp3", ""): pygame.mixer.Sound(join(path, s)) for s in sounds}
