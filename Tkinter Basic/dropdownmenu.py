# Combbox and Spinbox

import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.title('Combobox and Spinbox')
window.geometry('600x500')

# combobox
item = ('Ice', 'Pizza', 'Fries', 'Burger', 'Noodles', 'Pasta')
food_string = tk.StringVar(value= item[0])
combobox = ttk.Combobox(window, textvariable=food_string)
combobox['values'] = item
combobox.pack(padx=20, pady=20)

#event
combobox.bind('<<ComboboxSelected>>', lambda event: combo_label.config(text = f'Selected value: {food_string.get()}'))

combo_label = ttk.Label(window, text = 'A Label')
combo_label.pack()

# Spinbox
spin_int = tk.IntVar(value = 12)
spinbox = ttk.Spinbox(
    window,
      from_ = 1, 
      to = 20,
      increment=3,
      command= lambda: print('A arrow was Clicked'),
      textvariable= spin_int
      )
spinbox.bind('<<Increment>>', lambda event: print('Up'))
spinbox.bind('<<Decrement>>', lambda event: print('Down'))
# spinbox['value'] = (1,2,3,4,5,6,7,8,9,10)
spinbox.pack(padx=20, pady=20)


#run app
window.mainloop()