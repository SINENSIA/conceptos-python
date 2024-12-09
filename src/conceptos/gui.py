import tkinter as tk
import random
from tkinter import PhotoImage


def move_button(event):
    new_x = random.randint(50, 350)
    new_y = random.randint(50, 350)
    button.place(x=new_x, y=new_y)


# Create the main window
root = tk.Tk()
root.geometry('400x400')

# Load an image file
background_image = PhotoImage(file='are_you_sure.gif')

# Create a label with image
background_label = tk.Label(root, image=background_image)
# Ajusta la etiqueta al tamaño de la ventana
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Add a text label
label = tk.Label(
    root, text='Quiere cerrar esta ventana? Está seguro?', bg='white')
label.pack()

# Add a button
button = tk.Button(root, text='Está seguro!', bg='white')
button.place(x=200, y=200)

# Bind the move action to mouse enter event on button
button.bind('<Enter>', move_button)

# Run the application
root.mainloop()
