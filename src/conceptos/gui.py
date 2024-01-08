# https://docs.python.org/es/3/library/tkinter.html

import tkinter as tk
import random

def move_button(event):
    new_x = random.randint(50, 350)
    new_y = random.randint(50, 350)
    button.place(x=new_x, y=new_y)

# Create the main window
root = tk.Tk()
root.geometry('400x400')

# Add a text label
label = tk.Label(root, text='Quiere cerrar esta ventana? Está seguro?')
label.pack()

# Add a button
button = tk.Button(root, text='Está seguro!')
button.place(x=200, y=200)

# Bind the move action to mouse enter event on button
button.bind('<Enter>', move_button)

# Run the application
root.mainloop()