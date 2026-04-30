# functions that take functions as arguments
# You can pass a function into another function as an argument
# The sorted function is the best example
# The function determines how the iterable is sorted

# list1 = [4,2,3,1,5]
# print(sorted(list1))
# list1.sort()
# print(list1)
# print(sorted(list1, reverse = True))

# list2 = [('a', 3), ('b', 10), ('c', 6), ('d', 5)]
# def sort_function(item):
#     return item[1]
#print(sorted(list2, key = sort_function))
# print(sorted(list2, key = lambda item: item[1]))

# print(sorted(list2))
#print(sorted(list2, key = lambda x: x[1]))

# exercise
inventory = ['Screws','Wheels','Metal parts','Rubber bits','Screwdrevier','Wood']
inventory_numbers = [43,12,95,421,23,43]
combined_list = list(zip(inventory, inventory_numbers))
# sort this the list by inventory number
sorted_comp_num = sorted(combined_list, key = lambda inv_tuple: inv_tuple[1])
# print(sorted_comp_num)
# sort this list by length of the inventory name
sorted_comp_name = sorted(combined_list, key = lambda inv_tuple: len(inv_tuple[0]))
print(sorted_comp_name)

