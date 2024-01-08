"""
    Como crear un archivo en python
"""
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
    archivo.write("Contenido del nuevo archivo.")
    
with open('nuevo_archivo.txt', 'a', encoding='UTF-8') as archivo:
    archivo.write("\nAñadiendo contenido al archivo.")

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
print(total,used,free)

# Ruta al archivo que deseas eliminar
archivo_a_eliminar = 'archivo.txt'

# Comprobar si el archivo existe y luego eliminarlo
if os.path.exists(archivo_a_eliminar):
    os.remove(archivo_a_eliminar)
    print(f"El archivo {archivo_a_eliminar} ha sido eliminado.")
else:
    print(f"El archivo {archivo_a_eliminar} no existe.")


from pathlib import Path
archivo = Path('nuevo_archivo.txt')
size = archivo.stat().st_size

#Crear un Objeto Path:

from pathlib import Path
p = Path('.')

# Unir Partes de Rutas:
nuevo_archivo = p / 'subdirectorio' / 'nuevo_archivo.txt'

# Verificar si un Archivo/Directorio Existe:
existe = p.exists()

# Verificar si es un Directorio o un Archivo:
es_directorio = p.is_dir()
es_archivo = p.is_file()

# Leer el Contenido de un Archivo:
contenido = Path('archivo.txt').read_text()

#Escribir en un Archivo:
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