import os
import platform
import re
# ANSI para colores
COLOR_ROJO = "\033[91m"
COLOR_VERDE = "\033[92m"
COLOR_AZUL = "\033[94m"
COLOR_AMARILLO = "\033[93m"
COLOR_NARANJA = "\033[38;5;208m"  # naranja
COLOR_MORADO = "\033[95m"         # C morado claro
RESETEAR_COLOR = "\033[0m"


def limpiar_terminal():
    """
    Limpia la terminal de la consola dependiendo del sistema operativo.
    """
    if platform.system() == "Windows":
        os.system('cls')  # caso Win
    else:
        os.system('clear')  # caso Linux y macOS


def mostrar_menu():
    """
    Se encarga de mostrar el menú de opciones en la consola y devuelve la opción seleccionada.

    Returns:
        str: La opción elegida por el cliente.
    """
    print("\n" + COLOR_ROJO + "Gestión de Películas" + RESETEAR_COLOR)
    print('----------------------------')
    print(COLOR_VERDE + "1. Añadir película" + RESETEAR_COLOR)
    print(COLOR_AMARILLO + "2. Eliminar película" + RESETEAR_COLOR)
    print(COLOR_AZUL + "3. Mostrar películas" + RESETEAR_COLOR)
    print(COLOR_MORADO + "4. Buscar película" + RESETEAR_COLOR)
    print(COLOR_AMARILLO + "5. Modificar película" + RESETEAR_COLOR)
    print(COLOR_NARANJA + "6. Salir" + RESETEAR_COLOR)
    print('----------------------------')
    opcion = input(COLOR_VERDE + "Elige una opción: " + RESETEAR_COLOR)
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
    pelicula = input(
        COLOR_VERDE + "Nombre de la película a añadir: " + RESETEAR_COLOR)

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
        print(COLOR_VERDE + "Película " + COLOR_AZUL + pelicula +
              RESETEAR_COLOR + COLOR_VERDE + " añadida." + RESETEAR_COLOR)
    else:
        limpiar_terminal()
        print('----------------------------')
        print(COLOR_AMARILLO + "La película " + COLOR_AZUL + pelicula +
              RESETEAR_COLOR + COLOR_VERDE + " ya está en la lista." + RESETEAR_COLOR)
    print('----------------------------')


def eliminar_pelicula(peliculas):
    """
    Elimina una película de la lista si se encuentra en ella.

    Args:
        peliculas (dict): Diccionario de películas con sus detalles.
    """
    limpiar_terminal()
    if verificar_diccionario_vacio(peliculas):
        return
    print('----------------------------')
    print("Películas disponibles:")

    # Mostrar las películas con numeración
    peliculas_numeradas = list(peliculas.keys())
    for i, nombre in enumerate(peliculas_numeradas, start=1):
        print(f"{i}. {nombre}")

    print('----------------------------')
    seleccion = input(
        COLOR_VERDE + "Introduce el número de la película a eliminar: " + RESETEAR_COLOR)

    # Validar entrada
    if not seleccion.isdigit() or not (1 <= int(seleccion) <= len(peliculas_numeradas)):
        print(COLOR_ROJO + "Selección inválida. Por favor, introduce un número válido." + RESETEAR_COLOR)
        return

    # Obtener la película seleccionada
    indice = int(seleccion) - 1
    pelicula_a_eliminar = peliculas_numeradas[indice]

    # Confirmar eliminación
    confirmacion = input(
        COLOR_AMARILLO + f"¿Estás seguro de que quieres eliminar '{pelicula_a_eliminar}'? (s/n): " + RESETEAR_COLOR)
    if confirmacion.lower() == 's':
        peliculas.pop(pelicula_a_eliminar)
        limpiar_terminal()
        print('----------------------------')
        print(f"{COLOR_AMARILLO}Película {COLOR_AZUL}{pelicula_a_eliminar}{RESETEAR_COLOR}{COLOR_ROJO} eliminada.{RESETEAR_COLOR}")
    else:
        print(COLOR_VERDE + "Operación cancelada. Ninguna película ha sido eliminada." + RESETEAR_COLOR)
    print('----------------------------')


def mostrar_peliculas(peliculas):
    """
    Muestra todas las películas en la lista.

    Args:
        peliculas (list): La lista de películas.
    """
    limpiar_terminal()
    if verificar_diccionario_vacio(peliculas):
        return
    print('----------------------------')
    if peliculas:
        print("\n" + COLOR_VERDE + "Lista de Películas:" + RESETEAR_COLOR)

        for nombre, detalles in peliculas.items():
            print(
                f"{nombre} - Director: {detalles['director']}, Año: {detalles['año']}, Presupuesto: {detalles['presupuesto']} millones")
    else:
        limpiar_terminal()
        print('----------------------------')
        print(COLOR_AMARILLO + "No hay películas en la lista." + RESETEAR_COLOR)
    print('----------------------------')


def buscar_pelicula(peliculas):
    """
    Busca una película por nombre en la lista y muestra si está o no en la lista.

    Args:
        peliculas (list): La lista de películas.
    """
    limpiar_terminal()
    if verificar_diccionario_vacio(peliculas):
        return

    print('----------------------------')
    pelicula = input(
        COLOR_VERDE + "Nombre o fragmento de la película a buscar: " + RESETEAR_COLOR)

    if not validar(pelicula):
        print(COLOR_ROJO + "La entrada contiene caracteres no válidos. "
              "Esta actividad será registrada para su protección." + RESETEAR_COLOR)
        return

    # patrón de búsqueda para coincidir parcialmente, ignorando mayúsculas
    pattern = re.compile(re.escape(pelicula), re.IGNORECASE)
    encontrada = False  # Bandera para verificar si se encontró al menos una coincidencia

    for nombre, detalles in peliculas.items():
        if pattern.search(nombre):  # Buscar coincidencias parciales
            print(f"Encontrada: {nombre} - Director: {detalles['director']}, Año: {detalles['año']}, "
                  f"Presupuesto: {detalles['presupuesto']} millones")
            encontrada = True
        # buscar en las propiedades
        for clave, valor in detalles.items():
            # convertimos `valor` a string para buscar patrones
            if pattern.search(str(valor)):
                print(f"Coincidencia en {clave.capitalize()}: {nombre} - Director: {detalles['director']}, Año: {detalles['año']}, "
                      f"Presupuesto: {detalles['presupuesto']} millones")
                encontrada = True

    if not encontrada:
        print('----------------------------')
        print(COLOR_AMARILLO + "No se encontraron películas con el término " + COLOR_AZUL +
              pelicula + RESETEAR_COLOR + COLOR_AMARILLO + "." + RESETEAR_COLOR)
        print('----------------------------')


def modificar_pelicula(peliculas):
    """
    Modifica una película de la lista si se encuentra en ella.

    Args:
        peliculas (_type_): _description_
    """
    # si esta vacio informamos
    if verificar_diccionario_vacio(peliculas):
        return

    nombre = input("Nombre de la película a modificar: ").strip()
    if nombre in peliculas:
        print("Introduce los nuevos datos (deja en blanco para no modificar):")
        director = input(
            f"Nuevo director (Actual: {peliculas[nombre]['director']}): ") or peliculas[nombre]['director']
        año = input(
            f"Nuevo año (Actual: {peliculas[nombre]['año']}): ") or peliculas[nombre]['año']
        presupuesto = input(
            f"Nuevo presupuesto (Actual: {peliculas[nombre]['presupuesto']}): ") or peliculas[nombre]['presupuesto']
        peliculas[nombre] = {"director": director,
                             "año": año, "presupuesto": presupuesto}
        print("Película modificada.")
    else:
        print("La película no se encuentra en la lista.")


def validar(input):
    """ Usamos una expresión regular para comprobar que no se introducen carateres no esperados"""
    validacion = re.compile(r'^[A-Za-z0-9\s]+$')

    if validacion.match(input):
        return True
    else:
        return False


def verificar_diccionario_vacio(peliculas):
    """
    Verifica si el diccionario de películas está vacío.

    Args:
        peliculas (dict): Diccionario de películas.

    Returns:
        bool: True si está vacío, False en caso contrario.
    """
    if not peliculas:
        print(COLOR_ROJO + "No hay películas en la lista. Agrega películas primero." + RESETEAR_COLOR)
        return True
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
            print(COLOR_ROJO + "Saliendo del programa..." + RESETEAR_COLOR)
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 5.")
    print('----------------------------')


if __name__ == "__main__":
    main()
