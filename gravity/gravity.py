import sys; sys.path.append('.')
from math import *
from phys import *

def draw():
    world.draw()

def update(dt):
    screen.clear()
    world.update(dt)
            
# Parametros da simulacao
WIDTH = World.WIDTH = 800
HEIGHT = World.HEIGHT = 600
world = World(gravity=0, gravity_z=100)

# Cria objetos e insere no mundo
bird1 = PhysObj(Actor('bird0'), pos=(50, 550))
bird2 = PhysObj(Actor('birddead'), pos=(550, 50), vel=(-100, 300))
bird3 = PhysObj(Actor('bird2'), pos=(550, 550))
bird4 = PhysObj(Actor('birddead'), pos=(50, 50))
world.add(bird1)
world.add(bird2)
world.add(bird3)
world.add(bird4)

