import random

class Collectible:
    def __init__(self, screen, pygame):

        '''# loads collect-objects images into array
        self.collect_object
        self.collect_object.append(  )
        self.collect_object.append(  )
        self.collect_object.append(  )
        self.collect_object.append(  )
        self.collect_object.append(  )
        self.collect_object.append(  )'''

        self.screen = screen
        self.pygame = pygame
        
        # set position of object randomly
        self.setRandomPosition()

        choice = random.randint(0, 5)

        if choice == 0:
            self.collect_object_image = self.pygame.transform.scale(self.pygame.image.load("archive/collect/trash.png"), (50, 60))
        elif choice == 1:
            self.collect_object_image = self.pygame.transform.scale(self.pygame.image.load("archive/collect/apple.png"), (15, 24))
        elif choice == 2:
            self.collect_object_image = self.pygame.transform.scale(self.pygame.image.load("archive/collect/can.png"), (20, 24))
        elif choice == 3:
            self.collect_object_image = self.pygame.transform.scale(self.pygame.image.load("archive/collect/can2.png"), (15, 24))
        elif choice == 4:
            self.collect_object_image = self.pygame.transform.scale(self.pygame.image.load("archive/collect/banana.png"), (15, 24))
        elif choice == 5:
            self.collect_object_image = self.pygame.transform.scale(self.pygame.image.load("archive/collect/paper.png"), (15, 24))
        

        #self.collect_object_rect = self.collect_object.get_rect()

    def update_position(self, step):
        ''' Updates Y-axis position of object on screen. '''
        
        # checks if y is not greater than end of screen
        if self.position[1] < 600:
            # updates Y position 
            self.screen.blit( self.collect_object_image, self.position )
            self.position = ( self.position[0], self.position[1] + step )
        else:
            # moves object back to upper screen
            self.setRandomPosition()

    def setRandomPosition(self):
        self.position = ( random.randrange(5, 795) , random.randrange(-600, 0) ) # (x, y)



    '''def get_image(self):
        return self.collect_object_image'''
