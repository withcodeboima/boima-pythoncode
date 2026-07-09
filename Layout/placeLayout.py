# Wigdet are place by specifying the left,top,width and height
# There are numbers can be absolute or relative
import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.title('Place Layout')
window.geometry('400x600')

#widgets
label1 = ttk.Label(window, text = 'Label 1', background = 'red')
label2 = ttk.Label(window, text = 'Label 1', background = 'blue')
label3 = ttk.Label(window, text = 'Label 1', background = 'green')
button1 = ttk.Button(window, text = 'Click Me')

# layout
label1.place(x = 300, y = 100, width=100, height = 200)
label2.place(relx=0.2, rely = 0.1, relwidth = 0.4, relheight = 0.5)

# run
window.mainloop() 