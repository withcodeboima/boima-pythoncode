# Function and Scope
# Varibles create inside of a function are 
# only avialable inside of that function
# This is called local scope 
# Creating variables outside of function is the global scope

a = 10

# def test_func():
#     #a += 2 error
#     a = 2
#     print(a)
# test_func()

# def test_func_2():
#     a = 200
#     print(a)
# test_func_2()

# Functions are supposed to separate from the rest of the code
# Once the become more complex it is really easy
# to run out of variable names
# For example with the car both the battery and the tank
# might have a capacity variable
# Local scope inside of a function help to keep things organised

# Rules of Scope
# Every function has its own local scope 
# every local scrope is separate
# Global variables can be accessed in the local scope 
# but they cannot be changed or created

# def test_func_3(a):
#     # global a
#     a += 2
#     # print(a)
#     return a
# print(test_func_3(a))

# excrcise
# create 2 globe variables called multiplier and has calclated
# miltiplier should have any integer and has calculated should be set to the boolean false

multiplier = 5
has_calculated = False

def multiply_calculator(number):
    global has_calculated
    number * multiplier
    has_calculated = True
    result = number * multiplier
    return result
print(multiply_calculator(10))
print(has_calculated)








