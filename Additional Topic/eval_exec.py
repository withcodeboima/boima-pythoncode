# Eval Exec are special functions that translte string into python code and execute it. Eval is used to evaluate a string as a python expression and return the result. Exec is used to execute a string as a python statement.

# print(eval('10 + 5'))
# print(eval('"test".upper()'))
# exec('if True: print("This is true")')

my_string = 'test'
# print(my_string.upper())
# print(my_string.title())
# print(my_string.lower())
# print(my_string.casefold())

for operation in ['upper', 'title', 'lower', 'casefold']:
    print(eval(f'my_string.{operation}()'))
