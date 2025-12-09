from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QAbstractItemView
from PySide6.QtCore import QDate
from vista.empresa.pantalla_consulta6_ui import Ui_pantalla_consulta6

class PantallaConsulta6(QWidget):
    def __init__(self, app_manager=None):
        super().__init__()
        self.app_manager = app_manager
        self.ui = Ui_pantalla_consulta6()
        self.ui.setupUi(self)

        # Initialize dateEdit with current date
        self.ui.dateEdit.setDate(QDate.currentDate())
        
        # Set up table headers
        self.ui.QtableWidget_corridas.setColumnCount(7)
        self.ui.QtableWidget_corridas.setHorizontalHeaderLabels([
            "Corrida", "Salida", "Origen", "Destino",
            "Autobús", "Boletos Vendidos", "Boletos Disponibles"
        ])
        self.ui.QtableWidget_corridas.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.QtableWidget_corridas.verticalHeader().setVisible(False)
        self.ui.QtableWidget_corridas.setColumnWidth(0, 200)
        self.ui.QtableWidget_corridas.setColumnWidth(1, 200)
        self.ui.QtableWidget_corridas.setColumnWidth(2, 200)
        self.ui.QtableWidget_corridas.setColumnWidth(3, 200)
        self.ui.QtableWidget_corridas.setColumnWidth(4, 200)
        self.ui.QtableWidget_corridas.setColumnWidth(5, 200)
        self.ui.QtableWidget_corridas.setColumnWidth(6, 200)


        # Connect signals
        self.ui.dateEdit.dateChanged.connect(self._update_and_filter_corridas)

        # Initial call to populate data
        self._update_and_filter_corridas()

    def _update_and_filter_corridas(self):
        selected_date = self.ui.dateEdit.date().toString("yyyy-MM-dd")
        self.ui.lineEdit_fecha.setText(selected_date)

        if not self.app_manager or not hasattr(self.app_manager, 'controlador_pc') or not hasattr(self.app_manager.controlador_pc, 'corrida_dao'):
            QMessageBox.critical(self, "Error", "AppManager o CorridaDAO no está disponible.")
            return

        corrida_dao = self.app_manager.controlador_pc.corrida_dao
        filtered_corridas = corrida_dao.obtener_corridas_detalladas_por_fecha_y_origen(selected_date, None)
            
        self._populate_table(filtered_corridas)

    def _populate_table(self, corridas):
        self.ui.QtableWidget_corridas.setRowCount(0)

        if not corridas:
            return

        for row_num, corrida in enumerate(corridas):
            self.ui.QtableWidget_corridas.insertRow(row_num)
            self.ui.QtableWidget_corridas.setItem(row_num, 0, QTableWidgetItem(str(corrida['numero_viaje'])))
            self.ui.QtableWidget_corridas.setItem(row_num, 1, QTableWidgetItem(str(corrida['fecha_hora_salida'])))
            self.ui.QtableWidget_corridas.setItem(row_num, 2, QTableWidgetItem(corrida['ciudad_origen']))
            self.ui.QtableWidget_corridas.setItem(row_num, 3, QTableWidgetItem(corrida['ciudad_destino']))
            self.ui.QtableWidget_corridas.setItem(row_num, 4, QTableWidgetItem(str(corrida['autobus_numero'])))
            self.ui.QtableWidget_corridas.setItem(row_num, 5, QTableWidgetItem(str(corrida['boletos_vendidos'])))
            self.ui.QtableWidget_corridas.setItem(row_num, 6, QTableWidgetItem(str(corrida['boletos_disponibles'])))