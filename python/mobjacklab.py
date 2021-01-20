import random
import string

class Jackalopes:
    def __init__(self):
        self.age = 0
        self.dead = 10
        self.gestation = 2
        self.name = name

jack_pop = [Jackalopes(), Jackalopes()]

year = 0
while len(jack_pop) < 1000:

    year += 1

    for jack in jack_pop:

        jack.age += 1

        if 4 <= jack.age <= 8:
            jack_pop.append(Jackalopes())
        elif jack.age == jack.dead:
            jack_pop.remove(jack)

print(year)
print(len(jack_pop))