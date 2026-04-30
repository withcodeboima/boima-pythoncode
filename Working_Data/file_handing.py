# python can open simple files .txt files for example
#Pythoncan actually open nearly any file but often you will need external modules

file = open('../Working_Data/test.txt')
print(list(file))
file.close

# open and close it automatically
# with open('C:/Users/Codewithboima/Documents/Python-10App/Working_Data/test.txt') as file:
#     print(list(file))

# with open('C:/Users/Codewithboima/Documents/Python-10App/Working_Data/test.txt') as file:
#     # print(file.read())
#     for line in list(file):
#         print(line)

# write some file 

# with open('new_file.txt', 'w') as file:
#     file.write('\nxxxxThis is a new line xxxxxx')

# exercise
# create a new text file and draw a tree in it

# with open('tree_txt', 'w') as tree_file:
#     tree_string = ''' x
#     xxx
#     xxxxx
#     xxxxxxx
#     xxxxxxxx
#     xxxxxxxxxx
#     xxxxxxxxxxx
#     xxxxxxxxxxxx
#     xxxxxxxxxxxxxx
#     xxxxxxxxxxxxxxx
#     xxxxxxxxxxxxxxxx'''
#     tree_file.write(tree_string)

