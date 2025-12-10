#imports de pyside
import os
from PySide6.QtWidgets import (QApplication, QMainWindow, QStackedWidget, QWidget,QVBoxLayout,
                            QDialog, QPushButton, QLineEdit, QLabel, QMessageBox)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, QCoreApplication, Qt
from PySide6.QtGui import QCloseEvent
from utilidades.validaciones import Validaciones
from controladores.controlador_actualizar_corr_estado_dialog import ControladorActualizarCorrEstadoDialog


class PantallaCorridas(QWidget):

    def __init__(self, controlador, app_manager=None, parent=None):
        super().__init__(parent)
        self.controlador = controlador
        self.app_manager = app_manager  # NUEVO - Para acceder a controlador_viajar

        # Crear una instancia del loader
        loader = QUiLoader()
        

        # Esto construye la ruta correcta sin importar desde donde se ejecute el script
        path = os.path.join(os.path.dirname(__file__),"pantalla_corridas.ui")
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

        # Registrar la vista con el controlador
        if self.controlador:
            self.controlador.set_vista(self)

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
        self.boton_estadoCorr = self.ui.findChild(QPushButton, 'boton_estadoCorr')
        self.boton_ver_asientos = self.ui.findChild(QPushButton, 'boton_verAsientosCorrida')  # NUEVO - Botón ver asientos
        
        # NUEVO - Conectar botón ver asientos
        if self.boton_ver_asientos:
            self.boton_ver_asientos.clicked.connect(self.ver_asientos_corrida)
        
        # if self.boton_crear_reservacion:
            # Si el boton continuar fue recuperado as True, entonces ejecuata el metodo determinado.
            # self.boton_crear_reservacion.clicked.connect(self.crearReservacion)

    def ver_asientos_corrida(self):
        """
        NUEVO MÉTODO: Abre el diálogo de solo lectura para visualizar asientos.
        Se activa al hacer clic en boton_estadoCorr_2 (Ver asientos).
        """
        # Obtener la tabla de corridas desde el controlador
        tabla_corridas = self.controlador.tabla_corridas
        
        if not tabla_corridas:
            QMessageBox.warning(
                self,
                "Error",
                "No se pudo acceder a la tabla de corridas."
            )
            return
        
        # Obtener la fila seleccionada
        fila_actual = tabla_corridas.currentRow()
        
        if fila_actual < 0:
            QMessageBox.warning(
                self,
                "Sin selección",
                "Por favor, selecciona una corrida de la tabla para ver sus asientos."
            )
            return
        
        # Obtener el número de corrida de la columna 0
        item_numero_corrida = tabla_corridas.item(fila_actual, 0)
        
        if not item_numero_corrida:
            QMessageBox.warning(
                self,
                "Error",
                "No se pudo obtener el número de corrida."
            )
            return
        
        try:
            numero_corrida = int(item_numero_corrida.text())
            print(f"Abriendo visualización de asientos para corrida #{numero_corrida}")
            
            # Verificar que tenemos app_manager
            if not self.app_manager:
                QMessageBox.critical(
                    self,
                    "Error de configuración",
                    "No se puede abrir el diálogo de asientos. Falta configuración del sistema."
                )
                return
            
            # Abrir el diálogo de solo lectura
            from vista.empresa.verAsientosDialog import VerAsientosDialog
            
            dialog = VerAsientosDialog(
                self.app_manager,
                numero_corrida,
                self
            )
            dialog.exec()
            
        except ValueError:
            QMessageBox.warning(
                self,
                "Error",
                "El número de corrida no es válido."
            )
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"No se pudo abrir el diálogo de asientos:\n{str(e)}"
            )
            print(f"Error al abrir diálogo de asientos: {e}")
            import traceback
            traceback.print_exc()
        

    def crearReservacion(self):
        pass
        # abre el dialog
        #self.controlador.mostrarCrearReservacion()
    
    def cargar_interfaces(self):
        pass


    def setup_connections(self):
        pass