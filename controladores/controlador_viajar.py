from dao.viajar_dao import ViajarDAO

class ControladorViajar:
    
    
    def __init__(self, viajar_dao):
        self.viajar_dao = viajar_dao
    
    def obtener_ciudades_origen(self):
        
        try:
            return self.viajar_dao.obtener_ciudades_origen()
        except Exception as e:
            print(f"Error en ControladorViajar.obtener_ciudades_origen: {e}")
            return []
    
    def obtener_ciudades_destino(self, ciudad_origen):
        
        try:
            return self.viajar_dao.obtener_ciudades_destino(ciudad_origen)
        except Exception as e:
            print(f"Error en ControladorViajar.obtener_ciudades_destino: {e}")
            return []
    
    def obtener_fechas_disponibles(self, ciudad_origen, ciudad_destino):
        
        try:
            return self.viajar_dao.obtener_fechas_disponibles(ciudad_origen, ciudad_destino)
        except Exception as e:
            print(f"Error en ControladorViajar.obtener_fechas_disponibles: {e}")
            return []
    
    def buscar_corridas(self, ciudad_origen, ciudad_destino, fecha, num_pasajeros):
        
        try:
            return self.viajar_dao.obtener_corridas_disponibles(
                ciudad_origen, ciudad_destino, fecha, num_pasajeros
            )
        except Exception as e:
            print(f"Error en ControladorViajar.buscar_corridas: {e}")
            return []
    
    def obtener_asientos_disponibles(self, numero_corrida):
        
        try:
            return self.viajar_dao.obtener_asientos_disponibles(numero_corrida)
        except Exception as e:
            print(f"Error en ControladorViajar.obtener_asientos_disponibles: {e}")
            return []
    
    def validar_asientos_disponibles(self, numero_corrida, asientos_seleccionados):
        
        try:
            return self.viajar_dao.validar_asientos_disponibles(numero_corrida, asientos_seleccionados)
        except Exception as e:
            print(f"Error en ControladorViajar.validar_asientos_disponibles: {e}")
            return False
    
    def calcular_tipo_pasajero(self, fecha_nacimiento):
        
        try:
            return self.viajar_dao.calcular_tipo_pasajero(fecha_nacimiento)
        except Exception as e:
            print(f"Error en ControladorViajar.calcular_tipo_pasajero: {e}")
            return ('REGU', 'Regular', 0, 0)
    
    def procesar_compra(self, datos_compra, usuario_id=None):
        """Procesa la compra completa de boletos."""
        try:
            return self.viajar_dao.procesar_compra_boletos(datos_compra, usuario_id)
        except Exception as e:
            print(f"Error en ControladorViajar.procesar_compra: {e}")
            return {
                'exito': False,
                'mensaje': f'Error al procesar la compra: {str(e)}'
            }
    
    def obtener_boletos_reservacion(self, numero_reservacion):
        
        try:
            return self.viajar_dao.obtener_boletos_reservacion(numero_reservacion)
        except Exception as e:
            print(f"Error en ControladorViajar.obtener_boletos_reservacion: {e}")
            return []
    
    def obtener_reservaciones_usuario(self, usuario_id):
        
        try:
            return self.viajar_dao.obtener_reservaciones_usuario(usuario_id)
        except Exception as e:
            print(f"Error en ControladorViajar.obtener_reservaciones_usuario: {e}")
            return []