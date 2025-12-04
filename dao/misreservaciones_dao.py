from .conn import Connection
from mysql.connector import Error

class MisReservacionesDAO:
    def __init__(self):
        self.db = Connection.getConnection()

    def obtener_reservaciones_usuario(self, user_id):
        """Obtener reservaciones con origen y destino realizadas por un usuario"""
        try:
            # JOIN con corrida y luego con ruta para obtener origen y destino
            # Filtramos directamente por el usuario que realizó la reservación (r.usuario)
            comando = """
                SELECT r.numero, r.fecha, r.fechaLimPago, r.cantPasajeros, 
                    rt.ciudadOrigen, rt.ciudadDestino, r.subtotal, r.IVA, r.total
                FROM reservacion r 
                JOIN corrida c ON r.corrida = c.numero
                JOIN ruta rt ON c.ruta = rt.codigo  -- Ajusta según el nombre real de la FK
                WHERE r.usuario = %s -- Directamente usando el user_id para filtrar
                ORDER BY r.fecha DESC
            """
            cursor = self.db.cursor()
            cursor.execute(comando, (user_id,)) # Pass user_id as a parameter
            reservaciones = cursor.fetchall()
            cursor.close()
            return reservaciones
            
        except Error as e:
            print(f"Error al obtener reservaciones: {e}")
            return []
