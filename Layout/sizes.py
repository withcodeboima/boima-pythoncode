# Sizes Understanding widget size
# widget can have a custom size
# But that size will be overwritten by the layout methods

import tkinter as tk
from tkinter import ttk

# window 
window = tk.Tk()
window.title('Sizes')
window.geometry('400x300')

# widgets
label1 = ttk.Label(window, text = 'First Label', background = 'red')
label2 = ttk.Label(window, text = 'second Label', background = 'blue', width=50)

#layout
# label1.pack()
# label2.pack( fill= 'x')

# grid
window.columnconfigure((0,1), weight = 1, uniform = 'a')
window.rowconfigure((0,1), weight = 1, uniform = 'a')

label1.grid(row = 0, column = 0)
label2.grid(row = 1, column = 0, sticky='nsew')
# run
window.mainloop()