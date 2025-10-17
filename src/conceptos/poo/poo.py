from coche import Coche
from vehiculo import Vehiculo
from cliente import Cliente
from persona import Persona
from proveedor import Proveedor

# Aún no tengo NADA, peor puedo llamar a estáticos:
# metodo estático
print(Persona.metodo_estatico())

# Crear un objeto Coche
mi_coche = Coche("Ford", "Mustang", "Manual")
print(mi_coche)

# Al usar abs en Vehiculo se convierte en abstracto y no puede instaciar directamente
# mi_vehiculo = Vehiculo("Toyota", "Corolla")
# TypeError: Can't instantiate abstract class Vehiculo with abstract method mostrar_informacion

print(mi_coche.testing())  # Esto viene de vehiculo
"""======================================="""
mi_cliente = Cliente("12342094Z", "Juan", "Perez García", 29438)
mi_cliente2 = Cliente("12342094Z", "Juan", "Perez García",
                      29438, "juanperez@example.com")

mi_proveedor = Proveedor("4334092", "Pedro", "Rodriguez")

print("Es mi_cliente igual a mi_coche?")
print(mi_cliente == mi_coche)
"""======================================="""
print("="*12)
print("Nos saltamos name mangling")
mi_cliente_ana = Cliente("12345678A", "Ana", "López", 1, "ana@correo.com")
# print(mi_cliente_ana.__id_cliente)  # error
# print(mi_cliente_ana._Cliente__id_cliente)  # ok pero castigado... :(

print(mi_cliente_ana.id_cliente)

print("="*12)
"""======================================="""
# Esto sería false si no cambiamos el método __eq__
print("Son los dos clientes la misma persona? " + str(mi_cliente == mi_cliente2))

print(mi_cliente)
print(mi_cliente.saludo())


# método obstracto
print(mi_proveedor.saludar())
print(mi_cliente_ana.saludar())
