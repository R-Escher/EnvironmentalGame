import pygame

class Display:
    def __init__(self):
        # creates game screen
        self.screen = pygame.display.set_mode( (800,600) )
        
        # sets title and icon
        pygame.display.set_caption("Save the Rivers")
        pygame.display.set_icon( pygame.image.load("archive/icons/boatWindowIcon.png") )
        
        # sets background color
        self.screen.fill((255, 255, 255))
        pygame.display.update()