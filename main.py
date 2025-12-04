"""Este metodo es el metodo principal de todo el sistema.
    1. Inicia la conexion con la DB que todos usaran
    2. Hace las instancias e inyecta estas dependencias/instancias
    3. Inicia el UI
    4. Cierra el UI
    5. Cierra la conexion con la DB que todos usaron.
    6. Termina la ejecucion del sistema.
"""

#imports de librerias
import sys
import mysql.connector
from mysql.connector import Error
from PySide6.QtWidgets import QApplication, QDialog, QMessageBox

#importando conexion
from dao.conn import Connection

#importando ui y vistas
from vista.iniciosesionDialog import InicioSesionDialog
from vista.registroDialog import RegistroDialog
from vista.main_ui_empresa import MainUIEmpresa
from vista.main_ui_usuario import MainUIUsuario

#importando app manager
from utilidades.app_manager import AppManager

#importando dao's
from dao.index_dao import IndexDAO
from dao.usuario_dao import UsuarioDAO
from dao.reservacion_dao import ReservacionDAO 
from dao.corrida_dao import CorridaDAO
from dao.autobus_dao import AutobusDAO
from dao.ruta_dao import RutaDAO
from dao.operador_dao import OperadorDAO
from dao.pasajero_dao import PasajeroDAO
from dao.ciudad_dao import CiudadesDAO # Agregado
from dao.viajar_dao import ViajarDAO  # ⭐ NUEVO: DAO para compra de boletos

#importando controladores
from controladores.controlador_index_empresa import ControladorIndex
from controladores.controlador_inicio_sesion_dialog import ControladorInicioSesionDialog
from controladores.controlador_registro_dialog import ControladorRegistroDialog
from controladores.controlador_pantalla_reservaciones import ControlardorPantallaReservaciones
from controladores.controlador_pantalla_corridas import ControladorPantallaCorridas
from controladores.controlador_pantalla_autobuses import ControladorPantallaAutobuses
from controladores.controlador_pantalla_rutas import ControladorPantallaRutas
from controladores.controlador_pantalla_operadores import ControladorPantallaOperadores
from controladores.controlador_pantalla_pasajeros import ControladorPantallaPasajeros
from controladores.controlador_pantalla_ciudad import ControladorPantallaCiudad # Agregado
from controladores.controlador_viajar import ControladorViajar   # ⭐ NUEVO: Controlador para compra de boletos

from utilidades.validaciones import Validaciones

def main():
    print('Iniciando Transportes Cuervo Negro')
    app = QApplication(sys.argv) # inicia la app
    #Iniciando conexion que usara todo el sistema.
    try:
        Connection.getConnection()
        print('Conexion con la BD hecha.')

    except Error as e:
        error = f"ERROR IMPORTANTE: No se pudo iniciar el programita. {e}"
        QMessageBox.information(None,"Mensaje", error)
        
        Connection.closeConnection() #cerrando por si acaso algo quedo abierto en la conexion
        return #terminando la ejecucion del programa

    #Iniciando dao's
    index_dao = IndexDAO()
    usuario_dao = UsuarioDAO()
    reservacion_dao = ReservacionDAO()
    corrida_dao = CorridaDAO()
    autobus_dao = AutobusDAO()
    ruta_dao = RutaDAO()
    operador_dao = OperadorDAO()
    pasajero_dao = PasajeroDAO()
    ciudad_dao = CiudadesDAO() # Agregado
    viajar_dao = ViajarDAO() # Agregado por Hector :3

    #Iniciando controladores
    controlador_index = ControladorIndex(index_dao=index_dao)
    controlador_isd = ControladorInicioSesionDialog(usuario_dao=usuario_dao)
    controlador_rd = ControladorRegistroDialog(usuario_dao=usuario_dao)
    controlador_pr = ControlardorPantallaReservaciones(reservacion_dao=reservacion_dao)
    controlador_pc = ControladorPantallaCorridas(corrida_dao=corrida_dao)
    controlador_pa = ControladorPantallaAutobuses(autobus_dao=autobus_dao)
    # controlador_prutas ahora se inicializa sin app_manager
    controlador_prutas = ControladorPantallaRutas(ruta_dao=ruta_dao, ciudad_dao=ciudad_dao) 
    controlador_po = ControladorPantallaOperadores(operador_dao=operador_dao)
    controlador_pp = ControladorPantallaPasajeros(pasajero_dao=pasajero_dao)
    controlador_pcidad = ControladorPantallaCiudad(ciudad_dao=ciudad_dao) 
    controlador_viajar = ControladorViajar(viajar_dao=viajar_dao) # Agregado por Hector :3

    #iniciando app manager
    app_manager = AppManager(controlador_index=controlador_index, controlador_isd=controlador_isd, controlador_rd=controlador_rd, 
                            controlador_pr=controlador_pr, controlador_pc=controlador_pc, controlador_pa=controlador_pa, 
                            controlador_prutas=controlador_prutas, controlador_po=controlador_po, controlador_pp=controlador_pp,
                            controlador_pcidad=controlador_pcidad) 
    
    # ⭐ NUEVO: Inyectar controlador de viajar (despues de crear app_manager)
    app_manager.controlador_viajar = controlador_viajar
    
    #iniciando UI
    print('Iniciando UI')
    
    contador = 0
    while True: # Bucle principal de navegación 
        contador+=1
        #Si es la primera vez abre el dialog, si no, no lo hace, para no duplicar dialogs
        if contador == 1:        
            dialog_iniciosesion = InicioSesionDialog(app_manager)
            resultado = dialog_iniciosesion.exec()

        if resultado == InicioSesionDialog.ENTRAR_VISTA_EMPRESA:
            # Si el login es exitoso, salimos del bucle para abrir la app principal
            print("Abriendo la vista empresa...")
            main_window = MainUIEmpresa(app_manager)
            main_window.show()
            exit_code = app.exec() #Inica el bucle de la app   
            break 
        
        elif resultado == InicioSesionDialog.ENTRAR_VISTA_CLIENTE:
            # Si el login es exitoso, salimos del bucle para abrir la app principal
            print("Abriendo la vista cliente...")
            main_window = MainUIUsuario()
            main_window.show()
            exit_code = app.exec() #Inica el bucle de la app
            break

        elif resultado == RegistroDialog.ABRIR_INICIO_SESION_DIALOG:
            resultado = dialog_iniciosesion.exec()

        elif resultado == QDialog.Rejected:
            # Si el usuario cerro el dialogo (con la 'X' o 'Cancelar')
            # el bucle termina y la app se cierra limpiamente.
            print("Login cancelado o cerrado. Saliendo de la aplicación.")
            Connection.closeConnection() # Cerramos la conexión aquí
            sys.exit(0) # Salimos directamente    

    #cerrando conexion a la BD
    Connection.closeConnection()

    #Cerrando sistema
    print('Cerrando el sistema...')
    sys.exit(exit_code)


if __name__ == '__main__':
    main()