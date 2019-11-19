# Paul Moore

import pygame
from TitleScreen import TitleScreen
from Platform import Platform
from Player import Player
import time

pygame.init()
size = (1050, 650)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Epic Smash Siblings Omega")
done = False
clock = pygame.time.Clock()

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Vars
r = 255
g = 0
b = 0
RGB = (255, 0, 0)
font = pygame.font.SysFont(None, 48)

# Platforms
platforms = []
platforms.append(Platform(screen, BLACK, 275, 450, 500, 40))
platforms.append(Platform(screen, BLACK, 325, 350, 125, 10))
platforms.append(Platform(screen, BLACK, 465, 250, 125, 10))
platforms.append(Platform(screen, BLACK, 600, 350, 125, 10))

# Main background image
background_image = pygame.image.load('main_background.jpg').convert()

# Title screen
pygame.mixer.music.load('title_screen_theme.wav')
pygame.mixer.music.play(-1, 0.0)
title_image = pygame.image.load('smash_cover.jpeg').convert()
title_image.set_colorkey(WHITE)
title_text_image = pygame.image.load('title_text.png').convert_alpha()
play_button = TitleScreen(48, screen, 350, 575, "Press any key to play!")
play_button.colour = BLACK
git_gud = pygame.image.load('git gud.png').convert()

screen.fill(WHITE)
screen.blit(title_image, (0, 0))
screen.blit(title_text_image, (225, 50))
play_button.drawText()
pygame.display.update()
play_button.waitForPlayerToPressKey()
pygame.mixer.music.stop()
pygame.mixer.music.load('playing_theme.wav')
pygame.mixer.music.play(-1, 0.0)

# Players
players = []
players.append(Player(screen, RED, 300, 400, 20, 40, platforms))
players.append(Player(screen, GREEN, 725, 400, 20, 40, platforms))
player_1_text = TitleScreen(24, screen, 160, 600, "Player 1's stock:")
player_2_text = TitleScreen(24, screen, 460, 600, "Player 2's stock:")
player_1_health = TitleScreen(24, screen, 160, 550, "Player 1's Health:")
player_2_health = TitleScreen(24, screen, 460, 550, "Player 2's Health:")
player_info = [player_1_text, player_1_health, player_2_text, player_2_health]

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop

    # Colour loop
    if r > 0 and b == 0:
        r -= 1
        g += 1
        RGB = (r, g, b)
    elif g > 0 and r == 0:
        g -= 1
        b += 1
        RGB = (r, g, b)
    elif b > 0 and g == 0:
        r += 1
        b -= 1
        RGB = (r, g, b)

    # --- All events are detected here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                players[0].x_speed = -3
            elif event.key == pygame.K_d:
                players[0].x_speed = 3
            elif event.key == pygame.K_w:
                if players[0].jumps_available > 0:
                    players[0].jumping = True
            if event.key == pygame.K_LEFT:
                players[1].x_speed = -3
            elif event.key == pygame.K_RIGHT:
                players[1].x_speed = 3
            elif event.key == pygame.K_UP:
                if players[1].jumps_available > 0:
                    players[1].jumping = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                players[0].x_speed = 0
            elif event.key == pygame.K_d:
                players[0].x_speed = 0
            if event.key == pygame.K_LEFT:
                players[1].x_speed = 0
            elif event.key == pygame.K_RIGHT:
                players[1].x_speed = 0

    # --- Game logic should go here

    for player in players:
        player.Move()
        if player == players[0]:
            player.die(300)
        else:
            player.die(725)
        if player.stock_remaining == 0:
            done = True

    # --- Screen-clearing code goes here
    screen.fill(WHITE)

    # --- Drawing code should go here
    # Background
    screen.blit(background_image, (0, 0))
    # Platforms
    for platform in platforms:
        platform.draw_platform()

    # Players
    for player in players:
        player.draw()

    # Stocks
    for text in player_info:
        text.drawText()
    players[0].draw_health_bar(300)
    players[1].draw_health_bar(600)
    for player in players:
        for i in range(player.stock_remaining):
            if player == players[0]:
                pygame.draw.rect(screen, player.colour, (300 + (30 * i), 600, 20, 20))
            else:
                pygame.draw.rect(screen, player.colour, (600 + (30 * i), 600, 20, 20))

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
screen.blit(git_gud, (0, 0))
pygame.display.update()
time.sleep(2)
pygame.quit()
