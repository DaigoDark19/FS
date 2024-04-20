import pygame


class Character:
    def __init__(self, sp: dict, vida: int, x: int, y: int):
        self.sp = sp

        self.newposx = x
        self.newposy = y
        self.vida = vida

        self.direcction = False

        self.corazonImg = pygame.image.load('sprite\\Life\\corazon.png')
        self.corazonImg.convert_alpha()
        self.corazonImg2 = pygame.transform.scale(self.corazonImg, (50, 50))

    def create_skeletoA(self):
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

