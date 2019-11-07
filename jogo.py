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
from config import keyboard_handler

# init configuration settings
Screen, Player = init.game_init()

alive = True
while alive:
    # handle events such as keyboard presses and mouse
    for event in pygame.event.get():
        alive = keyboard_handler.handler(event, Screen, Player)
    
    
    # move boats when there is acceleration (speed>0)
    print("Speed: "+str(Player.playerSpeed))
    Player.move_player()
            
            

                       
exit()