


vowels = 'aeiou'
con = 'bcdfghjklmnpqrstvwxyz'
​
def get_name():
    name = random.choice(con) + random.choice(vowels) + random.choice(con) + random.choice(vowels)
    return name
​
class Jackalopes:
    def __init__(self, sex=random.choice(['male', 'female'])):
        self.age = 0
        self.dead = 10
        self.gestation = 2
        self.name = get_name()
        self.sex = sex
        self.pregnant = False
​
jack_pop = [Jackalopes('male'), Jackalopes('female')]
year = 0
while len(jack_pop) < 1000:
    year += 1
    for index, jack in enumerate(jack_pop):
        jack.age += 1
        if 4 <= jack.age <= 8:
            if jack.sex == 'female':
                if index + 1 < len(jack_pop):
                    if jack.sex != jack_pop[index + 1].sex:
                        
                jack_pop.append(Jackalopes())
            elif jack.age == jack.dead:
                jack_pop.remove(jack)
        
print(year)


loop to check if pregnant, add babies, then change to not pregnant
if 10 dead and remove jackaloupe