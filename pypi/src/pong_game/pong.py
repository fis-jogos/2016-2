from FGAme import *

world.add.margin(-200, 10)
p1 = world.add.aabb(shape=(20, 120), pos=(770, 300), mass='inf')
p2 = world.add.aabb(shape=(20, 120), pos=(30, 300), mass='inf')
c1 = world.add.circle(20, pos=(400, 300), color='red')
c2 = world.add.circle(10, pos=(450, 300), color='green')


@listen('long-press', 'up', dy=5)
@listen('long-press', 'down', dy=-5)
def move_p1(dy):
    p1.move(0, dy)
        

@listen('frame-enter')
def p2_play():
    if abs(p2.y - c1.y) < 30:
        pass
    elif p2.y > c1.y:
        p2.move(0, -5)
    else:
        p2.move(0, 5)

