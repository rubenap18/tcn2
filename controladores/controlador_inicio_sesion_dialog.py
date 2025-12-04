from objetos.usuario import Usuario

class ControladorInicioSesionDialog:
    def __init__(self, usuario_dao):
        self.usuario_dao = usuario_dao

    def validarInicioSesion(self, phone, password):
        # Si el usuario existe en la BD
        usuario = self.usuario_dao.consultarUsuario(phone)
        if not usuario:
            return None, 'Numero no encontrado.'
        if password != usuario.password:
            return None, 'Contrasena incorrecta.'
        
        # ⭐ CAMBIO: Retornar el usuario completo junto con el tipo
        return usuario, usuario.es_admin

    def crearUsuario(self, phone,password):
        #si el usuario si existe en la BD
        usuario_nuevo = Usuario(id_usuario=0,phone=phone,password=password,es_admin=0)
        respuesta = self.usuario_dao.crearUsuario(usuario_nuevo)
        return respuesta

        """Espacio para hacer validacion"""