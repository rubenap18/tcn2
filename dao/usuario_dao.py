from objetos.usuario import Usuario
from dao.conn import Connection
from mysql.connector import Error

class UsuarioDAO:
    conn = None

    def consultarUsuario(self,phone):

        try:
            conn = Connection.getConnection() #llamnado a la conexion
            #verificando conexion
            if not conn and not conn.is_connected():
                raise Error('No se puede establecer conexion con la BD.')

            query = f'SELECT * FROM usuario WHERE phone = {phone}'
            cursor = conn.cursor()
            cursor.execute(query)
            resultado = cursor.fetchall()

            #mapeando respuestas a un objeto
    
            usuario = None
            for fila in resultado:
                usuario = (Usuario(id_usuario=fila[0],phone=fila[1],password=fila[2],es_admin=fila[3]))

            cursor.close()
            return usuario
        
        except Error as e:
            print(f'Error en UsuarioDAO (consultarUsuario): {e}')
            raise e


    
    def crearUsuario(self, usuario: Usuario):
        try:
            conn = Connection.getConnection() #llamnado a la conexion
            #verificando conexion
            if not conn and not conn.is_connected():
                raise Error('No se puede establecer conexion con la BD.')

            query = f"INSERT INTO usuario (phone, password,es_admin) VALUES ('{usuario.phone}','{usuario.password}',{usuario.es_admin})"
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            cursor.close()
            return True
        
        except Error as e:
            print(f'Error en UsuarioDAO (crearUsuario): {e}')
            raise e
