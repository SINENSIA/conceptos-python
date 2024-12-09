from termometro import Termometro
# Ejemplo de uso:
# Crear una instancia de Termometro con temperatura inicial de 25 grados Celsius
termometro = Termometro(25, 'celsius')

# Imprimir la temperatura en diferentes escalas
print(f"Temperatura en Celsius: {termometro.celsius} °C")  # Debería ser 25 °C
# Debería ser 77 °F
print(f"Temperatura en Fahrenheit: {termometro.fahrenheit} °F")
print(f"Temperatura en Kelvin: {termometro.kelvin} K")  # Debería ser 298.15 K

# Cambiar la temperatura a 77 grados Fahrenheit
termometro.fahrenheit = 77

# Imprimir la temperatura actualizada en todas las escalas
# Debería ser cerca de 25 °C
print(f"Temperatura actualizada en Celsius: {termometro.celsius} °C")
# Debería ser 77 °F
print(f"Temperatura actualizada en Fahrenheit: {termometro.fahrenheit} °F")
print(f"Temperatura actualizada en Kelvin: {termometro.kelvin} K")

print(termometro.set_testing(7))
print(termometro.testing)
