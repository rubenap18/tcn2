from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QAbstractItemView
from PySide6.QtCore import QDate
from vista.empresa.pantalla_consulta9_ui import Ui_pantalla_consulta9

class PantallaConsulta9(QWidget):
    def __init__(self, app_manager=None):
        super().__init__()
        self.app_manager = app_manager
        self.ui = Ui_pantalla_consulta9()
        self.ui.setupUi(self)

        # Initialize dateEdit with current date
        self.ui.dateEdit.setDate(QDate.currentDate())
        
        # Set up table headers
        self.ui.QtableWidget_corridas.setColumnCount(6)
        self.ui.QtableWidget_corridas.setHorizontalHeaderLabels([
            "Fecha y Hora de Salida", "Corrida", "Destino",
            "Num. Autobús", "Matrícula Autobús", "Operador"
        ])
        self.ui.QtableWidget_corridas.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.QtableWidget_corridas.verticalHeader().setVisible(False)
        self.ui.QtableWidget_corridas.setColumnWidth(0, 220) # Fecha y Hora de Salida (increased)
        self.ui.QtableWidget_corridas.setColumnWidth(1, 150) # Número de Corrida (increased)
        self.ui.QtableWidget_corridas.setColumnWidth(2, 180) # Ciudad de Destino (increased)
        self.ui.QtableWidget_corridas.setColumnWidth(3, 180) # Número de Autobús (increased)
        self.ui.QtableWidget_corridas.setColumnWidth(4, 180) # Matrícula de Autobús (increased)
        self.ui.QtableWidget_corridas.setColumnWidth(5, 280) # Nombre del Operador (increased)

        # Connect signals
        self.ui.comboBox_filtroDestinoCorr.currentIndexChanged.connect(self._update_and_filter_corridas)
        self.ui.dateEdit.dateChanged.connect(self._update_and_filter_corridas)

        # Initial call to populate data
        self._update_and_filter_corridas()

    def _update_and_filter_corridas(self):
        
        selected_date = self.ui.dateEdit.date().toString("yyyy-MM-dd")
        selected_origin_city = self.ui.comboBox_filtroDestinoCorr.currentText()


        # Actualizar el lineEdit de origen con la ciudad seleccionada
        if selected_origin_city == "TODOS":
            self.ui.lineEdit_origen.setText("") # Limpiar si se selecciona "TODOS"
        else:
            self.ui.lineEdit_origen.setText(selected_origin_city)

        if not self.app_manager or not hasattr(self.app_manager, 'controlador_pc') or not hasattr(self.app_manager.controlador_pc, 'corrida_dao'):
            QMessageBox.critical(self, "Error", "AppManager o CorridaDAO no está disponible.")
            print("ERROR: AppManager or CorridaDAO not available.")
            return

        corrida_dao = self.app_manager.controlador_pc.corrida_dao
        
        # Si se selecciona :TODOS" no filtrar por ciudad de origen
        if selected_origin_city == "TODOS":
            filtered_corridas = corrida_dao.obtener_corridas_detalladas_por_fecha_y_origen(selected_date, None)
        else:
            filtered_corridas = corrida_dao.obtener_corridas_detalladas_por_fecha_y_origen(selected_date, selected_origin_city)
            
        self._populate_table(filtered_corridas)

    def _populate_table(self, corridas):
        self.ui.QtableWidget_corridas.setRowCount(0) # Limpiar datos

        if not corridas:
            return

        for row_num, corrida in enumerate(corridas):
            self.ui.QtableWidget_corridas.insertRow(row_num)
            self.ui.QtableWidget_corridas.setItem(row_num, 0, QTableWidgetItem(str(corrida['fecha_hora_salida'])))
            self.ui.QtableWidget_corridas.setItem(row_num, 1, QTableWidgetItem(str(corrida['numero_viaje'])))
            self.ui.QtableWidget_corridas.setItem(row_num, 2, QTableWidgetItem(corrida['ciudad_destino']))
            self.ui.QtableWidget_corridas.setItem(row_num, 3, QTableWidgetItem(str(corrida['autobus_numero'])))
            self.ui.QtableWidget_corridas.setItem(row_num, 4, QTableWidgetItem(corrida['matricula']))
            self.ui.QtableWidget_corridas.setItem(row_num, 5, QTableWidgetItem(corrida['nombre_operador']))