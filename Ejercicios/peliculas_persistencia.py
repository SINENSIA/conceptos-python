import os
import platform
import re
import json
import requests
from dotenv import load_dotenv

load_dotenv()


# ANSI para colores
COLOR_ROJO = "\033[91m"
COLOR_VERDE = "\033[92m"
COLOR_AZUL = "\033[94m"
COLOR_AMARILLO = "\033[93m"
COLOR_NARANJA = "\033[38;5;208m"  # naranja
COLOR_MORADO = "\033[95m"         # C morado claro
RESETEAR_COLOR = "\033[0m"

FICHERO_JSON = "resultado.json"


def limpiar_terminal():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def sincronizar_peliculas(peliculas):
    """
    Permite sincronizar las películas desde la API.
    Incluye confirmación del usuario y la posibilidad de cambiar la cadena de búsqueda.
    """
    limpiar_terminal()
    print(COLOR_AZUL + "Sincronización de películas con la API" + RESETEAR_COLOR)
    print('----------------------------')

    confirmacion = input(
        COLOR_AMARILLO + "¿Estás seguro de que deseas sincronizar las películas con la API? Esto actualizará los datos actuales. (s/n): " + RESETEAR_COLOR)
    if confirmacion.lower() != 's':
        print(COLOR_VERDE + "Sincronización cancelada." + RESETEAR_COLOR)
        return peliculas

    nueva_busqueda = input(
        COLOR_VERDE + "Introduce la cadena de búsqueda (presiona Enter para usar 'Avatar'): " + RESETEAR_COLOR).strip()
    busqueda = nueva_busqueda if nueva_busqueda else "Avatar"

    ombd_url = os.getenv("OMDB_URL")
    apikey = os.getenv("OMDB_API_KEY")
    url = f"{ombd_url}?apikey={apikey}&s={busqueda}"

    try:
        #  solicitud a la API
        print(
            COLOR_AZUL + f"Sincronizando con la búsqueda: '{busqueda}'..." + RESETEAR_COLOR)
        response = requests.get(url)
        response.raise_for_status()  # xcepción si la respuesta tiene un error HTTP

        datos = response.json()

        if "Search" not in datos:
            print(
                COLOR_ROJO + f"No se encontraron resultados para la búsqueda: '{busqueda}'." + RESETEAR_COLOR)
            return peliculas

        # Convertir los datos
        nuevas_peliculas = {pelicula["Title"]: {
            "Year": pelicula["Year"], "imdbID": pelicula["imdbID"]} for pelicula in datos["Search"]}

        # Fusionar l
        peliculas_actualizadas = {**peliculas, **nuevas_peliculas}

        guardar_datos(peliculas_actualizadas)
        print(COLOR_VERDE +
              f"Películas sincronizadas exitosamente con la búsqueda '{busqueda}'." + RESETEAR_COLOR)

        # Dpículas actualizadas para sincronizarlas en memoria
        return peliculas_actualizadas

    except requests.RequestException as e:
        print(COLOR_ROJO +
              f"Error al conectar con la API: {e}" + RESETEAR_COLOR)
    except Exception as e:
        print(COLOR_ROJO + f"Error inesperado: {e}" + RESETEAR_COLOR)

    return cargar_datos()


def cargar_datos():
    """Carga las películas desde un archivo JSON."""
    if os.path.exists(FICHERO_JSON):
        with open(FICHERO_JSON, "r") as archivo:
            try:
                datos = json.load(archivo)
                if isinstance(datos, dict):
                    return datos
                else:
                    print(
                        COLOR_ROJO + "El formato del archivo no es válido. Se esperaba un diccionario." + RESETEAR_COLOR)
                    return {}
            except json.JSONDecodeError:
                print(
                    COLOR_ROJO + "Error al leer el archivo JSON. Asegúrate de que tiene el formato correcto." + RESETEAR_COLOR)
                return {}
    else:
        print(COLOR_ROJO + "No se encuentra el fichero JSON. Se inicializará una lista vacía." + RESETEAR_COLOR)
    return {}


def guardar_datos(peliculas):
    """Guarda las películas en un archivo JSON."""
    with open(FICHERO_JSON, "w") as archivo:
        json.dump(peliculas, archivo, indent=4)


def mostrar_menu():
    print("\n" + COLOR_ROJO + "Gestión de Películas" + RESETEAR_COLOR)
    print('----------------------------')
    print(COLOR_VERDE + "1. Añadir película" + RESETEAR_COLOR)
    print(COLOR_AMARILLO + "2. Eliminar película" + RESETEAR_COLOR)
    print(COLOR_AZUL + "3. Mostrar películas" + RESETEAR_COLOR)
    print(COLOR_MORADO + "4. Buscar película" + RESETEAR_COLOR)
    print(COLOR_NARANJA + "5. Modificar película" + RESETEAR_COLOR)
    print(COLOR_AZUL + "6. Sincronizar películas desde la API" + RESETEAR_COLOR)
    print(COLOR_ROJO + "7. Salir" + RESETEAR_COLOR)
    print('----------------------------')
    opcion = input(COLOR_VERDE + "Elige una opción: " + RESETEAR_COLOR)
    print('----------------------------')
    return opcion if validar(opcion) else None


def añadir_pelicula(peliculas):
    limpiar_terminal()
    peliculas = cargar_datos()

    print('----------------------------')
    titulo = input(
        COLOR_VERDE + "Nombre de la película a añadir: " + RESETEAR_COLOR).strip()

    if titulo not in peliculas:
        año = input("Año de lanzamiento: ")
        imdbID = input("IMDb ID: ")

        peliculas[titulo] = {
            "Year": año,
            "imdbID": imdbID
        }
        guardar_datos(peliculas)
        print(COLOR_VERDE + f"Película '{titulo}' añadida." + RESETEAR_COLOR)
    else:
        print(COLOR_AMARILLO +
              f"La película '{titulo}' ya está en la lista." + RESETEAR_COLOR)


def eliminar_pelicula(peliculas):
    limpiar_terminal()
    peliculas = cargar_datos()

    if verificar_diccionario_vacio(peliculas):
        return

    print('----------------------------')
    print("Películas disponibles:")
    peliculas_numeradas = list(peliculas.keys())
    for i, nombre in enumerate(peliculas_numeradas, start=1):
        print(f"{i}. {nombre}")

    seleccion = input(
        COLOR_VERDE + "Introduce el número de la película a eliminar: " + RESETEAR_COLOR)
    if not seleccion.isdigit() or not (1 <= int(seleccion) <= len(peliculas_numeradas)):
        print(COLOR_ROJO + "Selección inválida." + RESETEAR_COLOR)
        return

    pelicula_a_eliminar = peliculas_numeradas[int(seleccion) - 1]
    confirmacion = input(
        COLOR_AMARILLO + f"¿Eliminar '{pelicula_a_eliminar}'? (s/n): " + RESETEAR_COLOR)
    if confirmacion.lower() == 's':
        peliculas.pop(pelicula_a_eliminar)
        guardar_datos(peliculas)
        print(COLOR_ROJO +
              f"Película '{pelicula_a_eliminar}' eliminada." + RESETEAR_COLOR)


def mostrar_peliculas(peliculas):
    limpiar_terminal()
    peliculas = cargar_datos()

    if verificar_diccionario_vacio(peliculas):
        return

    print("\n" + COLOR_VERDE + "Lista de Películas:" + RESETEAR_COLOR)
    for titulo, detalles in peliculas.items():
        print(
            f"{COLOR_AZUL}{titulo}{RESETEAR_COLOR} - Año: {detalles['Year']}, IMDb ID: {detalles['imdbID']}")


def buscar_pelicula(peliculas):
    limpiar_terminal()
    peliculas = cargar_datos()

    if verificar_diccionario_vacio(peliculas):
        return

    termino = input(
        COLOR_VERDE + "Introduce el nombre o fragmento a buscar: " + RESETEAR_COLOR).strip()
    if not validar(termino):
        print(COLOR_ROJO + "Entrada inválida." + RESETEAR_COLOR)
        return

    pattern = re.compile(re.escape(termino), re.IGNORECASE)
    encontrada = False

    for nombre, detalles in peliculas.items():
        if pattern.search(nombre):
            print(
                f"Encontrada: {nombre} - Año: {detalles['Year']}, IMDb ID: {detalles['imdbID']}")
            encontrada = True

    if not encontrada:
        print(COLOR_AMARILLO +
              f"No se encontraron coincidencias con '{termino}'." + RESETEAR_COLOR)


def modificar_pelicula(peliculas):
    limpiar_terminal()
    if verificar_diccionario_vacio(peliculas):
        return

    nombre = input(
        COLOR_VERDE + "Nombre de la película a modificar: " + RESETEAR_COLOR).strip()
    if nombre in peliculas:
        print("Introduce los nuevos datos (deja en blanco para no modificar):")
        año = input(
            f"Año actual: {peliculas[nombre]['Year']} - Nuevo Año: ").strip() or peliculas[nombre]['Year']
        imdbID = input(
            f"IMDb ID actual: {peliculas[nombre]['imdbID']} - Nuevo IMDb ID: ").strip() or peliculas[nombre]['imdbID']
        peliculas[nombre] = {"Year": año, "imdbID": imdbID}
        guardar_datos(peliculas)
        print(COLOR_VERDE +
              f"Película '{nombre}' modificada." + RESETEAR_COLOR)
    else:
        print(COLOR_ROJO + "Película no encontrada." + RESETEAR_COLOR)


def validar(input):
    return bool(re.match(r'^[A-Za-z0-9\s]+$', input))


def verificar_diccionario_vacio(peliculas):
    if not peliculas:
        print(COLOR_ROJO + "No hay películas en la lista. Agrega películas primero." + RESETEAR_COLOR)
        return True
    return False


def main():
    limpiar_terminal()
    peliculas = cargar_datos()

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
        elif opcion == "6":
            sincronizar_peliculas(peliculas)
        elif opcion == "7":
            print(COLOR_ROJO + "Saliendo del programa..." + RESETEAR_COLOR)
            break
        else:
            print(COLOR_ROJO + "Opción no válida." + RESETEAR_COLOR)


if __name__ == "__main__":
    main()
