import random

class Avoidable:
    def __init__(self, screen, pygame):

        self.screen = screen
        self.pygame = pygame
    
        # generates object and its rect
        self.avoid_object_image, self.rect = self.generateRandomObject()

        # will be valued when an object_image get atributted to this class
        #self.score_value = 0

    def collided(self):
        ''' Handles what to do when boat hits the object. '''
        # score will be increased by Objects class
        # move object back to top
        self.reset_position()

    def get_ScoreValue(self):
        return self.score_value


    def update_position(self, step):
        ''' Updates Y-axis position of object on screen. ''' 

        # checks if y is not greater than end of screen
        if self.rect.y < 600:

            # updates Y position 
            self.rect.y = self.rect.y + step
            self.screen.blit( self.avoid_object_image, (self.rect.x, self.rect.y) )
            
        else:
            # moves object back to upper screen
            self.reset_position()
            

    def reset_position(self):
        ''' Moves object to upper screen '''
        self.rect.x, self.rect.y=  self.getRandomPosition()

    def getRandomPosition(self):
        return random.randrange(5, 795) , random.randrange(-600, 0) # (x, y)


    def generateRandomObject(self):
        ''' Generates a random object and its Rect, in a random position on screen. '''
        #choice = random.randint(0, 1)
        choice = 0

        if choice == 0:
            lx, ly = 40, 45
            avoid_object_image = self.pygame.transform.scale(self.pygame.image.load("archive/avoid/lily-pad.png"), (lx, ly))
            self.score_value = -3
        '''elif choice == 1:
            lx, ly = 15, 24
            avoid_object_image = self.pygame.transform.scale(self.pygame.image.load("archive/avoid/apple.png"), (lx, ly))
            self.score_value = 1
        elif choice == 2:
            lx, ly = 20, 24
            avoid_object_image = self.pygame.transform.scale(self.pygame.image.load("archive/avoid/can.png"), (lx, ly))
            self.score_value = 2
        elif choice == 3:
            lx, ly = 15, 24
            avoid_object_image = self.pygame.transform.scale(self.pygame.image.load("archive/avoid/can2.png"), (lx, ly))
            self.score_value = 2
        elif choice == 4:
            lx, ly = 15, 24
            avoid_object_image = self.pygame.transform.scale(self.pygame.image.load("archive/avoid/banana.png"), (lx, ly))
            self.score_value = 1
        elif choice == 5:
            lx, ly = 15, 24
            avoid_object_image = self.pygame.transform.scale(self.pygame.image.load("archive/avoid/paper.png"), (lx, ly))
            self.score_value = 1'''

        # get ramdom position on screen
        x, y = self.getRandomPosition()

        # creates rect with random position and predefined width and height
        rect = self.pygame.Rect(x, y, lx, ly) 

        return avoid_object_image, rect

    '''def get_image(self):
        return self.avoid_object_image'''
