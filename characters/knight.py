
import pygame

from sprite import SpriteAnimation


class Knight:
    def __init__(self):
        self.sp = {
            'caballero': SpriteAnimation(
                "sprite\\caballero\\Knight_1\\idle\\idle", 4, 200, 200, 15
                ),
            'caballeroRun': SpriteAnimation(
                "sprite\\caballero\\Knight_1\\RunRight\\Run", 7, 200, 200, 10
                ),
            'caballeroAttackSoft': SpriteAnimation(
                'sprite\\caballero\\Knight_1\\attack1\\Attack', 5, 200, 200,
                0.10
                ),
            'caballeroAttackMiddle': SpriteAnimation(
                "sprite\\caballero\\Knight_1\\attack2\\Attack", 4, 200, 200,
                0.10
                ),
            'caballeroAttack3': SpriteAnimation(
                "sprite\\caballero\\Knight_1\\attack3\\Attack", 4, 200, 200,
                0.10
                ),
            'caballeroRunAttack': SpriteAnimation(
                'sprite\\caballero\\Knight_1\\RunAtack\\RunAttack', 6, 200,
                200, 8
                ),
            'caballeroDead':  SpriteAnimation(
                'sprite\\caballero\\Knight_1\\dead\\Dead', 6, 200, 200, 24
                ),
            'caballeroHurt': SpriteAnimation(
                "sprite\\caballero\\Knight_1\\hurt\\Hurt", 2, 200, 200, 10
                )
        }

        self.vida = 3
        self.ataque = False

        # poscionamiento del sprite
        self.newposx = 50
        self.newposy = 400
        self.direction = False

        # detertor de ataque
        self.acc = False

        # variables del salto
        self.isjump = False
        self.angulo = 0.0
        self.jump_sprites = [
            pygame.image.load(
                f"sprite\\caballero\\Knight_1\\jump\\jump{i}.png")
            .convert_alpha()
            for i in range(6)
            ]
        self.jump_sprite_index = 0

        # variables de hurt
        self.hurting = False

        self.corazonImg = pygame.image.load('sprite\\Life\\corazon.png')
        self.corazonImg.convert_alpha()
        self.corazonImg2 = pygame.transform.scale(self.corazonImg, (50, 50))

        # sprite predeterminada del caballero
        self.mov = self.sp['caballero']

        self.Dead = self.sp['caballeroDead']

        self.Hurt = self.sp['caballeroHurt']

    def corazon(self, screen: int):
        for i in range(self.vida):
            screen.blit(self.corazonImg2, (i*self.corazonImg2.get_width(), 10))

    def dead(self):
        return self.sp['caballeroDead']

    def hurt(self):
        return self.sp['caballeroHurt']

    # AAAAAAAAAAAAAAA TENGO QUE ESTUDIAR MATEMATICASSSS "EL METODO"
    def saltar(self, screen: int):
        # usando una función seno en el angulo
        # Esto crea un movimiento de salto que se parece a un arco.
        self.newposy = 413 - math.sin(self.angulo) * 200
        self.newposy -= 0.8888833905372
        # Calcula la fase actual del salto dividiendo el ángulo actual por pi
        # y multiplicándolo por el número de fases de salto
        fase = int((self.angulo / math.pi) * 6)
        # parte de seleccion y escalado y pintado del sprite
        img = self.jump_sprites[fase]
        img1 = pygame.transform.scale(img, (200, 200))
        img2 = pygame.transform.flip(img1, self.direction, False)
        screen.blit(img2, (self.newposx, self.newposy))

        # Si el ángulo es mayor que 0, lo incrementas en 0.070.
        # Esto hace que el personaje suba y luego baje,
        # ya que la función seno aumenta hasta que el ángulo es igual a pi,
        # y luego disminuye.
        # Cuando el ángulo alcanza o supera pi, lo reinicia a 0
        if self.angulo > 0:
            self.angulo += 0.070
        if self.angulo >= math.pi:
            self.isjump = False
            self.angulo = 0.0

    def mover(self, events, limt):
        limit_A = limt == 0 and self.newposx <= -50
        limit_B = limt == 2 and self.newposx <= -50
        teclas = pygame.key.get_pressed()

        if self.isjump is False and self.hurting is False:

            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x and self.direction is False:
                        self.acc = True
                        self.ataque = True
                        return self.sp['caballeroAttackMiddle']
                    if event.key == pygame.K_x and self.direction is True:
                        self.acc = True
                        self.ataque = True
                        return self.sp['caballeroAttackMiddle']

                    if event.key == pygame.K_z and self.direction is False:
                        self.acc = True
                        self.ataque = True
                        return self.sp['caballeroAttackSoft']
                    if event.key == pygame.K_z and self.direction is True:
                        self.acc = True
                        self.ataque = True
                        return self.sp['caballeroAttackSoft']

                    if event.key == pygame.K_c and self.direction is False:
                        self.acc = True
                        self.ataque = True
                        return self.sp['caballeroAttack3']
                    if event.key == pygame.K_c and self.direction is True:
                        self.acc = True
                        self.ataque = True
                        return self.sp['caballeroAttack3']

                    if event.key == pygame.K_SPACE:
                        self.isjump = True
                        self.angulo = 0.001

        if self.hurting is False:

            if teclas[pygame.K_RIGHT]:  # Flecha derecha
                self.direction = False
                if limt == 2 and self.newposx >= 1200-60:
                    self.newposx = 1200-60
                else:
                    self.newposx += 10
                return self.sp['caballeroRun']

            elif teclas[pygame.K_LEFT]:
                self.direction = True
                if (limit_A) or (limit_B):
                    self.newposx = -50
                else:
                    self.newposx -= 10
                return self.sp['caballeroRun']

            else:
                if self.direction is False:
                    return self.sp['caballero']
                else:
                    self.direction = True
                    return self.sp['caballero']

    def pintar(self, s: int, background: str):
        if self.vida != 0:
            if self.hurting is False:
                if self.acc:
                    self.mov.animation_2(s, self.newposx, self.newposy,
                                         self.direction, background)
                    self.acc = False
                else:
                    self.mov.animation(s, self.newposx, self.newposy,
                                       self.direction)
            else:
                self.Hurt.animation(s, self.newposx, self.newposy,
                                    self.direction)
                if self.Hurt.animationF:
                    self.hurting = False
        else:
            self.Dead.animation(s, self.newposx, self.newposy, self.direction)

