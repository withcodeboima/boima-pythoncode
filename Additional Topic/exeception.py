# Error handing in python
# try and except are used to handle errors in python. The code inside the try block is executed. If there is an error, the code inside the except block is executed. If there is no error, the code inside the except block is not executed.

#print(1/0)
# try:
#     print(1/0)
# except:
#     print("Something else went wrong")

# try:
#     print('try')
    # print(a)
    # print(1/0)
# except ZeroDivisionError:
#     print("You can't divide by zero")
# except NameError:
#     print("Variable is not defined")
# else:
#     print("No error occurred")

# finally:
#     print("This will always be executed")

# raising exceptions
# var_must_be_string = 'test string'
# if isinstance(var_must_be_string, str):
#     print(var_must_be_string)
# else:
#     raise TypeError('var_must_be_string must be a string')

#assert is used to check if a condition is true. If the condition is false, an AssertionError is raised. 
# a = 6
# assert a ==  5

my_list = [1,2,3,4,5]
try:
    print(my_list[4])
#    my_list[99]
except IndexError as e:
    print("Index out of range")
else:
    print('That index exists in the list')
finally:
    print('This will always run')