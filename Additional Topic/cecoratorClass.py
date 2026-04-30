from datetime import datetime

# Decorator Class
# A decorator is a function that takes another function as an argument and returns a new function that is a modified version of the original function. A decorator can be implemented as a class by defining the __call__ method. The __call__ method is called when the instance of the class is called as a function.

class Generic:
    def __init__(self):
        self.x = 10
    @property
    def x(self):
        print(datetime.now())
        return self._x
    
    @x.setter
    def x(self, value):
        print('set x')
        self._x = value
    
    @x.deleter
    def x(self):
        print('delete x')
        del self._x

    # x = property(getter,setter,deleter)
generic = Generic()
generic.x = 4
print(generic.x)
del generic.x