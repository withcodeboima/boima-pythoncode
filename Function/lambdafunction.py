# Lambdas are single line functions
# The synax is lambda para:expression
# lambda x: x+2
# The result is automatically returned

# a = lambda x: x + 1
# print(a(10))

# a = lambda x: x + 1
# simple_calc = lambda a,b: a + b
# print(simple_calc(10,20))
# some functions want other functions as arguments
# sort([1,5,2,3,4] function)
# graphical user interfaces 

# exercise 
#create a lambda that accept 1 integer argument
# if the interger is 5 return hello
# otherwise return goodbye

x = lambda x:'hello' if x > 5 else 'goodbye'
print(x(10))



