# __Dunder__method is a special method that is used to create special functions
# double underscore methods
# A dunder method is a method that is not called by the user
# Instead it is called by python when something happens

# __init__ is a special method that is used to create special functions
#  __len__ is called when the object is passed into len(object)
# __abs__ is called when the object is passed into abs(object)


class Monster:
    #attribute
    health = 90
    energy = 40

    def __init__(seft,health,energy):


        seft.health = health


        seft.energy = energy
        # print('A new monster has been created')
    def __len__(self):
        return self.health
    
    def __abs__(self):
        return self.energy
    
    def __call__(self):
        print(f'The monster has {self.health} health and {self.energy} energy')

    def __add__(self,other):
        return self.health + other
    
    def __str__(self):
        return 'A Monster'
        
        

    #method
    def attack(moster,amount):
        print('The monster has attacked')
        print(f'{amount} damage dealt')
        moster.energy -= 20
        print(moster.energy)

    def move(self,speed):
        print('The monster has moved')
        print(f'It has a spreed of {speed}')




monster1 = Monster(10,20)
# print(len([1,2,3,4,5]))
# print(len(monster1))
# print(abs(monster1))
# monster2 = Monster(health = 50,energy = 100)

# print(monster1.health)
# print(monster2.health)
# print(dir(monster1))
# print(monster1.__dict__)
# print(vars(monster1))
monster1()
print(monster1 + 10)
print(monster1)

