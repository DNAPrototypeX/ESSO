import pygame


class Player:
    def __init__(self, screen, colour, x, y, width, height, platforms, ID):
        self.colour = colour
        self.screen = screen
        self.x_speed = 0
        self.y_speed = 3
        self.on_ground = False
        self.platforms = platforms
        self.rect = pygame.Rect(x, y, width, height)
        self.jumping = False
        self.counter = 0
        self.jumps_available = 2
        self.stock_remaining = 3
        self.health = 100
        self.attacking = False
        self.sword_offset = 0
        self.sword_rect = pygame.Rect(self.rect.x + self.sword_offset, self.rect.y + 25, 20, 10)
        self.ID = ID
        self.direction = ""
        self.is_RGB = False
        self.RGB = [255, 0, 0]

    def draw(self):
        if self.is_RGB:
            if self.RGB[0] > 0 and self.RGB[2] == 0:
                self.RGB[0] -= 5
                self.RGB[1] += 5
            elif self.RGB[1] > 0 and self.RGB[0] == 0:
                self.RGB[1] -= 5
                self.RGB[2] += 5
            elif self.RGB[2] > 0 and self.RGB[1] == 0:
                self.RGB[0] += 5
                self.RGB[2] -= 5
            self.colour = self.RGB
        pygame.draw.rect(self.screen, self.colour, self.rect)
        if self.attacking:
            pygame.draw.rect(self.screen, self.colour, self.sword_rect)

    def Move(self):
        for platform in self.platforms:
            if self.is_on(platform):
                if self.rect.y < platform.rect.y + 39:
                    self.rect.bottom = platform.rect.top - 4
                    self.on_ground = True
                    self.jumps_available = 2
                else:
                    self.rect.top = platform.rect.bottom + 5
                    self.on_ground = False
        if self.on_ground:
            self.y_speed = 0

        if self.jumping:
            if self.counter < 25:
                self.counter += 1
                self.jumping = True
                self.y_speed = -4
            else:
                self.on_ground = False
                self.jumping = False
                self.counter = 0
                self.jumps_available -= 1
        else:
            self.y_speed = 4
        self.on_ground = False
        self.rect.move_ip(self.x_speed, self.y_speed)
        self.sword_rect.x = self.rect.x + self.sword_offset
        self.sword_rect.y = self.rect.y + 15

    def is_on(self, platform):
        return (pygame.Rect(self.rect.x, self.rect.y + self.y_speed + 1,
                            self.rect.width, self.rect.height)
                .colliderect(platform.rect))

    def die(self, x):
        if self.rect.y > 750 or self.health < 0 or self.rect.x <= - 100 or self.rect.x >= 1150:
            self.stock_remaining -= 1
            self.rect.x = x
            self.rect.y = 400
            self.health = 100

    def draw_health_bar(self, x):
        pygame.draw.rect(self.screen, (0, 255, 0), (x, 550, self.health, 20))

    def attack(self, players):
        if self.direction == "RIGHT":
            self.sword_offset = 20
        else:
            self.sword_offset = -20
        if self.attacking:
            if self.ID == 0:
                if pygame.Rect(self.sword_rect).colliderect(players[1]):
                    players[1].health -= 1
            elif self.ID == 1:
                if pygame.Rect(self.sword_rect).colliderect(players[0]):
                    players[0].health -= 1
