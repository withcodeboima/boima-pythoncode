# Other Comprehension
# Besides list comprephension you can also create dictionaries and sets comprehension
# dict_comp = (num : num for num in range(10))
# set_comp = {num for num in range(10)}

# set_comp = {num for num in range(100)}
# dict_comp = {num : num **2 for num in range(100)}   
# tuple_comp = tuple(num for num in range(100))
# print(tuple_comp)
# for value in tuple_comp:
#     print(value)
# print(tuple_comp)

exercise_comp = {letter:[1,2,3,4,5] for letter in 'ABCDE'}
print(exercise_comp) 