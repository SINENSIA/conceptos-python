from persona import Persona

class Cliente(Persona):
    def __init__(self, nif, nombre, apellidos, id_cliente, email=None):
        super().__init__(nif, nombre, apellidos)
        self._id_cliente = id_cliente
        self._email = email
    # operación de venta
    @property
    def id_cliente(self):
        return self._id_cliente
    
    @property
    def email(self):
        return self._email
    
    @id_cliente.setter
    def id_cliente(self, id_cliente):
        self._id_cliente = id_cliente
    
    @email.setter
    def email(self, email):
        self._email = email
    # Polimorfismo
    def saludo(self):
        return super().saludo() + f" Mi ID de cliente es {self.id_cliente}."
    
    def saludar(self):
        return "Hola, soy un cliente."