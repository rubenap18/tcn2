#imports de pyside
import os
from PySide6.QtWidgets import (QApplication, QMainWindow, QStackedWidget, QWidget,QVBoxLayout,
                            QDialog, QPushButton, QLineEdit, QLabel, QMessageBox)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, QCoreApplication, Qt
from PySide6.QtGui import QCloseEvent
from utilidades.validaciones import Validaciones


class PantallaPasajeros(QWidget):

    def __init__(self, controlador, parent=None):
        super().__init__(parent)
        self.controlador = controlador

        # Crear una instancia del loader
        loader = QUiLoader()

        # Esto construye la ruta correcta sin importar desde donde se ejecute el script
        path = os.path.join(os.path.dirname(__file__),"pantalla_pasajeros.ui")
        ui_file = QFile(path)

        # 3. Abrir el archivo.
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Error: No se puede abrir el archivo UI en: {path}")
            # Si no se carga el UI, no tiene sentido continuar
            return

        # 4. Cargar el UI. El loader devuelve un NUEVO WIDGET.
        # Guardamos este widget en una variable de instancia (self.ui) para que no sea eliminado
        # por el recolector de basura. Este es un paso FUNDAMENTAL.
        self.ui = loader.load(ui_file, self)
        ui_file.close()

        # --- Integración del widget cargado en este QDialog ---

        # 5. Crear un layout para nuestro QDialog.
        #    El QDialog está vacío por defecto, necesitamos un layout para organizar su contenido.
        layout = QVBoxLayout()

        # 6. Añadir el widget que cargamos (self.ui) al layout.
        layout.addWidget(self.ui)

        # 7. Establecer el layout en nuestro QDialog. Ahora el contenido del .ui es visible.
        self.setLayout(layout)

        # Opcional: Ajustar el tamaño del diálogo al contenido del UI
        self.resize(self.ui.size())

        #Obteniendo componentes del .ui
        # self.boton_crear_reservacion = self.ui.findChild(QPushButton,'boton_crear_reservacion')
        # self.boton_editar_reservacion = self.ui.findChild(QPushButton,'boton_editar_reservacion')
        
        
        # if self.boton_crear_reservacion:
            # Si el boton continuar fue recuperado as True, entonces ejecuata el metodo determinado.
            # self.boton_crear_reservacion.clicked.connect(self.crearReservacion)

    #Metodos para los botones y demas componentes de la UI