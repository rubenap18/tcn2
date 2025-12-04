from datetime import date

class Pasajero:
    def __init__(self, numero=None, nombre=None, apellPat=None, apellMat=None, 
                 fechaNac=None, edad=None, correoElect=None, telefono=None):
        self._numero = numero
        self._nombre = nombre
        self._apellPat = apellPat
        self._apellMat = apellMat
        self._fechaNac = fechaNac
        self._edad = edad
        self._correoElect = correoElect
        self._telefono = telefono
        
    def __str__(self):
        return f"Pasajero {self._numero}: {self._nombre} {self._apellPat}"
    
    # Getters
    def get_numero(self):
        return self._numero
    
    def get_nombre(self):
        return self._nombre
    
    def get_apellPat(self):
        return self._apellPat
    
    def get_apellMat(self):
        return self._apellMat
    
    def get_fechaNac(self):
        return self._fechaNac
    
    def get_edad(self):
        return self._edad
    
    def get_correoElect(self):
        return self._correoElect
    
    def get_telefono(self):
        return self._telefono
    
    # Setters
    def set_numero(self, numero):
        self._numero = numero
    
    def set_nombre(self, nombre):
        self._nombre = nombre
    
    def set_apellPat(self, apellPat):
        self._apellPat = apellPat
    
    def set_apellMat(self, apellMat):
        self._apellMat = apellMat
    
    def set_fechaNac(self, fechaNac):
        self._fechaNac = fechaNac
    
    def set_edad(self, edad):
        self._edad = edad
    
    def set_correoElect(self, correoElect):
        self._correoElect = correoElect
    
    def set_telefono(self, telefono):
        self._telefono = telefono