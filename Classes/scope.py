# Since every method has a reference to the class
# It is easy get and change class attributes
# Beceause of that methods rely much less on 
# parameters, global and return although you can use it
# Object can even be influence from the outside 
# and from a local scope of a function

# Scope Problem
# def update_health(amount):
#     global health
#     health += amount
# health = 10
# print(health)
# update_health(20)
# print(health)


def update_health(amount):
    monster.health += amount
class Monster:
    def __init__(self,health,energy):
        self.health = health
        self.energy = energy

    def update_energy(self, amount):
        self.energy += amount

    def set_energy(self, energy):
        new_energy = energy * 2
        return new_energy

monster = Monster(health = 100, energy = 50)
# monster.health += 20
# print(monster.health)
# update_health(20)
# print(monster.health)
# monster.update_energy(20)
print(monster.energy)

def get_damage(self, amount):
    self.health -= amount

class Hero:
    def __init__(self,damage,monster):
        self.damage = damage
        self.monster = monster

    def attack(self):
        self.monster.get_damage(self.damage)