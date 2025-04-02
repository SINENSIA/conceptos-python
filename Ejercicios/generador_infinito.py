def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# Prueba el generador infinito
fib = fibonacci()
for _ in range(25):  
    print(next(fib))
