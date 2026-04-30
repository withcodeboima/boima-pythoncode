# Widget are the building blocks of tkinter. They are the elements that make up the user interface of a tkinter application. Some common widgets include:
# - Label: Used to display text or images.
# - Button: Used to create buttons.
# - Entry: Used to create input fields.
# - Frame: Used to create containers for other widgets.
# - Scrollbar: Used to create scrollbars.
# - Listbox: Used to create lists.
# - Canvas: Used to create canvases for drawing graphics.
# - Checkbutton: Used to create checkboxes.
# - Radiobutton: Used to create radio buttons.
# We have two type of widgets in tkinter:
# tk widgets were the org\iginal ones
# ttk widgets were added later on those are more modern

import tkinter as tk
from tkinter import ttk

def button_func():
    print('Button was clicked')

def buttonfunc():
    print('Hello People')

# create a window
window = tk.Tk()
window.title('Boima window and Wigget')
window.geometry('300x150')
# create widgets
text = tk.Text(master = window,
bg="#1f0cd1",   # background color
fg="white",     # text color
insertbackground="white"  # cursor color
)
text.pack(padx = 30, pady = 30)

#ttk widgets
# label = ttk.Label(master = window, text = 'This is a test')
# label.pack()
entry = ttk.Entry(master = window)
entry.pack(padx=20, pady=20)

#ttk button
button = ttk.Button(master = window, text='Learn More', command = button_func)
button.pack()

# exercise
label = ttk.Label(master = window, text = 'My Label' )
label.pack()
entry = ttk.Entry(master = window)
entry.pack()
button = ttk.Button(master = window, command = buttonfunc, text = 'Click Me')
button.pack()

# run the app
window.mainloop() # the mainloop update the gui