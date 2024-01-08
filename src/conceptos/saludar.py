#!/usr/bin/env python3

import argparse

def parseargs():
    """ Esta función parsea los argumentos de la línea de comandos.

    Returns:
        args: Los argumentos parseados.
    """
    parser = argparse.ArgumentParser(description='Un script para saludar.')
    parser.add_argument('--name', help='El nombre de la persona a saludar.')
    args = parser.parse_args()
    return args

def di_hola(nombre):
    """
    Función que imprime "Hola {nombre}!"
    """
    if not nombre:
        nombre = input("Dime tu nombre: ")
    return f"Hola, {nombre}!"

def main():
    """
    Función principal del script.
    """
    args = parseargs()
    saludo = di_hola(args.name)
    print(saludo)

if __name__ == "__main__":
    main()
