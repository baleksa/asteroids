import pygame

from constants import *  # noqa


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # noqa
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color=pygame.Color(0, 0, 0))

        pygame.display.flip()


if __name__ == "__main__":
    main()
