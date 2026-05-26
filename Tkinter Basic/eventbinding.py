# Events can be lots of things
# Events can be mouse events
# Events can be key events
# Events can be window events
# Events can be widget events

import tkinter as tk
from tkinter import ttk

def get_pos(event):
    print(f'x: {event.x} y: {event.y}')

#window
window = tk.Tk()
window.title('Event Binding')
window.geometry('600x500')


# widgets
text = tk.Text(master = window)
text.pack()

entry = ttk.Entry(master = window)
entry.pack(padx=20, pady=20)

btn = ttk.Button(window, text='A Button', )
btn.pack()

#Event
# window.bind('<Alt-KeyPress-a>', lambda event: print("A event"))
# window.bind('<Motion>', get_pos)

# entry.bind('<FocusIn>', lambda event: print('entry field was selected'))

text.bind('<Shift-MouseWheel>', lambda event: print('Mouse wheel was scrolled'))

window.mainloop()