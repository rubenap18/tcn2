# vista/main_ui_empresa.py

import os
from PySide6.QtWidgets import (QApplication, QMainWindow, QStackedWidget, QWidget,QVBoxLayout,
                            QDialog, QPushButton, QLineEdit, QLabel)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, QCoreApplication, Qt
from PySide6.QtGui import QCloseEvent

#importaciones de las pantallas de vista empresa y vista usuario
from vista.empresa.pantalla_reservaciones import PantallaReservaciones
from vista.empresa.pantalla_corridas import PantallaCorridas
from vista.empresa.pantalla_autobuses import PantallaAutobuses
from vista.empresa.pantalla_rutas import PantallaRutas
from vista.empresa.pantalla_operadores import PantallaOperadores
from vista.empresa.pantalla_pasajeros import PantallaPasajeros
from vista.empresa.pantalla_index import PantallaIndex
from vista.empresa.pantalla_consulta9 import PantallaConsulta9
from vista.empresa.pantalla_consulta6 import PantallaConsulta6
from vista.empresa.pantalla_operadorescorridas import PantallaOperadoresCorridas


class MainUIEmpresa(QMainWindow):
    
    def __init__(self, app_manager):
        super().__init__()
        self.app_manager = app_manager
        
        # Configurar stacked widget
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        #Varibales para que el recolector de basura no haga su chamba
        self.index_ui = None
        self.pagina_autobuses_widget = None
        self.pagina_corridas_widget = None
        self.pagina_operadores_widget = None
        self.pagina_pasajeros_widget = None
        self.pagina_reservaciones_widget = None
        self.pagina_rutas_widget = None
        self.pagina_consulta9_widget = None
        self.pagina_consulta6_widget = None
        self.pagina_operadores_corridas_widget = None
        
        # Cargar todas las interfaces
        self.cargar_interfaces()
        self.setup_connections_pantalla_index()
        self.setup_connections_pantalla_reservaciones()
        self.setup_connections_pantalla_corridas()
        self.setup_connections_pantalla_autobuses()
        self.setup_connections_pantalla_rutas()
        self.setup_connections_pantalla_operadores()
        self.setup_connections_pantalla_pasajeros()
        self.setup_connections_pantalla_consulta9()
        self.setup_connections_pantalla_consulta6()
        self.setup_connections_pantalla_operadores_corridas()


        # Mostrar MainWindow por defecto (índice 0)
        self.stacked_widget.setCurrentIndex(0)
        self.setWindowTitle('Transportes Cuervo Negro - Administrador')
        self.showMaximized()

        
    def cargar_interfaces(self):
        # Cargar todas las interfaces
        base_path = os.path.dirname(__file__) # Ruta del directorio de main_ui.py
        
        # Pasar app_manager a PantallaIndex
        self.index_ui = PantallaIndex(self.app_manager.controlador_index, self.app_manager)
        
        # ACTUALIZADO - Pasar app_manager a PantallaReservaciones
        self.pagina_reservaciones_widget = PantallaReservaciones(self.app_manager.controlador_pr, self.app_manager)
        self.pagina_corridas_widget = PantallaCorridas(self.app_manager.controlador_pc)
        self.pagina_autobuses_widget = PantallaAutobuses(self.app_manager.controlador_pa)
        self.pagina_rutas_widget = PantallaRutas(self.app_manager)
        self.pagina_operadores_widget = PantallaOperadores(self.app_manager.controlador_po, self.app_manager)
        self.pagina_pasajeros_widget = PantallaPasajeros(self.app_manager.controlador_pp)
        self.pagina_consulta9_widget = PantallaConsulta9(self.app_manager)
        self.pagina_consulta6_widget = PantallaConsulta6(self.app_manager)
        self.pagina_operadores_corridas_widget = PantallaOperadoresCorridas(self.app_manager.controlador_index, None)
                                                    
        # Agregar al stacked widget en orden
        if self.index_ui: self.stacked_widget.addWidget(self.index_ui)
        if self.pagina_reservaciones_widget: self.stacked_widget.addWidget(self.pagina_reservaciones_widget)
        if self.pagina_corridas_widget: self.stacked_widget.addWidget(self.pagina_corridas_widget)
        if self.pagina_autobuses_widget: self.stacked_widget.addWidget(self.pagina_autobuses_widget)
        if self.pagina_rutas_widget: self.stacked_widget.addWidget(self.pagina_rutas_widget)
        if self.pagina_operadores_widget: self.stacked_widget.addWidget(self.pagina_operadores_widget)
        if self.pagina_pasajeros_widget: self.stacked_widget.addWidget(self.pagina_pasajeros_widget)
        if self.pagina_consulta9_widget: self.stacked_widget.addWidget(self.pagina_consulta9_widget)
        if self.pagina_consulta6_widget: self.stacked_widget.addWidget(self.pagina_consulta6_widget)
        if self.pagina_operadores_corridas_widget: self.stacked_widget.addWidget(self.pagina_operadores_corridas_widget)

    
    def load_ui(self, ui_path):
        file = QFile(ui_path)
        if not file.open(QFile.ReadOnly):
            print(f"ERROR: No se pudo abrir el archivo UI: {ui_path}")
            return None
        
        loader = QUiLoader()
        ui = loader.load(file)
        file.close()
        return ui
    
    def abrir_pantalla_viajar(self):
        """Abre la pantalla de compra de boletos."""
        from vista.compartido.pantalla_viajar import PantallaViajarWidget
        
        pantalla = PantallaViajarWidget(self.app_manager, self)
        pantalla.show()

    def setup_connections_pantalla_index(self):
        '''Agregando evento a los botones de navegacion del index.ui'''
        # Si el boton de inicio es presionado
        if self.index_ui:
            boton_inicio = self.index_ui.findChild(QWidget, "boton_inicio")
            if boton_inicio:
                boton_inicio.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        
        # Si el boton reservaciones es presionado
        if self.pagina_reservaciones_widget:
            boton_reservaciones = self.index_ui.findChild(QWidget, "boton_reservaciones")
            if boton_reservaciones:
                boton_reservaciones.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))

        # Si el boton corridas es presionado
        if self.pagina_corridas_widget:
            boton_corridas = self.index_ui.findChild(QWidget, "boton_corridas")
            if boton_corridas:
                boton_corridas.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))

        # Si el boton autobuses es presionado
        if self.pagina_autobuses_widget:
            boton_autobuses = self.index_ui.findChild(QWidget, "boton_autobuses")
            if boton_autobuses:
                boton_autobuses.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(3))

        # Si el boton rutas es presionado
        if self.pagina_rutas_widget:
            boton_rutas = self.index_ui.findChild(QWidget, "boton_rutas")
            if boton_rutas:
                boton_rutas.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(4))

        # Si el boton operadores es presionado
        if self.pagina_operadores_widget:
            boton_operadores = self.index_ui.findChild(QWidget, "boton_operadores")
            if boton_operadores:
                boton_operadores.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(5))
        
        # Si el boton comprar boleto es presionado
        boton_comprar_boleto = self.index_ui.findChild(QWidget, "boton_comprarboleto")
        if boton_comprar_boleto:
            boton_comprar_boleto.clicked.connect(self.abrir_pantalla_viajar)


    def setup_connections_pantalla_reservaciones(self):
        '''Agregando evento a los botones de navegacion del pantalla_reservaciones.ui'''
        # Si el boton de inicio es presionado
        if self.index_ui:
            boton_inicio = self.pagina_reservaciones_widget.findChild(QWidget, "boton_inicio")
            if boton_inicio:
                boton_inicio.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        
        # Si el boton reservaciones es presionado
        if self.pagina_reservaciones_widget:
            boton_reservaciones = self.pagina_reservaciones_widget.findChild(QWidget, "boton_reservaciones")
            if boton_reservaciones:
                boton_reservaciones.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))

        # Si el boton corridas es presionado
        if self.pagina_corridas_widget:
            boton_corridas = self.pagina_reservaciones_widget.findChild(QWidget, "boton_corridas")
            if boton_corridas:
                boton_corridas.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))

        # Si el boton autobuses es presionado
        if self.pagina_autobuses_widget:
            boton_autobuses = self.pagina_reservaciones_widget.findChild(QWidget, "boton_autobuses")
            if boton_autobuses:
                boton_autobuses.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(3))

        # Si el boton rutas es presionado
        if self.pagina_rutas_widget:
            boton_rutas = self.pagina_reservaciones_widget.findChild(QWidget, "boton_rutas")
            if boton_rutas:
                boton_rutas.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(4))

        # Si el boton operadores es presionado
        if self.pagina_operadores_widget:
            boton_operadores = self.pagina_reservaciones_widget.findChild(QWidget, "boton_operadores")
            if boton_operadores:
                boton_operadores.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(5))


    def setup_connections_pantalla_corridas(self):
        '''Agregando evento a los botones de navegacion de pantalla_corridas.ui'''
        # Si el boton de inicio es presionado
        if self.index_ui:
            boton_inicio = self.pagina_corridas_widget.findChild(QWidget, "boton_inicio")
            if boton_inicio:
                boton_inicio.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        
        # Si el boton reservaciones es presionado
        if self.pagina_reservaciones_widget:
            boton_reservaciones = self.pagina_corridas_widget.findChild(QWidget, "boton_reservaciones")
            if boton_reservaciones:
                boton_reservaciones.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))

        # Si el boton corridas es presionado
        if self.pagina_corridas_widget:
            boton_corridas = self.pagina_corridas_widget.findChild(QWidget, "boton_corridas")
            if boton_corridas:
                boton_corridas.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))

        # Si el boton autobuses es presionado
        if self.pagina_autobuses_widget:
            boton_autobuses = self.pagina_corridas_widget.findChild(QWidget, "boton_autobuses")
            if boton_autobuses:
                boton_autobuses.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(3))

        # Si el boton rutas es presionado
        if self.pagina_rutas_widget:
            boton_rutas = self.pagina_corridas_widget.findChild(QWidget, "boton_rutas")
            if boton_rutas:
                boton_rutas.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(4))

        # Si el boton operadores es presionado
        if self.pagina_operadores_widget:
            boton_operadores = self.pagina_corridas_widget.findChild(QWidget, "boton_operadores")
            if boton_operadores:
                boton_operadores.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(5))        
        
        # Si el boton_verCiudadFechaCorr es presionado
        if self.pagina_corridas_widget:
            boton_verCiudadFechaCorr = self.pagina_corridas_widget.findChild(QWidget, "boton_verCiudadFechaCorr")
            if boton_verCiudadFechaCorr:
                boton_verCiudadFechaCorr.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(7))

        # Si el boton_verBoletosVendidosCorr es presionado
        if self.pagina_corridas_widget:
            boton_verBoletosVendidosCorr = self.pagina_corridas_widget.findChild(QWidget, "boton_verBoletosVendidosCorr")
            if boton_verBoletosVendidosCorr:
                boton_verBoletosVendidosCorr.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(8))


    def setup_connections_pantalla_autobuses(self):
        '''Agregando evento a los botones de navegacion de pantalla_autobuses.ui'''
        # Si el boton de inicio es presionado
        if self.index_ui:
            boton_inicio = self.pagina_autobuses_widget.findChild(QWidget, "boton_inicio")
            if boton_inicio:
                boton_inicio.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        
        # Si el boton reservaciones es presionado
        if self.pagina_reservaciones_widget:
            boton_reservaciones = self.pagina_autobuses_widget.findChild(QWidget, "boton_reservaciones")
            if boton_reservaciones:
                boton_reservaciones.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))

        # Si el boton corridas es presionado
        if self.pagina_corridas_widget:
            boton_corridas = self.pagina_autobuses_widget.findChild(QWidget, "boton_corridas")
            if boton_corridas:
                boton_corridas.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))

        # Si el boton autobuses es presionado
        if self.pagina_autobuses_widget:
            boton_autobuses = self.pagina_autobuses_widget.findChild(QWidget, "boton_autobuses")
            if boton_autobuses:
                boton_autobuses.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(3))

        # Si el boton rutas es presionado
        if self.pagina_rutas_widget:
            boton_rutas = self.pagina_autobuses_widget.findChild(QWidget, "boton_rutas")
            if boton_rutas:
                boton_rutas.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(4))

        # Si el boton operadores es presionado
        if self.pagina_operadores_widget:
            boton_operadores = self.pagina_autobuses_widget.findChild(QWidget, "boton_operadores")
            if boton_operadores:
                boton_operadores.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(5))  


    def setup_connections_pantalla_rutas(self):
        '''Agregando evento a los botones de navegacion de pantalla_rutas.ui'''
        # Si el boton de inicio es presionado
        if self.index_ui:
            boton_inicio = self.pagina_rutas_widget.findChild(QWidget, "boton_inicio")
            if boton_inicio:
                boton_inicio.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        
        # Si el boton reservaciones es presionado
        if self.pagina_reservaciones_widget:
            boton_reservaciones = self.pagina_rutas_widget.findChild(QWidget, "boton_reservaciones")
            if boton_reservaciones:
                boton_reservaciones.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))

        # Si el boton corridas es presionado
        if self.pagina_corridas_widget:
            boton_corridas = self.pagina_rutas_widget.findChild(QWidget, "boton_corridas")
            if boton_corridas:
                boton_corridas.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))

        # Si el boton autobuses es presionado
        if self.pagina_autobuses_widget:
            boton_autobuses = self.pagina_rutas_widget.findChild(QWidget, "boton_autobuses")
            if boton_autobuses:
                boton_autobuses.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(3))

        # Si el boton rutas es presionado
        if self.pagina_rutas_widget:
            boton_rutas = self.pagina_rutas_widget.findChild(QWidget, "boton_rutas")
            if boton_rutas:
                boton_rutas.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(4))

        # Si el boton operadores es presionado
        if self.pagina_operadores_widget:
            boton_operadores = self.pagina_rutas_widget.findChild(QWidget, "boton_operadores")
            if boton_operadores:
                boton_operadores.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(5))        


    def setup_connections_pantalla_operadores(self):
        '''Agregando evento a los botones de navegacion de pantalla_operadores.ui'''
        # Si el boton de inicio es presionado
        if self.pagina_operadores_widget:
            boton_inicio = self.pagina_operadores_widget.findChild(QWidget, "boton_inicio")
            if boton_inicio:
                boton_inicio.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        
        # Si el boton reservaciones es presionado
        if self.pagina_operadores_widget:
            boton_reservaciones = self.pagina_operadores_widget.findChild(QWidget, "boton_reservaciones")
            if boton_reservaciones:
                boton_reservaciones.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))

        # Si el boton corridas es presionado
        if self.pagina_operadores_widget:
            boton_corridas = self.pagina_operadores_widget.findChild(QWidget, "boton_corridas")
            if boton_corridas:
                boton_corridas.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))

        # Si el boton autobuses es presionado
        if self.pagina_operadores_widget:
            boton_autobuses = self.pagina_operadores_widget.findChild(QWidget, "boton_autobuses")
            if boton_autobuses:
                boton_autobuses.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(3))

        # Si el boton rutas es presionado
        if self.pagina_operadores_widget:
            boton_rutas = self.pagina_operadores_widget.findChild(QWidget, "boton_rutas")
            if boton_rutas:
                boton_rutas.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(4))

        # Si el boton operadores es presionado
        if self.pagina_operadores_widget:
            boton_operadores = self.pagina_operadores_widget.findChild(QWidget, "boton_operadores")
            if boton_operadores:
                boton_operadores.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(5))  

    def setup_connections_pantalla_pasajeros(self):
        '''Agregando evento a los botones de navegacion de pantalla_pasajeros.ui'''
        # Si el boton de inicio es presionado
        if self.index_ui:
            boton_inicio = self.pagina_pasajeros_widget.findChild(QWidget, "boton_inicio")
            if boton_inicio:
                boton_inicio.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        
        # Si el boton reservaciones es presionado
        if self.pagina_reservaciones_widget:
            boton_reservaciones = self.pagina_pasajeros_widget.findChild(QWidget, "boton_reservaciones")
            if boton_reservaciones:
                boton_reservaciones.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))

        # Si el boton corridas es presionado
        if self.pagina_corridas_widget:
            boton_corridas = self.pagina_pasajeros_widget.findChild(QWidget, "boton_corridas")
            if boton_corridas:
                boton_corridas.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))

        # Si el boton autobuses es presionado
        if self.pagina_autobuses_widget:
            boton_autobuses = self.pagina_pasajeros_widget.findChild(QWidget, "boton_autobuses")
            if boton_autobuses:
                boton_autobuses.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(3))

        # Si el boton rutas es presionado
        if self.pagina_rutas_widget:
            boton_rutas = self.pagina_pasajeros_widget.findChild(QWidget, "boton_rutas")
            if boton_rutas:
                boton_rutas.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(4))

        # Si el boton operadores es presionado
        if self.pagina_operadores_widget:
            boton_operadores = self.pagina_pasajeros_widget.findChild(QWidget, "boton_operadores")
            if boton_operadores:
                boton_operadores.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(5)) 


    def setup_connections_pantalla_consulta9(self):
        '''Agregando evento a los botones de navegacion de pantalla_consulta9.ui'''
        if self.pagina_consulta9_widget:
            # Common navigation buttons
            common_buttons = {
                "boton_inicio": 0,
                "boton_reservaciones": 1,
                "boton_corridas": 2,
                "boton_autobuses": 3,
                "boton_rutas": 4,
                "boton_operadores": 5,
                "boton_pasajeros": 6,
                "boton_consulta9": 7,  # Self-reference
            }
            for btn_name, index in common_buttons.items():
                boton = self.pagina_consulta9_widget.findChild(QWidget, btn_name)
                if boton:
                    boton.clicked.connect(lambda _, idx=index: self.stacked_widget.setCurrentIndex(idx))

            # Connect boton_inicio_2 to go back to pantalla_corridas
            boton_inicio_2 = self.pagina_consulta9_widget.findChild(QWidget, "boton_inicio_2")
            if boton_inicio_2:
                boton_inicio_2.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2)) # Index for pantalla_corridas


    def setup_connections_pantalla_consulta6(self):
        '''Agregando evento a los botones de navegacion de pantalla_consulta6.ui'''
        if self.pagina_consulta6_widget:
            # Common navigation buttons
            common_buttons = {
                "boton_inicio": 0,
                "boton_reservaciones": 1,
                "boton_corridas": 2,
                "boton_autobuses": 3,
                "boton_rutas": 4,
                "boton_operadores": 5,
                "boton_pasajeros": 6,
                "boton_consulta9": 7,
                "boton_consulta6": 8,  # Self-reference
            }
            for btn_name, index in common_buttons.items():
                boton = self.pagina_consulta6_widget.findChild(QWidget, btn_name)
                if boton:
                    boton.clicked.connect(lambda _, idx=index: self.stacked_widget.setCurrentIndex(idx))

            # Connect boton_inicio_2 to go back to pantalla_corridas
            boton_inicio_2 = self.pagina_consulta6_widget.findChild(QWidget, "boton_inicio_2")
            if boton_inicio_2:
                boton_inicio_2.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2)) # Index for pantalla_corridas

    def setup_connections_pantalla_operadores_corridas(self):
        pass


    def closeEvent(self, event: QCloseEvent):
        """
        Este metodo que se llama cuando se preciona la X en esta ventana.
        """
        print("Terminando programa.")
        event.accept() 
        
# vista/main_ui_empresa.py

import os
from PySide6.QtWidgets import (QApplication, QMainWindow, QStackedWidget, QWidget,QVBoxLayout,
                            QDialog, QPushButton, QLineEdit, QLabel)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, QCoreApplication, Qt
from PySide6.QtGui import QCloseEvent

#importaciones de las pantallas de vista empresa y vista usuario
from vista.empresa.pantalla_reservaciones import PantallaReservaciones
from vista.empresa.pantalla_corridas import PantallaCorridas
from vista.empresa.pantalla_autobuses import PantallaAutobuses
from vista.empresa.pantalla_rutas import PantallaRutas
from vista.empresa.pantalla_operadores import PantallaOperadores
from vista.empresa.pantalla_pasajeros import PantallaPasajeros
from vista.empresa.pantalla_index import PantallaIndex
from vista.empresa.pantalla_operadorescorridas import PantallaOperadoresCorridas

class MainUIEmpresa(QMainWindow):
    
    def __init__(self, app_manager):
        super().__init__()
        self.app_manager = app_manager
        
        # Configurar stacked widget
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        #Varibales para que el recolector de basura no haga su chamba
        self.index_ui = None
        self.pagina_autobuses_widget = None
        self.pagina_corridas_widget = None
        self.pagina_operadores_widget = None
        self.pagina_pasajeros_widget = None
        self.pagina_reservaciones_widget = None
        self.pagina_rutas_widget = None
        self.pagina_operadores_corridas_widget = None
        
        # Cargar todas las interfaces
        self.cargar_interfaces()
        self.setup_connections_pantalla_index()
        self.setup_connections_pantalla_reservaciones()
        self.setup_connections_pantalla_corridas()
        self.setup_connections_pantalla_autobuses()
        self.setup_connections_pantalla_rutas()
        self.setup_connections_pantalla_operadores()
        self.setup_connections_pantalla_pasajeros()

        # Mostrar MainWindow por defecto (índice 0)
        self.stacked_widget.setCurrentIndex(0)
        self.setWindowTitle('Transportes Cuervo Negro - Administrador')
        self.showMaximized()

        
    def cargar_interfaces(self):
        # Cargar todas las interfaces
        base_path = os.path.dirname(__file__) # Ruta del directorio de main_ui.py
        
        # Pasar app_manager a PantallaIndex
        self.index_ui = PantallaIndex(self.app_manager.controlador_index, self.app_manager)
        
        # ACTUALIZADO - Pasar app_manager a PantallaReservaciones
        self.pagina_reservaciones_widget = PantallaReservaciones(self.app_manager.controlador_pr, self.app_manager)
        self.pagina_corridas_widget = PantallaCorridas(self.app_manager.controlador_pc)
        self.pagina_autobuses_widget = PantallaAutobuses(self.app_manager.controlador_pa)
        self.pagina_rutas_widget = PantallaRutas(self.app_manager)
        self.pagina_operadores_widget = PantallaOperadores(self.app_manager.controlador_po, self.app_manager)
        self.pagina_pasajeros_widget = PantallaPasajeros(self.app_manager.controlador_pp)
        self.pagina_operadores_corridas_widget = PantallaOperadoresCorridas(self.app_manager.controlador_index, None)
                                                    
        # Agregar al stacked widget en orden
        if self.index_ui: self.stacked_widget.addWidget(self.index_ui)
        if self.pagina_reservaciones_widget: self.stacked_widget.addWidget(self.pagina_reservaciones_widget)
        if self.pagina_corridas_widget: self.stacked_widget.addWidget(self.pagina_corridas_widget)
        if self.pagina_autobuses_widget: self.stacked_widget.addWidget(self.pagina_autobuses_widget)
        if self.pagina_rutas_widget: self.stacked_widget.addWidget(self.pagina_rutas_widget)
        if self.pagina_operadores_widget: self.stacked_widget.addWidget(self.pagina_operadores_widget)
        if self.pagina_pasajeros_widget: self.stacked_widget.addWidget(self.pagina_pasajeros_widget)
        if self.pagina_operadores_corridas_widget: self.stacked_widget.addWidget(self.pagina_operadores_corridas_widget)

    
    def load_ui(self, ui_path):
        file = QFile(ui_path)
        if not file.open(QFile.ReadOnly):
            print(f"ERROR: No se pudo abrir el archivo UI: {ui_path}")
            return None
        
        loader = QUiLoader()
        ui = loader.load(file)
        file.close()
        return ui
    
    def abrir_pantalla_viajar(self):
        """Abre la pantalla de compra de boletos."""
        from vista.compartido.pantalla_viajar import PantallaViajarWidget
        
        pantalla = PantallaViajarWidget(self.app_manager, self)
        pantalla.show()

    def setup_connections_pantalla_index(self):
        '''Agregando evento a los botones de navegacion del index.ui'''
        # Si el boton de inicio es presionado
        if self.index_ui:
            boton_inicio = self.index_ui.findChild(QWidget, "boton_inicio")
            if boton_inicio:
                boton_inicio.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        
        # Si el boton reservaciones es presionado
        if self.pagina_reservaciones_widget:
            boton_reservaciones = self.index_ui.findChild(QWidget, "boton_reservaciones")
            if boton_reservaciones:
                boton_reservaciones.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))

        # Si el boton corridas es presionado
        if self.pagina_corridas_widget:
            boton_corridas = self.index_ui.findChild(QWidget, "boton_corridas")
            if boton_corridas:
                boton_corridas.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))

        # Si el boton autobuses es presionado
        if self.pagina_autobuses_widget:
            boton_autobuses = self.index_ui.findChild(QWidget, "boton_autobuses")
            if boton_autobuses:
                boton_autobuses.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(3))

        # Si el boton rutas es presionado
        if self.pagina_rutas_widget:
            boton_rutas = self.index_ui.findChild(QWidget, "boton_rutas")
            if boton_rutas:
                boton_rutas.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(4))

        # Si el boton operadores es presionado
        if self.pagina_operadores_widget:
            boton_operadores = self.index_ui.findChild(QWidget, "boton_operadores")
            if boton_operadores:
                boton_operadores.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(5))
        
        # Si el boton comprar boleto es presionado
        boton_comprar_boleto = self.index_ui.findChild(QWidget, "boton_comprarboleto")
        if boton_comprar_boleto:
            boton_comprar_boleto.clicked.connect(self.abrir_pantalla_viajar)


    def setup_connections_pantalla_reservaciones(self):
        '''Agregando evento a los botones de navegacion del pantalla_reservaciones.ui'''
        # Si el boton de inicio es presionado
        if self.index_ui:
            boton_inicio = self.pagina_reservaciones_widget.findChild(QWidget, "boton_inicio")
            if boton_inicio:
                boton_inicio.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        
        # Si el boton reservaciones es presionado
        if self.pagina_reservaciones_widget:
            boton_reservaciones = self.pagina_reservaciones_widget.findChild(QWidget, "boton_reservaciones")
            if boton_reservaciones:
                boton_reservaciones.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))

        # Si el boton corridas es presionado
        if self.pagina_corridas_widget:
            boton_corridas = self.pagina_reservaciones_widget.findChild(QWidget, "boton_corridas")
            if boton_corridas:
                boton_corridas.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))

        # Si el boton autobuses es presionado
        if self.pagina_autobuses_widget:
            boton_autobuses = self.pagina_reservaciones_widget.findChild(QWidget, "boton_autobuses")
            if boton_autobuses:
                boton_autobuses.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(3))

        # Si el boton rutas es presionado
        if self.pagina_rutas_widget:
            boton_rutas = self.pagina_reservaciones_widget.findChild(QWidget, "boton_rutas")
            if boton_rutas:
                boton_rutas.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(4))

        # Si el boton operadores es presionado
        if self.pagina_operadores_widget:
            boton_operadores = self.pagina_reservaciones_widget.findChild(QWidget, "boton_operadores")
            if boton_operadores:
                boton_operadores.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(5))


    def setup_connections_pantalla_corridas(self):
        '''Agregando evento a los botones de navegacion de pantalla_corridas.ui'''
        # Si el boton de inicio es presionado
        if self.index_ui:
            boton_inicio = self.pagina_corridas_widget.findChild(QWidget, "boton_inicio")
            if boton_inicio:
                boton_inicio.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        
        # Si el boton reservaciones es presionado
        if self.pagina_reservaciones_widget:
            boton_reservaciones = self.pagina_corridas_widget.findChild(QWidget, "boton_reservaciones")
            if boton_reservaciones:
                boton_reservaciones.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))

        # Si el boton corridas es presionado
        if self.pagina_corridas_widget:
            boton_corridas = self.pagina_corridas_widget.findChild(QWidget, "boton_corridas")
            if boton_corridas:
                boton_corridas.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))

        # Si el boton autobuses es presionado
        if self.pagina_autobuses_widget:
            boton_autobuses = self.pagina_corridas_widget.findChild(QWidget, "boton_autobuses")
            if boton_autobuses:
                boton_autobuses.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(3))

        # Si el boton rutas es presionado
        if self.pagina_rutas_widget:
            boton_rutas = self.pagina_corridas_widget.findChild(QWidget, "boton_rutas")
            if boton_rutas:
                boton_rutas.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(4))

        # Si el boton operadores es presionado
        if self.pagina_operadores_widget:
            boton_operadores = self.pagina_corridas_widget.findChild(QWidget, "boton_operadores")
            if boton_operadores:
                boton_operadores.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(5))        


    def setup_connections_pantalla_autobuses(self):
        '''Agregando evento a los botones de navegacion de pantalla_autobuses.ui'''
        # Si el boton de inicio es presionado
        if self.index_ui:
            boton_inicio = self.pagina_autobuses_widget.findChild(QWidget, "boton_inicio")
            if boton_inicio:
                boton_inicio.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        
        # Si el boton reservaciones es presionado
        if self.pagina_reservaciones_widget:
            boton_reservaciones = self.pagina_autobuses_widget.findChild(QWidget, "boton_reservaciones")
            if boton_reservaciones:
                boton_reservaciones.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))

        # Si el boton corridas es presionado
        if self.pagina_corridas_widget:
            boton_corridas = self.pagina_autobuses_widget.findChild(QWidget, "boton_corridas")
            if boton_corridas:
                boton_corridas.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))

        # Si el boton autobuses es presionado
        if self.pagina_autobuses_widget:
            boton_autobuses = self.pagina_autobuses_widget.findChild(QWidget, "boton_autobuses")
            if boton_autobuses:
                boton_autobuses.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(3))

        # Si el boton rutas es presionado
        if self.pagina_rutas_widget:
            boton_rutas = self.pagina_autobuses_widget.findChild(QWidget, "boton_rutas")
            if boton_rutas:
                boton_rutas.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(4))

        # Si el boton operadores es presionado
        if self.pagina_operadores_widget:
            boton_operadores = self.pagina_autobuses_widget.findChild(QWidget, "boton_operadores")
            if boton_operadores:
                boton_operadores.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(5))  


    def setup_connections_pantalla_rutas(self):
        '''Agregando evento a los botones de navegacion de pantalla_rutas.ui'''
        # Si el boton de inicio es presionado
        if self.index_ui:
            boton_inicio = self.pagina_rutas_widget.findChild(QWidget, "boton_inicio")
            if boton_inicio:
                boton_inicio.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        
        # Si el boton reservaciones es presionado
        if self.pagina_reservaciones_widget:
            boton_reservaciones = self.pagina_rutas_widget.findChild(QWidget, "boton_reservaciones")
            if boton_reservaciones:
                boton_reservaciones.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))

        # Si el boton corridas es presionado
        if self.pagina_corridas_widget:
            boton_corridas = self.pagina_rutas_widget.findChild(QWidget, "boton_corridas")
            if boton_corridas:
                boton_corridas.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))

        # Si el boton autobuses es presionado
        if self.pagina_autobuses_widget:
            boton_autobuses = self.pagina_rutas_widget.findChild(QWidget, "boton_autobuses")
            if boton_autobuses:
                boton_autobuses.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(3))

        # Si el boton rutas es presionado
        if self.pagina_rutas_widget:
            boton_rutas = self.pagina_rutas_widget.findChild(QWidget, "boton_rutas")
            if boton_rutas:
                boton_rutas.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(4))

        # Si el boton operadores es presionado
        if self.pagina_operadores_widget:
            boton_operadores = self.pagina_rutas_widget.findChild(QWidget, "boton_operadores")
            if boton_operadores:
                boton_operadores.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(5))        


    def setup_connections_pantalla_operadores(self):
        '''Agregando evento a los botones de navegacion de pantalla_operadores.ui'''
        # Si el boton de inicio es presionado
        if self.pagina_operadores_widget:
            boton_inicio = self.pagina_operadores_widget.findChild(QWidget, "boton_inicio")
            if boton_inicio:
                boton_inicio.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        
        # Si el boton reservaciones es presionado
        if self.pagina_operadores_widget:
            boton_reservaciones = self.pagina_operadores_widget.findChild(QWidget, "boton_reservaciones")
            if boton_reservaciones:
                boton_reservaciones.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))

        # Si el boton corridas es presionado
        if self.pagina_operadores_widget:
            boton_corridas = self.pagina_operadores_widget.findChild(QWidget, "boton_corridas")
            if boton_corridas:
                boton_corridas.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))

        # Si el boton autobuses es presionado
        if self.pagina_operadores_widget:
            boton_autobuses = self.pagina_operadores_widget.findChild(QWidget, "boton_autobuses")
            if boton_autobuses:
                boton_autobuses.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(3))

        # Si el boton rutas es presionado
        if self.pagina_operadores_widget:
            boton_rutas = self.pagina_operadores_widget.findChild(QWidget, "boton_rutas")
            if boton_rutas:
                boton_rutas.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(4))

        # Si el boton operadores es presionado
        if self.pagina_operadores_widget:
            boton_operadores = self.pagina_operadores_widget.findChild(QWidget, "boton_operadores")
            if boton_operadores:
                boton_operadores.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(5))  

    def setup_connections_pantalla_pasajeros(self):
        '''Agregando evento a los botones de navegacion de pantalla_pasajeros.ui'''
        # Si el boton de inicio es presionado
        if self.index_ui:
            boton_inicio = self.pagina_pasajeros_widget.findChild(QWidget, "boton_inicio")
            if boton_inicio:
                boton_inicio.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        
        # Si el boton reservaciones es presionado
        if self.pagina_reservaciones_widget:
            boton_reservaciones = self.pagina_pasajeros_widget.findChild(QWidget, "boton_reservaciones")
            if boton_reservaciones:
                boton_reservaciones.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))

        # Si el boton corridas es presionado
        if self.pagina_corridas_widget:
            boton_corridas = self.pagina_pasajeros_widget.findChild(QWidget, "boton_corridas")
            if boton_corridas:
                boton_corridas.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))

        # Si el boton autobuses es presionado
        if self.pagina_autobuses_widget:
            boton_autobuses = self.pagina_pasajeros_widget.findChild(QWidget, "boton_autobuses")
            if boton_autobuses:
                boton_autobuses.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(3))

        # Si el boton rutas es presionado
        if self.pagina_rutas_widget:
            boton_rutas = self.pagina_pasajeros_widget.findChild(QWidget, "boton_rutas")
            if boton_rutas:
                boton_rutas.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(4))

        # Si el boton operadores es presionado
        if self.pagina_operadores_widget:
            boton_operadores = self.pagina_pasajeros_widget.findChild(QWidget, "boton_operadores")
            if boton_operadores:
                boton_operadores.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(5)) 


    def closeEvent(self, event: QCloseEvent):
        """
        Este metodo que se llama cuando se preciona la X en esta ventana.
        """
        print("Terminando programa.")
        event.accept() 
        
        #Nota: Luego de esto event.accept(), el flujo del programa regresa al main.py