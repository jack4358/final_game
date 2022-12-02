import sys
import time
import pygame
from ship import Ship
from moon import Moon
from settings import Settings

pygame.init()

# creating a screen and get rect parameters
screen = pygame.display.set_mode((1000, 1000))
screen_rect = screen.get_rect()

pygame.display.set_caption("To the Moon!")

# create a ship object and moon object
ship = Ship()
moon = Moon()
settings = Settings()

ship.blitme(screen)
moon.blitme(screen)

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


def _check_moon_edges():
    """Respond appropriately if the moon has reached an edge."""
    if moon.check_edges(screen):
        settings.moon_direction *= -1
    else:
        moon.rect.x = screen_rect.x

        #break


def _update_screen():
    """Update images on the screen, and flip to the new screen."""
    screen.fill(settings.bg_color)
    ship.blitme(screen)
    moon.blitme(screen)


while True:
    _check_events()

    moon.check_edges(screen)
    #moon.update()

    ship.update(screen_rect)

    _update_screen()

    #_check_moon_edges()

    pygame.display.flip()

    collision = pygame.sprite.collide_rect(ship, moon)
    if collision:
        screen = pygame.display.set_mode((1000, 1000))
        settings.bg_color = (0, 255, 0)
        pygame.display.set_caption("You win!")
        pygame.display.flip()












# rows = screen_rect.height
# cols = screen_rect.width

#def draw_background():
    # for x in range(rows):
    #     for y in range(cols):
    #         screen.blit(ship.image, ())


 #draw_background()