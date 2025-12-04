from dao.conn import Connection
from objetos.asiento import Asiento

class AsientoDAO:
    def __init__(self):
        self._conexion = Connection.getConnection()
    
    def crear_asientos_autobus(self, numero_autobus, tipo_servicio):
    
        cursor = self._conexion.cursor()
        try:
            # Determinar cantidad de asientos según tipo
            if tipo_servicio == "PLUS":
                cant_asientos = 44
            elif tipo_servicio == "PLATINO":
                cant_asientos = 34
            else:
                raise ValueError(f"Tipo de servicio no válido: {tipo_servicio}")
            
            # Secuencia de ubicaciones
            ubicaciones = ['ventana', 'pasillo', 'pasillo', 'ventana', 'pasillo', 'pasillo']
            
            # Crear cada asiento
            for i in range(1, cant_asientos + 1):
                # Determinar ubicación según patrón
                ubicacion = ubicaciones[(i - 1) % len(ubicaciones)]
                
                # Crear clave del asiento (ej: "107-01")
                clave = f"{numero_autobus}-{str(i).zfill(2)}"
                
                # Insertar asiento
                query = """
                INSERT INTO asiento (clave, numero, ubicacion, autobus)
                VALUES (%s, %s, %s, %s)
                """
                cursor.execute(query, (clave, i, ubicacion, numero_autobus))
            
            self._conexion.commit()
            return cant_asientos
            
        except Exception as e:
            self._conexion.rollback()
            raise e
        finally:
            cursor.close()
    
    def eliminar_asientos_autobus(self, numero_autobus):
        
        cursor = self._conexion.cursor()
        try:
            query = "DELETE FROM asiento WHERE autobus = %s"
            cursor.execute(query, (numero_autobus,))
            self._conexion.commit()
            return cursor.rowcount
        except Exception as e:
            self._conexion.rollback()
            raise e
        finally:
            cursor.close()