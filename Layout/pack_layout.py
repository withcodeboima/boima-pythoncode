# Pack Layout Manager
# The pack layout manager is a simple layout manager that arranges widgets in a row or column. It is useful for simple layouts, but it can be confusing to use if you have a complex layout.
# side - 'top' (default), 'bottom', 'left', 'right'
# expand - True or False (default)
# fill - 'x' (default), 'y', 'both'

import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.title("Pack Layout")
window.geometry('400x600')

# widgets
label1 = ttk.Label(window, text = 'First Label', background = 'red')
label2 = ttk.Label(window, text = 'second Label', background = 'blue')
label3 = ttk.Label(window, text = 'Third Label', background = 'green')
button = ttk.Button(window, text = 'Click Me')

# Layout
label1.pack(side = 'left', expand = True, fill = 'both')
label2.pack(side = 'top', expand = True, fill = 'both')
label3.pack(side = 'top', expand = True, fill = 'both')
button.pack(side = 'top',  expand = True, fill = 'x')
# run
window.mainloop()