import pygame

from src.commons import STAR_WIDTH, STAR_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT, STAR_VELOCITY


# create a rectangle player that can be moved from left to right
# and can jump


class Star:
    width = STAR_WIDTH
    height = STAR_HEIGHT
    velocity = STAR_VELOCITY

    def __init__(self, x: int, y: int, color: tuple) -> None:
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.color = color

    def move(self) -> None:
        self.rect.y += self.velocity
        return None
