class Asiento:
    def __init__(self, clave=None, numero=None, ubicacion=None, autobus=None):
        self._clave = clave
        self._numero = numero
        self._ubicacion = ubicacion
        self._autobus = autobus
        
    def to_dict(self):
        return {
            'clave': self._clave,
            'numero': self._numero,
            'ubicacion': self._ubicacion,
            'autobus': self._autobus
        }
    
    # Getters y Setters
    def get_clave(self):
        return self._clave
    
    def set_clave(self, clave):
        self._clave = clave
    
    def get_numero(self):
        return self._numero
    
    def set_numero(self, numero):
        self._numero = numero
    
    def get_ubicacion(self):
        return self._ubicacion
    
    def set_ubicacion(self, ubicacion):
        self._ubicacion = ubicacion
    
    def get_autobus(self):
        return self._autobus
    
    def set_autobus(self, autobus):
        self._autobus = autobus
    
    def __str__(self):
        return f"Asiento {self._clave} - {self._ubicacion}"
    
    