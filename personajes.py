import pygame
import math

from sprite import *












class knight:
    def __init__(self):
        self.sp={
            'caballero':SpriteAnimation("sprite\caballero\Knight_1\idle\idle",4,200,200,15),
            'caballeroRun':SpriteAnimation("sprite\caballero\Knight_1\RunRight\Run",7,200,200,10),
            'caballeroAttackSoft':SpriteAnimation('sprite\caballero\Knight_1\\attack1\Attack',5,200,200,0.10),
            'caballeroAttackMiddle':SpriteAnimation("sprite\\caballero\\Knight_1\\attack2\\Attack",4,200,200,0.10),
            'caballeroAttack3':SpriteAnimation("sprite\\caballero\\Knight_1\\attack3\\Attack",4,200,200,0.10),
            'caballeroRunAttack':SpriteAnimation('sprite\caballero\Knight_1\RunAtack\RunAttack',6,200,200,8),
            'caballeroDead':SpriteAnimation('sprite\caballero\Knight_1\\dead\\Dead',6,200,200,24),
            'caballeroHurt':SpriteAnimation("sprite\caballero\Knight_1\hurt\Hurt",2,200,200,10)
            
        }

        self.vida=3
        self.ataque=False

        #poscionamiento del sprite
        self.newposx=50
        self.newposy=400
        self.direction = False

        #detertor de ataque
        self.acc=False

        #variables del salto
        self.isjump=False
        self.angulo=0.0
        self.jump_sprites = [pygame.image.load(f"sprite\caballero\Knight_1\jump\jump{i}.png").convert_alpha() for i in range(6)]
        self.jump_sprite_index = 0

        #variables de hurt
        self.hurting=False
        # self.HurtSprite=[pygame.image.load(f'sprite\caballero\Knight_1\hurt\Hurt{i}.png').convert_alpha() for i in range(2)]
        # self.HurtSpriteS=[pygame.transform.scale(self.HurtSprite[a],(200,200)) for a in range(2)]

        self.corazonImg=pygame.image.load('sprite\\Life\\corazon.png').convert_alpha()
        self.corazonImg2=pygame.transform.scale(self.corazonImg,(50,50))
        

        #sprite predeterminada del caballero
        self.mov=self.sp['caballero']

        self.Dead=self.sp['caballeroDead']

        self.Hurt=self.sp['caballeroHurt']


    def corazon(self,screen):
        for i in range(self.vida):
            screen.blit(self.corazonImg2, (i*self.corazonImg2.get_width(), 10))
    
    def dead(self):
        return self.sp['caballeroDead']
    
    def hurt(self):
        return self.sp['caballeroHurt']
    
    
        


    #AAAAAAAAAAAAAAA TENGO QUE ESTUDIAR MATEMATICASSSS "EL METODO"
    def saltar(self,screen):
        #usando una función seno en el angulo. Esto crea un movimiento de salto que se parece a un arco.
        self.newposy = 413 - math.sin(self.angulo) * 200
        self.newposy-=0.8888833905372
        #Calcula la fase actual del salto dividiendo el ángulo actual por pi y multiplicándolo por el número de fases de salto
        fase = int((self.angulo / math.pi) * 6)
        #parte de seleccion y escalado y pintado del sprite
        img = self.jump_sprites[fase]
        img1 = pygame.transform.scale(img, (200, 200))
        img2 = pygame.transform.flip(img1, self.direction, False)
        screen.blit(img2, (self.newposx, self.newposy))

        #Si el ángulo es mayor que 0, lo incrementas en 0.070. 
        #Esto hace que el personaje suba y luego baje, ya que la función seno aumenta hasta que el ángulo es igual a pi, y luego disminuye. Cuando el ángulo alcanza o supera pi, lo reinicia a 0 
        if self.angulo > 0: 
            self.angulo += 0.070
        if self.angulo >= math.pi:
            self.isjump = False 
            self.angulo = 0.0
            

        
   
            
        

    def mover(self,events,limt):
        teclas = pygame.key.get_pressed()

        if self.isjump==False and self.hurting==False:

            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x and self.direction==False:
                        self.acc=True
                        self.ataque=True
                        return self.sp['caballeroAttackMiddle']
                    if event.key == pygame.K_x and self.direction==True:
                        self.acc=True
                        self.ataque=True
                        return self.sp['caballeroAttackMiddle']
                    
                    if event.key == pygame.K_z and self.direction==False:
                        self.acc=True
                        self.ataque=True
                        return self.sp['caballeroAttackSoft']
                    if event.key == pygame.K_z and self.direction==True:
                        self.acc=True
                        self.ataque=True
                        return self.sp['caballeroAttackSoft']
                    
                    if event.key == pygame.K_c and self.direction==False:
                        self.acc=True
                        self.ataque=True
                        return self.sp['caballeroAttack3']
                    if event.key == pygame.K_c and self.direction==True:
                        self.acc=True
                        self.ataque=True
                        return self.sp['caballeroAttack3']
                    

                    if event.key==pygame.K_SPACE:
                        self.isjump=True
                        self.angulo=0.001
                
        
        if self.hurting==False:
                
        


            
            if teclas[pygame.K_RIGHT]:  # Flecha derecha
                self.direction = False
                if limt==2 and self.newposx>=1200-60:
                    self.newposx=1200-60
                else:
                    self.newposx+= 10
                return self.sp['caballeroRun']
            
            elif teclas[pygame.K_LEFT]:
                self.direction = True
                if (limt==0 and self.newposx<=-50) or (limt==2 and self.newposx<=-50):
                    self.newposx=-50
                else:
                    self.newposx-=10
                return self.sp['caballeroRun']
            
            else:
                if self.direction==False:
                    return self.sp['caballero']
                else:
                    self.direction=True
                    return self.sp['caballero']
                
        
        

    def pintar(self, s, background):
        if self.vida!=0:
            if self.hurting==False:
                if self.acc:
                    self.mov.animation_2(s, self.newposx,self.newposy,self.direction,background)
                    self.acc=False
                else:
                    self.mov.animation(s, self.newposx,self.newposy,self.direction)
            else:
                self.Hurt.animation(s, self.newposx,self.newposy,self.direction)
                if self.Hurt.animationF:
                    self.hurting=False
        else:
            self.Dead.animation(s, self.newposx,self.newposy,self.direction)
    




class enemy:
    def __init__(self,s):
        self.sp={
            'esqueletoWalk':SpriteAnimation('sprite\esqueletos\Skeleton_Warrior\walk\Walk',7,200,200,24),
            'esqueletoattack':SpriteAnimation('sprite\esqueletos\Skeleton_Warrior\\attack2\\Attack',4,200,200,10),
            'esqueletoDead':SpriteAnimation('sprite\esqueletos\Skeleton_Warrior\\Dead\\Dead',4,200,200,20)
            
        }

        self.sp2={
            'esqueletoWalkL':SpriteAnimation('sprite\esqueletos\Skeleton_Spearman\\walk\Walk',7,200,200,24),
            'esqueletoattackL':SpriteAnimation('sprite\esqueletos\Skeleton_Spearman\\attack\Attack',4,200,200,10),
            'esqueletoDeadL':SpriteAnimation('sprite\esqueletos\Skeleton_Spearman\\dead\\Dead',5,200,200,20)
        }

        

        self.s=s
        self.newposx=600
        self.newposy=400
        self.direction=False
        self.acc=False
        self.walking=True
        self.vida=1
        self.move=self.sp['esqueletoWalk']
        self.atta=self.sp['esqueletoattack']
        self.Dead=self.sp['esqueletoDead']

    def dead(self):
        if self.s==0:
            
            return self.sp['esqueletoDead']
        if self.s==1:
        
            return self.sp2['esqueletoDeadL']

    def attack(self):
        if self.s==0:
            return self.sp['esqueletoattack']
        if self.s==1:
            return self.sp2['esqueletoattackL']

    def movE(self):

        if self.newposx <= 600:
            self.direction = False  # Mover a la derecha
            
        elif self.newposx >= 900:
            self.direction = True  # Mover a la izquierda

        if self.direction:
            self.newposx -= 1  # Mover a la derecha
            if self.s==0:
                return self.sp['esqueletoWalk']
            if self.s==1:
                return self.sp2['esqueletoWalkL']
            if self.s==3:
                return self.bos['bossWalk']
        else:
            self.newposx += 1  # Mover a la izquierda
            if self.s==0:
                return self.sp['esqueletoWalk']
            if self.s==1:
                return self.sp2['esqueletoWalkL']
            if self.s==3:
                return self.bos['bossWalk']


    def pintarE(self, s, background):
        if self.vida==1:
            if self.walking:
                if self.acc:
                    self.move.animation_2(s, self.newposx,self.newposy,self.direction,background)
                    self.acc=False
                else:
                    self.move.animation(s, self.newposx,self.newposy,self.direction)
            else:
                if self.acc:
                    self.atta.animation_2(s, self.newposx,self.newposy,self.direction,background)
                    self.acc=False
                else:
                    self.atta.animation(s, self.newposx,self.newposy,self.direction)
        else:
            self.Dead.animation(s, self.newposx,self.newposy,self.direction)
            


class Boss:
    def __init__(self):
        self.sp={
            'bossInicio':SpriteAnimation('sprite\\boss\Karasu_tengu\inicio\Idle',13,200,200,15),
            'bossWalk':SpriteAnimation('sprite\\boss\\Karasu_tengu\\walk\\Walk',8,200,200,20),
            'bossDead':SpriteAnimation('sprite\\boss\Karasu_tengu\Dead\Dead',6,200,200,24),
            'bossRun':SpriteAnimation('sprite\\boss\Karasu_tengu\Run\Run',8,200,200,20),
            'bossAttack1':SpriteAnimation('sprite\\boss\\Karasu_tengu\\ataque1\\Attack',6,200,200,15),
            'bossAttack2':SpriteAnimation('sprite\\boss\\Karasu_tengu\\ataque2\\Attack',4,200,200,15),
            'bossAttack3':SpriteAnimation('sprite\\boss\\Karasu_tengu\\ataque3\\Attack',3,200,200,15)
        }

        self.corazonImg=pygame.image.load('sprite\\Life\\corazon.png').convert_alpha()
        self.corazonImg2=pygame.transform.scale(self.corazonImg,(60,60))
        
        self.ini=True
        self.vida=11
        self.newposx=600
        self.newposy=400
        self.direction=False

        self.isjump=False
        self.angulo=0.0
        self.jump_sprite = [pygame.image.load(f"sprite\\boss\\Karasu_tengu\\jump\\Jump{i}.png").convert_alpha() for i in range(15)]
        self.jump_sprite_index = 0

        self.Move=self.sp['bossWalk']


    def inicio(self):
        return self.sp['bossInicio']
    
    def Run(self):
        return self.sp['bossRun']
    
    def Dead(self):
        return self.sp['bossDead']

    def saltar(self,screen):
        # Incrementar el ángulo
        self.angulo += 0.1

        # Usando una función seno en el ángulo. Esto crea un movimiento de salto que se parece a un arco.
        self.newposy = 413 - math.sin(self.angulo) * 200
        self.newposy-=0.8888833905372
        # Calcula la fase actual del salto dividiendo el ángulo actual por pi y multiplicándolo por el número de fases de salto
        fase = int((self.angulo / math.pi) * 14)
        # Parte de selección y escalado y pintado del sprite
        img = self.jump_sprite[fase]
        img1 = pygame.transform.scale(img, (200, 200))
        img2 = pygame.transform.flip(img1, self.direction, False)
        screen.blit(img2, (self.newposx, self.newposy))

        # Restablecer las variables angulo e isjump cuando se termina el salto
        if self.angulo > math.pi:
            fase=0
            self.angulo = 0.0
            self.isjump = False


    def atacar(self,atq):
        if atq==1:
            return self.sp['bossAttack1']
        if atq==2:
            return self.sp['bossAttack2']
        if atq==3:
            return self.sp['bossAttack3']

    def corazon(self,screen):
        for i in range(self.vida):
            screen.blit(self.corazonImg2, (i*2*self.corazonImg2.get_width(), 610))

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
        

    def pintar(self,s,background):
        self.Move.animation(s, self.newposx,self.newposy,self.direction)
