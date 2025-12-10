# vista/empresa/pantalla_consulta9.py

from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QHeaderView, QTableWidget # Added QHeaderView
from PySide6.QtCore import QDate, Qt
from PySide6.QtGui import QPainter, QColor
from vista.empresa.pantalla_consulta9_ui import Ui_pantalla_consulta9

class PantallaConsulta9(QWidget):
    def __init__(self, app_manager=None):
        super().__init__()
        self.app_manager = app_manager
        self.ui = Ui_pantalla_consulta9()
        self.ui.setupUi(self)
        self._setup_ui_logic() # Call the new setup method

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor('white'))
        
    def _setup_ui_logic(self):
        # Populate comboBox_filtroDestinoCorr
        self.ui.comboBox_filtroDestinoCorr.clear()
        self.ui.comboBox_filtroDestinoCorr.addItem("TODOS")

        # Check if app_manager and its components are available
        if self.app_manager and hasattr(self.app_manager, 'controlador_pc') and hasattr(self.app_manager.controlador_pc, 'corrida_dao'):
            corrida_dao = self.app_manager.controlador_pc.corrida_dao
            
            # Get distinct origin cities from corrida_dao
            origin_cities = corrida_dao.obtener_ciudades_origen_distintas()
            
            for city_name in origin_cities:
                self.ui.comboBox_filtroDestinoCorr.addItem(city_name)
        else:
            QMessageBox.critical(self, "Error de Inicialización", "No se pudo acceder a los datos de corridas. AppManager o CorridaDAO no disponible.")
            print("ERROR: AppManager or CorridaDAO not available in _setup_ui_logic.")

        # Hide the vertical header (row counter)
        self.ui.QtableWidget_corridas.verticalHeader().setVisible(False)
        
        # Set resize mode for horizontal header sections to Fixed to prevent user resizing.
        self.ui.QtableWidget_corridas.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        
        # Set specific widths for each column to sum to 1050px
        self.ui.QtableWidget_corridas.setColumnWidth(0, 215) # Salida
        self.ui.QtableWidget_corridas.setColumnWidth(1, 215) # Corrida
        self.ui.QtableWidget_corridas.setColumnWidth(2, 215) # Destino
        self.ui.QtableWidget_corridas.setColumnWidth(3, 215) # Autobús
        self.ui.QtableWidget_corridas.setColumnWidth(4, 215) # Matrícula
        self.ui.QtableWidget_corridas.setColumnWidth(5, 215) # Operador
        
        # Make the table non-editable
        self.ui.QtableWidget_corridas.setEditTriggers(QTableWidget.NoEditTriggers)
        
        # Manually center the table horizontally
        parent_width = 1920 
        table_width = self.ui.QtableWidget_corridas.width() # Current width from setGeometry is 1290
        x_position = (parent_width - table_width) / 2
        
        # Apply new geometry, keeping original y, height, and width
        self.ui.QtableWidget_corridas.setGeometry(int(x_position), 360, 1290, 551)
        
        # Set dateEdit to current date
        self.ui.dateEdit.setDate(QDate.currentDate())

        # Connect signals
        self.ui.dateEdit.dateChanged.connect(self._update_and_filter_corridas)
        self.ui.comboBox_filtroDestinoCorr.currentIndexChanged.connect(self._update_and_filter_corridas)

        # Initial load
        self._update_and_filter_corridas()

    def _update_and_filter_corridas(self):
        selected_date = self.ui.dateEdit.date().toString("yyyy-MM-dd")
        selected_origin_city = self.ui.comboBox_filtroDestinoCorr.currentText()

        # Actualizar el label_origen con la ciudad seleccionada
        if selected_origin_city == "TODOS":
            self.ui.label_origen.setText("") # Limpiar si se selecciona "TODOS"
        else:
            self.ui.label_origen.setText(selected_origin_city)

        if not self.app_manager or not hasattr(self.app_manager, 'controlador_pc') or not hasattr(self.app_manager.controlador_pc, 'corrida_dao'):
            QMessageBox.critical(self, "Error", "AppManager o CorridaDAO no está disponible.")
            print("ERROR: AppManager or CorridaDAO not available.")
            return

        corrida_dao = self.app_manager.controlador_pc.corrida_dao
        
        # Si se selecciona "TODOS" no filtrar por ciudad de origen
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
            
            # Columns: "Salida", "Corrida", "Destino", "Autobús", "Matrícula", "Operador"
            # Based on retranslateUi from pantalla_consulta9_ui.py
            
            # "Salida" (fecha_hora_salida)
            item_fecha_hora_salida = QTableWidgetItem(str(corrida['fecha_hora_salida']))
            item_fecha_hora_salida.setTextAlignment(Qt.AlignCenter)
            self.ui.QtableWidget_corridas.setItem(row_num, 0, item_fecha_hora_salida)
            
            # "Corrida" (numero_viaje)
            item_numero_viaje = QTableWidgetItem(str(corrida['numero_viaje']))
            item_numero_viaje.setTextAlignment(Qt.AlignCenter)
            self.ui.QtableWidget_corridas.setItem(row_num, 1, item_numero_viaje)
            
            # "Destino" (ciudad_destino)
            item_ciudad_destino = QTableWidgetItem(corrida['ciudad_destino'])
            item_ciudad_destino.setTextAlignment(Qt.AlignCenter)
            self.ui.QtableWidget_corridas.setItem(row_num, 2, item_ciudad_destino)
            
            # "Autobús" (autobus_numero)
            item_autobus_numero = QTableWidgetItem(str(corrida['autobus_numero']))
            item_autobus_numero.setTextAlignment(Qt.AlignCenter)
            self.ui.QtableWidget_corridas.setItem(row_num, 3, item_autobus_numero)
            
            # "Matrícula" (matricula)
            item_matricula = QTableWidgetItem(corrida['matricula'])
            item_matricula.setTextAlignment(Qt.AlignCenter)
            self.ui.QtableWidget_corridas.setItem(row_num, 4, item_matricula)
            
            # "Operador" (nombre_operador)
            item_nombre_operador = QTableWidgetItem(corrida['nombre_operador'])
            item_nombre_operador.setTextAlignment(Qt.AlignCenter)
            self.ui.QtableWidget_corridas.setItem(row_num, 5, item_nombre_operador)