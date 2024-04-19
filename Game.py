import pygame
from personajes import knight, enemy, Boss
import time
import random


pygame.init()

screen = pygame.display.set_mode((1280, 670))
pygame.display.set_caption("Fake Souls")
running = True

# Inicializa el mezclador de música
pygame.mixer.init()
# Carga la música
pygame.mixer.music.load(
    'music\\Soul-of-Cinder-True-8-Bit.mp3'
    )
# Reproduce la música
# El -1 hace que la música se repita indefinidamente
pygame.mixer.music.play(-1)


clock = pygame.time.Clock()


background = [
    pygame.image.load(
        "background\\PNG\\Battleground1\\Bright\\Battleground1.png"
        ).convert(),

    pygame.image.load(
        "background\\PNG\\Battleground4\\Bright\\Battleground4.png"
        ).convert(),

    pygame.image.load(
        "background\\PNG\\Battleground2\\Bright\\Battleground2.png"
        ).convert()
]


player = knight()
boss = Boss()
esqueletoS = enemy(0)
esqueletoL = enemy(1)

boss.Move = boss.inicio()
indBack = 0
ataqueR = 3

Background = background[indBack]

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # Actualización del fondo
    if player.newposx > 1230 and indBack <= 1:
        indBack += 1
        Background = background[indBack]
        player.newposx = -40
    elif player.newposx < -50 and indBack >= 1:
        indBack -= 1
        Background = background[indBack]
        player.newposx = 1200

    # Dibujar el fondo
    screen.blit(Background, [0, 0])

    # seleccionamos al enemigo a operar
    if indBack == 0:
        enemigo = esqueletoS
    if indBack == 1:
        enemigo = esqueletoL
    if indBack == 2:
        enemigo = boss

    # chekeadores de enemigo
    VIDACHECKP = player.vida != 0
    PLAYERDENE = abs(player.newposx - enemigo.newposx) <= 100
    PLAYERY_400 = player.newposy == 400
    PLAYERMEIENEMIGO_300 = player.newposx <= enemigo.newposx + 300
    PLAYERMEIENEMIGO_110 = player.newposx <= enemigo.newposx + 110
    PLAYERMAIENEMIGO_400 = player.newposx >= enemigo.newposx - 300
    PLAYERMAIENEMIGO_120 = player.newposx >= enemigo.newposx - 110
    PLAYERMAIENEMIGO = player.newposx >= enemigo.newposx
    PLAYERMEIENEMIGO = player.newposx <= enemigo.newposx

    # enemigo detecta posicion del personaje y ataca
    if indBack == 0 or indBack == 1:
        if enemigo.vida == 1:
            # Actualización y dibujo del enemigo
            if enemigo.walking:
                enemigo.move = enemigo.movE()
                enemigo.pintarE(screen, background)

            if PLAYERMAIENEMIGO and PLAYERMEIENEMIGO_300 and VIDACHECKP:
                enemigo.walking = False
                enemigo.direction = False
                enemigo.atta = enemigo.attack()
                hit = enemigo.atta.animationF
                enemigo.pintarE(screen, background)
                if PLAYERMEIENEMIGO_110 and PLAYERY_400 and hit:
                    player.hurting = True
                    player.vida -= 1
                    player.newposx += 100

            elif PLAYERMEIENEMIGO and PLAYERMAIENEMIGO_400 and VIDACHECKP:
                enemigo.walking = False
                enemigo.direction = True
                enemigo.atta = enemigo.attack()
                hit = enemigo.atta.animationF
                enemigo.pintarE(screen, background)
                if PLAYERMAIENEMIGO_120 and PLAYERY_400 and hit:
                    player.hurting = True
                    player.vida -= 1
                    player.newposx -= 100

            else:
                enemigo.walking = True

        if enemigo.vida == 0 and enemigo.Dead.animationF is False:
            enemigo.Dead = enemigo.dead()
            enemigo.pintarE(screen, background)

    else:
        # CODIGO DEL BOSS:
        boss.corazon(screen)

        # chekeadores del boss:
        PLAYERMEIBOSS = player.newposx <= boss.newposx
        PLAYERMAIBOSS = player.newposx >= boss.newposx
        PLAYERMAIBOSS_450 = player.newposx >= boss.newposx-450
        PLAYERMEIBOSS_450 = player.newposx <= boss.newposx+450
        PLAYERDBOSS = abs(player.newposx - enemigo.newposx) <= 150

        if boss.vida == 0:
            boss.Move = boss.Dead()

            if boss.Move.animationF:
                time.sleep(2)
                running = False
        else:

            if boss.ini:
                boss.Move = boss.inicio()
                if boss.Move.animationF:
                    boss.ini = False
            else:

                if PLAYERMEIBOSS and PLAYERMAIBOSS_450 and VIDACHECKP:
                    boss.direction = True
                    boss.Move = boss.Run()
                    if -abs(player.newposx - enemigo.newposx) <= -150:
                        boss.newposx -= 6
                elif PLAYERMAIBOSS and PLAYERMEIBOSS_450 and player.vida != 0:
                    boss.direction = False
                    boss.Move = boss.Run()
                    if abs(player.newposx - enemigo.newposx) >= 150:
                        boss.newposx += 6
                else:
                    boss.Move = boss.move()

                if PLAYERDBOSS and PLAYERY_400 and VIDACHECKP:
                    boss.Move = boss.atacar(ataqueR)
                    if boss.Move.animationF:
                        ataqueR = random.randint(1, 3)
                        player.vida -= 1
                        boss.Move.animationF = False

            boss.pintar(screen)
            # boss.saltar(screen)

    player.corazon(screen)

    # Jugador muerte GAME OVER
    if player.vida == 0:
        player.Dead = player.dead()
        player.pintar(screen, background)
        f = player.Dead.animationF
        if f:
            time.sleep(2)
            running = False
    else:
        # Actualización y dibujo del personaje
        player.mov = player.mover(events, indBack)

        if player.isjump:
            player.saltar(screen)
        else:
            player.pintar(screen, Background)

    # atacar al enemigo:
    if PLAYERDENE and PLAYERY_400 and player.ataque is True:
        if enemigo != boss and enemigo.vida > 0:
            enemigo.vida -= 1
            player.vida += 1

        if enemigo == boss:
            enemigo.vida -= 1
            if boss.direction is False:
                boss.newposx -= 250
            else:
                boss.newposx += 250

    player.ataque = False

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar los fps
    clock.tick(60)

pygame.mixer.music.stop()
pygame.quit()
