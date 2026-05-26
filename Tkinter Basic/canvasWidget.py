# A canvas is a widget that alows you to draw graphics on a window.

import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Canvas Widget')
window.geometry('600x400')

#canvas
canvas = tk.Canvas(window, bg='blue')
canvas.pack()

# canvas.create_rectangle((50,20,100,200),fill='red',width=10, dash=(1,2), outline='green')
# canvas.create_oval((200,0,300,200), fill='yellow', width=10, outline='green')
# canvas.create_line((0,0,200,200), fill='yellow', width=10)
# canvas.create_polygon((0,0,100,200,300,50), fill='black', outline='green', width=10)
# canvas.create_arc((100,100,300,300), start=0, extent=180, fill='black', outline='green', width=10, style = tk.ARC)

# canvas.create_text((100,200), text = 'This is some text')

# canvas.create_window((150,100), window = ttk.Label(window,text='This is a label'))

def draw_on_canvas(event):
    x = event.x
    y = event.y
    canvas.create_oval((x - brush_size / 2,y - brush_size / 2, x + brush_size / 2, y + brush_size /2), fill= 'black')

def brush_size_adjust(event):
    global brush_size
    if event.delta > 0:
        brush_size += 4
    else:
        brush_size -= 4

    brush_size =max(0,min(brush_size, 50))

brush_size = 2
canvas.bind('<Motion>', draw_on_canvas)
canvas.bind('<MouseWheel>', brush_size_adjust)


#run
window.mainloop()

# https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html