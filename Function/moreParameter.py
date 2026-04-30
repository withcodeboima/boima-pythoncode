#what if you want know the number of arguments?
# You can work with any number of arguments or 
# unlimited number of arguments is unpacking

def print_all(first,*arguments,extra):
    print(first)
    print(arguments)
    print(extra)
    # print all arguments
    for argument in arguments:
        print(argument)
# print_all(1,2,3,4,5, 'hello', 1,2,231.321,3,123,extra=12)
# print_all([1, 2, 3,4,5, 'hello', 'world', 'python', 'java', 'c++'])

#keyword unpacking
def print_more(**arguments):
    print(arguments)
#print_more(arg1='1', arg2='test', arg3=[1,2,3])

def print_even_more(*args, **kwargs):
    print(args)
    print(kwargs)
#print_even_more(1,2,3,54,21,3412,31,'hello', True,test = 1, test2 = 5)

# Exercises
#create a calculator for function that prints the sum 
# of an unlimited numbers

def calculator(*args):
    #print(args)
    result = sum(args)
    print(result)
calculator(1,2,3,4,5,6)





