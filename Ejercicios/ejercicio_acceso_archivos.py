# Intenta abrir un archivo llamado "mi_archivo.txt" en modo de lectura ('r’).

# Si el archivo no existe (se produce una excepción FileNotFoundError), emite un mensaje indicando que el archivo no existe y crea un nuevo archivo "mi_archivo.txt".
# Si el archivo existe, emite un mensaje de error indicando que el archivo ya existe y no puedes continuar.
# Abre el archivo en modo de escritura ('w') y sobrescribe el archivo con una cadena vacía
with open('mi_archivo.txt', 'w', encoding='utf-8') as archivo:
    archivo.write('')
"""
try:
    with open('mi_archivo.txt', 'r') as file:
        print('El archivo ya existe')
except FileNotFoundError:
    with open('mi_archivo.txt', 'w') as file:
        print('mi_archivo.txt creado correctamente')
"""

# Alternativa con +x
"""
try:
    # Intenta abrir el archivo en modo de exclusión ('+x')
    with open('mi_archivo.txt', 'x', encoding='utf-8') as archivo:
        print("El archivo no existe. Creando un nuevo archivo...")
except FileExistsError:
    # El archivo ya existe, emite un mensaje y no se crea
    print('EL archivo ya exsite')
"""

# Escribe una serie de líneas de texto en el archivo. Incluye al menos 5 líneas de texto con diferentes contenidos.    
with open('mi_archivo.txt', 'a', encoding='UTF-8') as file:
    file.write('\nEsta es una primera línea')
    file.write('\nEsta es una segunda línea')
    file.write('\nEsta es una tercera línea')
    file.write('\nEsta es una cuarta línea')
    file.write('\nEsta es una quinta línea')

"""
# Menos eficiente pero podemos practicas con comprensiones
with open('mi_archivo.txt', 'r', encoding='UTF-8') as file:
    [print(line) for line in file.readlines()]
"""    
# Abre el archivo en modo de lectura y utiliza un bucle para leer y mostrar cada línea del archivo en la consola.
# Usa el método tell() para obtener la posición actual del cursor después de leer cada línea y muestra esta posición en la consola.
with open('mi_archivo.txt', 'r', encoding='UTF-8') as file:
    while True:
        line = file.readline()
        if not line:
            break
        posicion = file.tell()
        print(f"Posición del cursor después de leer la línea: {posicion}")
        print(line, end='') # Print simpre añade un salto de linea, lo omitimos con end=''
    
# Abre el archivo en modo de escritura ('w') y agrega una nueva línea de texto al final del archivo.
with open('mi_archivo.txt', 'w') as file:
    file.write('\nEsta es una sexta línea que sobeescribe contenido')

with open('mi_archivo.txt', 'a+') as file:
    file.write('\nEsta es una séptima línea')
    file.seek(0)
    print(file.read())
    # file.close()
# Cierra el archivo después de cada operación de lectura o escritura.
# No es necesario. with open ya se encarga de esto. Si nos queremos asegurar podríamos usar file.close()
