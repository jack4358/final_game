import pygame
from settings import Settings

class Meteor:

    def __init__(self):
        self.settings = Settings()
        self.image = pygame.image.load('meteor.png')

        self.rect = self.image.get_rect()
        # Start each new moon at the top right of the screen.

        self.rect.x = 800
        self.rect.y = 300

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = True
        self.moving_left = True

    def update(self):
        """Move the meteor right or left."""
        self.x += self.settings.meteor_speed
        self.rect.x = self.x

    def check_edges(self,):
        """Return True if meteor is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def blitme(self, screen):
        """Draw the meteor at its current location"""
        screen.blit(self.image, self.rect)
