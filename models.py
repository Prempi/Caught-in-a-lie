import arcade.key
from random import randint
DIR_UP = 1
DIR_RIGHT = 2
DIR_DOWN = 3
DIR_LEFT = 4
BLOCK_SIZE = 10
MOVE_WAIT = 180 
STATE_RUN = 1
STATE_CHECK = 2


DIR_OFFSET = {DIR_UP:(0,1), DIR_RIGHT:(1,0), DIR_DOWN:(0,-1), DIR_LEFT:(-1,0)}

class Spy:
    BLOCK_SIZE = 20
    STATE_RUN = 1
    STATE_CHECK = 2
    MOVE_WAIT = 0.025
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.wait_time = 0
        self.direction = DIR_RIGHT
        self.state = STATE_RUN
        self.press = 0
        self.score = 0
        self.gg = 0
        
    
    def out_of_range(self):
        if self.x == 1000:
            self.x = 0
    def update(self, delta):
        
        self.wait_time += delta
        
        if self.state == STATE_CHECK:
            return
        if self.wait_time < self.MOVE_WAIT:
            return
            
        
        self.x += self.BLOCK_SIZE*DIR_OFFSET[self.direction][0]
        self.y += self.BLOCK_SIZE*DIR_OFFSET[self.direction][1]
        
        self.out_of_range()

        self.wait_time = 0

class Brain:
    def __init__(self,x,y):
        self.x = x
        self.y = y
            

class Security:
    SE_SIZE = 20
    ORDINARY = 1
    CLEVER = 2
    def __init__(self,world,x,y):
        self.world = world
        self.x = x
        self.y = y
        self.tempx = x
        self.tempy = y
        self.direction = 1
        self.realdir = 0
        self.type = randint(1,2)

    def randomdir(self):
        self.direction = randint(0,100)%4 + 1
        
    def update(self,count):
        if count>18:
            return
        if count == 9:
            self.tempx = self.x
            self.tempy = self.y
            self.x += self.SE_SIZE*DIR_OFFSET[self.direction][0]
            self.y += self.SE_SIZE*DIR_OFFSET[self.direction][1]
            self.realdir = self.direction
        elif count == 18:
            self.x = self.tempx
            self.y = self.tempy
           
class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.wait = 0
        self.spy = Spy(self,0,100)
        self.secure = Security(self,300,110)
        self.secure2 = Security(self,500,110)
        self.secure3 = Security(self,700,110)
        self.secure4 = Security(self,900,110)
        self.count = 1
        self.tpr = 0
        self.gg = 1
        self.mode = randint(1,2)
        self.correct = 0
        self.brain1 = Brain(300,180)
        self.brain2 = Brain(500,180)
        self.brain3 = Brain(700,180)
        self.brain4 = Brain(900,180)
        
    def update(self, delta):
        self.spy.update(delta)
        self.tpr += 1
        if self.spy.x == 200:
            self.checknaja(self.secure,self.mode)
        elif self.spy.x == 400:
            self.checknaja(self.secure2,self.mode)
        elif self.spy.x == 600:
            self.checknaja(self.secure3,self.mode)
        elif self.spy.x == 800:
            self.checknaja(self.secure4,self.mode)
        elif self.spy.x > 800:
            self.mode = randint(1,2)
            self.secure.type = randint(1,2)
            self.secure2.type = randint(1,2)
            self.secure3.type = randint(1,2)
            self.secure4.type = randint(1,2)
        if self.spy.x == 840 and self.gg >0:
            if self.tpr/60 < 5:
                self.spy.score+=2
            else:
                self.spy.score+=1
        if self.spy.x == 0:
            self.tpr = 0
           
    def checknaja(self,secur,mode):   
        self.spy.state = STATE_CHECK
        secur.randomdir()
        self.count += 1
        if(self.count%9==0):
            secur.update(self.count)
        self.wait += 1
        while self.wait < MOVE_WAIT and self.correct == 0:
            if secur.type == secur.CLEVER:
                if mode == 1:
                    mode = 2
                else:
                    mode = 1
            if mode == 1:
                if self.spy.press == 1 and self.spy.direction!=secur.realdir:
                    self.gg -= 1
                elif self.spy.press == 0 and self.count == MOVE_WAIT:
                    self.gg -= 1
                elif self.spy.press == 1 and self.spy.direction == secur.realdir :
                    self.correct = 1
            elif mode == 2:
                if self.spy.press == 1 and self.spy.direction==DIR_UP and secur.realdir != DIR_DOWN:
                    self.gg -= 1
                elif self.spy.press == 1 and self.spy.direction==DIR_DOWN and secur.realdir != DIR_UP:
                    self.gg -= 1
                elif self.spy.press == 1 and self.spy.direction==DIR_LEFT and secur.realdir != DIR_RIGHT:
                    self.gg -= 1
                elif self.spy.press == 1 and self.spy.direction==DIR_RIGHT and secur.realdir != DIR_LEFT:
                    self.gg -= 1
                elif self.spy.press == 0 and self.count == MOVE_WAIT:
                    self.gg -= 1
                elif self.spy.press == 1 and self.spy.direction==DIR_UP and secur.realdir == DIR_DOWN:
                    self.correct = 1
                elif self.spy.press == 1 and self.spy.direction==DIR_DOWN and secur.realdir == DIR_UP:
                    self.correct = 1
                elif self.spy.press == 1 and self.spy.direction==DIR_LEFT and secur.realdir == DIR_RIGHT:
                    self.correct = 1
                elif self.spy.press == 1 and self.spy.direction==DIR_RIGHT and secur.realdir == DIR_LEFT:
                    self.correct = 1
            return
        self.correct = 0
        self.wait = 0
        self.spy.state = STATE_RUN
        self.count = 1
        self.spy.press = 0
        self.spy.direction = DIR_RIGHT
        
    def on_key_press(self, key, key_modifiers):
            if self.spy.state == self.spy.STATE_RUN:
                return
            if key == arcade.key.UP:
                self.spy.direction = DIR_UP
                self.spy.press = 1
            elif key == arcade.key.DOWN:
                self.spy.direction = DIR_DOWN
                self.spy.press = 1
            elif key == arcade.key.LEFT:
                self.spy.direction = DIR_LEFT
                self.spy.press = 1
            elif key == arcade.key.RIGHT:
                self.spy.direction = DIR_RIGHT
                self.spy.press = 1

        
