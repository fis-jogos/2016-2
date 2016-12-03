from FGAme import *


class PongWorld(World):
    def init(self):
        self.add.margin(-200, 10)
        self.ball = Ball(pos=pos.middle)
        self.small_balls = [
            self.add.circle(10, pos=(450, 40 + 50 * x), color='green', density=2)
            for x in range(11)
        ]
        self.ball.vel = vel.random()
        
        self.player1 = HumanPlayer(pos=(770, 300))
        self.player2 = AIPlayer(self.ball, pos=(30, 300))
        self.add([self.player1, self.player2, self.ball])


class Ball(Circle):
    def __init__(self, **kwargs):
        super().__init__(20, color='red', **kwargs)
        on('frame-enter').do(self.update)

    def update(self):
        if abs(self.vel) < 700:
            self.vel *= 1.01        

class Player(AABB):
    def __init__(self, pos, **kwargs):
        super().__init__(pos=pos, shape=(20, 120), mass='inf', **kwargs)


class HumanPlayer(Player):
    def __init__(self, step=5, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.key_up_handler = on('long-press', 'up').do(self.move, (0, step))
        self.key_down_handler = on('long-press', 'down').do(self.move, (0, -step))

    
class AIPlayer(Player):
    def __init__(self, ball, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ball = ball
        on('frame-enter').do(self.update)

    def update(self):
        dy = self.y - self.ball.y
        if dy > 0:
            self.move(0, -min(5, abs(dy)))
        else:
            self.move(0, min(5, abs(dy)))  


def start_game():    
    world = PongWorld()
    world.run()    

