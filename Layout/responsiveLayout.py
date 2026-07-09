# Responsive Layouts
# Responsive layouts are layouts that adjust to the size of the window. They are useful for creating layouts that are responsive to the size of the window.
# Tkinter lack inbuilt tools fro resonsive layouts
# We cannot update on existing layout
# We  need to create a separate layout for each size


import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self, start_size):
       super().__init__()
       self.title('Responsive Layout')
       self.geometry(f'{start_size[0]}x{start_size[1]}')

       SizeNotifier(self, {900: self.create_large_layout, 600: self.create_medium_layout, 300: self.create_small_layout})

      

    #    self.bind('<Configure>', lambda event: print(event))
    
       self.mainloop()

    def create_small_layout(self):
        print('small layout')

    def create_medium_layout(self):
        print('medium layout')

    def create_large_layout(self):
        print('large layout') 

class SizeNotifier:
    def __init__(self, window, size_dict):
        self.window = window
        self.size_dict = {key: value for key, value in sorted(size_dict.items())}
        self.current_min_size = None

        self.window.update()

        min_width = self.window.winfo_width()
        min_height = self.window.winfo_height()

        self.window.minsize(min_width, min_height)
        
        self.window.bind('<Configure>', self.check_size)
        # self.window.bind('<Configure>, lambda event: print(event)')

    def check_size(self, event):
        window_width = event.width
        check_size = None
        
        for min_size in self.size_dict:
            delta = window_width - min_size
            if delta >= 0:
               check_size = min_size

            if check_size != self.current_min_size:
                self.current_min_size = check_size
                self.size_dict[check_size]()

app = App((400, 300))

    