import pygame, math

class Player:
    def __init__(self, screen):
        self.playerX = 300
        self.playerY = 300
        self.playerSpeed = 5
        self.playerImage = pygame.transform.scale( (pygame.image.load("archive/boat.png")), (50, 30) )
        self.screen = screen.screen
        self.screen.blit(self.playerImage, (self.playerX, self.playerY))
        pygame.display.update()        

    def move_player(self, way):
        if way == "ahead":
            self.playerX += self.playerSpeed
        if way == "reverse":
            self.playerY += self.playerSpeed
        print(self.playerX)
        self.screen.blit( self.playerImage, (self.playerX, self.playerY) )
        pygame.display.update()    

    def rotate_player(self):
        pass







