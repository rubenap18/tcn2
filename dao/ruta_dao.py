from .conn import Connection
from objetos.Ruta import Ruta
from mysql.connector import Error

class RutaDAO:
    def __init__(self):
        pass

    def obtener_todas(self):
 
        try:
            conn = Connection.getConnection()
            cursor = conn.cursor()
            cursor.execute("SELECT r.codigo, r.distancia, co.nombre, cd.nombre FROM ruta r JOIN ciudad co ON r.ciudadOrigen = co.codigo JOIN ciudad cd ON r.ciudadDestino = cd.codigo")
            
            rutas_data = cursor.fetchall()
            rutas = []
            for ruta_data in rutas_data:
                ruta = Ruta(ruta_data[0], ruta_data[2], ruta_data[3], ruta_data[1])
                rutas.append(ruta)
            
            return rutas

        except Error as e:
            print(f"Error en DAO al obtener rutas: {e}")
            return False
        finally:
            if 'conn' in locals() and conn.is_connected():
                cursor.close()

    def insertar(self, codigo_origen, codigo_destino, distancia):
    
        print(f"DAO: Intentando insertar ruta con Origen={codigo_origen}, Destino={codigo_destino}, Distancia={distancia}")
        try:
            conn = Connection.getConnection()
            if not conn or not conn.is_connected():
                print("DAO: Conexión a la base de datos no disponible.")
                return False
            cursor = conn.cursor()
            
            # Verificar si la ruta de ida o vuelta ya existe
            codigo_ida = f"{codigo_origen}-{codigo_destino}"
            codigo_vuelta = f"{codigo_destino}-{codigo_origen}"
            
            cursor.execute("SELECT codigo FROM ruta WHERE codigo = %s OR codigo = %s", (codigo_ida, codigo_vuelta))
            if cursor.fetchone():
                print(f"DAO: Ruta {codigo_ida} o {codigo_vuelta} ya existe.")
                return "duplicado"

            # Insertar la nueva ruta
            cursor.execute("INSERT INTO ruta (codigo, ciudadOrigen, ciudadDestino, distancia) VALUES (%s, %s, %s, %s)",
                           (codigo_ida, codigo_origen, codigo_destino, distancia))
            conn.commit()
            print(f"DAO: Ruta {codigo_ida} insertada con éxito.")
            return True

        except Error as e:
            if 'conn' in locals() and conn.is_connected():
                conn.rollback()
            print(f"Error en DAO al insertar ruta: {e}")
            return False
        finally:
            if 'conn' in locals() and conn.is_connected():
                cursor.close()

    def actualizar_distancia(self, codigo_ruta, distancia):
      
        print(f"DAO: Intentando actualizar distancia de ruta {codigo_ruta} a {distancia}")
        try:
            conn = Connection.getConnection()
            if not conn or not conn.is_connected():
                print("DAO: Conexión a la base de datos no disponible.")
                return False
            cursor = conn.cursor()
            cursor.execute("UPDATE ruta SET distancia = %s WHERE codigo = %s", (distancia, codigo_ruta))
            conn.commit()
            print(f"DAO: Distancia de ruta {codigo_ruta} actualizada con éxito.")
            return True

        except Error as e:
            if 'conn' in locals() and conn.is_connected():
                conn.rollback()
            print(f"Error en DAO al actualizar distancia: {e}")
            return False
        finally:
            if 'conn' in locals() and conn.is_connected():
                cursor.close()