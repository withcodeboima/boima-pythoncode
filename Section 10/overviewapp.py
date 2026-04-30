import tkinter as tk
from tkinter import ttk
import ttkbootstrap

def convert():
    mile_input = entry_int.get()
    kilometer_output = mile_input * 1.6     
    # print(entry_int.get())
    output_string.set(kilometer_output)

#window
# window = tk.Tk()
window = ttkbootstrap.Window(themename= 'darkly')
window.title('Demo App')
window.geometry('300x150')

# title
title_lable = ttk.Label(master = window,text = 'Mile to Kilometer Converter', font= 'Calibri 15 bold')
title_lable.pack()

#input field
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable= entry_int)
button = ttk.Button(master = input_frame, text = 'Convert', command = convert)
entry.pack(side = 'left', padx = 10)
button.pack( side = 'left')
input_frame.pack(pady = 10)

# Output field
output_string = tk.StringVar()
output_label = ttk.Label(
    master = window,
    text = 'Output',
    font = 'Calibri 24',
    textvariable= output_string)
output_label.pack(pady = 5)

#run the app
window.mainloop()