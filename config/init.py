import pygame
from config.player import Player
from config.screen import Screen

def game_init():
    ''' sets config settings, such as: 
    - window size, icon and title; 
    '''
    # initialiazes pygame
    pygame.init()

    # inits screen configs
    screen = Screen(pygame)

    # inits player configs
    player = Player(screen)

    clock = pygame.time.Clock()

    return screen, player, clock


