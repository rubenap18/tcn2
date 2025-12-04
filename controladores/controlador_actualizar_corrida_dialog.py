from PySide6.QtWidgets import QDialog, QMessageBox
from vista.empresa.actualizarCorridaDialog_ui import Ui_Form # Correct import
from dao.autobus_dao import AutobusDAO
from dao.operador_dao import OperadorDAO
from dao.corrida_dao import CorridaDAO
from objetos.autobus import Autobus
from objetos.Operador import Operador


class ControladorActualizarCorridaDialog(QDialog):
    def __init__(self, parent=None, corrida_data=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.autobus_dao = AutobusDAO()
        self.operador_dao = OperadorDAO()
        self.corrida_dao = CorridaDAO()
        self.corrida_data = corrida_data # Data of the corrida to be updated

        self.buses = [] # To store Autobus objects
        self.operadores = [] # To store Operador objects

        self.init_ui_connections()
        self.load_initial_data()
        if self.corrida_data:
            self.populate_form_with_corrida_data()

    def init_ui_connections(self):
        self.ui.boton_actualizarCorrida.clicked.connect(self.actualizar_corrida)
        self.ui.boton_cancelarActualizacion.clicked.connect(self.reject)

    def load_initial_data(self):
        self.populate_operador_combobox()

    def populate_form_with_corrida_data(self):
        # Assuming corrida_data is a dictionary with details
        if not self.corrida_data:
            return
        
        # Select operador
        operador_numero = self.corrida_data['operador_numero']
        for i in range(self.ui.comboBox_operadorCorrida.count()):
            item_data = self.ui.comboBox_operadorCorrida.itemData(i)
            if item_data and item_data.get_numero() == operador_numero:
                self.ui.comboBox_operadorCorrida.setCurrentIndex(i)
                break








    def populate_operador_combobox(self):
        self.ui.comboBox_operadorCorrida.clear()
        all_operadores = self.operador_dao.listar_operadores()
        
        self.operadores = all_operadores # Store all operators

        if not all_operadores:
            self.ui.comboBox_operadorCorrida.addItem("No hay operadores registrados")
            self.ui.comboBox_operadorCorrida.setEnabled(False)
        else:
            self.ui.comboBox_operadorCorrida.setEnabled(True)
            for operador in all_operadores:
                self.ui.comboBox_operadorCorrida.addItem(f"{operador.get_numero()} - {operador.get_nombre_completo()}", operador)



    def get_selected_operador(self):
        selected_index = self.ui.comboBox_operadorCorrida.currentIndex()
        if selected_index >= 0 and self.ui.comboBox_operadorCorrida.itemData(selected_index):
            return self.ui.comboBox_operadorCorrida.itemData(selected_index)
        return None
    


    def actualizar_corrida(self):
        if not self.corrida_data or 'numero_viaje' not in self.corrida_data:
            QMessageBox.critical(self, "Error", "No se proporcionaron datos de corrida para actualizar.")
            return

        numero_viaje = self.corrida_data['numero_viaje']
        selected_operador = self.get_selected_operador()

        if not selected_operador:
            QMessageBox.warning(self, "Error de Validación", "Por favor, seleccione un operador.")
            return
        


        operador_numero = selected_operador.get_numero()

        if self.corrida_dao.actualizar_operador_corrida(numero_viaje, operador_numero):
            QMessageBox.information(self, "Éxito", "Operador de corrida actualizado exitosamente.")
            self.accept() # Close the dialog on success
        else:
            QMessageBox.critical(self, "Error", "No se pudo actualizar el operador de la corrida. Verifique los datos e intente de nuevo.")
