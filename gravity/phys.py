from math import sqrt
import smallvectors as sv


Vec = sv.Vec[2, float]


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
    def __init__(self, actor, mass=1, pos=(0, 0), vel=(0, 0), 
                 gravity=0, gravity_z=0, damping=0, mu=0, drag=0):
        self.actor = actor
        self.pos = Vec(*pos)
        self.vel = Vec(*vel)
        self.force = Vec(0, 0)
        self.mass = mass
        self.gravity = gravity
        self.gravity_z = gravity_z
        self.damping = damping
        self.mu = mu
        self.drag = drag
        
    def kinetic_energy(self):
        return self.mass * self.vel.norm_sqr() / 2
        
    def potential_energy(self):
        return self.mass * self.gravity * self.pos.y

    def total_energy(self):
        return self.kinetic_energy() + self.potential_energy()
        
    def update(self, dt):
        # Calcula a aceleracao devido ao atrito
        v_abs = self.vel.norm()
        if v_abs == 0:
            u = Vec(0, 0)
        else:
            u = self.vel / v_abs
        friction = - self.mu * self.gravity_z * u
        
        # Arrasto aerodinamico
        drag = -self.drag * v_abs * v_abs * u 
        
        # Aceleracao devido a forca de dissipacao viscosa
        damping = -self.damping * self.vel
        
        # Aceleracao da gravidade
        gravity = Vec(0, -self.gravity)
        
        # Soma todas as forcas
        a = self.force / self.mass + friction + damping + gravity + drag
        
        self.vel += a * dt
        self.pos += self.vel * dt
        self.accel = a
        self.update_collisions()
    
    def update_collisions(self):
        v = self.vel
        if self.pos.x < 10 and self.vel.x < 0:
            self.vel = Vec(-v.x, v.y)
        elif self.pos.x > World.WIDTH - 10 and self.vel.x > 0:
            self.vel = Vec(-v.x, v.y)
        if self.pos.y < 10 and self.vel.y < 0:
            self.vel = Vec(v.x, -v.y)
        elif self.pos.y > World.HEIGHT - 10 and self.vel.y > 0:
            self.vel = Vec(v.x, -v.y)
    
    def draw(self):
        self.actor.x = self.pos.x
        self.actor.y = World.HEIGHT - self.pos.y
        self.actor.draw() 
