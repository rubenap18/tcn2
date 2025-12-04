from mysql.connector import Error
from utilidades.validaciones import Validaciones

class ControlardorPantallaReservaciones:
    def __init__(self, reservacion_dao):
        self.reservacion_dao = reservacion_dao

    def getTotalReservaciones(self):
        try:
            return self.reservacion_dao.consultarNumeroReservaciones()
        except Error as e:
            print(f'Error en ControladorVEReservaciones (getTotalReservaciones()): {e}')
            raise e


    def consultarTodasReservacionesParaTabla(self):
        try:
            return self.reservacion_dao.getTodasReservacionesParaTabla()
        except Error as e:
            print(f'Error en ControladorVEReservaciones (getTodasReservaciones()): {e}')
            raise e
        

    def consultarTablaReservacionesActuales(self):
        listado_reservaciones = []
        try:
            return self.reservacion_dao.getTodasReservaciones()

        except Error as e:
            print(f'Error en ControladorVEReservaciones (getTodasReservaciones()): {e}')
            raise e
        

    def consultarTablaReservacionesPasadas(self):
        try:
            return self.reservacion_dao.consultarTablaReservacionesPasadas()
        except Error as e:
            print(f'Error en ControladorVEReservaciones (getTodasReservaciones()): {e}')
            raise e
        

    def buscarReservacionPorNumero(self,numero):

        if not Validaciones.validar_id(numero):
            return False
        try:
            return self.reservacion_dao.buscarReservacionPorNumero(numero)
        except Error as e:
            print(f'Error en ControladorVEReservaciones (buscarReservacionesPorNUmero()): {e}')
            raise e
        
    def consultarTotalReservacionesPasadas(self):
        try:
            return self.reservacion_dao.consultarTotalReservacionesPasadas()
        except Error as e:
            print(f'Error en ControladorVEReservaciones (getTodasReservacionesPasadas()): {e}')
            raise e
        

    def consultarTotalReservacionesActivas(self):
        try:
            return self.reservacion_dao.consultarTotalReservacionesActivas()
        except Error as e:
            print(f'Error en ControladorVEReservaciones (getTodasReservacionesActivas()): {e}')
            raise e
        

    def buscarReservacionPorCorrida(self,numero):

        if not Validaciones.validar_id(numero):
            return False
        try:
            return self.reservacion_dao.buscarReservacionPorCorrida(numero)
        except Error as e:
            print(f'Error en ControladorVEReservaciones (buscarReservacionesPorNUmero()): {e}')
            raise e
        
    def buscarReservacionPorCiudadOrigen(self,ciudad):
        try:
            return self.reservacion_dao.buscarReservacionPorCiudadOrigen(ciudad)
        except Error as e:
            print(f'Error en ControladorVEReservaciones (buscarReservacionesPorCiudad()): {e}')
            raise e
        
    def buscarReservacionPorCiudadDestino(self,ciudad):
        try:
            return self.reservacion_dao.buscarReservacionPorCiudadDestino(ciudad)
        except Error as e:
            print(f'Error en ControladorVEReservaciones (buscarReservacionesPorCiudad()): {e}')
            raise e