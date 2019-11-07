import math

class Player:
    def __init__(self, Screen):
        self.playerX = 300
        self.playerY = 300
        self.angle = 45
        self.angleStep = 10
        self.playerSpeed = 5
        self.pygame = Screen.pygame
        self.playerImage = self.pygame.transform.scale( (self.pygame.image.load("archive/boat.png")), (50, 30) )
        self.originalImage = self.playerImage
        self.screen = Screen.screen
        self.update_player()

    def move_player(self, way):
        if way == "ahead":
            #self.playerX += self.playerSpeed
            self.calculate_new_xy(self.playerSpeed)
        if way == "reverse":
            #self.player -= self.playerSpeed
            self.calculate_new_xy(self.playerSpeed*(-1))
        self.update_player()

    def rotate_player(self, direction):
        if direction == "positive":
            self.angle += self.angleStep % 360
            self.playerImage = self.pygame.transform.rotate(self.originalImage, self.angle)
        if direction == "negative":
            self.angle -= self.angleStep % 360
            self.playerImage = self.pygame.transform.rotate(self.originalImage, self.angle)
        self.update_player()            

    def calculate_new_xy(self,speed):
        self.playerX = self.playerX + (speed*math.cos((-1)*self.angle*math.pi/180))
        self.playerY = self.playerY + (speed*math.sin((-1)*self.angle*math.pi/180))


    def update_player(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit( self.playerImage, (self.playerX, self.playerY) )
        self.pygame.display.update()        


