# List Comprehension is a way to create list on one line of code
# It is one of the most powerful feature in python
# You can use it to create simple lists and use it to manipulate existing lists

# my_list = []
# for num in range(0,100):
#     my_list.append(num)
# print(my_list)

#my_list_comp = [num * 2 for num in range(0,100)]
# my_list_comp = [(num,num,num) for num in range(0,100)]
# print(my_list_comp)

# You can combine the list comprehension with a ternary operator
# You can be used to filter lists.

# my_list_comp = [(num,num,num) for num in range(0,100) if num < 20]
# print(my_list_comp)

# my_list_comp = [(num,num,num) if num < 20 else 0 for num in range(0,100)]
# print(my_list_comp)

# inventory_names = ['Screws', 'Wheels', 'Metal parts', 'Rubber bits', 'Screwdrevier','Wood']
# inventory_numbers = [43,12,95,421,23,43]

# replenish_list = [thing for thing in zip(inventory_names,inventory_numbers)]
# replenish_list = [(name,number)for name,number in zip(inventory_names,inventory_numbers) if number < 25]
# print(replenish_list)

# Combine list comprehension
# combined_comp = [[x for x in range(5)] for y in range(10)]
# print(combined_comp)

# Better way of doing this
# combined_comp = [[x for x in range(5)] for y in range(10)]
# for row in combined_comp:
#     print(row)

# combined_comp = [[(x,y) for x in range(5)] for y in range(10)]
# for row in combined_comp:
#     print(row)

# exercise
# create the field for a chess board
# the field should be 8x8
# the field should be a list of lists

# chess_board = [[(letter,num) for num in range(1,9)] for letter in 'ABCDEFGH']
# for row in chess_board:
#   print(row)

chess_board = [[f'{letter}{num}' for num in range(1,9)] for letter in 'ABCDEFGH' [::-1]]
for row in chess_board:
  print(row)



