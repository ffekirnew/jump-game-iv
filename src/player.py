import pygame

from src.commons import PLAYER_WIDTH, PLAYER_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_VELOCITY


# create a rectangle player that can be moved from left to right
# and can jump


class Player:
    width = PLAYER_WIDTH
    height = PLAYER_HEIGHT
    velocity = PLAYER_VELOCITY

    def __init__(self, x: int, y: int, color: tuple) -> None:
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.color = color

    def move(self, keys_pressed) -> None:
        if keys_pressed[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.velocity
        if keys_pressed[pygame.K_RIGHT] and self.rect.x < SCREEN_WIDTH - self.width:
            self.rect.x += self.velocity
        return None
