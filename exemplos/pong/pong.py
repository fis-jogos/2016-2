from FGAme import *
from random import *
import pygame


WIDTH = 800
HEIGHT = 600


class PGZRunWorld(World):
    def init(self):
        self.add.margin(-200,0)
        self.player1 = Player(pos=(10, 300), mass='inf')
        self.player2 = Player(pos=(790, 300), mass='inf')
        self.ball = Ball(pos=pos.middle)
        self.add(self.player1)
        self.add(self.player2)
        self.add(self.ball)
        
    def draw(self):
        for obj in self:
            if isinstance(obj, (Player, Ball)):
                obj.draw()

    def checkWin(self):
        if self.ball.xmax < 0:
            self.ball.pos = pos.middle
            self.ball.vel = vel.random()
            self.player1.pontuation += 1
            
        elif self.ball.xmin > WIDTH:
            self.ball.pos = pos.middle
            self.ball.vel = vel.random()
            self.player2.pontuation += 1
                       

class Player(AABB):
    def __init__(self, *args, **kwargs):
        AABB.__init__(self, *args, shape=(24, 120), **kwargs)
        self.actor = Actor('pong', pos=self.pos)
        self.pontuation = 0
  
    def draw(self):
        x, y = self.pos
        self.actor.pos = x, HEIGHT - y 
        self.actor.draw()
    
        
class Ball(Circle):
    def __init__(self, *args, **kwargs):
        Circle.__init__(self, *args, vel=vel.random(), radius=20, **kwargs)
        self.actor = Actor('bird0', pos=self.pos)
    
    def draw(self):
        x, y = self.pos
        self.actor.pos = x, HEIGHT - y
        self.actor.draw()
        

world = PGZRunWorld()
input_ctrl = conf.get_input()

      
        
def draw():
    screen.clear()
    world.draw()
    x = world.player1.pontuation
    #screen.draw.text("sdfsdf")
    
    
def update(dt):
    dy = 3
    if keyboard.up:
        world.player2.move(0, dy)
    if keyboard.down:
        world.player2.move(0, -dy)
    if keyboard.w:
        world.player1.move(0, dy)
    if keyboard.s:
        world.player1.move(0, -dy)
        
    world.checkWin()
    world.update(dt)
    
