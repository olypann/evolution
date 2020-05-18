import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from evolution_classes import World
sns.set(style='darkgrid')


def show_analytics(data):
    df = pd.DataFrame(data)
    df = df.set_index('day')
    print(df)
    sns.lineplot(data=df, marker='o')
    plt.show()


def main():
    data = []
    days = 7
    world = World()
    for day in range(1, days+1):
        world.evolve()
        data.append({'day': day, 'population': len(world.creatures)})
    show_analytics(data)

if __name__ == '__main__':
    main()
