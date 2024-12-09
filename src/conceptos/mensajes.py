import sys
import time
import os
from ipywidgets import IntProgress, HTML, VBox
from IPython.display import display

# Formatea el texto en cuatro estilos
def messageFormatter(texto, tipo):
    if tipo == 'info': 
        return '\033[44m' + ' ' + texto + ' ' + '\033[0m' 
    if tipo == 'warning': 
        return '\033[43m\033[31m' + ' ' + texto + ' ' + '\033[0m' 
    if tipo == 'error':
        return '\033[41m' + ' ' + texto + ' ' + '\033[0m' 
    if tipo == 'success': 
        return '\033[42m' + ' ' + texto + ' ' + '\033[0m' 
    
    return '\033[0m' + ' ' + texto + ' ' + '\033[0m'


def loadingBar(carga):
    maximo = 50  # Tamaño de la barra de progreso
    # Si 100 es a 50, carga será a x = carga*50/100
    carga = int(carga / 100 * maximo)
    barra = '\033[42m' + '█'  * carga + '\033[0m' + '-' * (maximo - carga)
    return f"[{barra}] {carga * 2}%"

def loadingBar_jupyter(total):
    progress = IntProgress(value=0, min=0, max=total)  # Barra de progreso
    label = HTML()  # Etiqueta de texto para mostrar el progreso
    box = VBox(children=[label, progress])
    display(box)
    
    for i in range(1, total + 1):
        progress.value = i
        label.value = f"{i}/{total} completado"
        time.sleep(0.1)  # Simula trabajo con un sleep

def animateText(texto, velocidad=0.1):
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(velocidad)
    print()


# Definimos __name__ como __main__  
if __name__ == "__main__":  
    
    if len(sys.argv) < 3:  # Comprueba si se pasaron menos de 2 argumentos adicionales.
        print(f"Uso: {os.path.basename(__file__)} texto tipo")
        print("Este script necesita al menos 2 argumentos para funcionar correctamente. EL primer argumento es el texto a destacar, el segundo es el tipo (info, error, warning, success)")
    else:
        print(messageFormatter(sys.argv[1], sys.argv[2]))
        


