import os
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QComboBox, QPushButton, QLabel, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, Signal
from dao.corrida_dao import CorridaDAO # Import the DAO

class ControladorActualizarCorrEstadoDialog:
    estado_actualizado = Signal() # Signal to emit when status is updated

    def __init__(self, corrida_dao: CorridaDAO, vista_anterior=None):
        self.dialog = None
        self.vista_anterior = vista_anterior
        self.corrida_data = None
        self.corrida_dao = corrida_dao # Store the DAO instance

        # UI elements
        self.lineEdit_numeroCorrida = None
        self.label_estadoActual = None # To display the current status
        self.comboBox_estadoCorrida = None
        self.boton_actualizar = None
        self.boton_cancelar = None

    def cerrar_dialogo(self):
        if self.dialog:
            self.dialog.close()

    def _setup_ui(self, ui_form):
        self.lineEdit_numeroCorrida = ui_form.findChild(QLineEdit, 'lineEdit_numeroCorrida')
        self.label_estadoActual = ui_form.findChild(QLabel, 'label_estadoActual') # Assuming you have a QLabel with this objectName
        self.comboBox_estadoCorrida = ui_form.findChild(QComboBox, 'comboBox_estadoCorrida')
        self.boton_actualizar = ui_form.findChild(QPushButton, 'boton_actualizar')
        self.boton_cancelar = ui_form.findChild(QPushButton, 'boton_cancelar')

        if self.lineEdit_numeroCorrida:
            self.lineEdit_numeroCorrida.textChanged.connect(self._on_numero_corrida_changed)
        if self.boton_actualizar:
            self.boton_actualizar.clicked.connect(self._actualizar_estado_corrida)
        if self.boton_cancelar:
            self.boton_cancelar.clicked.connect(self.cerrar_dialogo)
        
        # Populate comboBox_estadoCorrida
        if self.comboBox_estadoCorrida:
            self.comboBox_estadoCorrida.clear()
            self.comboBox_estadoCorrida.addItem("ACTIVA")
            self.comboBox_estadoCorrida.addItem("INACTIVA")

    def _on_numero_corrida_changed(self, text):
        if not text.strip():
            self.label_estadoActual.setText("Estado Actual: N/A")
            return

        try:
            numero_viaje = int(text)
            corrida = self.corrida_dao.obtener_corrida_por_numero_viaje(numero_viaje)
            if corrida:
                self.label_estadoActual.setText(f"Estado Actual: {corrida['estado_corrida']}")
                # Set the combobox to the current state (map database code to display text)
                current_estado_db = corrida['estado_corrida']
                display_text = ""
                if current_estado_db == "ACTI":
                    display_text = "ACTIVA"
                elif current_estado_db == "INAC":
                    display_text = "INACTIVA"
                
                if display_text:
                    index = self.comboBox_estadoCorrida.findText(display_text)
                    if index != -1:
                        self.comboBox_estadoCorrida.setCurrentIndex(index)
                else:
                    # If current_estado_db is not 'ACTI' or 'INAC', set to default or clear selection
                    self.comboBox_estadoCorrida.setCurrentIndex(-1) # No selection

            else:
                self.label_estadoActual.setText("Estado Actual: No encontrada")
        except ValueError:
            self.label_estadoActual.setText("Estado Actual: Número inválido")

    def _actualizar_estado_corrida(self):
        numero_viaje_text = self.lineEdit_numeroCorrida.text()
        if not numero_viaje_text.strip():
            QMessageBox.warning(self.dialog, "Error", "Ingrese un número de corrida.")
            return

        try:
            numero_viaje = int(numero_viaje_text)
            nuevo_estado_display = self.comboBox_estadoCorrida.currentText()
            
            # Map displayed text to database value
            estado_db_value = ""
            if nuevo_estado_display == "ACTIVA":
                estado_db_value = "ACTI"
            elif nuevo_estado_display == "INACTIVA":
                estado_db_value = "INAC"
            
            if not estado_db_value: # Should not happen if combobox only has ACTIVA/INACTIVA
                QMessageBox.critical(self.dialog, "Error", "Seleccione un estado válido.")
                return

            if self.corrida_dao.actualizar_estado_corrida(numero_viaje, estado_db_value):
                QMessageBox.information(self.dialog, "Éxito", "Estado de la corrida actualizado correctamente.")
                self.estado_actualizado.emit() # Emit signal on success
                self.cerrar_dialogo()
            else:
                QMessageBox.critical(self.dialog, "Error", "No se pudo actualizar el estado de la corrida.")
        except ValueError:
            QMessageBox.critical(self.dialog, "Error", "Número de corrida inválido.")

    def mostrar_dialogo(self, corrida_data=None):
        self.corrida_data = corrida_data
        
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "vista", "empresa", "actualizarCorrEstadoDialog.ui")
        ui_file = QFile(path)

        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Error: No se puede abrir el archivo UI en: {path}")
            return

        self.dialog = QDialog()
        ui_form = loader.load(ui_file, self.dialog)
        ui_file.close()

        self.dialog.setWindowTitle(ui_form.windowTitle())
        layout = QVBoxLayout(self.dialog)
        layout.addWidget(ui_form)
        self.dialog.setFixedSize(500, 350)
        self.dialog.setModal(True)
        
        self._setup_ui(ui_form)

        if self.corrida_data and 'numero_viaje' in self.corrida_data:
            self.lineEdit_numeroCorrida.setText(str(self.corrida_data['numero_viaje']))
            self._on_numero_corrida_changed(str(self.corrida_data['numero_viaje']))

        self.dialog.exec()
