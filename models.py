import arcade.key
from random import randint
import math
DIR_UP = 1
DIR_RIGHT = 2
DIR_DOWN = 3
DIR_LEFT = 4
BLOCK_SIZE = 16
MOVE_WAIT = 80 
STATE_RUN = 1
STATE_CHECK = 2


DIR_OFFSET = {DIR_UP:(0,1), DIR_RIGHT:(1,0), DIR_DOWN:(0,-1), DIR_LEFT:(-1,0)}

class Spy:
    BLOCK_SIZE = 16
    #STATE_RUN = 1
    #STATE_CHECK = 2
    #LIE_WAIT = 1.5
    MOVE_WAIT = 0.18
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.wait_time = 0
        #self.lie_time = 0
        self.direction = DIR_RIGHT
        self.state = STATE_RUN
        self.score = 0
        self.gg = 0
    '''
    def lie(self,Security,count):
        if count%160==0 and self.direction != Security.direction:
            self.gg = 1
            return
        if(self.direction == Security.direction):
            self.score += 1
        self.lie_time = 0
    '''
    
    def out_of_range(self):
        if self.x == 960:
            self.x = 0
        elif self.x == 0:
            self.x = 960
 
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
            

class Security:
    SE_SIZE = 16
    def __init__(self,world,x,y):
        self.world = world
        self.x = x
        self.y = y
        self.tempx = x
        self.tempy = y
        self.direction = 1

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
            print('real dir = '+str(self.direction))
        elif count == 18:
            self.x = self.tempx
            self.y = self.tempy
           
class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.wait = 0
        self.spy = Spy(self,16,100)
        self.secure = Security(self,288,100)
        self.secure2 = Security(self,448,100)
        self.secure3 = Security(self,608,100)
        self.secure4 = Security(self,768,100)
        self.count = 1
        
        #self.state = STATE_RUN
        
    def update(self, delta):
        self.spy.update(delta)
        if self.spy.x == 256:
            self.spy.state = STATE_CHECK
            self.secure.randomdir()
            self.count += 1
            if(self.count%9==0):
                self.secure.update(self.count)
            self.wait += 0.5
            if self.wait < MOVE_WAIT:
                return
            self.wait = 0
            self.spy.state = STATE_RUN
            self.count = 1
           
        elif self.spy.x == 416:
            self.spy.state = STATE_CHECK
            
            self.secure2.randomdir()
            self.count += 1
            if(self.count%9==0):
                self.secure2.update(self.count)
            self.wait += 0.5
            if self.wait < MOVE_WAIT:
                return
            self.wait = 0
            self.spy.state = STATE_RUN
            self.count = 1
          
        elif self.spy.x == 576:
            self.spy.state = STATE_CHECK
            self.secure3.randomdir()
            self.count += 1
            if(self.count%9==0):
                self.secure3.update(self.count)
            self.wait += 0.5
            if self.wait < MOVE_WAIT:
                return
            self.wait = 0
            self.spy.state = STATE_RUN
            self.count = 1
            
        elif self.spy.x == 736:
            self.spy.state = STATE_CHECK
            self.secure4.randomdir()
            self.count += 1
            if(self.count%9==0):
                self.secure4.update(self.count)
            self.wait += 0.5
            if self.wait < MOVE_WAIT:
                return
            self.wait = 0
            self.spy.state = STATE_RUN
            self.count = 1
        #self.spy.lie(self.secure,delta)
        
def on_key_press(self, key, key_modifiers):
        if self.spy.state == self.spy.STATE_RUN:
            return
        if key == arcade.key.UP:
            self.spy.direction = DIR_UP
        elif key == arcade.key.DOWN:
            self.spy.direction = DIR_DOWN
        elif key == arcade.key.LEFT:
            self.spy.direction = DIR_LEFT
        elif key == arcade.key.RIGHT:
            self.spy.direction = DIR_RIGHT

        
