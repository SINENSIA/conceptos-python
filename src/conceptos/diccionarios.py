sizes = { 'XS' : 10, 'S': 15, 'L': 20, 'XL': 25 }
sizes['L'] = 21
print(sizes) #=> {'L': 21, 'XXL': 30, 'S': 15, 'XL': 25, 'XS': 10}
sizes['XSS'] = 30


sizes.update({'XSS': 5}) # Añadimos una nueva clave:valor
sizes.update({'XS': 7}) # Cambiamos una clave:valor existente
print(sizes)

del sizes['L']
print(sizes) #=> {'XXL': 30, 'S': 15, 'XL': 25, 'XS': 10}

print(list(sizes.keys())) #=> ['XSS', 'S', 'XL', 'XXL', 'XS']

print("XL" in sizes) # => True 
print("XS" not in sizes) # => False

for clave, valor in sizes.items():
   print(clave, valor)

for posicion, valor in enumerate(sizes):
   print(posicion, valor)

xi = {}      
for precio in precios.values():      
   xi.update({ precio : (precio - media) })         




return (media, varianza)


