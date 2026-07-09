# Tabs ttk notebook widget
# Has a couple of children which are frames each frame is one tab

import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Tabs')
window.geometry('600x400')

# notebook
notebook = ttk.Notebook(window)

tab1 = ttk.Frame(notebook)
label1 = ttk.Label(tab1, text = 'Text in tab1')
label1.pack()
button1 = ttk.Button(tab1, text = 'Button in tab1')
button1.pack()

tab2 = ttk.Frame(notebook)
label2 = ttk.Label(tab2, text = 'Text in tab2')
label2.pack()
button2 = ttk.Button(tab2, text = 'Button in tab2')
button2.pack()
entry2 = ttk.Entry(tab2)
entry2.pack()

notebook.add(tab1, text = 'Tab1')
notebook.add(tab2, text = 'Tab2')
notebook.pack()

#run
window.mainloop()