
class Screen:
    def __init__(self, pygame):
        # creates game screen
        self.pygame = pygame
        self.screen = self.pygame.display.set_mode( (800,600) )
        self.background = self.pygame.transform.scale(self.pygame.image.load("archive/background.png"), (800, 600))
        
        self.background_rect = self.background.get_rect()
        self.background_rect.left, self.background_rect.top = [0, 0]
        
        # sets title and icon
        self.pygame.display.set_caption("Save the Rivers")
        self.pygame.display.set_icon( self.pygame.image.load("archive/icons/boatWindowIcon.png") )
        
        # sets background color
        self.screen.fill((255, 255, 255))
        self.update_background()

        # updates display after changes
        self.pygame.display.update()

    
    def update_background(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.background, self.background.get_rect())