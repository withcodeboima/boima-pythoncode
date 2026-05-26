# Tkinter has a slider and a progress bar
# both show progress in one dimension

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# window
window = tk.Tk()
window.title('Sliders')
window.geometry('600x400')

#slider
scale_int = tk.DoubleVar(value = 15)
scale = ttk.Scale(window, command= lambda value: print(scale_int.get()), from_ = 0, to = 25, length = 300,orient='vertical', variable = scale_int)
scale.pack()

#progress bar

progress = ttk.Progressbar(window, variable = scale_int, maximum = 25, orient='horizontal',mode = 'indeterminate',length=400)
progress.pack(padx=20, pady=20)
# progress.start()

#Scrollededtext

scrolled_text = scrolledtext.ScrolledText(window, width=30, height=10)
scrolled_text.pack()


#run
window.mainloop()