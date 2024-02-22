import pygame

# definieer contstanten
WIDTH, HEIGHT = 1280, 720 # constanten met hoofdletters
FPS = 60

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

# reken wat dingen uit
player_pos = pygame.Vector2(WIDTH / 2, HEIGHT / 2)

while running:
    # wacht op events
    # pygame.QUIT event is als er op 'x' wordt gedrukt; dan sluit het spel af
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # vul het scherm met paars; dat leegt ook alles van het vorige scherm
    screen.fill("purple")

    # CODE HIER VERDER

    # flip() tekent het ook echt op het scherm
    pygame.display.flip()

    clock.tick(FPS)  # zet de frames per seconde naar 60

pygame.quit() # eindscenario: dit gebruit na de while-loop