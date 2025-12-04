from datetime import datetime

class Viaje:
    def __init__(self, corrida_id=None, cantidad_pasajeros=1):
        self._corrida_id = corrida_id
        self._cantidad_pasajeros = cantidad_pasajeros
        self._pasajeros = []  # Lista de objetos Pasajero
        self._asientos_seleccionados = []  # Lista de claves de asientos
        self._boletos = []  # Lista de objetos Boleto
        self._fecha_venta = datetime.now()
        self._reservacion_id = None

    def __str__(self):
        return f"Viaje: Corrida {self._corrida_id}, {self._cantidad_pasajeros} pasajeros"

    # Getters
    def get_corrida_id(self):
        return self._corrida_id
    
    def get_cantidad_pasajeros(self):
        return self._cantidad_pasajeros
    
    def get_pasajeros(self):
        return self._pasajeros
    
    def get_asientos_seleccionados(self):
        return self._asientos_seleccionados
    
    def get_boletos(self):
        return self._boletos
    
    def get_fecha_venta(self):
        return self._fecha_venta
    
    def get_reservacion_id(self):
        return self._reservacion_id
    
    # Setters
    def set_corrida_id(self, corrida_id):
        self._corrida_id = corrida_id
    
    def set_cantidad_pasajeros(self, cantidad):
        self._cantidad_pasajeros = cantidad
    
    def set_reservacion_id(self, reservacion_id):
        self._reservacion_id = reservacion_id
    
    # Métodos para agregar elementos
    def agregar_pasajero(self, pasajero):
        self._pasajeros.append(pasajero)
    
    def agregar_asiento(self, asiento_clave):
        self._asientos_seleccionados.append(asiento_clave)
    
    def agregar_boleto(self, boleto):
        self._boletos.append(boleto)
