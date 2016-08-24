import random

TITLE = 'Flappy'
WIDTH = 400
HEIGHT = 708
GRAVITY = 500
JUMPSPEED = 200
SPEED = 3
GAP = 130
OBS_HEIGHT = 500
HEIGHT_RANGE = (-50, 200)


bird = Actor('bird0', pos=(100, HEIGHT / 2))
bird.vy = 0
bird.dead = False
bottom = Actor('bottom', pos=(-100, 400))
top = Actor('top', pos=(-100, 400))


def set_random_height():
    top.y = random.randint(*HEIGHT_RANGE)
    bottom.y = top.y + GAP + OBS_HEIGHT
    if bird.dead:
        bird.y = HEIGHT / 2
        bird.image = 'bird0'
        bird.vy = 0
        bird.dead = False

def dead():
    bird.dead = True
    bird.image = 'birddead'

def update(dt):
    # Atualiza passaro
    bird.y += bird.vy * dt
    bird.vy += GRAVITY * dt
    if keyboard.space and not bird.dead:
        bird.vy = -JUMPSPEED
    if not bird.dead:
        if bird.vy < -20:
            bird.image = 'bird2'
        elif bird.vy > 20:
            bird.image = 'bird1'
        else:
            bird.image = 'bird0'
        
    # Atualiza obstaculos    
    bottom.x -= SPEED
    top.x -= SPEED
    if bottom.x < -100:
        set_random_height()
        bottom.x = top.x = WIDTH + 50
        
    # Checa colisao
    if not bird.dead and bird.right > top.left and bird.left < top.right:
        if bird.bottom > bottom.top or bird.top < top.bottom:
            dead()

def draw():
    screen.blit('background', pos=(0, 0))
    bottom.draw()
    top.draw()
    bird.draw()
    

