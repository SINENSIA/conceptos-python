from persona import Persona

class Proveedor(Persona):
    def __init__(self, nif, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
        self.nif = nif
    def saludar(self):
        return "Hola, soy un proveedor"