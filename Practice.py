import os
import random
import time
import pygame

SCREENRECT = pygame.Rect(0, 0, 640, 480)
WHITE = (255, 255, 255)
FPS = 50
main_dir = os.path.split(os.path.abspath(__file__))[0]


class Sova(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = load_image('sova.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREENRECT.width-self.rect.width)
        self.rect.y = random.randint(0, SCREENRECT.height-self.rect.height)

    def move(self):
        self.rect.x += 1


class Pizza(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = load_image('pizza.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREENRECT.width-self.rect.width)
        self.rect.y = random.randint(0, SCREENRECT.height-self.rect.height)


def load_image(file):
    file = os.path.join(main_dir, 'data', file)
    image = pygame.image.load(file)
    image = image.convert_alpha()
    return image


running = True
pygame.init()
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, FPS)
screen = pygame.display.set_mode(SCREENRECT.size)
screen.fill(WHITE)
pygame.display.flip()
sova = Sova()
sova_group = pygame.sprite.Group()
sova_group.add(sova)
pizza = Pizza()
food_group = pygame.sprite.Group()
food_group.add(pizza)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.USEREVENT:
            sova.move()

    screen.fill(WHITE)
    sova_group.draw(screen)
    food_group.draw(screen)
    pygame.display.flip()

pygame.quit()
