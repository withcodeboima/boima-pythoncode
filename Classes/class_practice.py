class Monster:
    #attribute
    health = 90
    energy = 40

    #method
    def attack(moster,amount):
        print('The monster has attacked')
        print(f'{amount} damage dealt')
        moster.energy -= 20
        print(moster.energy)

    def move(self,speed):
        print('The monster has moved')
        print(f'It has a spreed of {speed}')

monster = Monster()

# print(moster.health)
# print(moster.energy)
# moster.attack()
# moster.attack(40)
monster.move(10)

