import pygame
from p import *
import time

pygame.init()

screen = pygame.display.set_mode((1280, 670))
pygame.display.set_caption("Fake Souls")
clock=pygame.time.Clock()
running = True
background=pygame.image.load("prueba\\Battleground1.png").convert()


Player=player(50,50)
def handleMov():
    keys=pygame.key.get_pressed()
    Player.velx=0
    if keys[pygame.K_LEFT]:
        Player.movL(5)
    if keys[pygame.K_RIGHT]:
        Player.movD(5)


def flip(sprites):
    return[pygame.transform.flip(sprite,True,False) for sprite in sprites]
    

def loadSprite(sp,i2,anc,alt,posx,posy,flipx):
     # Cargamos las imágenes del sprite en una lista
        spriteArray = [pygame.image.load(f'{sp}{i}.png').convert_alpha() for i in range(i2)]
        #lo pasamos a otra lista para cambiar su escalado
        sprite_escalado = [pygame.transform.scale(spriteArray[i], (anc, alt)) for i in range(i2)]

        SpriteFlip = [pygame.transform.flip(sprite, flipx, False) for sprite in sprite_escalado]

        for i in range(i2):
            # Crea un rectángulo que cubre el sprite
            sprite_rect = pygame.Rect(posx, posy, SpriteFlip[i].get_width(), SpriteFlip[i].get_height())
            
            # Dibuja una porción del fondo sobre el sprite
            screen.blit(background, (posx, posy), sprite_rect)
            
            # Dibuja el sprite
            screen.blit(SpriteFlip[i], (posx, posy))
            
            pygame.display.flip()
            time.sleep(60)



while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(background, (0, 0))


    Player.loop(FPS)
    handleMov()
    Player.draw(screen)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar los fps
    clock.tick(60)


pygame.quit()
