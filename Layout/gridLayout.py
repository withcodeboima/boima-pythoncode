# Grid

import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.title('Grid Layout')
window.geometry('600x400')

#widgets
label1 = ttk.Label(window, text = 'First Label', background = 'red')
label2 = ttk.Label(window, text = 'second Label', background = 'blue')
label3 = ttk.Label(window, text = 'Third Label', background = 'green')
label4 = ttk.Label(window, text = 'Fourth Label', background = 'orange')
button = ttk.Button(window, text = 'Click Me')
button2 = ttk.Button(window, text = 'Learn More')
entry = ttk.Entry(window)

# define a grid
window.columnconfigure((0,1,2), weight = 1, uniform = 'a')
window.columnconfigure(1, weight = 1, uniform = 'a')
window.columnconfigure(2, weight = 1, uniform = 'a')

window.columnconfigure(3, weight = 10, uniform = 'a')
window.columnconfigure(0, weight = 1, uniform = 'a')
window.columnconfigure(1, weight = 1, uniform = 'a')
window.columnconfigure(2, weight = 1, uniform = 'a')
window.rowconfigure(3, weight = 3, uniform = 'a')

# place a widget
label1.grid(row = 0, column= 0, sticky = 'nsew')

label2.grid(row = 2, column= 1, sticky = 'nsew')
label3.grid(row = 1, column= 0, columnspan = 2, sticky = 'nsew',padx = 20, ipady=100)
label4.grid(row = 3,column = 3, sticky='se' )

button.grid(row = 0, column = 3, sticky = 'nesw')
button2.grid(row = 2, column = 2, sticky = 'nesw')

#run
window.mainloop()