from dao.misreservaciones_dao import MisReservacionesDAO

class ControladorPantallaMisReservaciones:
    def __init__(self):
        self.misreservaciones_dao = MisReservacionesDAO()

    def obtener_reservaciones_cliente(self, user_id):
        
        try:
            return self.misreservaciones_dao.obtener_reservaciones_usuario(user_id)
        except Exception as e:
            print(f"Error en ControladorPantallaMisReservaciones.obtener_reservaciones_cliente: {e}")
            return []