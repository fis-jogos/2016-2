class World:
    """
    Representa o conjunto de todos os objetos na simulacao.
    """
    
    WIDTH = 800
    HEIGHT = 600  
    
    def __init__(self, objects=[], gravity=0):
        self.objects = list(objects)
        self.gravity = gravity
        
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


class PhysObj:
    """
    Representa um objeto com uma fisica associada.
    """
    def __init__(self, actor, mass=1, x=0, y=0, vx=0, vy=0, 
                 gravity=0, gravity_z=0, damping=0, mu=0):
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
        
    def update(self, dt):
        ax = self.fx / self.mass - self.damping * self.vx
        ay = self.fy / self.mass - self.gravity - self.damping * self.vy
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

speed = 300
world = World(gravity=0)
bird1 = PhysObj(Actor('bird0'), x=50, y=50, vx=speed, vy=1.5*speed)
bird2 = PhysObj(Actor('bird1'), x=50, y=100, vx=speed, vy=1.5*speed, damping=2)
world.add(bird1)
world.add(bird2)

