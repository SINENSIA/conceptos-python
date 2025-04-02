# Datos de entrada: Lista de temperaturas en grados Celsius
temperaturas_celsius = [20, -150, -197, -100, -146, -200, 0, 30, -208]

# Temperatura crítica del nitrógeno en grados Celsius
temperatura_critica_nitrogeno = -196

# Solo incluir temperaturas donde el nitrógeno permanece gaseoso (temperatura >= temperatura crítica)
temperaturas_gaseosas = [
    temperatura for temperatura in temperaturas_celsius if temperatura >= temperatura_critica_nitrogeno]

print(temperaturas_gaseosas)

temperaturas_liquidas = [
    temperatura for temperatura in temperaturas_celsius if temperatura < temperatura_critica_nitrogeno]

print(temperaturas_liquidas)
