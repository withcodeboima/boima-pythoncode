# If canvas is point, treeview is excel
# We are creating a table

import tkinter as tk
from tkinter import ttk
from random import choice

# window
window = tk.Tk()
window.title('Table')
window.geometry('600x400')

# data
first_name = ['John', 'Jane', 'Bob', 'Alice', 'Tom', 'Emily']
last_name = ['Doe', 'Smith', 'Johnson', 'Williams', 'Brown', 'Jones']

#treeview
table = ttk.Treeview(window, columns = ('first', 'last', 'email'), show = 'headings')
table.heading('first', text = 'First Name')
table.heading('last', text = 'Last Name')
table.heading('email', text='Email')
table.pack(fill = 'both', expand = True)

# insert data
# table.insert(parent= '', index = 0, values = ('John', 'Doe', 'jdoe@gmail.com'))
for i in range(100):
    first = choice(first_name)
    last = choice(last_name)
    email = f'{first[0]}{last}@gmail.com'
    data = (first, last, email)
    table.insert(parent= '', index= 0, values = data)

# event

def item_select(event):
    print(table.selection())
    for i in table.selection():
        print( table.item(i)['values'])

def delete_items(event):
    for i in table.selection():
        table.delete(i)

table.bind('<<TreeviewSelect>>', item_select)
table.bind('<Delete>', delete_items)

# table.bind('<<TreeviewSelect>>', lambda event: print(table.selection()))


#run
window.mainloop()