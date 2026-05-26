# The are three major kinds of button 
# Button, Checkbutton and Radiobutton

import tkinter as tk
from tkinter import ttk

# Setup
window = tk.Tk()
window.title('Button with Boima') 
window.geometry('600x400')

# button
def button_func():
    print('You are loggin successfully')
    print(radio_var.get())

button_string = tk.StringVar(value="Please Click to logIn")

button = ttk.Button(master= window, text='You are loggin successfully',command=button_func, textvariable=button_string)
button.pack(padx=20, pady=20)

# Checkbutton
check_var = tk.IntVar()
check = ttk.Checkbutton(master = window, text='checkbox 1', command= lambda: print(check_var.get()), variable=check_var, onvalue=1, offvalue=0)
check.pack(padx=20, pady=20)

# radio button
radio_var  = tk.StringVar()
radio1 = ttk.Radiobutton(
    master = window, 
    text='Web Development',
    value='RADIO 1',
    variable= radio_var, 
    command= lambda: print(radio_var.get()))
radio1.pack(padx = 20, pady = 20)
radio2 = ttk.Radiobutton(
    master = window,
    variable= radio_var, 
    text='Python Programming', 
    value='RADIO 2',)
radio2.pack(padx = 20, pady = 20)
# run app
window.mainloop()