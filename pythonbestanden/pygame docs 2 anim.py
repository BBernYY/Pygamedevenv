import pygame
import functies

# definieer contstanten
WIDTH, HEIGHT = 1280, 720 # constanten met hoofdletters
FPS = 60
SPEED = 300
ANIMATION_SPEED = 10
GRAVITY = 700
JUMP_FORCE = 300

class Player:
    pos = pygame.Vector2(WIDTH / 2, HEIGHT / 2)
    is_looking_left = False
    v_grav = 0
    class sprites:
        idle = functies.unpack_animation(pygame.image.load(functies.get_asset('Idle (32x32).png', 'Main Characters', 'Mask Dude')))
        run = functies.unpack_animation(pygame.image.load(functies.get_asset('Run (32x32).png', 'Main Characters', 'Mask Dude')))
    Frame = None
    to_be_rendered: pygame.Surface

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

running = True
# reken wat dingen uit
dt = 0
t = 0

def handle_events():
    global running
    running = True
    # pygame.QUIT event is als er op 'x' wordt gedrukt; dan sluit het spel af
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    return running
def handle_movement(keys):
    if keys[pygame.K_w]:
        Player.pos[1] -= SPEED * dt
    if keys[pygame.K_s]:
        Player.pos[1] += SPEED * dt
    if keys[pygame.K_a]:
        Player.pos[0] -= SPEED * dt
        Player.is_looking_left = True
    if keys[pygame.K_d]:
        Player.pos[0] += SPEED * dt
        Player.is_looking_left = False
    if keys[pygame.K_SPACE]:
        Player.v_grav = JUMP_FORCE

def handle_physics():
    Player.v_grav -= GRAVITY*dt
    Player.pos[1] -= Player.v_grav*dt


def handle_animation(keys):
    if sum(keys):
        Player.Frame = Player.sprites.run[int(t*ANIMATION_SPEED) % len(Player.sprites.run)]
    else:
        Player.Frame = Player.sprites.idle[int(t*ANIMATION_SPEED) % len(Player.sprites.idle)]
    
    
    Player.Frame = pygame.transform.flip(Player.Frame, Player.is_looking_left, False)
    Player.Frame = pygame.transform.scale(Player.Frame, (128,128))

def handle_drawing():
    screen.fill("black")
    screen.blit(Player.Frame, Player.pos)

    pygame.display.flip()

while running:
    t += dt
    # wacht op events
    handle_events()

    keys = pygame.key.get_pressed()

    handle_movement(keys)
    handle_physics()
    handle_animation(keys)
    handle_drawing()

    # Dit zorgt ervoor dat beweging niet afhankelijk is van de fps (en zet hem op 60) 
    dt = clock.tick(FPS) / 1000

pygame.quit() # eindscenario: dit gebruit na de while-loop