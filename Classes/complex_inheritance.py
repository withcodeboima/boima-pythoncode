# Complex Inheritance
class Monster:
    def __init__(self, health, energy,**kwargs):
        print(kwargs)
        self.health = health
        self.energy = energy
        super().__init__(**kwargs)
    # method
    def attack(self, amount):
        print('The monster has attacked')
        print(f'{amount} damage dealt')
        self.energy -= 20
      
    def move(self, speed):
        print('The monster has moved')
        print(f'It has a speed of {speed}')

class Fish:
    def __init__(self,speed,has_scales,**kwargs):
        self.speed = speed
        self.has_scales = has_scales
        super().__init__(**kwargs)
    def swin(self):
        print(f'The fish has swum at a speed of {self.speed}')
        

class Shark(Monster, Fish):
    def __init__(self, bite_strength,health,energy,speed,has_scales):
        self.bite_strength = bite_strength
        super().__init__(health = health, energy = energy, speed = speed, has_scales = has_scales)
# mro = method resolution order
# print(Shark.mro())
shark = Shark(
    bite_strength=50,
    health = 200,
    energy = 55,
    speed = 120,
    has_scales = False)
# shark.attack(30)
# print(shark.health)
print(shark.speed)

        