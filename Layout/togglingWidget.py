# Toggling widgets
# widget can be hidden or shown
# widget can be disabled or enabled

import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Toggling Widgets')
window.geometry('400x300')


#wigdet place
# def toggle_label_place():
#     global label_visible

#     if label_visible:
#         label.place_forget()
#         label_visible = False
#     else:
#         label_visible = True
#         label.place(relx = 0.5, rely = 0.5, anchor = 'center')
 
# button = ttk.Button(window, text='toggle label', command = toggle_label_place)
# button.place(x = 10, y = 10)

# label_visible = True
# label = ttk.Label(window, text='A label')
# label.place(relx = 0.5, rely = 0.5, anchor = 'center')


# grid

# def toggle_label_grid():
#     global label_visible

#     if label_visible:
#         label.grid_forget()
#         label_visible = False
#     else:
#         label_visible = True
#         label.grid(column = 1, row = 0)

# window.columnconfigure((0,1), weight = 1,uniform = 'a')
# window.rowconfigure(0, weight = 1,uniform = 'a')

# button = ttk.Button(window, text='toggle label', command = toggle_label_grid)
# button.grid(row = 0, column = 0)

# label_visible = True
# label = ttk.Label(window, text='A label')
# label.grid(column = 1, row = 0)


# pack

def toggle_label_pack():
    label.pack_forget()

label_visible = True
label = ttk.Label(window, text = 'A label')
label.pack(expand = True)

button = ttk.Button(window, text = "toggle label", command = toggle_label_pack)
button.pack()




# layout

# run 
window.mainloop()