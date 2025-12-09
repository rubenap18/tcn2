from .conn import Connection
from mysql.connector import Error

class IndexDAO:
    def __init__(self):
        self.db = Connection.getConnection()

    def cargar_pasajeros_dashboard(self):
        
        try:
            comando = """
            SELECT numero, nombre, apellPat, apellMat, 
                   TIMESTAMPDIFF(YEAR, fechaNac, CURDATE()) as edad,
                   telefono
            FROM pasajero 
            ORDER BY numero DESC 
            
            """
            
            cursor = self.db.cursor()
            cursor.execute(comando)
            pasajeros = cursor.fetchall()
            cursor.close()
            return pasajeros
                
        except Error as e:
            print(f"Error en IndexDAO.cargar_pasajeros_dashboard: {e}")
            return []

    def cargar_corridas_dashboard(self):
        
        try:
            comando = """
            SELECT
                c.numero AS numero_viaje,
                CONCAT(c.fecha, ' ', c.hora_salida) AS fecha_hora_salida,
                ro.nombre AS ciudad_origen,
                rd.nombre AS ciudad_destino,
                a.numero AS autobus_numero
            FROM
                corrida c
            JOIN
                ruta r ON c.ruta = r.codigo
            JOIN
                ciudad ro ON r.ciudadOrigen = ro.codigo
            JOIN
                ciudad rd ON r.ciudadDestino = rd.codigo
            JOIN
                autobus a ON c.autobus = a.numero
            ORDER BY c.fecha, c.hora_salida
            """
            
            cursor = self.db.cursor(dictionary=True)
            cursor.execute(comando)
            corridas = cursor.fetchall()
            
            cursor.close()
            return corridas
                
        except Error as e:
            print(f"Error en IndexDAO.cargar_corridas_dashboard: {e}")
            return []

    def cargar_operadores_con_corridas_dashboard(self):
        
        try:
            comando = """
            SELECT DISTINCT
                op.numero AS numero_operador,
                CONCAT(op.nombre, ' ', op.apellPat, ' ', COALESCE(op.apellMat, '')) AS nombre_completo_operador
            FROM operador op
            ORDER BY op.numero
            """
            
            cursor = self.db.cursor(dictionary=True) # Added dictionary=True
            cursor.execute(comando)
            operadores = cursor.fetchall() # Changed variable name for clarity
            cursor.close()
            return operadores
                
        except Error as e:
            print(f"Error en IndexDAO.cargar_operadores_con_corridas_dashboard: {e}")
            return []

    def cargar_pasajeros_por_corrida(self, corrida_id):
        
        try:
            comando = """
            SELECT
                r.numero AS numero_boleto,
                a.numero AS numero_asiento,
                CONCAT(p.nombre, ' ', p.apellPat, ' ', COALESCE(p.apellMat, '')) AS nombre_pasajero,
                TIMESTAMPDIFF(YEAR, p.fechaNac, CURDATE()) AS edad
            FROM pasajero p
            JOIN reservacion r ON p.numero = r.pasajero
            JOIN asiento_reservacion ar ON r.numero = ar.reservacion
            JOIN asiento a ON ar.asiento = a.clave
            WHERE r.corrida = %s
            ORDER BY r.numero
            """
            cursor = self.db.cursor(dictionary=True) # Added dictionary=True
            cursor.execute(comando, (corrida_id,))
            pasajeros = cursor.fetchall()
            print(f"DEBUG: Pasajeros fetched for corrida_id {corrida_id}: {pasajeros}") # DEBUG
            cursor.close()
            return pasajeros
        except Error as e:
            print(f"Error en IndexDAO.cargar_pasajeros_por_corrida: {e}")
            return []
        
    def obtener_todas_las_corridas_detalladas(self, operator_id):
        corridas_detalladas = []
        try:
            conn = self.db
            cursor = conn.cursor(dictionary=True)
            query = """
                SELECT
                    c.numero AS numero_viaje,
                    ro.nombre AS ciudad_origen,
                    rd.nombre AS ciudad_destino,
                    r.codigo AS ruta_codigo,
                    r.distancia,
                    CONCAT(c.fecha, ' ', c.hora_salida) AS fecha_hora_salida,
                    CONCAT(c.fecha, ' ', c.hora_llegada) AS fecha_hora_llegada,
                    CONCAT(o.nombre, ' ', o.apellPat, ' ', COALESCE(o.apellMat, '')) AS nombre_operador,
                    c.operador AS operador_numero,
                    a.numero AS autobus_numero,
                    a.matricula,
                    a.cantAsientos AS cantidad_asientos,
                    c.tarifaBase AS precio,
                    (SELECT COUNT(*) FROM boleto b WHERE b.corrida = c.numero) AS cantidad_pasajeros
                FROM
                    corrida c
                JOIN
                    ruta r ON c.ruta = r.codigo
                JOIN
                    ciudad ro ON r.ciudadOrigen = ro.codigo
                JOIN
                    ciudad rd ON r.ciudadDestino = rd.codigo
                JOIN
                    operador o ON c.operador = o.numero
                JOIN
                    autobus a ON c.autobus = a.numero
                WHERE
                    c.operador = %s
            """
            cursor.execute(query, (operator_id,))
            corridas_detalladas = cursor.fetchall()
            cursor.close()
            return corridas_detalladas
        except Error as e:
            print(f"Error en IndexDAO.obtener_todas_las_corridas_detalladas: {e}")
            return []    