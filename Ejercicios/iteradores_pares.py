class Pares:
    def __init__(self, maximo):
        self.maximo = maximo
        self.actual = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.actual > self.maximo:
            raise StopIteration
        par = self.actual
        self.actual += 2
        return par


# Prueba el iterador
pares = Pares(10)
for numero in pares:
    print(numero)
