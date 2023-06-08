from typing import List

import pygame
import time
import random

from src.commons import PLAYER_WIDTH, PLAYER_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT
from src.player import Player
from src.star import Star

Time = float

pygame.init()
pygame.font.init()

FONT = pygame.font.SysFont("JetBrains Mono", 20)
GAME_OVER_FONT = pygame.font.SysFont("JetBrains Mono", 50)

display = (SCREEN_WIDTH, SCREEN_HEIGHT)
pygame.display.set_caption("Jump Game IV")
window = pygame.display.set_mode(display)

background = pygame.transform.scale(pygame.image.load("images/bg.jpeg"), display)


def draw(player: Player, elapsed_time: Time, stars: List[Star]) -> None:
    # draw the background
    window.blit(background, (0, 0))

    # draw the time label
    time_label = FONT.render(f"Time: {round(elapsed_time)}", True, (255, 255, 255))
    window.blit(time_label, (10, 10))

    # draw the stars
    for star in stars:
        pygame.draw.rect(window, (255, 255, 255), star)

    # draw the player
    pygame.draw.rect(window, player.color, player.rect)

    # update the display
    pygame.display.update()
    return None


def main() -> None:
    player = Player(0, SCREEN_HEIGHT - Player.height, (187, 102, 147))
    stars = []
    clock = pygame.time.Clock()

    start_time = time.time()
    star_cluster_count = 0
    max_star_cluster_count = 1000

    run = True
    hit = False
    while run:
        star_cluster_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if star_cluster_count >= max_star_cluster_count:
            star_cluster_count = 0
            for _ in range(random.randint(3, 4)):
                star = Star(random.randint(0, SCREEN_WIDTH - Star.width), -20, (255, 255, 255))
                stars.append(star)

            max_star_cluster_count = max(200, max_star_cluster_count - 50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys_pressed = pygame.key.get_pressed()
        player.move(keys_pressed)

        for star in stars[:]:
            star.move()

            if star.rect.y > SCREEN_HEIGHT:
                stars.remove(star)
                continue

            if star.rect.colliderect(player.rect):
                hit = True
                stars.remove(star)
                break

        if hit:
            draw_game_over = GAME_OVER_FONT.render("Game Over", True, (255, 255, 255))
            window.blit(draw_game_over, (
                SCREEN_WIDTH // 2 - draw_game_over.get_width() // 2,
                SCREEN_HEIGHT // 2 - draw_game_over.get_height() // 2))
            pygame.display.update()
        else:
            draw(player, elapsed_time, stars)

    pygame.quit()
    return None


if __name__ == "__main__":
    main()
