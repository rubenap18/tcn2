# objetos/Operador.py
from datetime import date

class Operador:
    # Atributos y constructor
    def __init__(self, numero, nombre, apellPat, apellMat, fechaNac, telefono, fechaContrato):
        self.__numero = numero
        self.__nombre = nombre
        self.__apellPat = apellPat
        self.__apellMat = apellMat
        self.__fechaNac = fechaNac
        self.__telefono = telefono
        self.__fechaContrato = fechaContrato
        
    def __str__(self):
        return f"Número: {self.__numero} \nNombre: {self.__nombre} {self.__apellPat} {self.__apellMat} \nTeléfono: {self.__telefono} \nFecha Nacimiento: {self.__fechaNac} \nFecha Contrato: {self.__fechaContrato}"
    
    # Getters y Setters
    def get_numero(self):
        return self.__numero
    def set_numero(self, numero):
        self.__numero = numero
    
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def get_apellPat(self):
        return self.__apellPat
    def set_apellPat(self, apellPat):
        self.__apellPat = apellPat
    
    def get_apellMat(self):
        return self.__apellMat
    def set_apellMat(self, apellMat):
        self.__apellMat = apellMat
    
    def get_fechaNac(self):
        return self.__fechaNac
    def set_fechaNac(self, fechaNac):
        self.__fechaNac = fechaNac
    
    def get_telefono(self):
        return self.__telefono
    def set_telefono(self, telefono):
        self.__telefono = telefono
    
    def get_fechaContrato(self):
        return self.__fechaContrato
    def set_fechaContrato(self, fechaContrato):
        self.__fechaContrato = fechaContrato
    
    # Método adicional para nombre completo
    def get_nombre_completo(self):
        return f"{self.__nombre} {self.__apellPat} {self.__apellMat}"