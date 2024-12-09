"""
    Como crear un archivo en python
"""
from pathlib import Path
import os
import time
import shutil

# Obtener directorio actual de trabajo
cwd = os.getcwd()
print(cwd)

# cRear nun directorio
if not os.path.exists('prueba'):
    os.mkdir('prueba')

# Cambiar directorio actual de trabajo
os.chdir('prueba')

with open('nuevo_archivo.txt', 'w', encoding='UTF-8') as archivo:
    archivo.write("Contenido del nuevo archivo con write.")

with open('nuevo_archivo.txt', 'a', encoding='UTF-8') as archivo:
    archivo.write("\nAñadiendo contenido 1 al archivo.")
    archivo.write("\nAñadiendo contenido 2 al archivo.")
    archivo.write("\nAñadiendo contenido 3 al archivo.")

# Ejemplo iterando por un list de lineas
lineas = ["Añadiendo contenido 4 al archivo.\n",
          "Añadiendo contenido 5 al archivo.\n", "Añadiendo contenido 6 al archivo.\n"]
with open('nuevo_archivo.txt', 'w', encoding='UTF-8') as file:
    for linea in lineas:
        file.write(linea)

# Uso con writelines (list)
lineas = ["Primera línea\n", "Segunda línea\n", "Tercera línea\n"]
with open('nuevo_archivo.txt', 'w', encoding='UTF-8') as file:
    file.writelines(lineas)

# Usando print y la redirección a archivo nos podemos beneficiar de que print
# siempre imprime el caracter de nueva línea
with open('nuevo_archivo.txt', 'w', encoding='UTF-8') as file:
    print("Primera línea con print", file=file)
    print("Segunda línea con print", file=file)

# Pero si no queremos sobreescribir el archivo usamos append
# Ejemplo básico
with open('ejemplo_append.txt', 'a', encoding='utf-8') as archivo:
    archivo.write("\nAñadiendo una nueva línea al archivo.")

# Append con bucle
datos = ["Dato 1", "Dato 2", "Dato 3"]
with open('ejemplo_append.txt', 'a', encoding='utf-8') as archivo:
    for dato in datos:
        archivo.write(f"\n{dato}")

# Lectura de archivos con read()
# Lee todo el archivo o el número especificado de caracteres.
with open('nuevo_archivo.txt', 'r', encoding='UTF-8') as file:
    contenido = file.read()
print('---- contenido con read ------')
print(contenido)

# Lee todo el archivo o el número especificado de caracteres, en este caso los 10 primeros.
with open('nuevo_archivo.txt', 'r', encoding='UTF-8') as file:
    contenido = file.read(10)
print('---- contenido con read 10  ------')
# print(contenido)

# Lee la siguiente línea del archivo.
"""
print('---- contenido con readline ------')  
contador = 0  
with open('nuevo_archivo.txt', 'r', encoding='UTF-8') as file:
    while True:
       linea = file.readline()
       if not linea:
           break
       
       print(f'---- linea {contador} ------')   
       contador += 1 
       print(linea.strip())

## Lee todas las líneas del archivo y las devuelve como una lista.
with open('nuevo_archivo.txt', 'r', encoding='UTF-8') as file:
    lineas = file.readlines()
print(lineas)
"""

# readlines() no permite especificar rango pero es fáci con lists
with open('nuevo_archivo.txt', 'r', encoding='UTF-8') as file:
    lineas = file.readlines()
# Las listas en Python tienen índice basado en cero
lineas_seleccionadas = lineas[2:7]
# print(lineas_seleccionadas)

# readline() leer un numero específico de lineas
lineas = []
with open('nuevo_archivo.txt', 'r', encoding='UTF-8') as file:
    for _ in range(5):
        linea = file.readline()
        if not linea:
            break
        lineas.append(linea)
# print(lineas)

# con enumerate
n = 10  # Número de líneas a leer
lineas = []
with open('nuevo_archivo.txt', 'r', encoding='UTF-8') as file:
    for i, linea in enumerate(file):
        if i >= n:
            break
        lineas.append(linea)
# print(lineas)

# Manejo de excepciones
"""
try:
    with open('archivo_inexistente.txt', 'r') as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print('El archivo no existe')       
     
"""
# Seek()
with open('nuevo_archivo.txt', 'r+', encoding='UTF-8') as archivo:
    archivo.seek(12)  # Mueve el cursor a la posición 10
    posicion = archivo.tell()  # Obtiene la posición actual del cursor
    print(f"Posición del cursor: {posicion}")
    archivo.write("##Texto en posición específica.##")
    # Vuelve a mover el cursor a la posición deseada para la lectura
    archivo.seek(0)
    contenido = archivo.read()
print('--- contenido ---')
print(contenido)


os.listdir('.')

size = os.path.getsize('nuevo_archivo.txt')
print(size)

mod_time = time.ctime(os.path.getmtime('nuevo_archivo.txt'))
print(mod_time)

c_time = time.ctime(os.path.getctime('nuevo_archivo.txt'))
print(c_time)

existe = os.path.exists('nuevo_archivo.txt')
print(existe)

# Es una buena práctica asegurarse que estmaos en el directorio correcto
# antes de relaizar operaciones destructivas
directorio_esperado = "D:\\ProyectosPython\\prueba"
if os.getcwd() == directorio_esperado:
    for root, dirs, files in os.walk('.'):
        for file in files:
            # os.path.join(root, file)) nos da la ruta relativa, si queremos la absoluta:
            print(os.path.abspath(os.path.join(root, file)))
            # Crea una ruta completa hacia el archivo y lo elimina
            os.remove(os.path.join(root, file))
        for dir in dirs:
            os.rmdir(os.path.join(root, dir))
    os.chdir('..')
    os.rmdir('prueba')
else:
    print("No se puede eliminar el directorio de trabajo, porque no es el esperado.")
    print("Cambia el directorio de trabajo al directorio esperado y vuelve a intentarlo.")
    print("Directorio esperado: ", directorio_esperado)
    print("Directorio actual: ", os.getcwd())

# Es una buena práctica asegurarse que estmaos en el directorio correcto
# antes de relaizar operaciones destructivas
directorio_esperado = "D:\\ProyectosPython\\prueba"
if os.getcwd() == directorio_esperado:
    shutil.rmtree(directorio_esperado)
else:
    print("No se puede eliminar el directorio de trabajo, porque no es el esperado.")
    print("Cambia el directorio de trabajo al directorio esperado y vuelve a intentarlo.")
    print("Directorio esperado: ", directorio_esperado)
    print("Directorio actual: ", os.getcwd())

shutil.copy('nuevo_archivo.txt', 'nuevo_archivo_destino.txt')
os.remove('nuevo_archivo_destino.txt')

shutil.copy2('nuevo_archivo.txt', 'nuevo_archivo_destino.txt')
os.remove('nuevo_archivo_destino.txt')


# shutil.copytree('test', 'test2')
# shutil.move('source.txt', 'destination_directory')
# shutil.rmtree('directory_path')
# shutil.make_archive('archive', 'zip', 'directory_path')
# shutil.unpack_archive('archive.zip', 'destination_directory')
total, used, free = shutil.disk_usage('/')
print(total, used, free)

# Ruta al archivo que deseas eliminar
archivo_a_eliminar = 'archivo.txt'

# Comprobar si el archivo existe y luego eliminarlo
if os.path.exists(archivo_a_eliminar):
    os.remove(archivo_a_eliminar)
    print(f"El archivo {archivo_a_eliminar} ha sido eliminado.")
else:
    print(f"El archivo {archivo_a_eliminar} no existe.")


archivo = Path('nuevo_archivo.txt')
size = archivo.stat().st_size

# Crear un Objeto Path:

p = Path('.')

# Unir Partes de Rutas:
nuevo_archivo = p / 'subdirectorio' / 'nuevo_archivo.txt'

# Verificar si un Archivo/Directorio Existe:
existe = p.exists()

# Verificar si es un Directorio o un Archivo:
es_directorio = p.is_dir()
es_archivo = p.is_file()
exit()
# Leer el Contenido de un Archivo:
contenido = Path('archivo.txt').read_text()

# Escribir en un Archivo:
Path('archivo.txt').write_text("Hola, mundo!")

# Trabajar con Directorios
# Listar Archivos en un Directorio:
archivos = [archivo for archivo in p.iterdir() if archivo.is_file()]

# Buscar Archivos con Patrones (Globbing):
jpg_files = list(p.glob('**/*.jpg'))

# Crear Nuevos Directorios:
(p / 'nuevo_directorio').mkdir(parents=True, exist_ok=True)

# Cambiar el Nombre o Mover Archivos/Directorios:
p.rename('nuevo_nombre')

# Eliminar Archivos:
Path('archivo_a_eliminar.txt').unlink()

# Eliminar Directorios Vacíos:
Path('directorio_vacio').rmdir()

# Obtener Propiedades del Archivo
# Obtener la Ruta Absoluta:
ruta_absoluta = p.resolve()

# Obtener Tamaño del Archivo:
tamano = Path('archivo.txt').stat().st_size

# Obtener Fecha de Modificación:
mod_time = Path('archivo.txt').stat().st_mtime

# Leer Archivo Binario:
data = Path('archivo.bin').read_bytes()

# Escribir en Archivo Binario:
Path('archivo.bin').write_bytes(data)
