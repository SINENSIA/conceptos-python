import os
import platform
import threading
from fastapi import FastAPI
import uvicorn

# =================== LÓGICA DE CONSOLA ===================

COLOR_ROJO = "\033[91m"
COLOR_VERDE = "\033[92m"
COLOR_AZUL = "\033[94m"
COLOR_AMARILLO = "\033[93m"
COLOR_NARANJA = "\033[38;5;208m"
COLOR_MORADO = "\033[95m"
RESET_COLOR = "\033[0m"

peliculas = {}


def limpiar_terminal():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def mostrar_menu():
    print("\n" + COLOR_ROJO + "Gestión de Películas" + RESET_COLOR)
    print('----------------------------')
    print(COLOR_VERDE + "1. Añadir película" + RESET_COLOR)
    print(COLOR_AMARILLO + "2. Eliminar película" + RESET_COLOR)
    print(COLOR_AZUL + "3. Mostrar películas" + RESET_COLOR)
    print(COLOR_MORADO + "4. Buscar película" + RESET_COLOR)
    print(COLOR_AMARILLO + "5. Salir" + RESET_COLOR)
    print('----------------------------')
    opcion = input(COLOR_VERDE + "Elige una opción: " + RESET_COLOR)
    print('----------------------------')
    return opcion


def añadir_pelicula(peliculas):
    limpiar_terminal()
    pelicula = input("Nombre de la película: ")
    if pelicula not in peliculas:
        director = input("Director: ")
        año = input("Año: ")
        presupuesto = input("Presupuesto (en millones): ")
        peliculas[pelicula] = {
            "director": director,
            "año": año,
            "presupuesto": presupuesto
        }
        print(COLOR_VERDE + f"Película {pelicula} añadida." + RESET_COLOR)
    else:
        print(COLOR_AMARILLO +
              f"La película {pelicula} ya existe." + RESET_COLOR)


def eliminar_pelicula(peliculas):
    limpiar_terminal()
    pelicula = input("Película a eliminar: ")
    if pelicula in peliculas:
        del peliculas[pelicula]
        print(COLOR_ROJO + f"Película {pelicula} eliminada." + RESET_COLOR)
    else:
        print(COLOR_AMARILLO +
              f"{pelicula} no está en la lista." + RESET_COLOR)


def mostrar_peliculas(peliculas):
    limpiar_terminal()
    if peliculas:
        print(COLOR_VERDE + "Listado de películas:" + RESET_COLOR)
        for nombre, datos in peliculas.items():
            print(
                f"{nombre} - Dir: {datos['director']}, Año: {datos['año']}, Presupuesto: {datos['presupuesto']}M")
    else:
        print(COLOR_AMARILLO + "No hay películas registradas." + RESET_COLOR)


def buscar_pelicula(peliculas):
    limpiar_terminal()
    termino = input("Buscar por nombre: ").lower()
    for nombre, datos in peliculas.items():
        if termino in nombre.lower():
            print(
                f"Encontrada: {nombre} - Dir: {datos['director']}, Año: {datos['año']}, Presupuesto: {datos['presupuesto']}M")
            return
    print(COLOR_AMARILLO + "No se encontró la película." + RESET_COLOR)

# =================== FASTAPI EN THREAD ===================


app = FastAPI(title="API de Películas")


@app.get("/peliculas")
def obtener_peliculas():
    return peliculas


def lanzar_api():
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="error")

# =================== MAIN ===================


def main():
    threading.Thread(target=lanzar_api, daemon=True).start()
    limpiar_terminal()
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
            print(COLOR_ROJO + "Saliendo..." + RESET_COLOR)
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    print(os.getcwd())
# main()
