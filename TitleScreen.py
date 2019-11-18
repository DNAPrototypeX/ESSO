import pygame
import sys

class TitleScreen:
    def __init__(self, size, screen, x, y, text):
        self.text = text
        self.font = pygame.font.SysFont(None, size)
        self.screen = screen
        self.colour = (0, 0, 0)
        self.x = x
        self.y = y

    def terminate(self):
        pygame.quit()
        sys.exit()

    def waitForPlayerToPressKey(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # pressing escape quits
                        self.terminate()

                    return

    def drawText(self):
        textobject = self.font.render(self.text, 1, self.colour)
        textrect = textobject.get_rect()
        textrect.topleft = (self.x, self.y)
        self.screen.blit(textobject, textrect)
