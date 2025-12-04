# objetos/Ruta.py
class Ruta:
    
    def __init__(self, codigo, ciudadorigen, ciudaddestino, distancia):
        self.__codigo = codigo
        self.__ciudadorigen = ciudadorigen
        self.__ciudaddestino = ciudaddestino
        self.__distancia = distancia
        
    def __str__(self):
        return f"Código: {self.__codigo} \nOrigen: {self.__ciudadorigen} \nDestino: {self.__ciudaddestino} \nDistancia: {self.__distancia} km"
    
    # Getters y Setters
    def get_codigo(self):
        return self.__codigo
    def set_codigo(self, codigo):
        self.__codigo = codigo
    
    def get_ciudadorigen(self):
        return self.__ciudadorigen
    def set_ciudadorigen(self, ciudadorigen):
        self.__ciudadorigen = ciudadorigen
    
    def get_ciudaddestino(self):
        return self.__ciudaddestino
    def set_ciudaddestino(self, ciudaddestino):
        self.__ciudaddestino = ciudaddestino
    
    def get_distancia(self):
        return self.__distancia
    def set_distancia(self, distancia):
        self.__distancia = distancia