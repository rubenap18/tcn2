from objetos.usuario import Usuario

class ControladorRegistroDialog:
    def __init__(self, usuario_dao):
        self.usuario_dao = usuario_dao


    def crearUsuario(self, phone,password):
        #si el usuario si existe en la BD
        usuario_nuevo = Usuario(id_usuario=0,phone=phone,password=password,es_admin=0)
        respuesta = self.usuario_dao.crearUsuario(usuario_nuevo)
        return respuesta

        """Espacio para hacer validacion"""