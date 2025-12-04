import mysql.connector
from mysql.connector import Error
from dao.conn import Connection
from objetos.Operador import Operador
from datetime import date

class OperadorDAO:
    def __init__(self):
        pass

    def listar_operadores(self):
        operadores = []
        try:
            conexion = Connection.getConnection()
            cursor = conexion.cursor()
            query = "SELECT numero, nombre, apellPat, apellMat, fechaNac, telefono, fechaContrato FROM operador"
            cursor.execute(query)
            resultados = cursor.fetchall()

            for fila in resultados:
                # Assuming fechaNac and fechaContrato are stored as strings in 'YYYY-MM-DD' format
                # and need to be converted to date objects.
                fecha_nac = date.fromisoformat(str(fila[4])) if fila[4] else None
                fecha_contrato = date.fromisoformat(str(fila[6])) if fila[6] else None
                operador = Operador(fila[0], fila[1], fila[2], fila[3], fecha_nac, fila[5], fecha_contrato)
                operadores.append(operador)

        except Error as e:
            print(f"Error al listar operadores: {e}")
        finally:
            if 'conexion' in locals() and conexion.is_connected():
                cursor.close()
                # Connection.closeConnection()
        return operadores
    def obtener_todos(self):
        try:
            conn = Connection.getConnection()
            if not conn or not conn.is_connected():
                raise Error('No se puede establecer conexion con la BD.')

            query = "SELECT numero, nombre, apellPat, apellMat, fechaNac, telefono, fechaContrato FROM operador"
            cursor = conn.cursor()
            cursor.execute(query)
            resultado = cursor.fetchall()

            operadores = []
            for fila in resultado:
                operador = Operador(numero=fila[0], nombre=fila[1], apellPat=fila[2], apellMat=fila[3], fechaNac=fila[4], telefono=fila[5], fechaContrato=fila[6])
                operadores.append(operador)

            cursor.close()
            return operadores
        
        except Error as e:
            print(f'Error en OperadorDAO (obtener_todos): {e}')
            raise e

    def insertar(self, operador: Operador):
        try:
            conn = Connection.getConnection()
            if not conn or not conn.is_connected():
                raise Error('No se puede establecer conexion con la BD.')

            query = "INSERT INTO operador (nombre, apellPat, apellMat, telefono, fechaNac, fechaContrato) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor = conn.cursor()
            
            # Explicitly format date objects to strings
            fechaNac_str = operador.get_fechaNac().strftime("%Y-%m-%d") if operador.get_fechaNac() else None
            fechaContrato_str = operador.get_fechaContrato().strftime("%Y-%m-%d") if operador.get_fechaContrato() else None
            
            cursor.execute(query, (operador.get_nombre(), operador.get_apellPat(), operador.get_apellMat(), operador.get_telefono(), fechaNac_str, fechaContrato_str))
            conn.commit()
            cursor.close()
            return True
        
        except Error as e:
            print(f'Error en OperadorDAO (insertar): {e}')
            raise e

    def actualizar(self, operador: Operador):
        try:
            conn = Connection.getConnection()
            if not conn or not conn.is_connected():
                raise Error('No se puede establecer conexion con la BD.')

            query = "UPDATE operador SET nombre = %s, apellPat = %s, apellMat = %s, fechaNac = %s, telefono = %s WHERE numero = %s"
            cursor = conn.cursor()
            
            # Explicitly format date objects to strings
            fechaNac_str = operador.get_fechaNac().strftime("%Y-%m-%d") if operador.get_fechaNac() else None
            # fechaContrato is not updated in this query based on the current structure, but should be formatted if it were.
            # Assuming fechaContrato is not part of the update for now based on the query.
            
            cursor.execute(query, (operador.get_nombre(), operador.get_apellPat(), operador.get_apellMat(), fechaNac_str, operador.get_telefono(), operador.get_numero()))
            conn.commit()
            cursor.close()
            return True
        
        except Error as e:
            print(f'Error en OperadorDAO (actualizar): {e}')
            raise e

    def buscar(self, criterio):
        try:
            conn = Connection.getConnection()
            if not conn or not conn.is_connected():
                raise Error('No se puede establecer conexion con la BD.')

            query = """
            SELECT numero, nombre, apellPat, apellMat, fechaNac, telefono, fechaContrato 
            FROM operador 
            WHERE nombre LIKE %s 
            OR apellPat LIKE %s 
            OR apellMat LIKE %s 
            OR numero LIKE %s
            """
            
            cursor = conn.cursor()
            criterio_like = f'%{criterio}%'
            cursor.execute(query, (criterio_like, criterio_like, criterio_like, criterio_like))
            resultado = cursor.fetchall()

            operadores = []
            for fila in resultado:
                operador = Operador(numero=fila[0], nombre=fila[1], apellPat=fila[2], apellMat=fila[3], fechaNac=fila[4], telefono=fila[5], fechaContrato=fila[6])
                operadores.append(operador)

            cursor.close()
            return operadores
        
        except Error as e:
            print(f'Error en OperadorDAO (buscar): {e}')
            raise e
