from dao.conn import Connection

class MarcaModeloDAO:
    def __init__(self):
        self._conexion = Connection.getConnection()
    
    def obtener_marcas(self):
        """Obtiene todas las marcas de la base de datos"""
        cursor = self._conexion.cursor(dictionary=True)
        try:
            query = "SELECT clave, nombre FROM marca ORDER BY nombre"
            cursor.execute(query)
            return cursor.fetchall()
        finally:
            cursor.close()
    
    def obtener_modelos_por_marca(self, marca_clave):
        """Obtiene los modelos de una marca específica"""
        cursor = self._conexion.cursor(dictionary=True)
        try:
            query = """
            SELECT m.clave, m.nombre 
            FROM modelo m 
            WHERE m.marca = %s 
            ORDER BY m.nombre
            """
            cursor.execute(query, (marca_clave,))
            return cursor.fetchall()
        finally:
            cursor.close()
    
    def obtener_codigo_marca_por_nombre(self, marca_nombre):
        """Obtiene el código de una marca por su nombre"""
        cursor = self._conexion.cursor()
        try:
            query = "SELECT clave FROM marca WHERE nombre = %s"
            cursor.execute(query, (marca_nombre,))
            result = cursor.fetchone()
            return result[0] if result else None
        finally:
            cursor.close()
    
    def obtener_codigo_modelo_por_nombre(self, modelo_nombre, marca_clave):
        """Obtiene el código de un modelo por su nombre y marca"""
        cursor = self._conexion.cursor()
        try:
            query = "SELECT clave FROM modelo WHERE nombre = %s AND marca = %s"
            cursor.execute(query, (modelo_nombre, marca_clave))
            result = cursor.fetchone()
            return result[0] if result else None
        finally:
            cursor.close()