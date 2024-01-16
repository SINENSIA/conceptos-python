import sys
import time

# Formatea el texto en cuatro estilos
def messageFormatter(texto, tipo):
    if (tipo == 'info'): 
         return '\033[44m' + ' ' + texto + ' ' + '\033[0m' 
    elif (tipo == 'warning'): 
        return '\033[43m\033[31m' + ' ' + texto + ' ' + '\033[0m' 
    elif (tipo == 'error'):
         return '\033[41m' + ' ' + texto + ' ' + '\033[0m' 
    elif (tipo == 'success'): 
         return '\033[42m' + ' ' + texto + ' ' + '\033[0m' 
    else: 
         return '\033[0m' + ' ' + texto + ' ' + '\033[0m'


def loadingBar(carga):
    maximo = 50  # Tamaño de la barra de progreso
    # Si 100 es a 50, carga será a x = carga*50/100
    carga = int(carga / 100 * maximo)
    barra = '\033[42m' + '█'  * carga + '\033[0m' + '-' * (maximo - carga)
    return f"[{barra}] {carga * 2}%"


def animateText(texto, velocidad=0.1):
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(velocidad)
    print()


# Definimos __name__ como __main__  
if __name__ == "__main__":    
    import sys    
    print(messageFormatter(sys.argv[1], sys.argv[2]) )


