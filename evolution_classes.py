class Creature:
    def __init__(self):
        self.death_rate = 0


class World:
    def __init__(self):
        self.birth_rate = 1
        self.creatures = []

    def spontaneous_birth(self):
        self.creatures.append(Creature())

    def evolve(self):
        self.spontaneous_birth()
