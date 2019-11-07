
class Screen:
    def __init__(self, pygame):
        # creates game screen
        self.pygame = pygame
        self.screen = self.pygame.display.set_mode( (800,600) )
        
        # sets title and icon
        self.pygame.display.set_caption("Save the Rivers")
        self.pygame.display.set_icon( self.pygame.image.load("archive/icons/boatWindowIcon.png") )
        
        # sets background color
        self.screen.fill((255, 255, 255))
        self.pygame.display.update()