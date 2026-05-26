import tkinter as tk
from tkinter import ttk

def button_func(entry_string):
    print('A button was Click')
    print(entry_string.get())

def outer_func(parameter):
    def inner_func():
        print("A button was pressed")
        print(parameter.get())
    return inner_func
# create a window

window = tk.Tk()
window.title('Button Arguments')
window.geometry("600x400")

#widgets
entry_string = tk.StringVar(value="Please Click to logIn" )
entry = ttk.Entry(window, textvariable=entry_string)
entry.pack(padx = 20, pady =20)

button = ttk.Button(window, text = 'Click Me', command= outer_func(entry_string))
button.pack(padx=5, pady=5)

# run App
window.mainloop()