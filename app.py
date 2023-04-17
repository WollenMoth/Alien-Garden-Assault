"""Alien Garden Assault

El juego consiste de un cañón que dispara balas a los aliens que se encuentran en el jardín,
el jugador debe destruir a todos los aliens para pasar de nivel,
cada nivel aumenta la dificultad del juego.

Autores:
    - Ángel Ricardo Gutierrez Meza (201847467)
    - Crhistian André Díaz Bonfigli Pastrana (201829189)
"""

import pygame

from shared import Animated, BLACK, FPS

TILE_SIZE = 96
WIDTH, HEIGHT = TILE_SIZE * 15, TILE_SIZE * 8

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Alien Garden Assault")


def draw(objects: list[Animated]) -> None:
    """Dibuja todos los elementos en la pantalla"""
    screen.fill(BLACK)

    for obj in objects:
        obj.draw(screen)

    pygame.display.flip()


def main() -> None:
    """Función principal del juego"""
    running = True

    clock = pygame.time.Clock()

    while running:
        clock.tick(FPS)

        draw([])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

    pygame.quit()


if __name__ == "__main__":
    main()
