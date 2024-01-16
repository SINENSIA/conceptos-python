# Datos de entrada: Lista de temperaturas en grados Celsius
temperaturas_celsius = [20, -150, -148, -100, -146, -200, 0, 30, -147]

# Temperatura crítica del nitrógeno en grados Celsius
temperatura_critica_nitrogeno = -147

# Utilizar una lista por comprensión para filtrar temperaturas
# Solo incluir temperaturas donde el nitrógeno permanece gaseoso (temperatura >= temperatura crítica)
temperaturas_gaseosas = [temp for temp in temperaturas_celsius if temp >= temperatura_critica_nitrogeno]

print(temperaturas_gaseosas)