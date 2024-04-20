from .character import Character


class Enemy(Character):
    def __init__(self):
        self.acc = False
        self.walking = True
        self.move = self.sp['esqueletoWalk']
        self.atta = self.sp['esqueletoattack']
        self.Dead = self.sp['esqueletoDead']
        print('merequetengue')

    @classmethod
    def create_enemy(cls):
        print('holaaa si')
        Enemy()

    def dead(self):
        if self.s == 0:
            return self.sp['esqueletoDead']
        if self.s == 1:
            return self.sp2['esqueletoDeadL']

    def attack(self):
        if self.s == 0:
            return self.sp['esqueletoattack']
        if self.s == 1:
            return self.sp2['esqueletoattackL']

    def movE(self):

        if self.newposx <= 600:
            self.direction = False  # Mover a la derecha

        elif self.newposx >= 900:
            self.direction = True  # Mover a la izquierda

        if self.direction:
            self.newposx -= 1  # Mover a la derecha
            if self.s == 0:
                return self.sp['esqueletoWalk']
            if self.s == 1:
                return self.sp2['esqueletoWalkL']
            if self.s == 3:
                return self.bos['bossWalk']
        else:
            self.newposx += 1  # Mover a la izquierda
            if self.s == 0:
                return self.sp['esqueletoWalk']
            if self.s == 1:
                return self.sp2['esqueletoWalkL']
            if self.s == 3:
                return self.bos['bossWalk']

    def pintarE(self, s: int, background: str):
        if self.vida == 1:
            if self.walking:
                if self.acc:
                    self.move.animation_2(
                        s, self.newposx, self.newposy,
                        self.direction, background)
                    self.acc = False
                else:
                    self.move.animation(
                        s, self.newposx,
                        self.newposy, self.direction)
            else:
                if self.acc:
                    self.atta.animation_2(
                        s, self.newposx, self.newposy,
                        self.direction, background)
                    self.acc = False
                else:
                    self.atta.animation(
                        s, self.newposx,
                        self.newposy, self.direction)
        else:
            self.Dead.animation(s, self.newposx, self.newposy, self.direction)

Enemy.create_enemy()