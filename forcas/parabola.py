import sys; sys.path.append('.')
from math import sqrt
from phys import World, PhysObj

frame = 0
time = []
energy = []

def draw():
    world.draw()


def update(dt):
    global frame
    frame += 1
    screen.clear()
    world.update(dt)
            
# Simulacao
WIDTH = World.WIDTH = 800
HEIGHT = World.HEIGHT = 600

speed = 400
world = World(gravity=0, gravity_z=100)
bird1 = PhysObj(Actor('bird0'), x=50, y=50, vx=speed, vy=speed, mu=1.4142)
bird2 = PhysObj(Actor('birddead'), x=50, y=50, vx=speed, vy=speed, damping=0.5)
bird3 = PhysObj(Actor('bird2'), x=50, y=50, vx=speed, vy=speed, drag=0.0035)
bird4 = PhysObj(Actor('birddead'), x=50, y=50, vx=speed, vy=speed, gravity=500)
world.add(bird1)
world.add(bird2)
world.add(bird3)
world.add(bird4)

