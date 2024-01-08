def switch(case):
    return {
        'caso1': 'Este es el caso 1',
        'caso2': 'Este es el caso 2',
        'caso3': 'Este es el caso 3',
    }.get(case, 'Caso no encontrado')  # 'Caso no encontrado' es el default

# Uso del 'switch'
resultado = switch('caso2')
print(resultado)

# También podemos llamar funciones
# Definir funciones
def funcion_caso1():
    return "Resultado del caso 1"

def funcion_caso2():
    return "Resultado del caso 2"

def funcion_caso3():
    return "Resultado del caso 3"

# Diccionario que simula el switch
def switch(caso):
    casos = {
        'caso1': funcion_caso1,
        'caso2': funcion_caso2,
        'caso3': funcion_caso3,
    }
    # Obtener la función correspondiente al caso y llamarla
    # Si el caso no existe, devuelve 'Caso no encontrado'
    funcion = casos.get(caso, lambda: "Caso no encontrado")
    return funcion()

# Llamada de ejemplo
resultado = switch('caso2')
print(resultado)