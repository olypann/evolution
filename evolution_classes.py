import os

import pygame
import random
from config import *


main_dir = os.path.split(os.path.abspath(__file__))[0]


class Creature(pygame.sprite.Sprite):
    def __init__(self, day):
        super().__init__()
        self.replication_rate = 0
        self.death_rate = 0
        self.birthday = day

    def is_dead(self):
        self.death_rate *= 1.1
        if random.random() < self.death_rate:
            return True
        return False

    def replicate(self, day):
        if random.random() < self.replication_rate:
            return Creature(day=day)
        return None


class World:
    def __init__(self):
        self.birth_rate = 1
        self.creatures = []
        self.days = 0
        self.creatures_group = pygame.sprite.Group()
        self.init_birth()

    def init_birth(self):
        for _ in range(NUSHA_I):
            new_creature = Nusha(day=self.days)
            self.creatures.append(new_creature)
            self.creatures_group.add(new_creature)
        for _ in range(KOPATICH_I):
            new_creature = Kopatich(day=self.days)
            self.creatures.append(new_creature)
            self.creatures_group.add(new_creature)

    def spontaneous_birth(self):
        new_creature = Nusha(day=self.days)
        self.creatures.append(new_creature)
        self.creatures_group.add(new_creature)
        new_creature = Kopatich(day=self.days)
        self.creatures.append(new_creature)
        self.creatures_group.add(new_creature)

    def death(self):
        for creature in self.creatures:
            if creature.is_dead():
                self.creatures.remove(creature)
                creature.kill()

    def replication(self):
        for creature in self.creatures:
            new_creature = creature.replicate(day=self.days)
            if new_creature is not None:
                self.creatures.append(new_creature)
                self.creatures_group.add(new_creature)

    def evolve(self):
        self.days += 1
        self.replication()
        # self.spontaneous_birth()
        self.death()


class Nusha(Creature):
    def __init__(self, day):
        super().__init__(day)
        self.death_rate = NUSHA_D
        self.replication_rate = NUSHA_R
        self.image = load_image('nusha.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREENRECT.width-self.rect.width)
        self.rect.y = random.randint(0, SCREENRECT.height-self.rect.height)

    def replicate(self, day):
        if random.random() < self.replication_rate:
            return Nusha(day=day)
        return None


class Kopatich(Creature):
    def __init__(self, day):
        super().__init__(day)
        self.death_rate = KOPATICH_D
        self.replication_rate = KOPATICH_R
        self.image = load_image('kopatich.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREENRECT.width-self.rect.width)
        self.rect.y = random.randint(0, SCREENRECT.height-self.rect.height)

    def replicate(self, day):
        if random.random() < self.replication_rate:
            return Kopatich(day=day)
        return None


def load_image(file):
    file = os.path.join(main_dir, 'data', file)
    image = pygame.image.load(file)
    image = image.convert_alpha()
    return image





