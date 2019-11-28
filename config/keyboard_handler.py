import pygame



def handler(key, Screen, Player):
    ''' Handles keyboard presses, if any. '''
    alive = True

    #print("Boat's Speed: " + str(Player.playerSpeed) )

    #keys = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]: Player.rotate_player("negative")
    if key[pygame.K_LEFT]: Player.rotate_player("positive")
    if key[pygame.K_UP]: Player.accelerate_player("ahead")
    if key[pygame.K_DOWN]: Player.accelerate_player("reverse")
    if key[pygame.K_SPACE]: Player.break_player()
    if key[pygame.K_ESCAPE]: alive = False

    return alive    