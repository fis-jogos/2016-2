class World:
    """
    Representa o conjunto de todos os objetos na simulacao.
    """
    
    WIDTH = 800
    HEIGHT = 600  
    
    def __init__(self, objects=[]):
        self.objects = list(objects)
        
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


class PhysObj:
    """
    Representa um objeto com uma fisica associada.
    """
    def __init__(self, actor, mass=1, x=0, y=0, vx=0, vy=0):
        self.actor = actor
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.fx = 0
        self.fy = 0
        self.mass = mass
        
    def update(self, dt):
        ax = self.fx / self.mass
        ay = self.fy / self.mass
        self.vx += ax * dt
        self.vy += ay * dt
        self.x += self.vx * dt + ax * dt**2 / 2
        self.y += self.vy * dt + ay * dt**2 / 2
    
    def draw(self):
        self.actor.x = self.x
        self.actor.y = World.HEIGHT - self.y
        self.actor.draw()     
        
