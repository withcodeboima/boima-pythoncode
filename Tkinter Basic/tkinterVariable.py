# Tkinter Variables are special variables that can be used to store and retrieve data from widgets. They are used to create a link between the widget and the variable, so that when the widget is updated, the variable is also updated.

import tkinter as tk
from tkinter import ttk

# button function to update the label text
def button_func():
    print(string_var.get())
    string_var.set('Data updated!') # update the variable, which will automatically update the label text

# window
window = tk.Tk()
window.title('Tkinter Variables - Boima')
window.geometry('300x150')

# create a tkinter variable
string_var = tk.StringVar(value='Hello, Tkinter!')

label = ttk.Label(master = window, text='Welcome to Tkinter Variables!', textvariable=string_var)
label.pack(padx=20, pady=10)

entry = ttk.Entry(master = window, textvariable=string_var)
entry.pack(padx=30, pady=10)

button = ttk.Button(master = window, text='Update Label', command=button_func)
button.pack(padx=20, pady=10)

# entry2 =ttk.Entry(window, textvariable=string_var)
# entry2.pack(padx=20,pady=10)

# run the app
window.mainloop()

# exercise
# create 2 entry fields and 1 label, they should all be connected  vai a stringVar set a start value of test 