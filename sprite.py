import pygame
import time



class SpriteAnimation(pygame.sprite.Sprite):
    def __init__(self, sp, i2, anc, alt, fps):
        super().__init__()
        #toma la ruta de la imagen hasta el nombre de la imagen sin contar su extencion (obligatoriamente tiene que ser png)
        self.sp = sp
        #indica la cantida de sprite que tiene la animacion
        self.i2 = i2

        #el tamano de la imagen
        self.anc=anc
        self.alt=alt

    
        self.indSprite = 0

        self.cont=0
       
        #es la pausa por cada frame que va a tener para el cambio de cada imgaen
        self.fps=fps

        self.animationF = False  # variable para rastrear si la animación ha terminado

        # Cargamos los sprites al inicializar
        self.sprites = self.cargadesrpite()



    def cargadesrpite(self):
        # Cargamos las imágenes del sprite en una lista
        spriteArray = [pygame.image.load(f'{self.sp}{i}.png').convert_alpha() for i in range(self.i2)]
        #lo pasamos a otra lista para cambiar su escalado
        sprite_escalado = [pygame.transform.scale(spriteArray[i], (self.anc, self.alt)) for i in range(self.i2)]
        return sprite_escalado

    def animation(self, screen,posx,posy,flipx):

        SpriteFlip = [pygame.transform.flip(sprite, flipx, False) for sprite in self.sprites]
        
        # Dibujamos el sprite actual en la pantalla
        screen.blit(SpriteFlip[self.indSprite], (posx,posy))

        
        self.cont+=1

        if self.cont==self.fps:
            # Actualizamos el índice del sprite (cambiamos al siguiente sprite)
            self.indSprite = (self.indSprite + 1) % len(self.sprites)

            self.cont=0
            
            #detecta si ya se llego al ultimo sprite
            if self.indSprite == len(self.sprites) - 1:
                self.animationF = True
            else:
                self.animationF = False

    

    def animation_2(self, screen,posx,posy,flipx,background):
       SpriteFlip = [pygame.transform.flip(sprite, flipx, False) for sprite in self.sprites]

       for i in range(self.i2):
        # Crea un rectángulo que cubre el sprite
        sprite_rect = pygame.Rect(posx, posy, SpriteFlip[i].get_width(), SpriteFlip[i].get_height())
        
        # Dibuja una porción del fondo sobre el sprite
        screen.blit(background, (posx, posy), sprite_rect)
        
        # Dibuja el sprite
        screen.blit(SpriteFlip[i], (posx, posy))


        if i==self.i2:
            self.animationF = True
        else:
            self.animationF = False

        pygame.display.flip()
        time.sleep(self.fps)




   
