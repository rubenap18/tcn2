from dao.conn import Connection
from mysql.connector import Error

class PasajeroDAO:
    """
    DAO para operaciones CRUD con pasajeros.
    """
    
    def __init__(self):
        pass
    
    def crear_pasajero(self, nombre, apellido_pat, apellido_mat, fecha_nac, edad, correo, telefono):
        
        conn = None
        cursor = None
        
        try:
            conn = Connection.getConnection()
            if not conn or not conn.is_connected():
                raise Error('No se puede establecer conexión con la BD.')
            
            cursor = conn.cursor()
            
            query = """
                INSERT INTO pasajero (nombre, apellPat, apellMat, fechaNac, edad, correoElect, telefono)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            
            cursor.execute(query, (nombre, apellido_pat, apellido_mat, fecha_nac, edad, correo, telefono))
            conn.commit()
            
            return cursor.lastrowid
            
        except Error as e:
            if conn:
                conn.rollback()
            print(f'Error en PasajeroDAO.crear_pasajero: {e}')
            return None
        finally:
            if cursor:
                cursor.close()
    
    def obtener_pasajero_por_id(self, pasajero_id):
        
        conn = None
        cursor = None
        
        try:
            conn = Connection.getConnection()
            cursor = conn.cursor(dictionary=True)
            
            query = """
                SELECT numero, nombre, apellPat, apellMat, fechaNac, edad, correoElect, telefono
                FROM pasajero
                WHERE numero = %s
            """
            
            cursor.execute(query, (pasajero_id,))
            pasajero = cursor.fetchone()
            
            return pasajero
            
        except Error as e:
            print(f'Error en PasajeroDAO.obtener_pasajero_por_id: {e}')
            return None
        finally:
            if cursor:
                cursor.close()
    
    def buscar_pasajeros_por_nombre(self, nombre):
        
        pasajeros = []
        conn = None
        cursor = None
        
        try:
            conn = Connection.getConnection()
            cursor = conn.cursor(dictionary=True)
            
            query = """
                SELECT numero, nombre, apellPat, apellMat, fechaNac, edad, correoElect, telefono
                FROM pasajero
                WHERE nombre LIKE %s OR apellPat LIKE %s OR apellMat LIKE %s
                ORDER BY nombre, apellPat
            """
            
            patron = f'%{nombre}%'
            cursor.execute(query, (patron, patron, patron))
            pasajeros = cursor.fetchall()
            
            return pasajeros
            
        except Error as e:
            print(f'Error en PasajeroDAO.buscar_pasajeros_por_nombre: {e}')
            return []
        finally:
            if cursor:
                cursor.close()
    
    def obtener_todos_pasajeros(self):
        
        pasajeros = []
        conn = None
        cursor = None
        
        try:
            conn = Connection.getConnection()
            cursor = conn.cursor(dictionary=True)
            
            query = """
                SELECT numero, nombre, apellPat, apellMat, fechaNac, edad, correoElect, telefono
                FROM pasajero
                ORDER BY nombre, apellPat
            """
            
            cursor.execute(query)
            pasajeros = cursor.fetchall()
            
            return pasajeros
            
        except Error as e:
            print(f'Error en PasajeroDAO.obtener_todos_pasajeros: {e}')
            return []
        finally:
            if cursor:
                cursor.close()