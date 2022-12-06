import pygame
from settings import Settings

class Ship:
    """A class to manage the ship."""
    def __init__(self):
        # Load the ship image and  get its rect.

        self.settings = Settings()
        self.image = pygame.image.load("final_game\spaceship.png")
        self.rect = self.image.get_rect()

        self.deadimage = pygame.image.load("final_game\explosion.png")
        self.health = 100


        # Start each new ship at the bottom center of the screen.
        self.rect.x = 500
        self.rect.y = 720

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False


    def update(self, screen_rect):
        """Update the ship's position based on the movement flags."""
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y += self.settings.ship_up_speed


        # Update rect object from self.x and self.y.
        self.rect.x = self.x
        self.rect.y = self.y



    def blitme(self, screen):
        """Draw the ship at its current location"""
        if self.health == 100:
            self.image = self.image
        if self.health == 0:
            self.image = self.deadimage
        screen.blit(self.image, self.rect)
