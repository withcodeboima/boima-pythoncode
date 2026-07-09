import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Pack Parent")
window.geometry("400x600")

# Top frame
top_frame = ttk.Frame(window)

label1 = tk.Label(top_frame, text="First Label", bg="red")
label2 = tk.Label(top_frame, text="Second Label", bg="blue")

label1.pack(side="left", fill="both", expand=True)
label2.pack(side="left", fill="both", expand=True)

top_frame.pack(fill="both", expand=True)

# Middle widget
label3 = tk.Label(window, text="Third Label", bg="green")
label3.pack(expand=True)

# Bottom frame
bottom_frame = ttk.Frame(window)

button = ttk.Button(bottom_frame, text="Click Me")
label4 = tk.Label(bottom_frame, text="Fourth Label", bg="orange")
button2 = ttk.Button(bottom_frame, text="Another Button")

button.pack(side="left",expand=True,fill = "both")
label4.pack(side="left", expand=True, fill = "both")
button2.pack(side="left", expand=True, fill = "both")

bottom_frame.pack(expand=True, fill = "both", padx = 20, pady = 20)

window.mainloop()