from sprite import SpriteAnimation


class Enemy:
    def __init__(self, s: int):
        self.sp = {
            'esqueletoWalk': SpriteAnimation(
                'sprite\\esqueletos\\Skeleton_Warrior\\walk\\Walk',
                7, 200, 200, 24
                ),
            'esqueletoattack': SpriteAnimation(
                'sprite\\esqueletos\\Skeleton_Warrior\\attack2\\Attack',
                4, 200, 200, 10
                ),
            'esqueletoDead': SpriteAnimation(
                'sprite\\esqueletos\\Skeleton_Warrior\\Dead\\Dead',
                4, 200, 200, 20)

        }

        self.sp2 = {
            'esqueletoWalkL': SpriteAnimation(
                'sprite\\esqueletos\\Skeleton_Spearman\\walk\\Walk',
                7, 200, 200, 24
                ),
            'esqueletoattackL': SpriteAnimation(
                'sprite\\esqueletos\\Skeleton_Spearman\\attack\\Attack',
                4, 200, 200, 10
                ),
            'esqueletoDeadL': SpriteAnimation(
                'sprite\\esqueletos\\Skeleton_Spearman\\dead\\Dead',
                5, 200, 200, 20
                )
        }

        self.s = s
        self.newposx = 600
        self.newposy = 400
        self.direction = False
        self.acc = False
        self.walking = True
        self.vida = 1
        self.move = self.sp['esqueletoWalk']
        self.atta = self.sp['esqueletoattack']
        self.Dead = self.sp['esqueletoDead']

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

