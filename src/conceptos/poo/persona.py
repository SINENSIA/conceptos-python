from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nif, nombre, apellidos):
        self._nif = nif
        self._nombre = nombre
        self._apellidos = apellidos
        
    def __str__(self):
        return self.nif + " " + self.nombre + " " + self.apellidos
    
    def __del__(self):
        print("Se ha eliminado el objeto " + self.nif)
        
    @property    
    def nif(self):
        return self._nif
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def apellidos(self):
        return self._apellidos
    
    @nif.setter
    def nif(self, nif):
        self._nif = nif
        
    @nombre.setter    
    def nombre(self, nombre):
        self._nombre = nombre
        
    @apellidos.setter 
    def apellidos(self, apellidos):
        self._apellidos = apellidos
    
    def __eq__(self, other):
        if isinstance(other, Persona):
            return self.nif == other.nif
        else:
            return NotImplemented
        
    def saludo(self):
        return f"Hola, mi nombre es {self.nombre} {self.apellidos}."
    
    @staticmethod
    def metodo_estatico():
        return "este es un método estático"
    
    @abstractmethod
    def saludar(self):
        pass