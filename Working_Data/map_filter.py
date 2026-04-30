# More function that take functions as arguments
# Besides sorted there is also map and filter at least for basic python
# Those have mostly been replaced by list comprehension though.


my_list = [1,2,3,4,5]

#map change values with a function inside of a iterable
# def power_function(num):
#     return num ** 2
# print(list(map(power_function, my_list)))
# print(list(map(lambda num: num ** 2, my_list)))

#  filter - filter out values from a condition
# def get_below_4(num):
#     if num < 4:
#         return True
#     else:
#         False

# print(list(filter(get_below_4, my_list)))
# print(list(filter(lambda num: num < 4, my_list)))

# exercise
# convert the power function and the filter one to list comprehension
print(list(map(lambda num: num ** 2, my_list)))

print([num ** 2 for num in my_list])
print(list(filter(lambda num: num < 4, my_list)))

print([num for num in my_list if num < 4])
