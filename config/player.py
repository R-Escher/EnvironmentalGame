import math, time

class Player:
    def __init__(self, Screen):
        self.playerX = 300                          # x-axis position
        self.playerY = 300                          # y-axis position
        self.angle = 0                              # start-angle (pointing towards right-side of screen)
        self.angleStep = 4                          # angle-step variation at key-press
        self.playerSpeed = 0                        # player current speed
        self.platerMaxSpeed = 3.5                     # player's max speed
        self.playerAcceleration = 0.1               # speed-step variation at ket-press
        self.waterDragConstant = 0.07               # defines water drag force
        self.pygame = Screen.pygame                 # pygame library 
        self.playerImage = self.pygame.transform.scale( (self.pygame.image.load("archive/boat.png")), (50, 30) )
        self.originalImage = self.playerImage       # stores original image which this only will be rotated due to memory bug
        self.screen = Screen.screen                 # stores pygame.screen
        self.update_player()                        # updates player


    def accelerate_player(self, way):
        ''' Increases (UPKEY) or Decreases (DOWNKEY) boat's current speed. '''
        if way == "ahead":
            # hits gas pedal if not at max speed
            if self.playerSpeed <= self.platerMaxSpeed:
                self.playerSpeed += self.playerAcceleration
        if way == "reverse":
            # releases gas pedal and reverses when speed<0, if not at maximum reverse speed
            if self.playerSpeed >= ((self.platerMaxSpeed - 0.5)*(-1)):
                self.playerSpeed -= self.playerAcceleration
        self.update_player()


    def break_player(self):
        ''' Gradually slows down boat until fully stops. '''
        if self.playerSpeed > 0:
            while self.playerSpeed > 0:
                self.playerSpeed -= self.waterDragConstant
                self.calculate_new_xy(self.playerSpeed)
                self.update_player()
                time.sleep(0.05)
        elif self.playerSpeed < 0:
            while self.playerSpeed < 0:
                self.playerSpeed += self.waterDragConstant
                self.calculate_new_xy(self.playerSpeed)
                self.update_player()
                time.sleep(0.05)
        self.playerSpeed = 0
    
    
    def move_player(self):
        ''' Moves boat when there is acceleration (speed>0). '''
        self.calculate_new_xy(self.playerSpeed)
        self.update_player()


    def rotate_player(self, direction):
        ''' Rotates boat when RIGHTKEY or LEFTKEY are pressed. '''
        if direction == "positive":
            self.angle += self.angleStep % 360
            self.playerImage = self.pygame.transform.rotate(self.originalImage, self.angle)
        if direction == "negative":
            self.angle -= self.angleStep % 360
            self.playerImage = self.pygame.transform.rotate(self.originalImage, self.angle)
        self.update_player()


    def calculate_new_xy(self,speed):
        ''' Calculates boat's new location, when moving, based on it's angle direction. '''
        self.playerX = self.playerX + (speed*math.cos((-1)*self.angle*math.pi/180))
        self.playerY = self.playerY + (speed*math.sin((-1)*self.angle*math.pi/180))


    def update_player(self):
        ''' Updates boat's image on screen. '''
        self.screen.fill((255, 255, 255))
        self.screen.blit( self.playerImage, (self.playerX, self.playerY) )
        self.pygame.display.update()        


