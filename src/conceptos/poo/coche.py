from vehiculo import Vehiculo

class Coche(Vehiculo):
    """
    Clase para representar un automóvil, heredando de la clase Vehiculo.

    Atributos heredados:
        _marca (str): Marca del vehículo.
        _modelo (str): Modelo del vehículo.

    Atributos:
        _tipo_transmision (str): Tipo de transmisión del automóvil.
    """

    def __init__(self, marca, modelo, tipo_transmision):
        """
        Inicializa los atributos del automóvil con marca, modelo y tipo de transmisión.

        Parámetros:
            marca (str): Marca del automóvil.
            modelo (str): Modelo del automóvil.
            tipo_transmision (str): Tipo de transmisión del automóvil.
        """
        super().__init__(marca, modelo)
        self._tipo_transmision = tipo_transmision

    @property
    def tipo_transmision(self):
        """ Retorna el tipo de transmisión del automóvil. """
        return self._tipo_transmision

    @tipo_transmision.setter
    def tipo_transmision(self, valor):
        """ Establece el tipo de transmisión del automóvil. """
        self._tipo_transmision = valor

    def mostrar_informacion(self):
        """
        Retorna una cadena de caracteres que representa la información del automóvil.

        Retorna:
            str: Representación en cadena de la información del automóvil, incluyendo marca, modelo y tipo de transmisión.
        """
        return f"Automóvil {self._marca} {self._modelo}, Transmisión: {self._tipo_transmision}"
    
    def __str__(self) -> str:
        return self.mostrar_informacion()

    def __eq__(self, other):
        if isinstance(other, Coche):
            return self._marca == other._marca and self._modelo == other._modelo and self._tipo_transmision == other._tipo_transmision
        return False

    def __hash__(self) -> int:
        return hash((self._marca, self._modelo, self._tipo_transmision))