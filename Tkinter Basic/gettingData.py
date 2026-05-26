# There are two way to get data for the widget
# Tkinter variables and the get method

import tkinter as tk
from tkinter import ttk

# Function to get data from the entry widget
def button_func():
    print(entry.get()) # get method is used to get the data from the entry widget

# Update the label 
    # label.config(text = 'Data retrieved!')
    label['text'] = 'Data retrieved!' # another way to update the label

#create a window

window = tk.Tk()
window.title('Getting Data')
window.geometry('300x150')
# widget label
label = ttk.Label(master = window, text = 'Enter your name')
label.pack(padx=20, pady=20)
# entery widget
entry = ttk.Entry(master = window)
entry.pack(padx=30, pady=30)
# button widget
button = ttk.Button(master = window, text = 'Get Data', command = button_func)
button.pack()
# run the app
window.mainloop()