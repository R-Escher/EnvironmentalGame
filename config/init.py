import pygame
from config.player import Player
from config.screen import Screen
from objects.objects import Objects

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

    # inits objects on-screen
    objects = Objects(pygame, screen, player)

    # inits game clock
    clock = pygame.time.Clock()

    return screen, player, objects, clock


