from cliente import Cliente


class Factura:
    def __init__(self, id_factura: str, cliente: Cliente):

        self.id_factura = id_factura
        # Aquí cliente es una instancia de la clase Cliente
        self.cliente = cliente

    def mostrar_detalle(self):
        # utiliza __str__ de cliente
        print(f"Factura ID: {self.id_factura} Cliente: {self.cliente}")

    def __eq__(self, other):
        if isinstance(other, Factura):
            return self.id_factura == other.id_factura and self.cliente == other.cliente
        return False

    def __hash__(self):
        return hash((self.id_factura, self.cliente))

    def __repr__(self):
        return f"Factura(id_factura={self.id_factura}, cliente={self.cliente!r})"

    def __str__(self):
        return f"Factura con ID {self.id_factura} para cliente {self.cliente}"


# Creando una instancia de Cliente
mi_cliente = Cliente("4332542F", "Juan", "Pérez",
                     12342, "juan.perez@example.com")
# Creando instancias de ContadorDeInstancias
instancia1 = Cliente("4333242F", "Pedro", "Pérez", 12343, "jpedro@example.com")

Cliente.mostrar_numero_de_instancias()  # Salida: Numero de instancias: 1

instancia2 = Cliente("43397442F", "Pepe", "Pérez",
                     1249783, "jpepe@example.com")
Cliente.mostrar_numero_de_instancias()  # Salida: Numero de instancias: 2

instancia3 = Cliente("4343242F", "Carlos", "Pérez",
                     12453, "jcarlos@example.com")
instancia3.id_cliente = 443
Cliente.mostrar_numero_de_instancias()  # Salida: Numero de instancias: 3
# Creando una instancia de Factura que incluye el cliente creado anteriormente
factura1 = Factura("FAC001", mi_cliente)
factura2 = Factura("FAC001", mi_cliente)

if (factura1 == factura2):
    print("Las facturas son la misma")
else:
    print("Las facturas son distintas")
# Mostrando los detalles de la factura, incluyendo la información del cliente
factura1.mostrar_detalle()
print(factura1)

miset = {factura1, factura2}

print(miset)
