
import pygame
import math
from sprite import SpriteAnimation


class Boss:
    def __init__(self):
        self.sp = {
            'bossInicio': SpriteAnimation(
                'sprite\\boss\\Karasu_tengu\\inicio\\Idle', 13, 200, 200, 15
                ),
            'bossWalk': SpriteAnimation(
                'sprite\\boss\\Karasu_tengu\\walk\\Walk', 8, 200, 200, 20
                ),
            'bossDead': SpriteAnimation(
                'sprite\\boss\\Karasu_tengu\\Dead\\Dead', 6, 200, 200, 24
                ),
            'bossRun': SpriteAnimation(
                'sprite\\boss\\Karasu_tengu\\Run\\Run', 8, 200, 200, 20
                ),
            'bossAttack1': SpriteAnimation(
                'sprite\\boss\\Karasu_tengu\\ataque1\\Attack', 6, 200, 200, 15
                ),
            'bossAttack2': SpriteAnimation(
                'sprite\\boss\\Karasu_tengu\\ataque2\\Attack', 4, 200, 200, 15
                ),
            'bossAttack3': SpriteAnimation(
                'sprite\\boss\\Karasu_tengu\\ataque3\\Attack', 3, 200, 200, 15
                )
        }

        self.corazonImg = pygame.image.load('sprite\\Life\\corazon.png')
        self.corazonImg.convert_alpha()
        self.corazonImg2 = pygame.transform.scale(self.corazonImg, (60, 60))

        self.ini = True
        self.vida = 11
        self.newposx = 600
        self.newposy = 400
        self.direction = False

        self.isjump = False
        self.angulo = 0.0
        self.jump_sprite = [
            pygame.image.load(f"sprite\\boss\\Karasu_tengu\\jump\\Jump{i}.png")
            .convert_alpha()
            for i in range(15)
            ]
        self.jump_sprite_index = 0

        self.Move = self.sp['bossWalk']

    def inicio(self):
        return self.sp['bossInicio']

    def Run(self):
        return self.sp['bossRun']

    def Dead(self):
        return self.sp['bossDead']

    def saltar(self, screen: int):
        # Incrementar el ángulo
        self.angulo += 0.1

        # Usando una función seno en el ángulo.
        # Esto crea un movimiento de salto que se parece a un arco.
        self.newposy = 413 - math.sin(self.angulo) * 200
        self.newposy -= 0.8888833905372
        # Calcula la fase actual del salto dividiendo el ángulo actual
        # por pi y multiplicándolo por el número de fases de salto
        fase = int((self.angulo / math.pi) * 14)
        # Parte de selección y escalado y pintado del sprite
        img = self.jump_sprite[fase]
        img1 = pygame.transform.scale(img, (200, 200))
        img2 = pygame.transform.flip(img1, self.direction, False)
        screen.blit(img2, (self.newposx, self.newposy))

        # Restablecer las variables angulo e isjump cuando se termina el salto
        if self.angulo > math.pi:
            fase = 0
            self.angulo = 0.0
            self.isjump = False

    def atacar(self, atq: int):
        if atq == 1:
            return self.sp['bossAttack1']
        if atq == 2:
            return self.sp['bossAttack2']
        if atq == 3:
            return self.sp['bossAttack3']

    def corazon(self, screen: int):
        for i in range(self.vida):
            screen.blit(
                self.corazonImg2, (i*2*self.corazonImg2.get_width(), 610)
                )

    def move(self):

        if self.newposx <= 600:
            self.direction = False  # Mover a la derecha
        elif self.newposx >= 900:
            self.direction = True  # Mover a la izquierda

        if self.direction:
            self.newposx -= 1  # Mover a la derecha
            return self.sp['bossWalk']

        else:
            self.newposx += 1  # Mover a la izquierda
            return self.sp['bossWalk']

    def pintar(self, s: int):
        self.Move.animation(s, self.newposx, self.newposy, self.direction)
