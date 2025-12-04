#imports de pyside
import os
from PySide6.QtWidgets import (QApplication, QMainWindow, QStackedWidget, QWidget,QVBoxLayout,
                            QDialog, QPushButton, QLineEdit, QLabel,QMessageBox)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, QCoreApplication, Qt
from PySide6.QtGui import QCloseEvent

# importando validaciones
from utilidades.validaciones import Validaciones

class RegistroDialog(QDialog):
    ABRIR_INICIO_SESION_DIALOG = 25

    def __init__(self, app_manager, parent=None):
        super().__init__(parent)
        self.controlador = app_manager.controlador_rd

        # Crear una instancia del loader
        loader = QUiLoader()

        # Esto construye la ruta correcta sin importar desde donde se ejecute el script
        path = os.path.join(os.path.dirname(__file__), "../vista/registroDialog.ui")
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
        self.setWindowTitle("Registrate") # Puedes ponerlo aquí o en el Designer

        #Obteniendo componentes del .ui
        self.boton_continuar = self.ui.findChild(QPushButton,'boton_continuar')
        self.boton_identificate = self.ui.findChild(QPushButton,'pushButton_estatico_identificate')

        self.lineEdit_telefono = self.ui.findChild(QLineEdit,'lineEdit_telefono')
        self.lineEdit_contrasena = self.ui.findChild(QLineEdit,'lineEdit_contrasena')
        
        if self.boton_continuar:
            # Si el boton continuar fue recuperado as True, entonces ejecuata el metodo determinado.
            self.boton_continuar.clicked.connect(self.registrarUsuario)
            # Si el boton registrar se presiona    
        if self.boton_identificate:
            self.boton_identificate.clicked.connect(self.identificar)
            

    def identificar(self):
        self.reject()

    def registrarUsuario(self):
        # Aqui se valida el num de telefono y el password
        phone = str(self.lineEdit_telefono.text())
        validacion = Validaciones.validarPhone(phone)
        if phone != validacion:
            QMessageBox.warning(self,'Mensaje',validacion)
            return
        
        password = str(self.lineEdit_contrasena.text())
        validacion = Validaciones.validarContrasena(password)
        if password != validacion:
            QMessageBox.warning(self,'Mensaje',validacion)
            return

        respuesta_del_controlador = self.controlador.crearUsuario(phone,password)
        print(respuesta_del_controlador)
        if respuesta_del_controlador:
            QMessageBox.information(self,"Mensaje","Registro exitoso")
        else:
            QMessageBox.critical(self,"Error de registro","Error al registrar al usuario.")

        
        
