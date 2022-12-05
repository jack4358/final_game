import pygame
from settings import Settings

class Meteor:
    screen = pygame.display.set_mode((1000, 1000))
    screen_rect = screen.get_rect()

    def __init__(self):
        self.settings = Settings()
        self.image = pygame.image.load('final_game\ufo.png')

        self.rect = self.image.get_rect()
        # Start each new ufo at middle left of screen.

        self.rect.x = 200
        self.rect.y = 650

        # Store a decimal value for the ufo's horizontal position.
        self.x = float(self.rect.x)

    def update(self):
        """Move the ufo right or left."""
        self.check_edges()
        self.x += (self.settings.ufo_speed * self.settings.ufo_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Return True if ufo is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            self.settings.ufo_direction = -1 * self.settings.ufo_direction

    def blitme(self, screen):
        """Draw the ufo at its current location"""
        screen.blit(self.image, self.rect)