def cuadrados(maximo):
    for numero in range(1, maximo + 1):
        yield numero ** 2


# Prueba el generador
for cuadrado in cuadrados(5):
    print(cuadrado)
