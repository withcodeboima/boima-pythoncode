import time
# Decortator are function that decorte other functions. They are used to modify the behavior of a function without changing its code. A decorator is a function that takes another function as an argument and returns a new function that is a modified version of the original function.
# For example e can create a decorator for a fuction that makes the function execute twice when called.
# You want to test your code without changing it
# You working in a team and to to aviod unnecessary code changes

# def func():
#     print('This is a function')
# def wrapper(func):
#     print("Helo from wrapper")
#     func()
#     print("Goodbye from wrapper")

# def function_generator():
#     def new_function():
#         print("This is a new function")
#     return new_function
# # wrapper(func)
# new_func = function_generator()
# new_func()

def decorator(func):
    def wrapper():
        print('Decorator is called')
        func()
        print('decorator ends')
    return wrapper
def duration_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        duration = time.time() - start_time
        print(f'Function took {duration} seconds to execute')
    return wrapper
def double_decorator(func):
    def wrapper():
        func()
        func()
    return wrapper

@double_decorator
@decorator
@duration_decorator
def func():
    print('This is a function')
    time.sleep(1)

# new_func = decorator(func)
# new_func()

func()
