import pygame



def handler(event, Screen, Player):
    alive = True

    if event.type == pygame.QUIT:
        alive = False
        
    # if key is pressed down
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            print("right key")
            Player.rotate_player("negative")
        if event.key == pygame.K_LEFT:
            print("left key")
            Player.rotate_player("positive")
        if event.key == pygame.K_UP:
            print("up key")
            Player.move_player("ahead")
        if event.key == pygame.K_DOWN:
            print("down key")
            Player.move_player("reverse")
        if event.key == pygame.K_ESCAPE:
            print("Exit program.")
            alive = False    


    return alive    