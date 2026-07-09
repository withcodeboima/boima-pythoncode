import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# https://docs.python.org/3/library/tkinter.messagebox.html

class extra(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Extra window')
        self.geometry('300x400')
        ttk.Label(self, text = 'This is a new window').pack()
        ttk.Entry(self).pack(padx=10, pady=10)
        ttk.Button(self, text = 'Click Me').pack()

def ask_yes_no():
    messagebox.showwarning('Info title', 'Here are some infromation')
    #messagebox.showerror('Info title', 'Here are some infromation')
    #messagebox.showinfo('Info title', 'Here are some infromation')
    # answer = messagebox.askquestion('Title', 'Body')
    # print(answer)

def create_window():
    global extra_window
    extra_window = extra()
    # extra_window = tk.Toplevel()
    # extra_window.title('Extra Window')
    # extra_window.geometry('300x400')
    # ttk.Label(extra_window, text = 'This is a new window').pack()
    # ttk.Entry(extra_window).pack(padx=10, pady=10)
    # ttk.Button(extra_window, text = 'Click Me').pack()

def close_window():
    extra_window.destroy()

#window
window = tk.Tk()
window.title('Multiple Windows')
window.geometry('600x400')

button1 = ttk.Button(window, text = 'open main window', command = create_window)
button1.pack(expand = True)

button2 = ttk.Button(window, text = 'Close main window', command = close_window)
button2.pack(expand = True)

button3 = ttk.Button(window, text = 'create yes no window', command = ask_yes_no)
button3.pack(expand = True)

# run
window.mainloop()

