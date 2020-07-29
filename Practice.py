import os
import random
import pygame

SCREENRECT = pygame.Rect(0, 0, 1500, 900)
WHITE = (255, 255, 255)
FPS = 30
MAX_COUNTER = 200
main_dir = os.path.split(os.path.abspath(__file__))[0]
RED = pygame.Color(255, 0, 0, 30)
PURPLE = pygame.Color(255, 0, 255, 30)
ORANGE = pygame.Color(255, 165, 0, 50)


class Creature(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = load_image('sova.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREENRECT.width-self.rect.width)
        self.rect.y = random.randint(0, SCREENRECT.height-self.rect.height)
        self.ate = 0
        self.speed = 5
        self.vision_radius = 200

    def move(self, goal, danger=None):
        if self.ate < 2:
            min_dist = 10000
            nearest_food = None
            nearest_danger = None
            if danger is not None:
                for predator in danger:
                    dist_x = self.rect.x - predator.rect.x
                    dist_y = self.rect.y - predator.rect.y
                    dist = (dist_x**2 + dist_y**2)**0.5
                    if dist < min_dist and dist <= self.vision_radius:
                        min_dist = dist
                        nearest_danger = predator
                if nearest_danger is not None:
                    dist_x = nearest_danger.rect.x - self.rect.x
                    dist_y = nearest_danger.rect.y - self.rect.y
                    dist = (dist_x**2 + dist_y**2)**0.5
                    if dist:
                        dx = dist_x * self.speed / dist
                        dy = dist_y * self.speed / dist
                        if 0 <= self.rect.x + int(dx) <= SCREENRECT.width - self.rect.width and \
                           0 <= self.rect.y + int(dy) <= SCREENRECT.height - self.rect.height:
                            self.rect.x -= int(dx)
                            self.rect.y -= int(dy)
                else:
                    self.move(goal)
            else:
                for meal in goal:
                    dist_x = self.rect.x - meal.rect.x
                    dist_y = self.rect.y - meal.rect.y
                    dist = (dist_x**2 + dist_y**2)**0.5
                    if dist < min_dist and dist <= self.vision_radius:
                        min_dist = dist
                        nearest_food = meal
            if nearest_food is None and nearest_danger is None:
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
            elif nearest_food is not None:
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
        self.vision_radius = 90


class Nusha(Creature):
    def __init__(self):
        super().__init__()
        self.image = load_image('nusha.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREENRECT.width-self.rect.width)
        self.rect.y = random.randint(0, SCREENRECT.height-self.rect.height)
        self.speed = 10
        self.vision_radius = 60


class Kopatich(Creature):
    def __init__(self):
        super().__init__()
        self.image = load_image('kopatich.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREENRECT.width-self.rect.width)
        self.rect.y = random.randint(0, SCREENRECT.height-self.rect.height)
        self.speed = 12
        self.vision_radius = 50


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
surface = pygame.Surface(SCREENRECT.size, pygame.SRCALPHA, 32)
surface_1 = pygame.Surface(SCREENRECT.size, pygame.SRCALPHA, 32)
surface_2 = pygame.Surface(SCREENRECT.size, pygame.SRCALPHA, 32)
surfaces = [surface, surface_1, surface_2]
pygame.display.flip()
nusha_group = pygame.sprite.Group()
sova_group = pygame.sprite.Group()
kopatich_group = pygame.sprite.Group()
herbivorous_group = pygame.sprite.Group()
for _ in range(10):
    nusha = Nusha()
    nusha_group.add(nusha)
    herbivorous_group.add(nusha)
for _ in range(10):
    sova = Sova()
    sova_group.add(Sova())
    herbivorous_group.add(sova)
for _ in range(5):
    kopatich_group.add(Kopatich())
food_group = pygame.sprite.Group()
for _ in range(100):
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
                            if type(animal) == Nusha:
                                animal.move(food_group, kopatich_group)
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
                        if type(animal) == Sova:
                            sova = Sova()
                            sova_group.add(sova)
                            herbivorous_group.add(sova)
                            print('родилась новая сова')
                        elif type(animal) == Nusha:
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
                for _ in range(100):
                    food_group.add(Pizza())

            screen.fill(WHITE)
            for animal in herbivorous_group:
                if type(animal) == Nusha:
                    surface = pygame.Surface(SCREENRECT.size, pygame.SRCALPHA, 32)
                    pygame.draw.circle(surface, RED, (animal.rect.x, animal.rect.y), animal.vision_radius)
                    screen.blit(surface, (0, 0))
                else:
                    surface = pygame.Surface(SCREENRECT.size, pygame.SRCALPHA, 32)
                    pygame.draw.circle(surface, PURPLE, (animal.rect.x, animal.rect.y), animal.vision_radius)
                    screen.blit(surface, (0, 0))
            for kopatich in kopatich_group:
                surface = pygame.Surface(SCREENRECT.size, pygame.SRCALPHA, 32)
                pygame.draw.circle(surface, ORANGE, (kopatich.rect.x, kopatich.rect.y), kopatich.vision_radius)
                screen.blit(surface, (0, 0))
            kopatich_group.draw(screen)
            herbivorous_group.draw(screen)
            food_group.draw(screen)
            pygame.display.flip()
            counter = (counter + 1) % MAX_COUNTER
            print(counter)
            print(len(herbivorous_group), len(kopatich_group), len(nusha_group), len(sova_group), len(food_group))
            print()



pygame.quit()
