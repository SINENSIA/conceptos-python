import os
import platform
import re
# Ejemplo de códigos ANSI para diferentes colores
COLOR_ROJO = "\033[91m"
COLOR_VERDE = "\033[92m"
COLOR_AZUL = "\033[94m"
COLOR_AMARILLO = "\033[93m"
COLOR_NARANJA = "\033[38;5;208m"  # Código ANSI para naranja
COLOR_MORADO = "\033[95m"         # Código ANSI para morado claro
RESET_COLOR = "\033[0m"  # Para resetear el color a su valor por defecto


def limpiar_terminal():
    """
    Limpia la terminal de la consola dependiendo del sistema operativo.
    """
    if platform.system() == "Windows":
        os.system('cls')  # Para Windows
    else:
        os.system('clear')  # Para Linux y macOS

def mostrar_menu():
    """
    Muestra el menú de opciones en la consola y devuelve la opción seleccionada por el usuario.
    
    Returns:
        str: La opción elegida por el usuario.
    """
    print("\n" + COLOR_ROJO + "Gestión de Películas" + RESET_COLOR)
    print('----------------------------')
    print(COLOR_VERDE + "1. Añadir película"  + RESET_COLOR)
    print(COLOR_AMARILLO + "2. Eliminar película"+ RESET_COLOR)
    print(COLOR_AZUL +"3. Mostrar películas"+ RESET_COLOR)
    print(COLOR_MORADO +"4. Buscar película"+ RESET_COLOR)
    print(COLOR_AMARILLO +"5. Modificar película"+ RESET_COLOR)
    print(COLOR_NARANJA +"6. Salir"+ RESET_COLOR)
    print('----------------------------')
    opcion = input(COLOR_VERDE + "Elige una opción: " + RESET_COLOR)
    print('----------------------------')
    if (validar(opcion)):
        return opcion
    else:
        print("La entrada contiene caracteres no válidos. Está actividad será registrada para su protección.")

def añadir_pelicula(peliculas):
    """
    Añade una nueva película a la lista si no está ya en ella.
    
    Args:
        peliculas (list): La lista de películas.
    """
    limpiar_terminal()
    print('----------------------------')
    pelicula = input(COLOR_VERDE + "Nombre de la película a añadir: "+ RESET_COLOR)
    
    if pelicula not in peliculas:
        
        director = input("Director de la película: ")
        año = input("Año de lanzamiento: ")
        presupuesto = input("Presupuesto (en millones): ")
        
        peliculas[pelicula] = {
            "director": director,
            "año": año,
            "presupuesto": presupuesto
        }
        print("Película añadida.")
        limpiar_terminal()
        print('----------------------------')
        print(COLOR_VERDE + "Película " + COLOR_AZUL + pelicula + RESET_COLOR + COLOR_VERDE +" añadida."+ RESET_COLOR)
    else:
        limpiar_terminal()
        print('----------------------------')
        print(COLOR_AMARILLO +"La película " + COLOR_AZUL + pelicula + RESET_COLOR + COLOR_VERDE +" ya está en la lista."+ RESET_COLOR)
    print('----------------------------')

def eliminar_pelicula(peliculas):
    """
    Elimina una película de la lista si se encuentra en ella.
    
    Args:
        peliculas (list): La lista de películas.
    """
    limpiar_terminal()
    print('----------------------------')
    pelicula = input(COLOR_VERDE + "Nombre de la película a eliminar: "+ RESET_COLOR)
    if pelicula in peliculas:
        peliculas.pop(pelicula)
        limpiar_terminal()
        print('----------------------------')
        print(f"{COLOR_AMARILLO} Película {COLOR_AZUL} pelicula  {RESET_COLOR}{COLOR_ROJO} eliminada.{RESET_COLOR}")
    else:
        limpiar_terminal()
        print('----------------------------')
        print(f"{COLOR_AMARILLO}La Película {COLOR_AZUL}{pelicula}{RESET_COLOR}{COLOR_AMARILLO} no se encuentra en la lista.{RESET_COLOR}")
    print('----------------------------')
    
def mostrar_peliculas(peliculas):
    """
    Muestra todas las películas en la lista.
    
    Args:
        peliculas (list): La lista de películas.
    """
    limpiar_terminal()
    print('----------------------------')
    if peliculas:
        print("\n" +  COLOR_VERDE + "Lista de Películas:" + RESET_COLOR)
        
        for nombre, detalles in peliculas.items():
            print(f"{nombre} - Director: {detalles['director']}, Año: {detalles['año']}, Presupuesto: {detalles['presupuesto']} millones")
    else:
        limpiar_terminal()
        print('----------------------------')
        print(COLOR_AMARILLO + "No hay películas en la lista." + RESET_COLOR)
    print('----------------------------')

def buscar_pelicula(peliculas):
    """
    Busca una película por nombre en la lista y muestra si está o no en la lista.
    
    Args:
        peliculas (list): La lista de películas.
    """
    limpiar_terminal()
    print('----------------------------')
    pelicula = input( COLOR_VERDE + "Nombre de la película a buscar: "+ RESET_COLOR)
    if validar(pelicula):
        pattern = re.compile(pelicula, re.IGNORECASE)
        for nombre, detalles in peliculas.items():
            if pattern.search(nombre):
                print(f"Encontrada: {nombre} - Director: {detalles['director']}, Año: {detalles['año']}, Presupuesto: {detalles['presupuesto']} millones")
                limpiar_terminal()
                print('----------------------------')
                print(COLOR_VERDE +"La Película " + COLOR_AZUL + pelicula + RESET_COLOR + COLOR_VERDE +" se ha encontrado en la lista."+ RESET_COLOR)
                break
    
            else:
                limpiar_terminal()
                print('----------------------------')
                print(COLOR_AMARILLO + "La película " + COLOR_AZUL + pelicula + RESET_COLOR + COLOR_AMARILLO + " no se encuentra" + RESET_COLOR)
                print('----------------------------')
    else:
        print("La entrada contiene caracteres no válidos. Está actividad será registrada para su protección.")
        limpiar_terminal()
        
def modificar_pelicula(peliculas):
    """
    Modifica una película de la lista si se encuentra en ella.

    Args:
        peliculas (_type_): _description_
    """
    nombre = input("Nombre de la película a modificar: ").strip()
    if nombre in peliculas:
        print("Introduce los nuevos datos (deja en blanco para no modificar):")
        director = input(f"Nuevo director (Actual: {peliculas[nombre]['director']}): ") or peliculas[nombre]['director']
        año = input(f"Nuevo año (Actual: {peliculas[nombre]['año']}): ") or peliculas[nombre]['año']
        presupuesto = input(f"Nuevo presupuesto (Actual: {peliculas[nombre]['presupuesto']}): ") or peliculas[nombre]['presupuesto']
        peliculas[nombre] = {"director": director, "año": año, "presupuesto": presupuesto}
        print("Película modificada.")
    else:
        print("La película no se encuentra en la lista.")
        
def validar(input):
    """ Usamos una expresión regular para comprobar que no se introcucen carateres no esperados"""
    validacion = re.compile(r'^[A-Za-z0-9\s]+$')

    if validacion.match(input):
        return True
    else:
        return False
        
def main():
    """
    Función principal que ejecuta el programa de gestión de películas.
    """
    limpiar_terminal()
    peliculas = {}
    
    while True:
        
        opcion = mostrar_menu()
        if opcion == "1":
            añadir_pelicula(peliculas)
        elif opcion == "2":
            eliminar_pelicula(peliculas)
        elif opcion == "3":
            mostrar_peliculas(peliculas)
        elif opcion == "4":
            buscar_pelicula(peliculas)
        elif opcion == "5":
            modificar_pelicula(peliculas)
        elif opcion == '6':
            print( COLOR_ROJO + "Saliendo del programa..." + RESET_COLOR)
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 5.")
    print('----------------------------')
    
if __name__ == "__main__":
    main()

