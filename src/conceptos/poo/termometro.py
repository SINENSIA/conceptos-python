class Termometro:
    """
    Clase Termometro para representar y convertir temperaturas entre las escalas
    Fahrenheit, Celsius y Kelvin.

    Métodos:
    celsius: Obtiene o establece la temperatura en grados Celsius.
    fahrenheit: Obtiene o establece la temperatura en grados Fahrenheit.
    kelvin: Obtiene o establece la temperatura en Kelvin.
    """

    def __init__(self, temperatura=0, escala='celsius'):
        self._celsius = self._fahrenheit = self._kelvin = 0  # Inicializa valores a 0
        self.testing = 1
        if escala not in ['celsius', 'fahrenheit', 'kelvin']:
            raise ValueError(
                "La escala debe ser 'celsius', 'fahrenheit' o 'kelvin'")

        if escala == 'celsius':
            self.celsius = temperatura
        elif escala == 'fahrenheit':
            self.fahrenheit = temperatura
        elif escala == 'kelvin':
            self.kelvin = temperatura

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._celsius = value
        self._fahrenheit = (value * 9 / 5) + 32
        self._kelvin = value + 273.15

    @property
    def fahrenheit(self):
        return self._fahrenheit

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._fahrenheit = value
        self._celsius = (value - 32) * 5 / 9
        self._kelvin = (value + 459.67) * 5 / 9

    @property
    def kelvin(self):
        return self._kelvin

    @kelvin.setter
    def kelvin(self, value):
        self._kelvin = value
        self._celsius = value - 273.15
        self._fahrenheit = (value * 9 / 5) - 459.67

    def set_testing(self, value):
        self.testing = value
