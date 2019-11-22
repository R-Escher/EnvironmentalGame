import random
from objects.collectible import Collectible
#from avoidable import avoidable


class Objects:
    
    def __init__(self, pygame, screen):

        # loads game libraries
        self.pygame = pygame
        self.screen = screen.screen

        # declares arrays that will contain the objects on-screen
        #self.collect_objects = []
        #self.avoid_objects = []

        # sets max-number of objects on-screen
        self.objects_onscreen = []
        self.max_collect_objects = 10

        # loads avoid-objects images into array
        #self.avoid_objects.append( self.pygame.transform.scale(self.pygame.image.load("../archive/avoid/.png"), (50, 80)) )


    def manage_objects(self, step):
        ''' Spawns collectible and avoidable objects randomly on screen, and moves them down in water-flux direction.\n 
            This function should be executed every game clock. '''

        # spawns objects if less then max are on screen
        if len(self.objects_onscreen) <= self.max_collect_objects:
            self.objects_onscreen.append( Collectible( self.screen, self.pygame ) )
            #self.screen.blit( self.collect_objects[ random.randrange(6) ], (random.randrange(5, 795) , 50) )

        # moves objects in water-flux direction
        for obj in self.objects_onscreen:
            self.objects_onscreen[0].update_position(step)
        

        

    