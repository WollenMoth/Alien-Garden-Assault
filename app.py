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

from models import Alien, Ball, Boss, Cannon, Knight, Pawn, Stats
from shared import BLACK, FPS, Background, Drawable

TILE_SIZE = 96
WIDTH, HEIGHT = TILE_SIZE * 15, TILE_SIZE * 8

CANNON_HEALTH = 20

SPAWN_DELAY = 5000
SPAWN_NUMBER = 4
SPAWN_PROB = 0.5
TYPES = {
    Pawn: Stats(1, 3, 0.6),
    Knight: Stats(3, 2, 0.3),
    Boss: Stats(5, 1, 0.1),
}

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

    screen_rect = screen.get_rect()
    balls_to_remove = set()
    aliens_to_remove = set()

    for ball in balls:
        ball.move()
        ball_rect = ball.mask.get_rect(center=ball.center)
        if not screen_rect.colliderect(ball_rect):
            balls_to_remove.add(ball)

    for alien in aliens:
        alien.move()
        if not screen_rect.colliderect(alien.rect):
            cannon.receive_damage(math.ceil(alien.health))
            aliens_to_remove.add(alien)

        for ball in balls:
            offset = (ball.center[0] - alien.rect.x, ball.center[1] - alien.rect.y)
            if alien.mask.overlap_area(ball.mask, offset):
                alien.receive_damage()
                balls_to_remove.add(ball)

                if alien.health <= 0:
                    aliens_to_remove.add(alien)

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
    types = list(TYPES.keys())
    types_prob = [TYPES[t].prob for t in types]

    selection = random.choices(types, types_prob, k=HEIGHT // TILE_SIZE)

    x = WIDTH - TILE_SIZE // 2
    y = TILE_SIZE // 2

    return [
        t((x, y + i * TILE_SIZE), TYPES[t])
        for i, t in enumerate(selection)
        if random.random() < SPAWN_PROB
    ]


def start_round() -> None:
    """Comienza una nueva ronda"""
    pygame.time.set_timer(pygame.USEREVENT, SPAWN_DELAY, SPAWN_NUMBER)
    pygame.time.set_timer(pygame.USEREVENT + 1, SPAWN_DELAY * SPAWN_NUMBER)


def increase_difficulty() -> None:
    """Aumenta la dificultad del juego"""
    globals()["SPAWN_DELAY"] = max(500, SPAWN_DELAY - 100)
    globals()["SPAWN_NUMBER"] = min(50, SPAWN_NUMBER + 1)
    globals()["SPAWN_PROB"] = min(1, SPAWN_PROB + 0.05)

    for stats in TYPES.values():
        stats.health = min(100, stats.health * 1.1)
        stats.speed = min(10, stats.speed * 1.1)
        stats.prob = max(0.05, stats.prob - 0.02)

    TYPES[Boss].prob = 1 - sum(s.prob for t, s in TYPES.items() if t != Boss)


def main() -> None:
    """Función principal del juego"""
    running = True

    clock = pygame.time.Clock()

    background = Background((TILE_SIZE, TILE_SIZE))

    cannon = Cannon((0, HEIGHT // 2), 0, CANNON_HEALTH)

    balls: list[Ball] = []

    aliens = generate_aliens()

    last_pressed = False

    start_round()
    spawns_finished = False

    while running:
        clock.tick(FPS)

        draw([background, cannon, *balls, *aliens])

        handle_movement(cannon, balls, aliens)

        last_pressed = handle_shooting(cannon, balls, last_pressed)

        if spawns_finished and not aliens:
            increase_difficulty()
            start_round()
            spawns_finished = False

        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                aliens.extend(generate_aliens())
            elif event.type == pygame.USEREVENT + 1:
                spawns_finished = True
            elif event.type == pygame.QUIT:
                running = False
                break

    pygame.quit()


if __name__ == "__main__":
    main()
