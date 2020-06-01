import os

from pygame.locals import *
import pygame
import random
import PIL


SCREENRECT = Rect(0, 0, 640, 480)


main_dir = os.path.split(os.path.abspath(__file__))[0]


class Creature(pygame.sprite.Sprite):
    def __init__(self, day):
        super().__init__()
        self.death_rate = 0
        self.birthday = day


class World:
    def __init__(self):
        self.birth_rate = 1
        self.creatures = []
        self.days = 0
        self.creatures_group = pygame.sprite.Group()

    def spontaneous_birth(self):
        new_creature = Nusha(day=self.days)
        self.creatures.append(new_creature)
        self.creatures_group.add(new_creature)
        new_creature = Kopatich(day=self.days)
        self.creatures.append(new_creature)
        self.creatures_group.add(new_creature)

    def evolve(self):
        self.days += 1
        self.spontaneous_birth()


class Nusha(Creature):
    def __init__(self, day):
        super().__init__(day)
        self.image = load_image('nusha.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREENRECT.width-self.rect.width)
        self.rect.y = random.randint(0, SCREENRECT.height-self.rect.height)


class Kopatich(Creature):
    def __init__(self, day):
        super().__init__(day)
        self.image = load_image('kopatich.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREENRECT.width-self.rect.width)
        self.rect.y = random.randint(0, SCREENRECT.height-self.rect.height)


def load_image(file):
    file = os.path.join(main_dir, 'data', file)
    image = pygame.image.load(file)
    image = image.convert_alpha()
    return image





