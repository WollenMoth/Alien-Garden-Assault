"""Módulo para cargar los sprites"""

from os import listdir
from os.path import isfile, join

import pygame

from .types import Coordinate


def flip(sprites: tuple[pygame.Surface, ...]) -> tuple[pygame.Surface, ...]:
    """Invierte los sprites"""
    return tuple(pygame.transform.flip(s, True, False) for s in sprites)


def get_sprites(
    sprite_sheet: pygame.Surface, size: Coordinate, scale: int
) -> tuple[pygame.Surface, ...]:
    """Obtiene los sprites de un sprite sheet"""
    sprites = []

    for i in range(0, sprite_sheet.get_width(), size[0]):
        surface = pygame.Surface(size, pygame.SRCALPHA, 32)
        rect = pygame.Rect(i, 0, size[0], size[1])
        surface.blit(sprite_sheet, (0, 0), rect)
        sprites.append(pygame.transform.scale_by(surface, scale))

    return tuple(sprites)


def load_sprites(
    directory: str, size: Coordinate, flipped: bool = False, scale: int = 2
) -> dict[str, tuple[pygame.Surface, ...]]:
    """Carga los sprites de un directorio"""
    path = join("images", directory)
    images = [f for f in listdir(path) if isfile(join(path, f))]

    all_sprites = {}

    for image in images:
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()

        sprites = get_sprites(sprite_sheet, size, scale)
        name = image.replace(".png", "")

        if flipped:
            all_sprites[name + "_right"] = sprites
            all_sprites[name + "_left"] = flip(sprites)
        else:
            all_sprites[name] = flip(sprites)

    return all_sprites
