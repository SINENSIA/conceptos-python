def numeros_infinito():
    numero = 1
    while True:
        yield numero
        numero += 1


class Limitar:
    def __init__(self, generador, maximo):
        self.generador = generador
        self.maximo = maximo
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.contador >= self.maximo:
            raise StopIteration
        self.contador += 1
        return next(self.generador)


# Prueba el iterador y el generador
gen_infinito = numeros_infinito()
limite = Limitar(gen_infinito, 10)
for numero in limite:
    print(numero)
