from PySide6.QtWidgets import QDialog, QMessageBox
from vista.empresa.corridaDialog_ui import Ui_Form
from dao.autobus_dao import AutobusDAO
from dao.operador_dao import OperadorDAO
from dao.corrida_dao import CorridaDAO
from objetos.autobus import Autobus
from objetos.Operador import Operador
import re # For route parsing

class ControladorCorridaDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.autobus_dao = AutobusDAO()
        self.operador_dao = OperadorDAO()
        self.corrida_dao = CorridaDAO()

        self.buses = [] # To store Autobus objects
        self.operadores = [] # To store Operador objects

        self.init_ui_connections()
        self.load_initial_data()

    def init_ui_connections(self):
        self.ui.dateEdit_fechaCorrida.dateChanged.connect(self.update_available_resources)
        self.ui.boton_crearCorrida.clicked.connect(self.crear_corrida)
        self.ui.boton_cancelar.clicked.connect(self.reject) 

    def load_initial_data(self):
        
        self.ui.dateEdit_fechaCorrida.setDate(self.ui.dateEdit_fechaCorrida.minimumDate())
        self.update_available_resources()
        self.populate_ruta_combobox() 

    def populate_ruta_combobox(self):
        #
        if self.ui.comboBox_rutaCorrida.count() > 0 and self.ui.comboBox_rutaCorrida.itemText(0) == "Ruta":
            self.ui.comboBox_rutaCorrida.removeItem(0) 
        self.ui.comboBox_rutaCorrida.setCurrentIndex(-1) 

    def update_available_resources(self):
        selected_date = self.ui.dateEdit_fechaCorrida.date().toString("yyyy-MM-dd")
        self.populate_autobus_combobox(selected_date)
        self.populate_operador_combobox(selected_date)

    def populate_autobus_combobox(self, selected_date):
        self.ui.comboBox_autobusCorrida.clear()
        all_buses = self.autobus_dao.listar_autobuses()
        
        print(f"DEBUG CTLR: all_buses retrieved: {all_buses}") 
        
        self.buses = all_buses 
        
        if not all_buses:
            self.ui.comboBox_autobusCorrida.addItem("No hay autobuses registrados")
            self.ui.comboBox_autobusCorrida.setEnabled(False)
            print("DEBUG CTLR: ComboBox autobus deshabilitado (no hay autobuses registrados).") 
        else:
            self.ui.comboBox_autobusCorrida.setEnabled(True)
            print("DEBUG CTLR: ComboBox autobus habilitado. Agregando autobuses...") 
            for bus in all_buses: # Iterate through all buses
                self.ui.comboBox_autobusCorrida.addItem(f"{bus.get_numero()} - {bus.get_marca()} {bus.get_modelo()} ({bus.get_matricula()})", bus)
            self.ui.comboBox_autobusCorrida.setCurrentIndex(-1) 

    def populate_operador_combobox(self, selected_date):
        self.ui.comboBox_operadorCorrida.clear()
        all_operadores = self.operador_dao.listar_operadores()
        available_operadores = []

        for operador in all_operadores:
            if not self.corrida_dao.operador_ocupado_en_fecha(operador.get_numero(), selected_date):
                available_operadores.append(operador)
        
        self.operadores = available_operadores 

        if not available_operadores:
            self.ui.comboBox_operadorCorrida.addItem("No hay operadores disponibles para esta fecha")
            self.ui.comboBox_operadorCorrida.setEnabled(False)
        else:
            self.ui.comboBox_operadorCorrida.setEnabled(True)
            for operador in available_operadores:
                self.ui.comboBox_operadorCorrida.addItem(f"{operador.get_numero()} - {operador.get_nombre_completo()}", operador)
            self.ui.comboBox_operadorCorrida.setCurrentIndex(-1) # No selection initially

    def get_selected_autobus(self):
        selected_index = self.ui.comboBox_autobusCorrida.currentIndex()
        if selected_index >= 0 and self.ui.comboBox_autobusCorrida.itemData(selected_index):
            return self.ui.comboBox_autobusCorrida.itemData(selected_index)
        return None

    def get_selected_operador(self):
        selected_index = self.ui.comboBox_operadorCorrida.currentIndex()
        if selected_index >= 0 and self.ui.comboBox_operadorCorrida.itemData(selected_index):
            return self.ui.comboBox_operadorCorrida.itemData(selected_index)
        return None
    
    def get_selected_ruta_codigo(self):
        selected_text = self.ui.comboBox_rutaCorrida.currentText()
        if selected_text and selected_text != "Ruta": # Avoid placeholder
            # Assuming format like "TIJ-TEC", we want "TIJ-TEC"
            return selected_text
        return None

    def crear_corrida(self):
        ruta_codigo = self.get_selected_ruta_codigo()
        fecha = self.ui.dateEdit_fechaCorrida.date().toString("yyyy-MM-dd")
        hora_salida = self.ui.timeEdit_horaSalCorrida.time().toString("HH:mm:ss")
        hora_llegada = self.ui.timeEdit_horaLegCorrida.time().toString("HH:mm:ss")
        precio_text = self.ui.lineEdit_precioCorrida.text()
        
        selected_operador = self.get_selected_operador()
        selected_autobus = self.get_selected_autobus()

        # Input validation
        if not ruta_codigo:
            QMessageBox.warning(self, "Error de Validación", "Por favor, seleccione una ruta.")
            return
        if not selected_autobus:
            QMessageBox.warning(self, "Error de Validación", "Por favor, seleccione un autobús.")
            return
        if not selected_operador:
            QMessageBox.warning(self, "Error de Validación", "Por favor, seleccione un operador.")
            return
        
        try:
            precio = float(precio_text)
            if precio <= 0:
                raise ValueError("El precio debe ser un número positivo.")
        except ValueError:
            QMessageBox.warning(self, "Error de Validación", "Por favor, ingrese un precio válido.")
            return
        
        operador_numero = selected_operador.get_numero()
        autobus_numero = selected_autobus.get_numero()
        lugares_disponibles = selected_autobus.get_cantAsientos() # Get capacity from selected bus
        estado = 'ACT' # Default state for new corridas

        if self.corrida_dao.crear_corrida(ruta_codigo, fecha, hora_salida, hora_llegada, precio, operador_numero, autobus_numero, lugares_disponibles, estado):
            QMessageBox.information(self, "Éxito", "Corrida creada exitosamente.")
            self.accept() # Close the dialog on success
        else:
            QMessageBox.critical(self, "Error", "No se pudo crear la corrida. Verifique los datos e intente de nuevo.")
