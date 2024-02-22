import pygame
import classes

# definieer contstanten
WIDTH, HEIGHT = 1280, 720 # constanten met hoofdletters
FPS = 60
SPEED = 300

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

# reken wat dingen uit
player_pos = pygame.Vector2(WIDTH / 2, HEIGHT / 2)
dt = 0
t = 0

while running:
    t += 1
    # wacht op events
    # pygame.QUIT event is als er op 'x' wordt gedrukt; dan sluit het spel af
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # vul het scherm met paars; dat leegt ook alles van het vorige scherm
    screen.fill("purple")

    screen.blit(classes.b[t % len(classes.b)], player_pos) # teken de speler

    

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= SPEED * dt
    if keys[pygame.K_s]:
        player_pos.y += SPEED * dt
    if keys[pygame.K_a]:
        player_pos.x -= SPEED * dt
    if keys[pygame.K_d]:
        player_pos.x += SPEED * dt

    # flip() tekent het ook echt op het scherm
    pygame.display.flip()

    # Dit zorgt ervoor dat beweging niet afhankelijk is van de fps (en zet hem op 60) 
    dt = clock.tick(FPS) / 1000

pygame.quit() # eindscenario: dit gebruit na de while-loop