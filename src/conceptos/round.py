import math

# Definimos algunos números para practicar redondeo
numeros = [1.5, 2.3, 2.7, -1.5, -2.1, -2.9]

# Usando round()
print("Redondeo con round()")
for num in numeros:
    print(f"round({num}) =", round(num))

# Usando floor() - Redondea hacia abajo
print("\nRedondeo hacia abajo con floor()")
for num in numeros:
    print(f"floor({num}) =", math.floor(num))

# Usando ceil() - Redondea hacia arriba
print("\nRedondeo hacia arriba con ceil()")
for num in numeros:
    print(f"ceil({num}) =", math.ceil(num))

# Usando trunc() - Trunca los decimales, sin redondear, solo elimina la parte decimal
print("\nTruncamiento con trunc()")
for num in numeros:
    print(f"trunc({num}) =", math.trunc(num))
    
class Proveedor:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

    def __str__(self):
        return self.nombre + " " + self.apellidos

    def compra(self):
        # operación de compra
        pass

