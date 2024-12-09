
try:
    # Intenta ejecutar este código
    resultado = 10 / 0
except:
    # Ejecuta este código si hay una división entre cero
    print("¡No se puede dividir por cero!")

try:
    # Intenta ejecutar este código
    resultado = 10 / 0
except ZeroDivisionError:
    # Ejecuta este código si hay una división entre cero
    print("¡No se puede dividir por cero!")

try:
    resultado = 10 / 2
except ZeroDivisionError:
    print("¡No se puede dividir por cero!")
else:
    print("La división fue exitosa. Resultado:", resultado)

try:
    archivo = open("ejemplo.txt")
    resultado = archivo.read()
except FileNotFoundError:
    print("El archivo no fue encontrado.")
    # archivo = None # para que el bloque finally no de un error si archivo no existe
else:
    print("El archivo se leyó correctamente.")
finally:
    print("Cerrando archivo.")
    try:
        archivo.close()
    except NameError:
        print('No puedo cerrar un archivo que no existe')
