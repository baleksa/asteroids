import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *  # noqa
from player import Player
from shot import Shot


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # noqa
    clock = pygame.time.Clock()
    dt = 0

    updatable, drawable = pygame.sprite.Group(), pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)  # type: ignore
    Asteroid.containers = (asteroids, updatable, drawable)  # type: ignore
    AsteroidField.containers = updatable  # type: ignore
    Shot.containers = (shots, updatable, drawable)  # type: ignore

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  # noqa
    asteroid_field = AsteroidField()  # noqa
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for object in drawable:
            object.draw(screen)

        for object in updatable:
            object.update(dt)

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                return

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
