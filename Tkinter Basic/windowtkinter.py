import tkinter as tk
from tkinter import ttk

# we can olny changed the title and size of the window 
# we can change a lots more opcacity, position, full screen title bar etc

# window 
window = tk.Tk()
window.title('This is the Window title')
window.geometry('600x400+100+200')
window.iconbitmap('C:\\Users\\Codewithboima\\Documents\\Python-10App\\Tkinter Basic\\python.ico')

# window attributes
window.minsize(200, 100)
window.maxsize(800, 700)
# window.resizable(True, False)

# screen attributes
print(window.winfo_screenwidth())
print(window.winfo_screenheight())

window.attributes('-alpha', 1)
# window.attributes('-topmost', True)

# security event
window.bind('<Escape>', lambda event:window.quit())
# window.attributes('-disable', True)
# window.attributes('-fullscreen', True)
# window.state('zoomed')

# title bar
window.overrideredirect(True)
grip = ttk.Sizegrip(window)
grip.place(relx = 1.0, rely = 1.0, anchor = 'se')

# run app
window.mainloop()