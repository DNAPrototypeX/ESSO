import pygame


class Player:
    def __init__(self, screen, colour, x, y, width, height, platforms):
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

    def draw(self):
        pygame.draw.rect(self.screen, self.colour, self.rect)

    def Move(self):
        for platform in self.platforms:
            if self.is_on(platform):
                if self.rect.y < platform.rect.y + 39:
                    self.rect.bottom = platform.rect.top - 3
                    self.on_ground = True
                    self.jumps_available = 2
                else:
                    self.rect.top = platform.rect.bottom + 5
                    self.on_ground = False
        if self.on_ground:
            self.y_speed = 0

        if self.jumping:
            if self.counter < 30:
                self.counter += 1
                self.jumping = True
                self.y_speed = -3
            else:
                self.on_ground = False
                self.jumping = False
                self.counter = 0
                self.jumps_available -= 1
        else:
            self.y_speed = 3
        self.on_ground = False
        self.rect.move_ip(self.x_speed, self.y_speed)

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

    # def attack(self):







