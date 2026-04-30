# Advanced data operator
# Python has a of ways to manipulate data
# It is incredibly popular for data science and machine learning for reason

# More advance ways to loop Sorting data List comprehension and data handling

# Manipulating lists and for loops
# Ofter you want to merge lists and loop over the result
# We can zip lists together and we can give each list and index inside of the loop

inventory_names = ['Screws', 'Wheels', 'Metal parts', 'Rubber bits', 'Screwdrevier','Wood']
inventory_numbers = [43,12,95,421,23,43]

# print(list(zip(inventory_names, inventory_numbers)))
#for thing in zip(inventory_names,inventory_numbers):
    #print(thing)
    #print(thing[0]) # 0 will give you the name of the items
    #print(thing[1]) # 1 will give you the number
#for name, number in zip(inventory_names, inventory_numbers):
    # print(name)
    # print(number)
    #print(f'{name} cureent inventory: {number}')

# Enumerate function get the current index
#print(enumerate(inventory_names)) # enumerate returns object 
#print(list(enumerate(inventory_names)))
#for thing in enumerate(inventory_names):
# for index, name in enumerate(inventory_names):
#     print(f'{index}: {name}')
#     if index == len(inventory_names) // 2:
#         print('Half way done')
    # print(thing)
    # print(thing[0])
    # print(thing[1])

# excercise
# combine zip and enumerate to get 'Screws [id: 0] inventory: 43'

# for name, num in enumerate(zip(inventory_names, inventory_numbers)):
#     print(f'{name} - inventory: {num}')
for index, inventory_tuple in enumerate(zip(inventory_names, inventory_numbers)):
    print(f'{inventory_tuple[0]} [id: {index}] - inventory: {inventory_tuple[1]}')

