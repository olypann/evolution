import pygame
import time
import pandas as pd
import matplotlib.pyplot as plt
from evolution_classes import World
import seaborn as sns
from config import *
sns.set(style='darkgrid')


def show_analytics(data):
    df = pd.DataFrame(data)
    df = df.set_index('day')
    print(df)
    sns.lineplot(data=df)
    plt.show()


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREENRECT.size)
    screen.fill(WHITE)
    data = []
    world = World()
    print('day | population | average age')
    print('-------------------------------')
    running = True
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
        if total_age == 0:
            mean_age = 0
        else:
            mean_age = total_age / len(world.creatures)
        print('{:^3} | {:^10} | {:^11}'.format(world.days, len(world.creatures), mean_age))
        data.append({
            'day': world.days,
            'population': len(world.creatures),
            'average age': mean_age,
            'nusha population': len([c for c in world.creatures if type(c).__name__ == 'Nusha']),
            'kopatich population': len([c for c in world.creatures if type(c).__name__ == 'Kopatich']),
        })
        screen.fill(WHITE)
        world.creatures_group.draw(screen)
        pygame.display.flip()
        time.sleep(0.03)
    show_analytics(data)
    pygame.quit()


if __name__ == '__main__':
    main()
