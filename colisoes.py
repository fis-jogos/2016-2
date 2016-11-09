from FGAme import *
from FGAme.physics import Collision
conf.set_resolution(1200, 800)


class CollisionWorld(World):
    def init(self):
        self.add.margin(10)
        self.objects = []
        for _ in range(10):
            rect = Rectangle(shape=(30, 40), pos=pos.random())
            rect.vel = vel.random()
            rect.inertia *= 5
            self.add(rect)
            self.objects.append(rect)
        
        
def resolve_collision(col):
    A, B = col
    n = col.normal
    e = 1
    mu = 1 / A.mass + 1 / B.mass
    J = (1 + e) * (B.vel - A.vel).dot(n) / mu
    Jvec = J * n
    A.vel += Jvec / A.mass
    B.vel -= Jvec / B.mass
    
    
Collision.resolve = resolve_collision

        
if __name__ == '__main__':
    world = CollisionWorld()
    world.run()
