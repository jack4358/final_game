import sys
import pygame.font
import time
import pygame
from ship import Ship
from moon import Moon
from meteor import Meteor
from ufo import Ufo
from settings import Settings


#initialize program
pygame.init()

# #####
# #Click to start screen
# screen1 = pygame.display.set_mode(1000,1000)
# screen1_rect = screen1.get_rect()

#####

# creating a screen and get rect parameters
screen = pygame.display.set_mode((1000, 1000))
screen_rect = screen.get_rect()
pygame.display.set_caption("To the Moon!")

# create a ship object and moon object
ship = Ship()
moon = Moon()
meteor = Meteor()
ufo = Ufo()
settings = Settings()


#initialize game sounds
space_sound = pygame.mixer.Sound("final_game\space.mp3")
space_sound.set_volume(0.4)
boom = pygame.mixer.Sound("final_game\kaboom.mp3")
boom.set_volume(1.0)

#blit images
ship.blitme(screen)
moon.blitme(screen)
meteor.blitme(screen)
ufo.blitme(screen)

def ambient_sound():
    pygame.mixer.Sound.play(space_sound)
    space_sound.play(-1)

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
    #keypress for reset
    if event.key == pygame.K_r:
        reset()
    #keypresses for ship
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_SPACE:
        ship.moving_up = True
    #keypresses for ufo
    elif event.key == pygame.K_a:
        ufo.moving_left = True
    elif event.key == pygame.K_d:
        ufo.moving_right = True
    elif event.key == pygame.K_w:
        ufo.moving_up = True
    elif event.key == pygame.K_s:
        ufo.moving_down = True

def _check_keyup_events(event):
    """Respond to key releases."""
    # keypresses for ship
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    # keypresses for ufo
    elif event.key == pygame.K_a:
        ufo.moving_left = False
    elif event.key == pygame.K_d:
        ufo.moving_right = False
    elif event.key == pygame.K_w:
        ufo.moving_up = False
    elif event.key == pygame.K_s:
        ufo.moving_down = False

def _update_screen():
    """Update images on the screen, and flip to the new screen."""
    screen.fill(settings.bg_color)
    ship.blitme(screen)
    moon.blitme(screen)
    meteor.blitme(screen)
    ufo.blitme(screen)

def check_collisions():
    if pygame.sprite.collide_rect(ship,moon):
        ship.moving_up = False
        ship.moving_left = False
        ship.moving_right = False
        ufo.moving_left = False
        ufo.moving_right = False
        ufo.moving_up = False
        ufo.moving_down = False
        settings.bg_color = (0, 220, 0)
        screen.fill(settings.bg_color)
        font = pygame.font.SysFont(None, 38)
        word = font.render("YOU WIN!", True, (200, 200, 200))
        img_rect = word.get_rect()
        img_rect.center = screen.get_rect().center
        screen.blit(word, img_rect)
        #pygame.display.flip()
        pygame.time.wait(3000)
    if pygame.sprite.collide_rect(ship,meteor) or pygame.sprite.collide_rect(ship,ufo):
        ship.health = 0
        ship.blitme(screen)
        pygame.mixer.Sound.stop(space_sound)
        pygame.mixer.Sound.play(boom)
        ship.moving_up = False
        ship.moving_left = False
        ship.moving_right = False
        ufo.moving_left = False
        ufo.moving_right = False
        ufo.moving_up = False
        ufo.moving_down = False
        pygame.time.wait(1000)
        settings.bg_color = (220, 0, 0)
        screen.fill(settings.bg_color)
        font = pygame.font.SysFont(None, 38)
        word = font.render(f"Health is {ship.health}. You are dead!", True, (200, 200, 200))
        img_rect = word.get_rect()
        img_rect.center = screen.get_rect().center
        screen.blit(word, img_rect)
        #pygame.display.flip()
        pygame.time.wait(3000)
    pygame.display.flip()

def reset():
    settings.bg_color = (0,0,0)
    screen.fill(settings.bg_color)
    ship.health = 100
    ship.blitme(screen)
    moon.blitme(screen)
    meteor.blitme(screen)
    ufo.blitme(screen)
    #pygame.display.flip()


# main game loop
while True:
    ambient_sound()
    _check_events()
    moon.update()
    meteor.update()
    ufo.update(screen_rect)
    ship.update(screen_rect)
    #_update_screen()
    check_collisions()
    _update_screen()
    #reset()
    # pygame.display.flip()

