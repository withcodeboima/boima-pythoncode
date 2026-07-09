# frame and parenting are just another widget, but they are used to group other widgets together. They are also used to create a hierarchy of widgets, which can be useful for organizing your GUI.

import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Frames and Parenting')
window.geometry('600x400')

# frame
frame = ttk.Frame(window, width = 200, height = 200, borderwidth = 10, relief = tk.GROOVE)
frame.pack_propagate(False)
frame.pack()

# Master setting
label = ttk.Label(frame, text = 'This is a label')
label.pack()

button = ttk.Button(frame, text = 'Click Me')
button.pack() 

label2 = ttk.Label(frame, text = "Label outside the frame")
label2.pack(side ='left')

# run
window.mainloop()