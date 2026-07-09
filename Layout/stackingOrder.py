# Stacking widgets
# Stack widgets in tkinter using the pack() method
# Pack is a layout manager that arranges widgets in a row or column. It is useful for simple layouts, but it can be confusing to use if you have a complex layout.

import tkinter as tk
from tkinter import ttk

# window 
window = tk.Tk()
window.title('Stacking Widgets')
window.geometry('400x300')

#widgets
label1 = ttk.Label(window, text='Label 1', background = 'red')
label2 = ttk.Label(window, text='Label 1', background = 'green')


# label1.lift()
# label2.lower()




button1 = ttk.Button(window, text = 'raise label 1', command = lambda: label1.lift())
button2 = ttk.Button(window, text = 'raise label 2', command = lambda: label2.lift())

# Layout
label1.place(x = 50, y = 100,width = 200, height = 150)
label2.place(x = 150, y = 60,width = 140, height = 100)

button1.place(rely = 1, relx = 0.8,  anchor = 'se')
button1.place(rely = 1, relx = 1,  anchor = 'se')
#run
window.mainloop()