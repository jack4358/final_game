import pygame
from settings import Settings

class Ufo:
    screen = pygame.display.set_mode((1000, 1000))
    screen_rect = screen.get_rect()

    def __init__(self):
        self.settings = Settings()
        self.image = pygame.image.load('final_game\enemy.png')
        self.rect = self.image.get_rect()

        # Start each new ufo at middle left of screen.
        self.rect.x = 200
        self.rect.y = 550

        # Store a decimal value for the ufo's horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def update(self, screen_rect):
        """Update the ufo's position based on the movement flags."""
        # Update the ufo's x value, not the rect.
        if self.moving_right and self.rect.right < screen_rect.right:
            self.x += self.settings.ufo_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ufo_speed
        if self.moving_up and self.rect.top > 0:
            self.y += self.settings.ufo_up_speed
        if self.moving_down and self.rect.bottom < screen_rect.bottom:
            self.y += self.settings.ufo_down_speed

        # Update rect object from self.x and self.y.
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self, screen):
        """Draw the ufo at its current location"""
        screen.blit(self.image, self.rect)
