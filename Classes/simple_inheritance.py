# Inheritance means that 1 class gets attributes and methods from another class or classes.
# A class can inhert from an unlimited number of other classes.
# A class can be also be inherited from by an unlimited number of classes.

class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy
    # method
    def attack(self, amount):
        print('The monster has attacked')
        print(f'{amount} damage dealt')
        self.energy -= 20
      
    def move(self, speed):
        print('The monster has moved')
        print(f'It has a speed of {speed}')

class Shark(Monster):
    def __init__(self, speed, health, energy):
        # Monster.__init__(self,health,energy)
        super().__init__(health,energy)
        super().move(10)
        self.speed = speed
    def bite(self):
        print('The shark has bitten you')

    def move(self):
        print('The shark has moved')
        print(f'It has a speed of {self.speed}')

# shark = Shark(120)
# print(shark.energy)
# shark.bite()
# shark.attack(20)
shark = Shark(speed = 120, health = 100, energy = 80)
# shark.move()
print(shark.speed)
print(shark.health)
print(shark.energy)


    
