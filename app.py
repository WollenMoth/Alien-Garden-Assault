"""Alien Garden Assault

El juego consiste de un cañón que dispara balas a los aliens que se encuentran en el jardín,
el jugador debe destruir a todos los aliens para pasar de nivel,
cada nivel aumenta la dificultad del juego.

Autores:
    - Ángel Ricardo Gutierrez Meza (201847467)
    - Crhistian André Díaz Bonfigli Pastrana (201829189)
"""

import math
import random

import pygame

from models import Alien, Ball, Boss, Cannon, Knight, Pawn
from shared import BLACK, FPS, Background, Drawable

TILE_SIZE = 96
WIDTH, HEIGHT = TILE_SIZE * 15, TILE_SIZE * 8

SPAWN_DELAY = 5000
SPEED = 3

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Alien Garden Assault")


def draw(objects: list[Drawable]) -> None:
    """Dibuja todos los elementos en la pantalla"""
    screen.fill(BLACK)

    for obj in objects:
        obj.draw(screen)

    pygame.display.flip()


def handle_movement(cannon: Cannon, balls: list[Ball], aliens: list[Alien]) -> None:
    """Maneja el movimiento del cañón"""
    pos = pygame.mouse.get_pos()
    angle = math.atan2(*(pos[i] - cannon.center[i] for i in [1, 0]))

    cannon.move(angle)

    for ball in balls:
        ball.move()

    aliens_to_remove = []

    for alien in aliens:
        alien.move(SPEED)

        balls_to_remove = []

        for ball in balls:
            offset = (ball.center[0] - alien.rect.x, ball.center[1] - alien.rect.y)
            if alien.mask.overlap_area(ball.mask, offset):
                alien.receive_damage()
                balls_to_remove.append(ball)

                if alien.health <= 0:
                    aliens_to_remove.append(alien)

        for ball in balls_to_remove:
            balls.remove(ball)

    for alien in aliens_to_remove:
        aliens.remove(alien)


def handle_shooting(cannon: Cannon, balls: list[Ball], last_pressed: bool) -> bool:
    """Manera el disparo del cañón"""
    pressed = pygame.mouse.get_pressed()[0]

    if pressed and not last_pressed:
        balls.append(cannon.shoot())

    return pressed


def generate_aliens() -> list[Alien]:
    """Genera una oleada de aliens aleatorios al final del jardín"""
    types = (Pawn, Knight, Boss)
    types_prob = (0.6, 0.3, 0.1)
    healths = (1, 3, 5)

    selection = random.choices(types, types_prob, k=HEIGHT // TILE_SIZE)

    x = WIDTH - TILE_SIZE // 2
    y = TILE_SIZE // 2

    aliens = []

    for i, alien_type in enumerate(selection):
        if random.random() < 0.5:
            continue

        center = (x, y + i * TILE_SIZE)
        health = healths[types.index(alien_type)]

        aliens.append(alien_type(center, health))

    return aliens


def main() -> None:
    """Función principal del juego"""
    running = True

    clock = pygame.time.Clock()

    background = Background((TILE_SIZE, TILE_SIZE))

    cannon = Cannon((0, HEIGHT // 2), 0)

    balls: list[Ball] = []

    aliens = generate_aliens()

    last_pressed = False

    pygame.time.set_timer(pygame.USEREVENT, SPAWN_DELAY)

    while running:
        clock.tick(FPS)

        draw([background, cannon, *balls, *aliens])

        handle_movement(cannon, balls, aliens)

        last_pressed = handle_shooting(cannon, balls, last_pressed)

        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                aliens.extend(generate_aliens())
            elif event.type == pygame.QUIT:
                running = False
                break

    pygame.quit()


if __name__ == "__main__":
    main()
