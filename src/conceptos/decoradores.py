def mi_decorador(func):
    def envoltura():
        print("Esto se ejecutará antes de la función.")
        func()
        print("Esto después de la función.")
    return envoltura


@mi_decorador
def decir_verdades():
    print("Python mola!")


decir_verdades()
