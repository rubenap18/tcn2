#imports de pyside
import os
from PySide6.QtWidgets import (QApplication, QMainWindow, QStackedWidget, QWidget,QVBoxLayout,
                            QDialog, QPushButton, QLineEdit, QLabel, QMessageBox)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, QCoreApplication, Qt
from PySide6.QtGui import QCloseEvent
from utilidades.validaciones import Validaciones

#Importando el dialog del registro
from vista.registroDialog import RegistroDialog

class InicioSesionDialog(QDialog):
    #variables de respuestas de este Dialog
    ENTRAR_VISTA_EMPRESA = 20
    ENTRAR_VISTA_CLIENTE = 30
    ENTRAR_DIALOJ_REGISTRO = 40

    def __init__(self, app_manager, parent=None):
        super().__init__(parent)
        self.controlador = app_manager.controlador_isd
        self.app_manager = app_manager #Solo en este caso 

        #Creamos la variable donde se guardara el dialogo por lo del garbage collector
        self.dialogo_registro = None

        # Crear una instancia del loader
        loader = QUiLoader()

        # Esto construye la ruta correcta sin importar desde donde se ejecute el script
        path = os.path.join(os.path.dirname(__file__), "../vista/iniciosesionDialog.ui")
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
        self.setWindowTitle("Inicio de Sesión") # Puedes ponerlo aquí o en el Designer

        #Obteniendo componentes del .ui
        self.boton_continuar = self.ui.findChild(QPushButton,'boton_continuar')
        self.boton_registrate = self.ui.findChild(QPushButton,'boton_registrate')
        self.boton_invitado = self.ui.findChild(QPushButton,'boton_invitado')

        self.lineEdit_telefono = self.ui.findChild(QLineEdit,'lineEdit_telefono')
        self.lineEdit_contrasena = self.ui.findChild(QLineEdit,'lineEdit_contrasena')
        

        
        if self.boton_continuar:
            # Si el boton continuar fue recuperado as True, entonces ejecuata el metodo determinado.
            self.boton_continuar.clicked.connect(self.continuar)
            # Si el boton registrar se presiona    
        if self.boton_registrate:
            self.boton_registrate.clicked.connect(self.abrirDialogRegistro)
            # Si el boton ingresar como invitado se presiona
        if self.boton_invitado:
            self.boton_invitado.clicked.connect(self.ingresarComoInvitado)

    def continuar(self):
        # Aqui se valida el num de telefono y el password
        phone = str(self.lineEdit_telefono.text())
        validacion = Validaciones.validarNumeroDeTelefono(phone)
        if phone != validacion:
            QMessageBox.warning(self, 'Mensaje', validacion)
            return
        
        password = str(self.lineEdit_contrasena.text())
        validacion = Validaciones.validarPassword(password)
        if password != validacion:
            QMessageBox.warning(self, 'Mensaje', validacion)
            return

        # Recibir el usuario y el tipo
        usuario, es_admin = self.controlador.validarInicioSesion(phone, password)
        
        # Si hubo error (usuario es None)
        if usuario is None:
            QMessageBox.information(self, "Mensaje", es_admin)  # es_admin contiene el mensaje de error
            return
        
        # NUEVO: Guardar el usuario en AppManager
        self.app_manager.set_usuario_actual(usuario)
        
        # Cerrar este dialog correctamente
        if es_admin == 1:
            print(f'Admin logueado: {usuario.phone}')
            self.done(self.ENTRAR_VISTA_EMPRESA)
        elif es_admin == 0:
            print(f'Usuario logueado: {usuario.phone}')
            self.done(self.ENTRAR_VISTA_CLIENTE)


    def abrirDialogRegistro(self):
        #En lugar de cerrar este dialog lo ocultamos unos segundillos
        self.hide()

        #Creamos el dialog
        if not self.dialogo_registro:
            self.dialogo_registro = RegistroDialog(self.app_manager)

        # Mostramos el dialog registro
        self.dialogo_registro.exec()
        
        # Mostramos el dialog de login, luego del registro dialog cerrarse. 
        self.show()
        self.done(RegistroDialog.ABRIR_INICIO_SESION_DIALOG)

    def ingresarComoInvitado():
        pass