 # Creating custom widgets with returns

import tkinter as tk
from tkinter import ttk

def create_segment(parent, label_text, button_text):
    frame = ttk.Frame( master = parent)


    #grid layout
    frame.rowconfigure(0, weight = 1)
    frame.columnconfigure(0, weight = 1, uniform = 'a')

    #widgets
    ttk.Label(frame, text = label_text).grid(row = 0, column = 0, sticky = 'nsew')
    ttk.Button(frame, text = button_text).grid(row = 0, column = 1, sticky = 'nsew')



    return frame

class Segment(ttk.Frame):
    def __init__(self, parent, label_text, button_text):
        super().__init__(master = parent)

        # grid layout
        self.rowconfigure(0, weight = 1)
        self.columnconfigure(0, weight = 1, uniform = 'a')
        ttk.Label(self, text = label_text).grid(row = 0, column = 0, sticky = 'nsew')
        ttk.Button(self, text = button_text).grid(row = 0, column = 1, sticky = 'nsew')

        self.pack(expand = True, fill = 'both', padx = 10, pady = 10)

# window
window = tk.Tk()
window.title('Custom Widgets')
window.geometry('400x600')

# widgets
# Segment(window, 'Label', 'Button')
# Segment(window, 'test', 'Click')
# Segment(window, 'bye', 'launch')
# Segment(window, 'hello', 'test')
# Segment(window, 'last one', 'exit')

create_segment(window, 'Label', 'Button').pack(expand = True, fill = 'both')
create_segment(window, 'test', 'Click').pack(expand = True, fill = 'both')
create_segment(window, 'bye', 'launch').pack(expand = True, fill = 'both')
create_segment(window, 'hello', 'test').pack(expand = True, fill = 'both')
create_segment(window, 'last one', 'exit').pack(expand = True, fill = 'both')


# run
window.mainloop()