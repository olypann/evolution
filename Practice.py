import os
import random
import pygame

SCREENRECT = pygame.Rect(0, 0, 640, 480)
WHITE = (255, 255, 255)
FPS = 30
MAX_COUNTER = 200
main_dir = os.path.split(os.path.abspath(__file__))[0]


class Creature(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = load_image('sova.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREENRECT.width-self.rect.width)
        self.rect.y = random.randint(0, SCREENRECT.height-self.rect.height)
        self.ate = 0
        self.speed = 5
        self.radius_food = 200

    def move(self, goal):
        if self.ate < 2:
            min_dist = 10000
            nearest_food = None
            for food in goal:
                dist_x = self.rect.x - food.rect.x
                dist_y = self.rect.y - food.rect.y
                dist = (dist_x**2 + dist_y**2)**0.5
                if dist < min_dist and dist <= self.radius_food:
                    min_dist = dist
                    nearest_food = food
            if nearest_food is None:
                while True:
                    dist_x = random.randint(-20, 20)
                    dist_y = random.randint(-20, 20)
                    dist = (dist_x**2 + dist_y**2)**0.5
                    if dist:
                        dx = dist_x * self.speed / dist
                        dy = dist_y * self.speed / dist
                        if 0 <= self.rect.x + int(dx) <= SCREENRECT.width - self.rect.width and\
                           0 <= self.rect.y + int(dy) <= SCREENRECT.height - self.rect.height:
                            self.rect.x += int(dx)
                            self.rect.y += int(dy)
                            break

            else:
                dist_x = nearest_food.rect.x - self.rect.x
                dist_y = nearest_food.rect.y - self.rect.y
                dist = (dist_x**2 + dist_y**2)**0.5
                if dist:
                    dx = dist_x * self.speed / dist
                    dy = dist_y * self.speed / dist
                    self.rect.x += int(dx)
                    self.rect.y += int(dy)

    def eat(self):
        self.ate += 1


class Sova(Creature):
    def __init__(self):
        super().__init__()
        self.image = load_image('sova.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREENRECT.width-self.rect.width)
        self.rect.y = random.randint(0, SCREENRECT.height-self.rect.height)
        self.speed = 5
        self.radius_food = 200


class Nusha(Creature):
    def __init__(self):
        super().__init__()
        self.image = load_image('nusha.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREENRECT.width-self.rect.width)
        self.rect.y = random.randint(0, SCREENRECT.height-self.rect.height)
        self.speed = 10
        self.radius_food = 100


class Kopatich(Creature):
    def __init__(self):
        super().__init__()
        self.image = load_image('kopatich.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREENRECT.width-self.rect.width)
        self.rect.y = random.randint(0, SCREENRECT.height-self.rect.height)
        self.speed = 15
        self.radius_food = 50


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
nusha_group = pygame.sprite.Group()
sova_group = pygame.sprite.Group()
kopatich_group = pygame.sprite.Group()
herbivorous_group = pygame.sprite.Group()
for _ in range(5):
    nusha = Nusha()
    nusha_group.add(nusha)
    herbivorous_group.add(nusha)
for _ in range(3):
    sova = Sova()
    sova_group.add(Sova())
    herbivorous_group.add(sova)
for _ in range(3):
    kopatich_group.add(Kopatich())
food_group = pygame.sprite.Group()
for _ in range(10):
    food_group.add(Pizza())

counter = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.USEREVENT:
            if food_group or nusha_group:
                if food_group:
                    for animal in herbivorous_group:
                        if pygame.sprite.spritecollide(animal, food_group, dokill=True):
                            animal.eat()
                        else:
                            animal.move(food_group)
                if nusha_group:
                    for animal in kopatich_group:
                        tokill = pygame.sprite.spritecollide(animal, nusha_group, dokill=False)
                        if tokill:
                            for victim in tokill:
                                victim.kill()
                            animal.eat()
                        else:
                            animal.move(nusha_group)
            if counter == MAX_COUNTER - 1:
                for animal in herbivorous_group:
                    if animal.ate == 0:
                        animal.kill()
                    elif animal.ate == 2:
                        if type(animal).__name__ == 'Sova':
                            sova = Sova()
                            sova_group.add(sova)
                            herbivorous_group.add(sova)
                            print('родилась новая сова')
                        elif type(animal).__name__ == 'Nusha':
                            nusha = Nusha()
                            nusha_group.add(nusha)
                            herbivorous_group.add(nusha)
                    animal.ate = 0
                for animal in kopatich_group:
                    if animal.ate == 0:
                        animal.kill()
                    elif animal.ate == 2:
                        kopatich_group.add(Kopatich())
                    animal.ate = 0

                for food in food_group:
                    food.kill()
                for _ in range(10):
                    food_group.add(Pizza())

            screen.fill(WHITE)
            #sova_group.draw(screen)
            #nusha_group.draw(screen)
            kopatich_group.draw(screen)
            herbivorous_group.draw(screen)
            food_group.draw(screen)
            pygame.display.flip()
            counter = (counter + 1) % MAX_COUNTER
            print(counter)


pygame.quit()
