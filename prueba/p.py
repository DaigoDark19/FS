import pygame
from pygame.sprite import Group
FPS=60

class player(pygame.sprite.Sprite):
    gravity=1
    def __init__(self,x,y ):
        self.rect=pygame.Rect(x,y,200,200)
        self.x=x
        self.y=y
        self.velx=0
        self.vely=0
        self.mask=None
        self.animationnCount=0
        self.countA=0
        self.direction='left'

    def mov(self,dx,dy):
        self.rect.x+=dx
        self.rect.y+=dy
    
    def movL(self,vel):
        self.velx-=vel
        if self.direction!='left':
            self.direction='left'
            self.animationnCount=0

    def movD(self,vel):
        self.velx+=vel
        if self.direction!='right':
            self.direction='right'
            self.animationnCount=0

    #todas las cosas que necesitamos constante del personaje
    def loop(self,fps):
        self.vely+=min(1,self.countA/FPS*self.gravity)
        self.mov(self.velx,self.vely)
        self.countA+=1

    def draw(self,w):
        pygame.draw.rect(w,(255,0,0),self.rect)


