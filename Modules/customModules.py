# The main reason to create your modules is organisation. If you have a lot of code it can be hard to find the part you want to change or fix
# By creating modules we can split our code into different files and import them when we need them  

import myModules
from myModules import sum_calculator
print(myModules.test_var)
myModules.test_function(123)

test = myModules.Test()
test.do_something()

result = sum_calculator(1, 2, 3, 4, 5)
print(f"The sum is: {result}")

print(__name__)