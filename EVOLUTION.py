import pygame
from pygame.locals import *
import pandas as pd
import matplotlib.pyplot as plt
from evolution_classes import World
import seaborn as sns
sns.set(style='darkgrid')

SCREENRECT = Rect(0, 0, 640, 480)
DAYS = 10


def show_analytics(data):
    df = pd.DataFrame(data)
    df = df.set_index('day')
    print(df)
    sns.lineplot(data=df, marker='o')
    plt.show()


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREENRECT.size)
    data = []
    world = World()
    running = True
    print('day | population | average age')
    print('-------------------------------')
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        world.evolve()
        if world.days == DAYS:
            running = False
        total_age = 0
        for creature in world.creatures:
            total_age += world.days - creature.birthday
        mean_age = total_age / len(world.creatures)
        print('{:^3} | {:^10} | {:^11}'.format(world.days, len(world.creatures), mean_age))
        data.append({'day': world.days, 'population': len(world.creatures), 'average age': mean_age})
    show_analytics(data)
    pygame.quit()

if __name__ == '__main__':
    main()
