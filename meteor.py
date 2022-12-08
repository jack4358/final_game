import pygame
from settings import Settings

class Meteor:
    screen = pygame.display.set_mode((1000, 1000))
    screen_rect = screen.get_rect()

    def __init__(self):
        self.settings = Settings()
        self.image = pygame.image.load('final_game\meteor.png')
        self.rect = self.image.get_rect()

        # Start each new meteor towards top right of the screen.
        self.rect.x = 800
        self.rect.y = 350

        # Store a decimal value for the meteor's horizontal position.
        self.x = float(self.rect.x)

    def update(self):
        """Move the meteor right or left."""
        self.check_edges()
        self.x += (self.settings.meteor_speed * self.settings.meteor_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Return True if meteor is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            self.settings.meteor_direction = -1 * self.settings.meteor_direction

    def blitme(self, screen):
        """Draw the meteor at its current location"""
        screen.blit(self.image, self.rect)
