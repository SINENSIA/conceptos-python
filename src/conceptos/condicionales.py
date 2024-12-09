# uso simple
nota = 6
if nota >= 5:
    print("Aprobado.")

# uso if else
if nota >= 5:
    print("Aprobado.")
else:
    print("Suspenso.")

# use elif
if nota >= 9:
    print("Sobresaliente.")
elif nota >= 7:
    print("Notable.")
elif nota >= 6:
    print("Bien")
elif nota >= 5:
    print('Suficiente.')
elif nota <= 2:
    print('Muy deficiente.')
else:
    print("Suspenso.")

# Condiciones anidadas
edad = 20
carnet = True
if edad >= 18:
    if carnet:
        print("Puedes conducir.")
    else:
        print("Necesitas una licencia para conducir.")
else:
    print("No eres mayor de edad para conducir.")

# operadores lógicos

if edad >= 18 and carnet:
    print("Puedes conducir.")
else:
    print("No puedes conducir.")

# operador "ternario"
edad = 18
mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(mensaje)


'''
    Java tiene un sistema de tipos estricto, y las condiciones deben ser expresiones booleanas. 
    Intentar usar valores no booleanos en una condición resultará en un error de compilación.

    Python es más flexible y permite el uso de varios tipos de datos en expresiones condicionales. 
    Valores como 0, None, listas vacías ([]), 
    tuplas vacías (()), diccionarios vacíos ({}), 
    y la cadena vacía ('') son considerados False cuando se evalúan en un contexto booleano. 
    Otros valores se consideran True.
    '''

# En Python, el valor 0 es considerado False cuando se evalúa en un contexto booleano.
# Esto significa que cualquier condicional que solo evalúe un número se comportará de manera diferente si el número es 0 o cualquier otro valor.
numero = 0
if numero:
    print(numero)
    # Este bloque NO se ejecuta porque 0 se considera False en Python

# No sólo 0, sino también otras estructuras como {} o []
mi_array = []
if mi_array:
    print(mi_array)
    # Este bloque NO se ejecuta porque 0 se considera False en Python

mi_tupla = ()
if mi_tupla:
    print(mi_tupla)

'''
En java:
int numero = 0;
if (numero) { // Error de compilación "numero" no es boolean
    
}
if (numero == 0) { 
    print(numero)
    # Este bloque se ejecuta porque numero es igual a 0
}
'''

x = 0

# Comparaciones lógicas múltiples,observa este posible error:
# Queremos verificar si un número x es menor que 10 o si es mayor que 20 y al mismo tiempo es un número par.
if x < 10 or x > 20 and x % 2 == 0:
    print("x es menor que 10 o es mayor que 20 y par")


# Comparaciones múltiples: Usar and y or correctamente puede ser confuso. Ejemplo erróneo y correcto:
x = 27
# Incorrecto
if 0 < x < 20 or 30 < x < 50:
    print("x está en un rango permitido")

# Correcto
if (0 < x < 20) or (30 < x < 50):
    print("x está en un rango permitido")

# Comparar dicetmanete con None se hace con "is"
if x is None:
    print("x no tiene valor")

# Operador ternario
x = 13
mensaje1 = "x es igual a 12"
mensaje2 = "x no es igual a 12"
print(mensaje1 if (x == 12) else mensaje2)


x = True
if x is True:
    print("x es exactamente True")


x = 1  # Este es un número, pero evalúa como verdadero.
if x == True:
    print("x es verdadero en un sentido lógico")
x = 0
if x == True:
    print("x es falso en un sentido lógico")
