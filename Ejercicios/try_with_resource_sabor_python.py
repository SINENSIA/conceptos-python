class RecursoControlado:
    def __enter__(self):
        print("[ENTER] Abriendo recurso...")
        self.recurso = open("demo.txt", "w")
        return self.recurso  # el objeto retornado se asigna al alias en 'as'

    def __exit__(self, exc_type, exc_value, traceback):
        print("[EXIT] Cerrando recurso...")
        if self.recurso:
            self.recurso.close()
        if exc_type:
            print(f"[ERROR] Se ha producido una excepción: {exc_value}")
        # Devuelve False para propagar la excepción si la hubo
        return False


# Uso normal (sin excepción)
print("--- Caso 1: sin excepción ---")
with RecursoControlado() as archivo:
    archivo.write("Esto se escribe sin errores.\n")

# Uso con excepción intencionada
print("\n--- Caso 2: con excepción ---")
try:
    with RecursoControlado() as archivo:
        archivo.write("Esto lanzará una excepción...\n")
        raise ValueError("Error de prueba dentro del with")
except Exception as e:
    print(f"[MAIN] Excepción capturada: {e}")
