"""Alien Garden Assault

El juego consiste de un cañón que dispara balas a los aliens que se encuentran en el jardín,
el jugador debe destruir a todos los aliens para pasar de nivel,
cada nivel aumenta la dificultad del juego.

Autores:
    - Ángel Ricardo Gutierrez Meza (201847467)
    - Crhistian André Díaz Bonfigli Pastrana (201829189)
"""

import math

import pygame

from models import Ball, Cannon
from shared import Background, Drawable, BLACK, FPS

TILE_SIZE = 96
WIDTH, HEIGHT = TILE_SIZE * 15, TILE_SIZE * 8

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Alien Garden Assault")


def draw(objects: list[Drawable]) -> None:
    """Dibuja todos los elementos en la pantalla"""
    screen.fill(BLACK)

    for obj in objects:
        obj.draw(screen)

    pygame.display.flip()


def handle_movement(cannon: Cannon) -> None:
    """Maneja el movimiento del cañón"""
    pos = pygame.mouse.get_pos()
    angle = math.atan2(*(pos[i] - cannon.center[i] for i in [1, 0]))

    cannon.move(angle)


def handle_shooting(cannon: Cannon, balls: list[Ball], last_pressed: bool) -> bool:
    """Manera el disparo del cañón"""
    pressed = pygame.mouse.get_pressed()[0]

    if pressed and not last_pressed:
        balls.append(cannon.shoot())

    return pressed


def main() -> None:
    """Función principal del juego"""
    running = True

    clock = pygame.time.Clock()

    background = Background((TILE_SIZE, TILE_SIZE))

    cannon = Cannon((0, HEIGHT // 2), 0)

    balls: list[Ball] = []

    last_pressed = False

    while running:
        clock.tick(FPS)

        draw([background, cannon, *balls])

        handle_movement(cannon)

        last_pressed = handle_shooting(cannon, balls, last_pressed)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

    pygame.quit()


if __name__ == "__main__":
    main()
