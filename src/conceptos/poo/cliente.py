from persona import Persona


class Cliente(Persona):

    # Variable estática para contar las instancias
    _numero_de_instancias = 0

    @staticmethod
    def mostrar_numero_de_instancias():
        # Método estático para mostrar el número de instancias
        # print(f"Numero de instancias: {Cliente._numero_de_instancias}")
        print(f"Numero de instancias: {Cliente._numero_de_instancias}")

    @classmethod
    def mostrar_numero_de_instancias_cm(cls):
        return print(f"Numero de instancias: {cls._numero_de_instancias}")

    """_summary_

    Args:
        Persona (_type_): _description_
    """

    def __init__(self, nif, nombre: str, apellidos: str, id_cliente: int, email: str = None):
        super().__init__(nif, nombre, apellidos)
        # Aquí llamamos a setter. La propiedad es privada como vemos en el cuerpo del setter y del getter
        self.id_cliente = id_cliente
        self._email = email
        Cliente._numero_de_instancias += 1
    # operación de venta

    @property
    def id_cliente(self) -> int:
        return self.__id_cliente

    @property
    def email(self):
        return self._email

    @id_cliente.setter
    def id_cliente(self, id_cliente) -> int:
        if id_cliente < 0:
            raise ValueError("El ID no puede ser negativo")
        self.__id_cliente = id_cliente

    @email.setter
    def email(self, email) -> str:
        self._email = email
    # Polimorfismo

    def saludo(self) -> str:
        return super().saludo() + f" Mi ID de cliente es {self.id_cliente}."

    def saludar(self) -> str:
        return "Hola, soy un cliente."

    def __str__(self) -> str:
        return f"Cliente: {self.nombre} {self.apellidos}, ID: {self.id_cliente}"

    def __eq__(self, other):
        if isinstance(other, Cliente):
            return self.id_cliente == other.id_cliente and self.nif == other.nif
        return False

    def __hash__(self):
        return hash((self.id_cliente, self.nif))

    def __repr__(self):
        return f"Cliente(id_cliente={self.id_cliente}, nombre={self.nombre}, apellidos={self.apellidos})"
