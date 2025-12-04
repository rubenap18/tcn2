import mysql.connector 
from mysql.connector import Error

#importando variables de entorno
import config

#Esta es una clase tipo Singleton (una instancia para todo el sistema).
class Connection:

    _conexion = None

    #este metodo regresa una sola conexion que se utilizara en todo el sistema.

    @classmethod
    def getConnection(cls):
        if cls._conexion == None or not cls._conexion.is_connected():
            try:
                cls._conexion = mysql.connector.connect(
                host = config.DB_HOST,
                port = config.DB_PORT, 
                user = config.DB_USER, 
                password = config.DB_PASSWORD, 
                database = config.DB_DATABASE,
                use_pure = config.DB_USE_PURE)
            except Error as e:
                cls._conexion = None
                print(f'Error: Fallo conectar con la DB.{e}')
                raise Error(f'Error de MySQL al intectar conectar con la BD. {e}')
        #si no hay falla se regresa la conexion
        return cls._conexion
    

    """Este metodo cierra la unica conexion que hay en el sistema."""
    @classmethod
    def closeConnection(cls):
        if cls._conexion and cls._conexion.is_connected():
            print('Cerrando la conexion con la BD.')
            cls._conexion.close()
        cls._conexion = None