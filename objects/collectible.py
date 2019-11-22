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
        self.position = ( random.randrange(5, 795) , 50 )

        choice = random.randint(0, 5)

        if choice == 1:
            self.collect_object_image = self.pygame.transform.scale(self.pygame.image.load("archive/collect/apple.png"), (15, 24))
        elif choice == 2:
            self.collect_object_image = self.pygame.transform.scale(self.pygame.image.load("archive/collect/can.png"), (20, 24))
        elif choice == 3:
            self.collect_object_image = self.pygame.transform.scale(self.pygame.image.load("archive/collect/can2.png"), (15, 24))
        elif choice == 4:
            self.collect_object_image = self.pygame.transform.scale(self.pygame.image.load("archive/collect/banana.png"), (15, 24))
        elif choice == 5:
            self.collect_object_image = self.pygame.transform.scale(self.pygame.image.load("archive/collect/paper.png"), (15, 24))
        elif choice == 6:
            self.collect_object_image = self.pygame.transform.scale(self.pygame.image.load("archive/collect/trash.png"), (50, 60))

        #self.collect_object_rect = self.collect_object.get_rect()

    def update_position(self, step):
        ''' Updates Y-axis position of object on screen. '''
        self.screen.blit( self.collect_object_image, self.position )
        self.position = ( self.position[0], self.position[1] + step )

    '''def get_image(self):
        return self.collect_object_image'''
