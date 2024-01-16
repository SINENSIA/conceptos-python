from mensajes import messageFormatter
from mensajes import animateText
from mensajes import loadingBar
import time

print(messageFormatter("Error: Este mensaje es de error", "error"))
print()
print(messageFormatter("Éxito: Ete mensaje es de éxito", "success"))
print()
print(messageFormatter("Advertencia: Este mensaje es una advertencia", "warning"))
print()
print(messageFormatter("Información: Este mensaje es informativo", "info"))
print()
print("Este mensaje es normal")

# Ejemplo de uso
animateText("Escribiendo texto en tiempo real...", velocidad=0.1)

# Simulando un bucle de progreso

for i in range(101):
    print(loadingBar(i), end='\r', flush=True)
    time.sleep(0.1)  # Ajusta el tiempo de espera para simular el progreso

print("\nProgreso completado!")

     



   

