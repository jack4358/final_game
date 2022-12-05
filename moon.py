import pygame
from settings import Settings

class Moon:
    screen = pygame.display.set_mode((1000, 1000))
    screen_rect = screen.get_rect()

    def __init__(self):
        self.settings = Settings()
        self.image = pygame.image.load('final_game\planet.png')

        self.rect = self.image.get_rect()
        # Start each new moon at the top right of the screen.

        self.rect.x = 800
        self.rect.y = 150

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

    def update(self):
        """Move the moon right or left."""
        self.check_edges()
        self.x += (self.settings.moon_speed * self.settings.moon_direction)
        self.rect.x = self.x

        # if self.rect.right >= screen_rect.right:
        #     self.x -= self.settings.moon_speed
        #     #self.rect.x = self.x
        # if self.rect.left < 0:
        #     self.x += self.settings.moon_speed
        #     #self.rect.x = self.x
        # if not self.rect.right > screen_rect.right or self.rect.left < 0:


    def check_edges(self):
        """Return True if moon is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            #return True
            self.settings.moon_direction = -1*self.settings.moon_direction


    def blitme(self, screen):
        """Draw the moon at its current location"""
        screen.blit(self.image, self.rect)
