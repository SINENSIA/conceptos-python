# Calcula el precio medio y varianza de los productos
def precio_stats(precios): 
   total = 0
   num_productos = len(precios) 
   for precio in precios.values():
     total += precio
     media = total / num_productos
   xi = {}
   for precio in precios.values():
       xi.update({ precio : (precio - media) })

   xi2 ={ }
   for valor, desviacion in xi.items():
       xi2.update({valor : desviacion**2})

   sumaxi2 = sum(xi2.values())
   varianza = sumaxi2 / (num_productos)
   return (media, varianza)


precios = { 'producto_a': 17, 'producto_b': 32, 'producto_c': 56 }
media, varianza = precio_stats(precios)

print(media, varianza)

def anadir_precio_stats(producto, precio):

    # Añade un producto con su precio y recalcula estadísticas, no devuelve nada 
    # pero llama a otras funciones para que lo hagan  
  
    precio = round(precio, 2)    
    precios.update({producto : precio})    
    media, varianza = precio_stats(precios)    
    print(media, varianza)
    
anadir_precio_stats('producto_d', 17.245)


#####Otra aopción anidando funciones
def new_anadir_precio_stats(producto, precio):   
   def formatear(precio):      
      return round(precio, 2)   
   def anadir_precio(producto, precio):      
      precios.update({producto : precio})       
      return precios   
   
   precio_formateado = formatear(precio)   
   nuevos_precios = anadir_precio(producto, precio_formateado)
   print(nuevos_precios)
   print(precio_stats(nuevos_precios))

new_anadir_precio_stats('producto_e', 23.674)

# Tipo explícito (sólo documentación) y ... para indicar que no tiene implementación
def mi_funcion() -> int:
   ...

