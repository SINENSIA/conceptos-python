import tkinter as tk
import os

# Función para listar contenido del directorio actual
def list_directory():
    # Obtiene una lista de nombres de archivos y directorios en el directorio actual
    return os.listdir('.')

# Crea la ventana principal
root = tk.Tk()
root.title("Contenido del Directorio Actual")

frame = tk.Frame(root, padx=30, pady=30)
frame.pack(expand=True, fill='both')
# Obtén la lista del contenido del directorio
directory_content = list_directory()

label = tk.Label(frame, text="Contenido del Directorio Actual")
label.pack(padx=20, pady=20)
# Crea un widget Listbox para mostrar la lista de archivos/directorios
listbox = tk.Listbox(frame, width=50, height=20)
listbox.pack(padx=20, pady=20)

# Añade el contenido del directorio al Listbox
for item in directory_content:
    listbox.insert(tk.END, item)

# Ejecuta la aplicación
root.mainloop()