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
from objects import objects

# init configuration settings
Screen, Player, Objects, clock = init.game_init()

my_image = pygame.image.load('archive/background.png')



alive = True
while alive:
    #Screen.update_background()




    if pygame.event.get(pygame.QUIT): 
        exit()

    # handle events such as keyboard presses and mouse
    pygame.event.pump()
    key = pygame.key.get_pressed()  
    alive = keyboard_handler.handler(key, Screen, Player)
    
    # moves boat when there is acceleration (speed>0)
    Player.move_player()

    # moves background image
    Screen.background_y += 0.5
            
    # moves collect/avoid-objects when on-screen
    Objects.manage_objects( 0.5 )
            


    # updates screen changes - this should be at the end of this code            
    pygame.display.update()
                       
    clock.tick(30)

exit()