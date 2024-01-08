import tkinter as tk

# Crea una ventana principal
root = tk.Tk()

# Establece un título para la ventana
root.title("Hello World Application")

frame = tk.Frame(root, padx=30, pady=30)
frame.pack(expand=True, fill='both')

# Crea una etiqueta con el texto "Hello, World!" y la añade a la ventana
label = tk.Label(frame, text="Hello, World!", font=("Arial", 30))
label.pack()



# Ejecuta el bucle principal de la aplicación
root.mainloop()