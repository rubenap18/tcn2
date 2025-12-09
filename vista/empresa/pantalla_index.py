#imports de pyside
import os
from PySide6.QtWidgets import (QApplication, QMainWindow, QStackedWidget, QWidget,QVBoxLayout,
                            QDialog, QPushButton, QLineEdit, QLabel, QMessageBox, QTableWidgetItem, QHeaderView, QAbstractItemView)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, QCoreApplication, Qt
from PySide6.QtGui import QCloseEvent, QFont
from utilidades.validaciones import Validaciones
from vista.empresa.pantalla_operadorescorridas import PantallaOperadoresCorridas


class PantallaIndex(QWidget):

    def __init__(self, controlador, app_manager, parent=None):  # ⭐ AGREGAR app_manager
        super().__init__(parent)
        self.controlador = controlador
        self.app_manager = app_manager  # ⭐ NUEVO: Guardar app_manager

        # Crear una instancia del loader
        loader = QUiLoader()

        # Esto construye la ruta correcta sin importar desde donde se ejecute el script
        path = os.path.join(os.path.dirname(__file__),"pantalla_index.ui")
        ui_file = QFile(path)

        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Error: No se puede abrir el archivo UI en: {path}")
            return
        
        # Cargar el UI en self.ui
        self.ui = loader.load(ui_file, self)
        ui_file.close()

        # Integrar el widget cargado en este QWidget usando un layout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.ui)
        self.setLayout(layout)

        # Configurar las tablas para que no sean editables y los datos estén centrados
        self.ui.QtableWidget_operadores.setColumnCount(2) # Set column count to 2
        self.ui.QtableWidget_operadores.setHorizontalHeaderLabels(["Número", "Nombre Completo"])
        self.ui.QtableWidget_operadores.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.QtableWidget_operadores.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.QtableWidget_operadores.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.selected_operator_id = None
        
        self.ui.QtableWidget_corridasact.setColumnCount(5) # Set column count
        self.ui.QtableWidget_corridasact.setHorizontalHeaderLabels([
            "Corrida", "Fecha y Hora de Salida", "Origen", "Destino", "Autobus"
        ])
        self.ui.QtableWidget_corridasact.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # Set specific resize mode for the "Fecha y Hora de Salida" column (index 1)
        self.ui.QtableWidget_corridasact.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.ui.QtableWidget_corridasact.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.QtableWidget_corridasact.setSelectionBehavior(QAbstractItemView.SelectRows)
        
        self.ui.QtableWidget_pasajeros.setColumnCount(4) # Set column count to 4
        self.ui.QtableWidget_pasajeros.setHorizontalHeaderLabels(["Boleto", "Asiento", "Pasajero", "Edad"])
        self.ui.QtableWidget_pasajeros.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.QtableWidget_pasajeros.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.QtableWidget_pasajeros.setSelectionBehavior(QAbstractItemView.SelectRows)
        
        self.cargar_datos_dashboard()
        self._setup_connections()

    def _setup_connections(self):
        self.ui.comboBox_bfecha.currentIndexChanged.connect(self._filter_corridas_by_fecha)
        self.ui.QtableWidget_corridasact.itemClicked.connect(self._on_corrida_selected)
        self.ui.boton_corridasoperadores.clicked.connect(self._mostrar_pantalla_operadores_corridas)
        self.ui.QtableWidget_operadores.itemClicked.connect(self._on_operator_selected)

    def _on_operator_selected(self, item):
        fila_seleccionada = item.row()
        self.selected_operator_id = int(self.ui.QtableWidget_operadores.item(fila_seleccionada, 0).text())
        print(f"Operator selected, ID: {self.selected_operator_id}")

    def _mostrar_pantalla_operadores_corridas(self):
        if self.selected_operator_id is None:
            QMessageBox.warning(self, "Operador no seleccionado", "Por favor, seleccione un operador de la tabla.")
            return

        print("Opening PantallaOperadoresCorridas...")
        dialog = QDialog(self)
        dialog.setWindowTitle("Corridas de Operadores")
        
        layout = QVBoxLayout()
        pantalla = PantallaOperadoresCorridas(self.controlador, self.selected_operator_id, dialog)
        layout.addWidget(pantalla)
        
        dialog.setLayout(layout)
        dialog.exec()

    def cargar_datos_dashboard(self):
        # The passenger table is now populated via corrida selection, so no direct load here
        self.cargar_corridas_dashboard()
        self.cargar_operadores_dashboard()
        
        # Automatically select the first corrida to populate the passenger table
        if self.ui.QtableWidget_corridasact.rowCount() > 0:
            self.ui.QtableWidget_corridasact.selectRow(0)
            # Manually trigger the itemClicked signal for the first row
            first_item = self.ui.QtableWidget_corridasact.item(0, 0)
            if first_item:
                self._on_corrida_selected(first_item)
    
    def _on_corrida_selected(self, item):
        fila_seleccionada = item.row()
        corrida_numero = int(self.ui.QtableWidget_corridasact.item(fila_seleccionada, 0).text())
        print(f"Corrida seleccionada, Numero: {corrida_numero}")
        
        try:
            pasajeros_data = self.controlador.obtener_pasajeros_por_corrida(corrida_numero)
            self.ui.QtableWidget_pasajeros.setRowCount(0) # Clear existing passengers
            
            font_bold = QFont()
            font_bold.setBold(True)

            if pasajeros_data:
                for fila_idx, pasajero in enumerate(pasajeros_data):
                    self.ui.QtableWidget_pasajeros.insertRow(fila_idx)
                    
                    # Column 0: Numero Boleto
                    item_boleto = QTableWidgetItem(str(pasajero['numero_boleto']))
                    item_boleto.setTextAlignment(Qt.AlignCenter)
                    item_boleto.setFont(font_bold)
                    self.ui.QtableWidget_pasajeros.setItem(fila_idx, 0, item_boleto)
                    
                    # Column 1: Numero Asiento
                    item_asiento = QTableWidgetItem(str(pasajero['numero_asiento']))
                    item_asiento.setTextAlignment(Qt.AlignCenter)
                    item_asiento.setFont(font_bold)
                    self.ui.QtableWidget_pasajeros.setItem(fila_idx, 1, item_asiento)
                    
                    # Column 2: Nombre Pasajero
                    item_nombre_pasajero = QTableWidgetItem(pasajero['nombre_pasajero'])
                    item_nombre_pasajero.setTextAlignment(Qt.AlignCenter)
                    item_nombre_pasajero.setFont(font_bold)
                    self.ui.QtableWidget_pasajeros.setItem(fila_idx, 2, item_nombre_pasajero)
                    
                    # Column 3: Edad
                    item_edad = QTableWidgetItem(str(pasajero['edad']))
                    item_edad.setTextAlignment(Qt.AlignCenter)
                    item_edad.setFont(font_bold)
                    self.ui.QtableWidget_pasajeros.setItem(fila_idx, 3, item_edad)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al cargar pasajeros por corrida: {e}")



    def cargar_corridas_dashboard(self):
        try:
            self.all_corridas_data = self.controlador.obtener_corridas_dashboard()
            self._populate_fecha_combobox(self.all_corridas_data)
            self._display_corridas_in_table(self.all_corridas_data)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al cargar corridas dashboard: {e}")

    def _populate_fecha_combobox(self, corridas_data):
        self.ui.comboBox_bfecha.clear()
        self.ui.comboBox_bfecha.addItem("Todas las fechas")
        
        # Extract date part from 'fecha_hora_salida' string (e.g., "YYYY-MM-DD HH:MM:SS" -> "YYYY-MM-DD")
        unique_dates = sorted(list(set([corrida['fecha_hora_salida'].split(' ')[0] for corrida in corridas_data])))
        for date_str in unique_dates:
            self.ui.comboBox_bfecha.addItem(date_str)

    def _display_corridas_in_table(self, corridas_to_display):
        self.ui.QtableWidget_corridasact.setRowCount(0)

        font_bold = QFont()
        font_bold.setBold(True)
        
        if corridas_to_display:
            for fila_idx, corrida in enumerate(corridas_to_display):
                self.ui.QtableWidget_corridasact.insertRow(fila_idx)
                
                # Column 0: Corrida (numero_viaje)
                item_numero = QTableWidgetItem(str(corrida['numero_viaje']))
                item_numero.setTextAlignment(Qt.AlignCenter)
                item_numero.setFont(font_bold)
                self.ui.QtableWidget_corridasact.setItem(fila_idx, 0, item_numero)
                
                # Column 1: Fecha y Hora de Salida (fecha_hora_salida)
                item_fecha_hora_salida = QTableWidgetItem(corrida['fecha_hora_salida'])
                item_fecha_hora_salida.setTextAlignment(Qt.AlignCenter)
                item_fecha_hora_salida.setFont(font_bold)
                self.ui.QtableWidget_corridasact.setItem(fila_idx, 1, item_fecha_hora_salida)
                
                # Column 2: Origen (ciudad_origen)
                item_origen = QTableWidgetItem(corrida['ciudad_origen'])
                item_origen.setTextAlignment(Qt.AlignCenter)
                item_origen.setFont(font_bold)
                self.ui.QtableWidget_corridasact.setItem(fila_idx, 2, item_origen)
                
                # Column 3: Destino (ciudad_destino)
                item_destino = QTableWidgetItem(corrida['ciudad_destino'])
                item_destino.setTextAlignment(Qt.AlignCenter)
                item_destino.setFont(font_bold)
                self.ui.QtableWidget_corridasact.setItem(fila_idx, 3, item_destino)
                
                # Column 4: Autobus (autobus_numero)
                item_autobus = QTableWidgetItem(str(corrida['autobus_numero']))
                item_autobus.setTextAlignment(Qt.AlignCenter)
                item_autobus.setFont(font_bold)
                self.ui.QtableWidget_corridasact.setItem(fila_idx, 4, item_autobus)

    def _filter_corridas_by_fecha(self):
        selected_text = self.ui.comboBox_bfecha.currentText()
        corridas_to_display = []
        if selected_text == "Todas las fechas":
            corridas_to_display = self.all_corridas_data
        else:
            # Filter by the date part of 'fecha_hora_salida'
            corridas_to_display = [corrida for corrida in self.all_corridas_data if corrida['fecha_hora_salida'].split(' ')[0] == selected_text]

        # Sort the corridas_to_display by fecha_hora_salida
        corridas_to_display.sort(key=lambda x: x['fecha_hora_salida'])
        self._display_corridas_in_table(corridas_to_display)

    def cargar_operadores_dashboard(self):
        try:
            operadores_data = self.controlador.obtener_operadores_con_corridas_dashboard()
            self.ui.QtableWidget_operadores.setRowCount(0)

            font_bold = QFont()
            font_bold.setBold(True)
            
            if operadores_data:
                for fila_idx, operador in enumerate(operadores_data):
                    self.ui.QtableWidget_operadores.insertRow(fila_idx)
                    
                    # Column 0: Numero Operador
                    item_numero = QTableWidgetItem(str(operador['numero_operador']))
                    item_numero.setTextAlignment(Qt.AlignCenter)
                    item_numero.setFont(font_bold)
                    self.ui.QtableWidget_operadores.setItem(fila_idx, 0, item_numero)
                    
                    # Column 1: Nombre Completo
                    item_nombre_completo = QTableWidgetItem(operador['nombre_completo_operador'])
                    item_nombre_completo.setTextAlignment(Qt.AlignCenter)
                    item_nombre_completo.setFont(font_bold)
                    self.ui.QtableWidget_operadores.setItem(fila_idx, 1, item_nombre_completo)
                    
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al cargar operadores dashboard: {e}")