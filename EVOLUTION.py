from random import choice


class Creature:
    def __init__(self):
        self.death_rate = 0


class World:
    def __init__(self):
        self.birth_rate = 1
        self.creatures = []

    def spontaneous_birth(self):
        self.creatures.append(Creature())


def main():
    days = 7
    world = World()
    print('day | population')
    print('----------------')
    for day in range(1, days+1):
        world.spontaneous_birth()
        print('{:^3} | {:^10} '.format(day, len(world.creatures)))




if __name__ == '__main__':
    main()
