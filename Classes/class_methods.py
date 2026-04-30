# Everything in python is an object
# Including the inbuilt strings, integers etc
# Even functions are objects
# A function and a method both execute a block of code
# The difference is that method belongs to an object

# test = 'a'

# print(dir(test))

# def test():
#     pass
# a = test
# print(dir(a))

def add(a, b):
    return a + b
class Test:
    def __init__(self,add_function):
        self.add_function = add_function
test = Test(add_function = add)
print(test.add_function(1,2))


class Monster:
    def __init__(self, func):
        self.func = func
class Attacks:
    def bite(self):
        print('bite')

    def strike(self):
        print('strike')

    def slash(self):
        print('slash')

    def kick(self):
        print('kick')

monster = Monster(func = Attacks().slash)
monster.func() 

      