# Layout Overview in tkinter
# In this tutorial, we will learn about the different layout managers in tkinter and how to use them to create a responsive GUI application. We will cover the pack, grid, and place layout managers, and see how they can be used to arrange widgets in a window.

# pack layout manager
# The pack layout manager is a simple layout manager that arranges widgets in a row or column. It is useful for simple layouts, but it can be confusing to use if you have a complex layout.

# grid layout manager
# The grid layout manager is a more complex layout manager that arranges widgets in a grid. It is useful for complex layouts, but it can be confusing to use if you have a simple layout.

# place layout manager  
# The place layout manager is a more complex layout manager that arranges widgets in a grid. It is useful for complex layouts, but it can be confusing to use if you have a simple layout.

import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.title("Layout Overview")
window.geometry('600x400')

#widgets
label1 = ttk.Label(window, text="Label 1", background='red')

label2 = ttk.Label(window, text="Label 2", background='green')

#pack layout
    # label1.pack(side = 'left', expand = True, fill = 'y')
    # label2.pack(side = 'left', expand = True, fill = 'both')

#grid layout
# window.columnconfigure(0, weight = 1)
# window.columnconfigure(1, weight = 1)
# window.columnconfigure(2, weight = 2)
# window.rowconfigure(1, weight = 1)

# label1.grid(row = 0, column = 1, sticky = 'nsew')
# label2.grid(row = 1, columnspan = 2, column = 1, sticky = 'nsew')

# ploace layout
label1.place(x = 100, y = 200, width = 200, height = 100)
label2.place(relx = 0.5, rely = 0.5, relwidth = 1, anchor = 'se')
#run
window.mainloop()