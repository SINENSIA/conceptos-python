def filtrar_divisibles(numeros, divisor):
    for numero in numeros:
        if numero % divisor == 0:
            yield numero


# Prueba el generador
numeros = [10, 15, 20, 27, 31, 35]
for divisible in filtrar_divisibles(numeros, 5):
    print(divisible)
