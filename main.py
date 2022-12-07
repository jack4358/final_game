import sys
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
boom = pygame.mixer.Sound("final_game\kaboom.mp3")

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

def end_game():
    if ship.health == 0:
        screen.fill((255, 0, 0))
        font = pygame.font.Font("""""""", 18)
        word = "YOU LOSE - press r"
        end = font.render(word, True, (200,200,200))
        img_rect = end.get_rect()
        img_rect.center = screen.get_rect().center
        screen.blit(end, img_rect)
    if ship.health == 100:
        screen.fill((0, 255, 0))
        font = pygame.font.Font("""""""", 18)
        word = "YOU WIN! - press r"
        end = font.render(word, True, (200, 200, 200))
        img_rect = end.get_rect()
        img_rect.center = screen.get_rect().center
        screen.blit(end, img_rect)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.key == pygame.K_r:




# def _wincollision_update_screen():
#     """update to win screen if a good collision occurs."""
#     # write text over screen, so player can still see images.
#
# def _losecollision_update_screen():
#     """update to lose screen if a bad collision occurs"""

#main game loop
while True:
    ambient_sound()
    _check_events()
    moon.update()
    meteor.update()
    ufo.update(screen_rect)
    ship.update(screen_rect)
    _update_screen()
    # pygame.display.flip()

    collision = pygame.sprite.collide_rect(ship,moon)
    if collision:
        ship.moving_up = False
        ship.moving_left = False
        ship.moving_right = False
        ufo.moving_left = False
        ufo.moving_right = False
        ufo.moving_up = False
        ufo.moving_down = False
        end_game()
        #stop moon update and meteor update from running
        #_wincollision_update_screen()

    # badcollision1 = pygame.sprite.collide_rect(ship,meteor)
    # if badcollision1:
    #     pygame.mixer.Sound.play(boom)
    #     ship.health -= 100
    #     print(f"Health is {ship.health}. You are dead!")
    #     ship.moving_up = False
    #     ship.moving_left = False
    #     ship.moving_right = False
    #     ufo.moving_left = False
    #     ufo.moving_right = False
    #     ufo.moving_up = False
    #     ufo.moving_down = False
    #     #stop moon update and meteor update from running
    #     _losecollision_update_screen()
    #
    # badcollision2 = pygame.sprite.collide_rect(ship,ufo)
    # if badcollision2:
    #     pygame.mixer.Sound.play(boom)
    #     ship.health -= 100
    #     print(f"Health is {ship.health}. You are dead!")
    #     ship.moving_up = False
    #     ship.moving_left = False
    #     ship.moving_right = False
    #     ufo.moving_left = False
    #     ufo.moving_right = False
    #     ufo.moving_up = False
    #     ufo.moving_down = False
    #     # stop moon update and meteor update from running
#         _losecollision_update_screen()


    pygame.display.flip()