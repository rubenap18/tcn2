class Autobus:
    def __init__(self, numero=None, matricula=None, claveWIFI=None, cantAsientos=None, 
                 tipoAutobus=None, marca=None, modelo=None, estado=None):
        self._numero = numero
        self._matricula = matricula
        self._claveWIFI = claveWIFI
        self._cantAsientos = cantAsientos
        self._tipoAutobus = tipoAutobus
        self._marca = marca
        self._modelo = modelo
        self._estado = estado
        
    def to_dict(self):
        return {
            'numero': self._numero,
            'matricula': self._matricula,
            'claveWIFI': self._claveWIFI,
            'cantAsientos': self._cantAsientos,
            'tipoAutobus': self._tipoAutobus,
            'marca': self._marca,
            'modelo': self._modelo,
            'estado': self._estado
        }
    
    # Getters y Setters
    def get_numero(self):
        return self._numero
    
    def set_numero(self, numero):
        self._numero = numero
    
    def get_matricula(self):
        return self._matricula
    
    def set_matricula(self, matricula):
        self._matricula = matricula
    
    def get_claveWIFI(self):
        return self._claveWIFI
    
    def set_claveWIFI(self, claveWIFI):
        self._claveWIFI = claveWIFI
    
    def get_cantAsientos(self):
        return self._cantAsientos
    
    def set_cantAsientos(self, cantAsientos):
        self._cantAsientos = cantAsientos
    
    def get_tipoAutobus(self):
        return self._tipoAutobus
    
    def set_tipoAutobus(self, tipoAutobus):
        self._tipoAutobus = tipoAutobus
    
    def get_marca(self):
        return self._marca
    
    def set_marca(self, marca):
        self._marca = marca
    
    def get_modelo(self):
        return self._modelo
    
    def set_modelo(self, modelo):
        self._modelo = modelo
    
    def get_estado(self):
        return self._estado
    
    def set_estado(self, estado):
        self._estado = estado
    
    def __str__(self):
        return f"Autobus {self._numero} - {self._matricula} ({self._estado})"
    

