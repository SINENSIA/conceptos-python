#!/usr/bin/python
""" Probar identación en Python."""
def indentacion():
    """ Probar identación en Python. """
    a = 1
    if  a == 1:
        print ( "A es 1"  )
        print("Test A es 1")
    else:
        print("A no es 1")
        print("Test a no es 1")

print("Esto siempre se imprime")

if __name__ == "__main__":
    indentacion()