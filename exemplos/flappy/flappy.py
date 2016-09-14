from random import randint 

WIDTH = 400 
HEIGHT = 800
GRAVITY = 500
JUMP_SPEED = 300
OBS_SPEED = 150
PAUSED = False

# Cria passarinho
bird = Actor('bird0', pos=(70, 300))
bird.vy = 0 
bird.is_dead = False


# Cria canos
top = Actor('top', pos=(WIDTH, 100))
bottom = Actor('bottom', pos=(WIDTH, top.y + 650))

def kill_bird():
    bird.is_dead = True
    bird.image = 'birddead'
    
def update(dt):
    global PAUSED

    if PAUSED:
        if keyboard.p:
            PAUSED = False
        return

    # Atualiza estado do passarinho
    bird.vy = bird.vy + GRAVITY * dt 
    bird.y = bird.y + bird.vy * dt
    
    # Atualiza estado dos obstáculos
    top.right -= OBS_SPEED * dt
    bottom.right -= OBS_SPEED * dt
    if top.right < 0:
        top.x += WIDTH + 100
        bottom.x += WIDTH + 100
        top.y = randint(-150, 250)
        bottom.y = top.y + 650
    
    # Controle de teclado
    if keyboard.space or keyboard.up:
        if bird.is_dead:
            bird.vy = 0
            bird.is_dead = False
            bird.y = 300
            bird.image = 'bird0'
        else:
            bird.vy = -JUMP_SPEED
    if keyboard.p:
        PAUSED = True
            
    # Detecta colisão
    if bird.y >= HEIGHT:
        kill_bird()
    if bird.right > top.left and bird.left < top.right:
        if bird.bottom > bottom.top:
            kill_bird()
        if bird.top < top.bottom:
            kill_bird()
                
    
    
def draw():
    screen.clear()
    top.draw()
    bottom.draw()
    bird.draw()
    

