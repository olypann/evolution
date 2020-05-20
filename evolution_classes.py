class Creature:
    def __init__(self, day):
        self.death_rate = 0
        self.birthday = day


class World:
    def __init__(self):
        self.birth_rate = 1
        self.creatures = []
        self.days = 0

    def spontaneous_birth(self):
        self.creatures.append(Creature(day=self.days))

    def evolve(self):
        self.days += 1
        self.spontaneous_birth()

