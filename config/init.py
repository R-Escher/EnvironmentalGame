import pygame
from config.player import Player
from config.display import Display

def game_init():
    ''' sets config settings, such as: 
    - window size, icon and title; 
    '''
    # initialiazes pygame
    pygame.init()

    # inits display configs
    display = Display()

    # inits player configs
    player = Player(display)

    return display, player


