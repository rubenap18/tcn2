# objetos/corrida.py
from datetime import date, time

class Corrida:
    def __init__(self, numero, ruta_codigo, fecha, hora_salida, hora_llegada, precio, operador_numero, autobus_id):
        self.__numero = numero
        self.__ruta_codigo = ruta_codigo
        self.__fecha = fecha
        self.__hora_salida = hora_salida
        self.__hora_llegada = hora_llegada
        self.__precio = precio
        self.__operador_numero = operador_numero
        self.__autobus_id = autobus_id

    def __str__(self):
        return (f"Corrida Numero: {self.__numero}, Ruta: {self.__ruta_codigo}, Fecha: {self.__fecha}, "
                f"Salida: {self.__hora_salida}, Llegada: {self.__hora_llegada}, Precio: {self.__precio}, "
                f"Operador: {self.__operador_numero}, Autobus: {self.__autobus_id}")

    # Getters
    def get_numero(self):
        return self.__numero

    def get_ruta_codigo(self):
        return self.__ruta_codigo

    def get_fecha(self):
        return self.__fecha

    def get_hora_salida(self):
        return self.__hora_salida

    def get_hora_llegada(self):
        return self.__hora_llegada

    def get_precio(self):
        return self.__precio

    def get_operador_numero(self):
        return self.__operador_numero

    def get_autobus_id(self):
        return self.__autobus_id

    # Setters
    def set_numero(self, numero):
        self.__numero = numero

    def set_ruta_codigo(self, ruta_codigo):
        self.__ruta_codigo = ruta_codigo

    def set_fecha(self, fecha):
        self.__fecha = fecha

    def set_hora_salida(self, hora_salida):
        self.__hora_salida = hora_salida

    def set_hora_llegada(self, hora_llegada):
        self.__hora_llegada = hora_llegada

    def set_precio(self, precio):
        self.__precio = precio

    def set_operador_numero(self, operador_numero):
        self.__operador_numero = operador_numero

    def set_autobus_id(self, autobus_id):
        self.__autobus_id = autobus_id
