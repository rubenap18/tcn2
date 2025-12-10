# vista/empresa/pantalla_consulta6.py

from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QHeaderView # Added QHeaderView
from PySide6.QtCore import QDate, Qt
from PySide6.QtGui import QPainter, QColor
from vista.empresa.pantalla_consulta6_ui import Ui_Form

class PantallaConsulta6(QWidget):
    def __init__(self, app_manager=None):
        super().__init__()
        self.app_manager = app_manager
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self._setup_ui_logic() # Call the new setup method

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor('white'))
        
    def _setup_ui_logic(self):
        # Hide the vertical header (row counter)
        self.ui.QtableWidget_corridas.verticalHeader().setVisible(False)
        
        # Make columns stretch to fill available width
        self.ui.QtableWidget_corridas.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        # Manually center the table horizontally
        # Get the parent (Form) width. self.width() gives the widget's current width.
        # Initial Form size is 1920x1080 as per .ui file
        parent_width = 1920 
        table_width = self.ui.QtableWidget_corridas.width() # Current width from setGeometry is 1270
        x_position = (parent_width - table_width) / 2
        
        # Apply new geometry, keeping original y, height, and width
        self.ui.QtableWidget_corridas.setGeometry(int(x_position), 360, 1270, 551)
        
        # Set dateEdit to current date
        self.ui.dateEdit.setDate(QDate.currentDate())
        
        # Connect signals
        self.ui.dateEdit.dateChanged.connect(self._update_and_filter_corridas_by_date)
        
        # Initial load
        self._update_and_filter_corridas_by_date()

    def _update_and_filter_corridas_by_date(self):
        selected_date = self.ui.dateEdit.date()
        selected_date_str = selected_date.toString("yyyy-MM-dd")

        # Update label_fecha
        self.ui.label_fecha.setText(selected_date.toString("dd-MM-yyyy"))

        if not self.app_manager or not hasattr(self.app_manager, 'controlador_pc') or not hasattr(self.app_manager.controlador_pc, 'corrida_dao'):
            QMessageBox.critical(self, "Error", "AppManager o CorridaDAO no está disponible.")
            print("ERROR: AppManager or CorridaDAO not available.")
            return

        corrida_dao = self.app_manager.controlador_pc.corrida_dao
        
        # Use existing method, passing None for origin city to get all for the date
        filtered_corridas = corrida_dao.obtener_corridas_detalladas_por_fecha_y_origen(selected_date_str, None)
            
        self._populate_table(filtered_corridas)

    def _populate_table(self, corridas):
        # Clear existing data
        self.ui.QtableWidget_corridas.setRowCount(0)

        if not corridas:
            return

        for row_num, corrida in enumerate(corridas):
            self.ui.QtableWidget_corridas.insertRow(row_num)
            
            # Columns: "Corrida", "Salida", "Origen", "Destino", "Autobús", "Boletos Vendidos", "Boletos disponibles"
            # Based on retranslateUi from pantalla_consulta6_ui.py
            
            # "Corrida" (numero_viaje)
            item_corrida = QTableWidgetItem(str(corrida['numero_viaje']))
            item_corrida.setTextAlignment(Qt.AlignCenter)
            self.ui.QtableWidget_corridas.setItem(row_num, 0, item_corrida)
            
            # "Salida" (fecha_hora_salida)
            item_salida = QTableWidgetItem(str(corrida['fecha_hora_salida']))
            item_salida.setTextAlignment(Qt.AlignCenter)
            self.ui.QtableWidget_corridas.setItem(row_num, 1, item_salida)

            # "Origen" (ciudad_origen)
            item_origen = QTableWidgetItem(corrida['ciudad_origen'])
            item_origen.setTextAlignment(Qt.AlignCenter)
            self.ui.QtableWidget_corridas.setItem(row_num, 2, item_origen)
            
            # "Destino" (ciudad_destino)
            item_destino = QTableWidgetItem(corrida['ciudad_destino'])
            item_destino.setTextAlignment(Qt.AlignCenter)
            self.ui.QtableWidget_corridas.setItem(row_num, 3, item_destino)
            
            # "Autobús" (autobus_numero)
            item_autobus = QTableWidgetItem(str(corrida['autobus_numero']))
            item_autobus.setTextAlignment(Qt.AlignCenter)
            self.ui.QtableWidget_corridas.setItem(row_num, 4, item_autobus)
            
            # "Boletos Vendidos" (boletos_vendidos)
            item_boletos_vendidos = QTableWidgetItem(str(corrida['boletos_vendidos']))
            item_boletos_vendidos.setTextAlignment(Qt.AlignCenter)
            self.ui.QtableWidget_corridas.setItem(row_num, 5, item_boletos_vendidos)
            
            # "Boletos disponibles" (boletos_disponibles)
            item_boletos_disponibles = QTableWidgetItem(str(corrida['boletos_disponibles']))
            item_boletos_disponibles.setTextAlignment(Qt.AlignCenter)
            self.ui.QtableWidget_corridas.setItem(row_num, 6, item_boletos_disponibles)
