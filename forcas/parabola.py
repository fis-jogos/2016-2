import sys; sys.path.append('.')
from math import sqrt
from phys import World
print(sorted(sys.modules.keys()))

class World:
    """
    Representa o conjunto de todos os objetos na simulacao.
    """
    
    WIDTH = 800
    HEIGHT = 600  
    
    def __init__(self, objects=[], gravity=0, gravity_z=0):
        self.objects = list(objects)
        self.gravity = gravity
        self.gravity_z = gravity_z
        
    def draw(self):
        """
        Desenha todos objetos na tela.
        """
        for obj in self.objects:
            obj.draw()
            
    def update(self, dt):
        """
        Atualiza o estado da simulacao, evoluindo por um intervalo dt.
        """
        for obj in self.objects:
            obj.update(dt)
            
    def add(self, obj):
        """
        Adiciona objeto ao mundo.
        """
        self.objects.append(obj)
        if obj.gravity == 0:
            obj.gravity = self.gravity
        if obj.gravity_z == 0:
            obj.gravity_z = self.gravity_z


class PhysObj:
    """
    Representa um objeto com uma fisica associada.
    """
    def __init__(self, actor, mass=1, x=0, y=0, vx=0, vy=0, 
                 gravity=0, gravity_z=0, damping=0, mu=0, drag=0):
        self.actor = actor
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.fx = 0
        self.fy = 0
        self.mass = mass
        self.gravity = gravity
        self.gravity_z = gravity_z
        self.damping = damping
        self.mu = mu
        self.drag = drag
        
    def update(self, dt):
        # Calcula a aceleracao devido ao atrito
        v_abs = sqrt(self.vx**2 + self.vy**2)
        ux = self.vx / v_abs
        uy = self.vy / v_abs
        friction_x = -self.mu * self.gravity_z * ux
        friction_y = -self.mu * self.gravity_z * uy
        
        # Arrasto aerodinamico
        drag_x = -self.drag * ux * self.vx**2 
        drag_y = -self.drag * ux * self.vy**2
        
        # Aceleracao devido a forca de dissipacao viscosa
        damping_x = -self.damping * self.vx
        damping_y = -self.damping * self.vy
        
        # Aceleracao da gravidade
        gravity_x = 0
        gravity_y = -self.gravity
        
        # Soma todas as forcas
        ax = self.fx / self.mass + friction_x + damping_x + gravity_x + drag_x
        ay = self.fy / self.mass + friction_y + damping_y + gravity_y + drag_y  
        
        self.vx += ax * dt
        self.vy += ay * dt
        self.x += self.vx * dt + ax * dt**2 / 2
        self.y += self.vy * dt + ay * dt**2 / 2
        self.update_collisions()
    
    def update_collisions(self):
        if self.x < 10 and self.vx < 0:
            self.vx *= -1
        elif self.x > World.WIDTH - 10 and self.vx > 0:
            self.vx *= -1
        if self.y < 10 and self.vy < 0:
            self.vy *= -1
        elif self.y > World.HEIGHT - 10 and self.vy > 0:
            self.vy *= -1
    
    def draw(self):
        self.actor.x = self.x
        self.actor.y = World.HEIGHT - self.y
        self.actor.draw() 

def update(dt):
    screen.clear()
    world.update(dt)
    
def draw():
    world.draw() 

# Simulacao
WIDTH = World.WIDTH = 800
HEIGHT = World.HEIGHT = 600

speed = 400
world = World(gravity=0, gravity_z=100)
bird1 = PhysObj(Actor('bird0'), x=50, y=50, vx=speed, vy=speed, mu=1.4142)
bird2 = PhysObj(Actor('birddead'), x=50, y=50, vx=speed, vy=speed, damping=0.5)
bird3 = PhysObj(Actor('bird2'), x=50, y=50, vx=speed, vy=speed, drag=0.0035)
world.add(bird1)
world.add(bird2)
world.add(bird3)
