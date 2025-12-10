from dao.conn import Connection
from objetos.corrida import Corrida
import mysql.connector
from mysql.connector import Error

class CorridaDAO:
    def __init__(self):
        pass

    def obtener_ciudades_origen_distintas(self):
        origin_cities = []
        try:
            conn = Connection.getConnection()
            cursor = conn.cursor(dictionary=True)
            query = """
                SELECT DISTINCT
                    ro.nombre AS ciudad_origen
                FROM
                    corrida c
                JOIN
                    ruta r ON c.ruta = r.codigo
                JOIN
                    ciudad ro ON r.ciudadOrigen = ro.codigo
                ORDER BY
                    ro.nombre
            """
            cursor.execute(query)
            for row in cursor.fetchall():
                origin_cities.append(row['ciudad_origen'])
        except Exception as e:
            print(f"Error al obtener ciudades de origen distintas: {e}")
        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()
        return origin_cities

    def obtener_todas_las_corridas_detalladas(self):
        corridas_detalladas = []
        try:
            conn = Connection.getConnection()
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
                    (a.cantAsientos - (SELECT COUNT(*) FROM reservacion res WHERE res.corrida = c.numero)) AS boletos_disponibles,
                    (SELECT COUNT(*) FROM reservacion res WHERE res.corrida = c.numero) AS boletos_vendidos
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
            """
            cursor.execute(query)
            corridas_detalladas = cursor.fetchall()
        except Exception as e:
            print(f"Error al obtener corridas detalladas: {e}")
        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()
        return corridas_detalladas

    def obtener_corridas_detalladas_por_fecha_y_origen(self, fecha_str, ciudad_origen_nombre):
        corridas_detalladas = []
        try:
            conn = Connection.getConnection()
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
                    (a.cantAsientos - (SELECT COUNT(*) FROM reservacion res WHERE res.corrida = c.numero)) AS boletos_disponibles,
                    (SELECT COUNT(*) FROM reservacion res WHERE res.corrida = c.numero) AS boletos_vendidos
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
                    c.fecha = %s
            """
            params = [fecha_str]
            
            if ciudad_origen_nombre is not None:
                query += " AND ro.nombre = %s"
                params.append(ciudad_origen_nombre)

            cursor.execute(query, tuple(params))
            corridas_detalladas = cursor.fetchall()
        except Exception as e:
            print(f"Error al obtener corridas detalladas por fecha y origen: {e}")
        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()
        return corridas_detalladas

    def obtener_corridas_por_fecha_autobus_u_operador(self, fecha_str, id_autobus=None, numero_operador=None):
        corridas = []
        conexion = None
        cursor = None
        try:
            conexion = Connection.getConnection()
            cursor = conexion.cursor()
            query = """
                SELECT numero, ruta, fecha, hora_salida, hora_llegada, tarifaBase, operador, autobus
                FROM corrida
                WHERE fecha = %s
            """
            params = [fecha_str]

            if id_autobus is not None:
                query += " AND autobus = %s"
                params.append(id_autobus)
            if numero_operador is not None:
                query += " AND operador = %s"
                params.append(numero_operador)

            cursor.execute(query, tuple(params))
            resultados = cursor.fetchall()

            for fila in resultados:
                corrida = Corrida(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7])
                corridas.append(corrida)

        except Error as e:
            print(f"Error al obtener corridas por fecha, autobus u operador: {e}")
        finally:
            if cursor:
                cursor.close()
        return corridas

    def autobus_ocupado_en_fecha(self, numero_autobus, fecha_str): # Renamed id_autobus to numero_autobus
        conexion = None
        cursor = None
        try:
            conexion = Connection.getConnection()
            cursor = conexion.cursor()
            query = "SELECT COUNT(*) FROM corrida WHERE autobus = %s AND fecha = %s"
            cursor.execute(query, (numero_autobus, fecha_str))
            count = cursor.fetchone()[0]
            return count > 0
        except Error as e:
            print(f"Error al verificar si el autobús está ocupado: {e}")
            return False
        finally:
            if cursor:
                cursor.close()

    def operador_ocupado_en_fecha(self, numero_operador, fecha_str):
        conexion = None
        cursor = None
        try:
            conexion = Connection.getConnection()
            cursor = conexion.cursor()
            query = "SELECT COUNT(*) FROM corrida WHERE operador = %s AND fecha = %s"
            cursor.execute(query, (numero_operador, fecha_str))
            count = cursor.fetchone()[0]
            return count > 0
        except Error as e:
            print(f"Error al verificar si el operador está ocupado: {e}")
            return False
        finally:
            if cursor:
                cursor.close()
    
    def crear_corrida(self, ruta_codigo, fecha, hora_salida, hora_llegada, tarifaBase, operador_numero, autobus_numero, lugares_disponibles, estado='ACT'):
        conexion = None
        cursor = None
        try:
            conexion = Connection.getConnection()
            cursor = conexion.cursor()
            query = """
                INSERT INTO corrida (fecha, hora_salida, hora_llegada, tarifaBase, lugaresDisp, autobus, ruta, operador,estado)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            print(fecha, hora_salida, hora_llegada, tarifaBase, lugares_disponibles, autobus_numero,ruta_codigo,operador_numero,estado)
            cursor.execute(query, (fecha, hora_salida, hora_llegada, tarifaBase, lugares_disponibles, autobus_numero,ruta_codigo,operador_numero,estado))
            conexion.commit()
            return True
        except Error as e:
            print(f"Error al crear corrida: {e}")
            if conexion:
                conexion.rollback()
            return False
        finally:
            if cursor:
                cursor.close()

    def actualizar_corrida(self, numero_viaje, ruta_codigo, fecha_hora_salida, fecha_hora_llegada, precio, operador_numero, autobus_numero, lugares_disponibles, estado):
        conexion = None
        cursor = None
        try:
            conexion = Connection.getConnection()
            cursor = conexion.cursor()
            query = """
                UPDATE corrida
                SET ruta = %s, fecha = %s, hora_salida = %s, hora_llegada = %s,
                    tarifaBase = %s, operador = %s, autobus = %s, lugaresDisp = %s, estado = %s
                WHERE numero = %s
            """
            fecha_salida, hora_salida = fecha_hora_salida.split(' ')
            fecha_llegada, hora_llegada = fecha_hora_llegada.split(' ')
            
            cursor.execute(query, (ruta_codigo, fecha_salida, hora_salida, hora_llegada,
                                   precio, operador_numero, autobus_numero, lugares_disponibles, estado,
                                   numero_viaje))
            conexion.commit()
            return True
        finally:
            if cursor:
                cursor.close()

    def actualizar_operador_corrida(self, numero_viaje, operador_numero):
        conexion = None
        cursor = None
        try:
            conexion = Connection.getConnection()
            cursor = conexion.cursor()
            query = """
                UPDATE corrida
                SET operador = %s
                WHERE numero = %s
            """
            cursor.execute(query, (operador_numero, numero_viaje))
            conexion.commit()
            return True
        except Error as e:
            print(f"Error al actualizar el operador de la corrida: {e}")
            if conexion:
                conexion.rollback()
            return False
        finally:
            if cursor:
                cursor.close()

    def obtener_corrida_por_numero_viaje(self, numero_viaje):
        corrida_data = None
        try:
            conn = Connection.getConnection()
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
                    c.estado AS estado_corrida,
                    (SELECT COUNT(*) FROM reservacion res WHERE res.corrida = c.numero) AS cantidad_pasajeros
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
                    c.numero = %s
            """
            cursor.execute(query, (numero_viaje,))
            corrida_data = cursor.fetchone()
        except Exception as e:
            print(f"Error al obtener corrida por numero de viaje: {e}")
        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()
        return corrida_data

    def actualizar_estado_corrida(self, numero_viaje, nuevo_estado):
        conexion = None
        cursor = None
        try:
            conexion = Connection.getConnection()
            cursor = conexion.cursor()
            query = """
                UPDATE corrida
                SET estado = %s
                WHERE numero = %s
            """
            cursor.execute(query, (nuevo_estado, numero_viaje))
            conexion.commit()
            return True
        except Error as e:
            print(f"Error al actualizar el estado de la corrida: {e}")
            if conexion:
                conexion.rollback()
            return False
        finally:
            if cursor:
                cursor.close()