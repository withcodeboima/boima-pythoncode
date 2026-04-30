test_var = "Welcome to modules in python!"

def test_function(content):
    print(f'This is an imported function with the parameter: {content}')

class Test:
    def __init__(self):
        self.name = "My Application"
        self.value = 12

    def do_something(self):
        print("This is a method in the class")

def sum_calculator(*nums):
    return sum(nums)