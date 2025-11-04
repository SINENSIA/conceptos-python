# List of temperatures in Celsius
temperaturas_celsius = [-200, -150, -100, -148, -145, 0, 25]

# Usando list comprehension para filtrar las temperaturas por debajo
nitrogen_gaseous_temperatures = [ temp for temp in temperaturas_celsius if temp >= -196 ]

print(nitrogen_gaseous_temperatures)