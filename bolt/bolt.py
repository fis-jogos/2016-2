WIDTH = 900
HEIGHT = 600

class Runner:
    """
    Representa um corredor de 100m rasos.
    """
    
    def __init__(self, name, country, x=0, v=0, tr=0.3, a0=4, vmax=7, lane=0):
        self.name = name
        self.country = country
        self.x = x
        self.v = v
        self.tr = tr
        self.a0 = a0
        self.vmax = vmax
        self.lane = lane
        self.sprite = Actor(country.lower(), pos=(x, lane * 50))
        self.sprite.left = x
        self.time = 0
        
    def __repr__(self):
        return "Runner(%r, x=%s)" % (self.name, self.x)
        
    def update(self, dt):
        """
        Atualiza posição e velocidade para o proximo frame.
        
        Args:
            dt (float):
                Intervalo de tempo (em segundos) entre um frame e o proximo.
        """
        self.time += dt
        if self.time > self.tr:
            a = self.a0 * (1 - self.v / self.vmax)**1.2
            self.v = self.v + a * dt
            self.x = self.x + self.v * dt + a * dt**2 / 2
        self.sprite.left = 8 * self.x
        
    def draw(self):
        """
        Desenha corredor na tela.
        """
        
        self.sprite.draw() 
        
class World:
    def __init__(self, objects=[]):
        self.objects = list(objects)
        
    def draw(self):
        for obj in self.objects:
            obj.draw()
            
    def update(self, dt):
        for obj in self.objects:
            obj.update(dt)
            
    def add(self, obj):
        self.objects.append(obj)
   
world = World([
    Runner("Usain Bolt", "Jamaica", tr=0.151, a0=8.3, vmax=12.2, lane=1),
    Runner("Gatlin", "USA", tr=0.0, a0=8.0, vmax=11.0, lane=2),
    Runner("Joao da Silva", "Brazil", lane=3),
])
 
def update(dt):
    world.update(dt)
    

def draw():
    screen.clear()
    world.draw()
 
