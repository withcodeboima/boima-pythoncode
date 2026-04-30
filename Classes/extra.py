class Monster:
    """A class representing a monster with health and energy."""
    def __init__(self, health, energy,):
      
        self.health = health
        self.energy = energy

        self._id = 5
        
    # method
    def attack(self, amount):
        print('The monster has attacked')
        print(f'{amount} damage dealt')
        self.energy -= 20
      
    def move(self, speed):
        print('The monster has moved')
        print(f'It has a speed of {speed}')

monster = Monster(20,10)
# print(monster._id)


# hasattr and setattr
# hasattr(monster, 'health')
# if hasattr(monster, 'health'):
#     print(f'The monster has {monster.health} health')

setattr(monster, 'weapon', 'sword')
# monster.weapon = 'Sword'
# print(monster.weapon)
# new_attributes = (['weapon', 'Axe'], ['armor', 'Shield'], ['potion', 'mana'])
# for attr, value in new_attributes:
#     setattr(monster, attr, value)
# print(vars(monster))
# doc string
# print(Monster.__doc__)
help(str)