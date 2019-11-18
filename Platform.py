import pygame
import sys


class Platform:
    def __init__(self, screen, colour, x, y, width, height):
        self.screen = screen
        self.colour = colour
        self.rect = pygame.Rect(x,  y, width, height)

    def draw_platform(self):
        pygame.draw.rect(self.screen, self.colour, self.rect)

