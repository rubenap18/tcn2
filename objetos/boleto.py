class Boleto:
    def __init__(self, numero=None, precio=None, asiento=None, 
                 pasajero=None, tipoPasajero=None, corrida=None):
        self._numero = numero
        self._precio = precio
        self._asiento = asiento  # clave del asiento
        self._pasajero = pasajero  # ID del pasajero
        self._tipoPasajero = tipoPasajero  # código tipo pasajero
        self._corrida = corrida  # ID de la corrida
    
    # Getters
    def get_numero(self):
        return self._numero
    
    def get_precio(self):
        return self._precio
    
    def get_asiento(self):
        return self._asiento
    
    def get_pasajero(self):
        return self._pasajero
    
    def get_tipoPasajero(self):
        return self._tipoPasajero
    
    def get_corrida(self):
        return self._corrida
    
    # Setters
    def set_numero(self, numero):
        self._numero = numero
    
    def set_precio(self, precio):
        self._precio = precio
    
    def set_asiento(self, asiento):
        self._asiento = asiento
    
    def set_pasajero(self, pasajero):
        self._pasajero = pasajero
    
    def set_tipoPasajero(self, tipoPasajero):
        self._tipoPasajero = tipoPasajero
    
    def set_corrida(self, corrida):
        self._corrida = corrida
    
    def __str__(self):
        return f"Boleto {self._numero}: ${self._precio:.2f} - Pasajero {self._pasajero}"