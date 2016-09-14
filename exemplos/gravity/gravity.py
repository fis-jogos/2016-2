import sys; sys.path.append('.')
from math import *
from phys import *

def draw():
    world.draw()

def update(dt):
    screen.clear()
    compute_forces()
    world.update(dt)
            
def compute_forces():
    bird2.force = Vec(0, 0)
    bird3.force = Vec(0, 0)
    
    s_vec = bird3.pos - bird2.pos
    s = s_vec.norm()
    u_vec = s_vec / s 
    
    F32 = -G * bird3.mass * bird2.mass / (s + e)**2 * u_vec
    bird2.force -= F32
    bird3.force += F32
       
# Parametros da simulacao
G = 5e7
e = 200
WIDTH = World.WIDTH = 800
HEIGHT = World.HEIGHT = 600
world = World(gravity=0, gravity_z=100)

# Cria objetos e insere no mundo
damp = 0
bird1 = PhysObj(Actor('bird0'), pos=(50, 550))
bird2 = PhysObj(Actor('birddead'), pos=(550, 50), vel=(-100, 300), damping=damp)
bird3 = PhysObj(Actor('bird2'), pos=(550, 550), damping=damp)
bird4 = PhysObj(Actor('birddead'), pos=(50, 50))
world.add(bird1)
world.add(bird2)
world.add(bird3)
world.add(bird4)

