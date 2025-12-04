import os
from PySide6.QtWidgets import (QApplication, QMainWindow, QStackedWidget, QWidget,QVBoxLayout,
                            QDialog, QPushButton, QLineEdit, QLabel)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, QCoreApplication, Qt
from PySide6.QtGui import QCloseEvent


class MainUIUsuario(QMainWindow):
    def __init__(self, app_manager): #AGREGAR app_manager como parámetro
        super().__init__()
        self.app_manager = app_manager  # GUARDAR app_manager
        
        # Configurar stacked widget
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        #Varibales para que el recolector de basura no haga su chamba
        self.index_ui = None
        
        # Cargar todas las interfaces
        self.cargar_interfaces()
        self.setup_connections()  

        # Mostrar MainWindow por defecto (índice 0)
        self.stacked_widget.setCurrentIndex(0)
        self.setWindowTitle('Transportes Cuervo Negro - Usuario')
        self.showMaximized()

    def cargar_interfaces(self):
        # Cargar todas las interfaces
        base_path = os.path.dirname(__file__) # Ruta del directorio de main_ui.py
        # Cargar el resto de interfaces con rutas absolutas
        self.index_ui = self.load_ui(os.path.join(base_path,'usuario','index.ui'))
                                                    
        # Agregar al stacked widget en orden (el índice 0 ya está ocupado por main_index_widget)
        if self.index_ui: self.stacked_widget.addWidget(self.index_ui) #Index 0
        
    def load_ui(self, ui_path):
        file = QFile(ui_path)
        if not file.open(QFile.ReadOnly):
            print(f"ERROR: No se pudo abrir el archivo UI: {ui_path}")
            return None # Retorna None explícitamente en caso de error
        
        loader = QUiLoader()
        ui = loader.load(file)
        file.close()
        return ui
    
    def abrir_pantalla_viajar(self):
        """Abre la pantalla de búsqueda de viajes."""
        
        from vista.compartido.pantalla_viajar import PantallaViajarWidget
        
        pantalla = PantallaViajarWidget(self.app_manager, self)
        pantalla.show()

    def setup_connections(self):
        
        if self.index_ui:
            boton_viajar = self.index_ui.findChild(QWidget, "boton_viajar")
            if boton_viajar:
                boton_viajar.clicked.connect(self.abrir_pantalla_viajar)
            else:
                print(" ADVERTENCIA: No se encontró el botón 'boton_viajar' en el UI")
        
        


    def closeEvent(self, event: QCloseEvent):
        """
        Este metodo que se llama cuando se preciona la X en esta ventana.
        """
        print("Terminando programa.")

        event.accept() 
        
        #Nota: Luego de esto event.accept(), el flujo del programa regresa al main.py