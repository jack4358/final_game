import pygame
from settings import Settings

class Moon:
    screen = pygame.display.set_mode((1000, 1000))
    screen_rect = screen.get_rect()

    def __init__(self):
        self.settings = Settings()
        self.image = pygame.image.load('planet.png')

        self.rect = self.image.get_rect()
        # Start each new moon at the top right of the screen.

        self.rect.x = 800
        self.rect.y = 150

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = True
        self.moving_left = True

    def update(self):
        """Move the moon right or left."""
        self.x += self.settings.moon_speed
        self.rect.x = self.x


    def check_edges(self, screen):
        """Return True if moon is at edge of screen."""
        # if screen.get_rect().contains(self.rect):
        #     return True

        screen_rect = screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True



    def blitme(self, screen):
        """Draw the moon at its current location"""
        screen.blit(self.image, self.rect)
