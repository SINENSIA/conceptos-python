
from abc import ABC, abstractmethod
import gc
import time


class Persona(ABC):
    def __init__(self, nombre, apellidos, id_fiscal):
        self.nombre = nombre
        self.apellidos = apellidos
        self.__id_fiscal = id_fiscal

    @abstractmethod
    def saludar(self):
        pass

    @property
    def id_fiscal(self):
        return self.__id_fiscal

    @id_fiscal.setter
    def id_fiscal(self, valor):
        self.__id_fiscal = valor


class Cliente(Persona):
    contador_clientes = 0

    def __init__(self, nombre, apellidos, id_fiscal, id_cliente, email):
        super().__init__(nombre, apellidos, id_fiscal)
        self.id_cliente = id_cliente
        self.email = email
        Cliente.contador_clientes += 1

    @staticmethod
    def clientes_creados():
        return Cliente.contador_clientes

    def __str__(self):
        return (f"Cliente: {self.nombre} {self.apellidos}, ID Fiscal: {self.id_fiscal}, "
                f"ID Cliente: {self.id_cliente}, Email: {self.email}")

    def __del__(self):
        print(f"Cliente id: {self.id_cliente} eliminado")
        Cliente.contador_clientes = max(0, Cliente.contador_clientes - 1)

    def __eq__(self, otro):
        if isinstance(otro, Cliente):
            return self.id_fiscal == otro.id_fiscal
        return False

    def saludar(self):
        return f"Hola, soy {self.nombre} {self.apellidos}, encantado de conocerte."


class Factura:
    def __init__(self, id_factura, cliente):
        self.id_factura = id_factura
        self.cliente = cliente

    def __str__(self):
        return (f"Factura ID: {self.id_factura}, Cliente: [{self.cliente}]")

    def __eq__(self, otro):
        if isinstance(otro, Factura):
            return (self.id_factura == otro.id_factura and
                    self.cliente == otro.cliente)
        return False


# uso declietne
if __name__ == "__main__":
    cliente1 = Cliente("Pepito", "Pérez", "12345678Z",
                       1, "pepito.perez@example.com")
    cliente2 = Cliente("Juanita", "López", "876548821B",
                       2, "juanita.lopez@example.com")
    cliente3 = Cliente("Carlos", "Arranz", "978545678A",
                       3, "carlos.arranz@example.com")

    print(cliente1.saludar())

    # mostrmaos clientes
    print(cliente1)
    print(cliente2)

    # comaparamos clientes
    print("--- ¿Tienen el mismo id fiscal? ---")
    print(cliente1 == cliente3)  # False -> no tienen el mismo id_fiscal

    # ahora las facturas
    factura1 = Factura(101, cliente1)
    factura2 = Factura(102, cliente2)
    factura3 = Factura(101, cliente1)

    print(factura1)
    print(factura2)

    # vaemos si son iguales
    # debería ser True porque tienen el mismo id_factura y cliente
    print("--- ¿Son la misma factura si pertenecen al mismo cliente e id_factura? ---")
    print(factura1 == factura3)

    # cuantos clientes se han creado?
    print(f"Clientes creados: {Cliente.clientes_creados()}")
    factura1.cliente = None
    factura2.cliente = None
    factura3.cliente = None
    # Eliminar cliente
    del cliente1
    del cliente2
    del cliente3

    print(f"Clientes creados tras eliminación: {Cliente.clientes_creados()}")
