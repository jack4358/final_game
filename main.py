import sys
import time
import pygame
from ship import Ship
from moon import Moon
from meteor import Meteor
from settings import Settings

pygame.init()

# creating a screen and get rect parameters
screen = pygame.display.set_mode((1000, 1000))
screen_rect = screen.get_rect()
pygame.display.set_caption("To the Moon!")

# create a ship object and moon object
ship = Ship()
moon = Moon()
meteor = Meteor()
settings = Settings()


ship.blitme(screen)
moon.blitme(screen)
meteor.blitme(screen)

def _check_events():
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            _check_keydown_events(event)
        elif event.type == pygame.KEYUP:
            _check_keyup_events(event)


def _check_keydown_events(event):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_SPACE:
        ship.moving_up = True


def _check_keyup_events(event):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def _update_screen():
    """Update images on the screen, and flip to the new screen."""
    screen.fill(settings.bg_color)
    ship.blitme(screen)
    moon.blitme(screen)
    meteor.blitme(screen)


while True:
    _check_events()
    moon.update()
    meteor.update()
    ship.update(screen_rect)
    _update_screen()


    pygame.display.flip()

    collision = pygame.sprite.collide_rect(ship,moon)
    if collision:
        ship.moving_up = False
        ship.moving_left = False
        ship.moving_right = False
        #stop moon update and meteor update from running
        screen = pygame.display.set_mode((1000, 1000))
        settings.bg_color = (0, 255, 0)
        pygame.display.set_caption("You win!")
        pygame.display.flip()

    badcollsion1 = pygame.sprite.collide_rect(ship,meteor)

    badcollision2 = pygame.sprite.collide_rect(ship,ufo)

