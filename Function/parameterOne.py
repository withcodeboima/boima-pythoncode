def test_function(arg1, arg2, arg3, arg4):
    print(arg1)
    print(arg2)
    print(arg3)
    print(arg4)


# test_function(1, "Hello", True, ['1', 2, 'test'])
test_function(1, arg2="Hello", arg3=True, arg4= ['1', 2, 'test'])

def greeter(person = 'person', greet ='Hello', weekday = 'Monday'):
    print(f'{person}, {greet}')
    print(f'It is {weekday}')
greeter() 
    