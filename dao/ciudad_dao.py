from objetos.ciudad import Ciudad
from dao.conn import Connection
from mysql.connector import Error

class CiudadesDAO:
    def obtener_todas(self):
        """Obtiene todas las ciudades ordenadas por nombre"""
        try:
            conn = Connection.getConnection()
            if not conn or not conn.is_connected():
                raise Error("No se pudo establecer conexión con la base de datos.")

            query = "SELECT codigo, nombre FROM ciudad ORDER BY nombre"
            cursor = conn.cursor()
            cursor.execute(query)
            resultado = cursor.fetchall()

            ciudades = []
            for fila in resultado:
                ciudad = Ciudad(codigo=fila[0], nombre=fila[1])
                ciudades.append(ciudad)

            cursor.close()
            return ciudades

        except Error as e:
            print(f"Error en CiudadesDAO (obtener_todas): {e}")
            return []

    def insertar(self, ciudad: Ciudad):
        """Inserta una nueva ciudad en la base de datos."""
        try:
            # Validación del código
            if len(ciudad.get_codigo()) != 3:
                return "codigo_invalido"

            conn = Connection.getConnection()
            if not conn or not conn.is_connected():
                raise Error("No se pudo establecer conexión con la base de datos.")

            cursor = conn.cursor()
            
            # Verificar si ya existe el código o el nombre
            query_verificar = "SELECT codigo FROM ciudad WHERE codigo = %s OR nombre = %s"
            cursor.execute(query_verificar, (ciudad.get_codigo().upper(), ciudad.get_nombre()))
            if cursor.fetchone():
                cursor.close()
                return "duplicado"

            # Insertar nueva ciudad
            query_insertar = "INSERT INTO ciudad (codigo, nombre) VALUES (%s, %s)"
            cursor.execute(query_insertar, (ciudad.get_codigo().upper(), ciudad.get_nombre()))
            conn.commit()
            cursor.close()
            return True
        
        except Error as e:
            print(f"Error en CiudadesDAO (insertar): {e}")
            raise e

    def actualizar(self, codigo_actual, nuevo_codigo, nuevo_nombre):
        """Actualiza una ciudad existente."""
        try:
            # Validación del nuevo código
            if len(nuevo_codigo) != 3:
                return "codigo_invalido"

            conn = Connection.getConnection()
            if not conn or not conn.is_connected():
                raise Error("No se pudo establecer conexión con la base de datos.")

            cursor = conn.cursor()
            
            # Si el código se está cambiando, verificar que el nuevo no exista ya (excluyendo el actual)
            if codigo_actual.upper() != nuevo_codigo.upper():
                query_verificar = "SELECT codigo FROM ciudad WHERE codigo = %s"
                cursor.execute(query_verificar, (nuevo_codigo.upper(),))
                if cursor.fetchone():
                    cursor.close()
                    return "duplicado"

            query = "UPDATE ciudad SET codigo = %s, nombre = %s WHERE codigo = %s"
            cursor.execute(query, (nuevo_codigo.upper(), nuevo_nombre, codigo_actual))
            conn.commit()
            cursor.close()
            return True
        
        except Error as e:
            print(f"Error en CiudadesDAO (actualizar): {e}")
            return False

    def buscar_por_nombre(self, nombre):
        """Busca ciudades por nombre"""
        try:
            conn = Connection.getConnection()
            if not conn or not conn.is_connected():
                raise Error("No se pudo establecer conexión con la base de datos.")
            
            cursor = conn.cursor()
            query = "SELECT codigo, nombre FROM ciudad WHERE nombre LIKE %s ORDER BY nombre"
            cursor.execute(query, (f"%{nombre}%",))
            
            resultado = cursor.fetchall()
            ciudades = []
            for fila in resultado:
                ciudades.append(Ciudad(codigo=fila[0], nombre=fila[1]))
            
            cursor.close()
            return ciudades
        except Exception as e:
            print(f"Error al buscar ciudades: {e}")
            return []

    def eliminar(self, codigo):
        """Elimina una ciudad de la base de datos por su código."""
        try:
            conn = Connection.getConnection()
            if not conn or not conn.is_connected():
                raise Error("No se pudo establecer conexión con la base de datos.")

            cursor = conn.cursor()
            query = "DELETE FROM ciudad WHERE codigo = %s"
            cursor.execute(query, (codigo,))
            conn.commit()
            
            if cursor.rowcount == 0:
                cursor.close()
                return False

            cursor.close()
            return True
        
        except Error as e:
            print(f"Error en CiudadesDAO (eliminar): {e}")
            return False
