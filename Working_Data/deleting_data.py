# The way you can delete thing in python is del thing
# This would remove variables but you rarely use it that way
# In most cases you only delete values inside of list

# a = 1
# del a
# print(a)

# remove item from list
# a = [1,2,3]
# del remove item by item
# del a[1]
# print(a)

# remove an item by value
# a.remove(3)
# print(a)

student_name = ['John', 'Mark', 'Jane', 'Boima']
# del student_name[1]
# print(student_name)

# student_name.remove('John')
# print(student_name)

# pop
# student_name.pop(-2)
# print(student_name)
# print(student_name.pop(-2))

# clear the entire list
student_name.clear()
print(student_name)