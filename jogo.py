'''
2D GAME USING PYGAME LIBRARY

AUTHOR: RAFAEL M. ESCHER
FEDERAL UNIVERSITY OF RIO GRANDE
RIO GRANDE DO SUL
BRASIL

2019
'''

# imports configuration file
from config import init
#from config.player import Player
#from config.display import Display
import pygame

# init configuration settings
Display, Player = init.game_init()

alive = True
while alive:
    # handle events such as keyboard presses and mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            alive = False

        # if key is pressed down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("right key")
                Player.rotate_player()
            if event.key == pygame.K_LEFT:
                print("left key")
                Player.rotate_player()
            if event.key == pygame.K_UP:
                print("up key")
                Player.move_player("ahead")
            if event.key == pygame.K_DOWN:
                print("down key")
                Player.move_player("reverse")
            
            

                       

    
    