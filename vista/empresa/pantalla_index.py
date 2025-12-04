#imports de pyside
import os
from PySide6.QtWidgets import (QApplication, QMainWindow, QStackedWidget, QWidget,QVBoxLayout,
                            QDialog, QPushButton, QLineEdit, QLabel, QMessageBox, QTableWidgetItem, QHeaderView, QAbstractItemView)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, QCoreApplication, Qt
from PySide6.QtGui import QCloseEvent, QFont
from utilidades.validaciones import Validaciones


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
        self.ui.QtableWidget_operadores.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.QtableWidget_operadores.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.QtableWidget_operadores.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.ui.QtableWidget_corridasact.setColumnCount(4) # Set column count
        self.ui.QtableWidget_corridasact.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.QtableWidget_corridasact.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.QtableWidget_corridasact.setSelectionBehavior(QAbstractItemView.SelectRows)
        
        self.ui.QtableWidget_pasajeros.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.QtableWidget_pasajeros.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.QtableWidget_pasajeros.setSelectionBehavior(QAbstractItemView.SelectRows)
        
        self.cargar_datos_dashboard()
        self._setup_connections()

    def _setup_connections(self):
        self.ui.comboBox_bfecha.currentIndexChanged.connect(self._filter_corridas_by_fecha)
        self.ui.QtableWidget_corridasact.itemClicked.connect(self._on_corrida_selected)

    def cargar_datos_dashboard(self):
        self.cargar_pasajeros_dashboard()
        self.cargar_corridas_dashboard()
        self.cargar_operadores_dashboard()
    
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
                    numero, nombre, apellPat, apellMat, edad, telefono = pasajero
                    self.ui.QtableWidget_pasajeros.insertRow(fila_idx)
                    
                    item_numero = QTableWidgetItem(str(numero))
                    item_numero.setTextAlignment(Qt.AlignCenter)
                    item_numero.setFont(font_bold)
                    self.ui.QtableWidget_pasajeros.setItem(fila_idx, 0, item_numero)
                    
                    item_nombre_completo = QTableWidgetItem(f"{nombre} {apellPat} {apellMat}")
                    item_nombre_completo.setTextAlignment(Qt.AlignCenter)
                    item_nombre_completo.setFont(font_bold)
                    self.ui.QtableWidget_pasajeros.setItem(fila_idx, 1, item_nombre_completo)
                    
                    item_edad = QTableWidgetItem(str(edad))
                    item_edad.setTextAlignment(Qt.AlignCenter)
                    item_edad.setFont(font_bold)
                    self.ui.QtableWidget_pasajeros.setItem(fila_idx, 2, item_edad)
                    
                    item_telefono = QTableWidgetItem(telefono)
                    item_telefono.setTextAlignment(Qt.AlignCenter)
                    item_telefono.setFont(font_bold)
                    self.ui.QtableWidget_pasajeros.setItem(fila_idx, 3, item_telefono)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al cargar pasajeros por corrida: {e}")

    def cargar_pasajeros_dashboard(self):
        try:
            pasajeros_data = self.controlador.obtener_pasajeros_dashboard()
            self.ui.QtableWidget_pasajeros.setRowCount(0)
            
            font_bold = QFont()
            font_bold.setBold(True)

            if pasajeros_data:
                for fila_idx, pasajero in enumerate(pasajeros_data):
                    numero, nombre, apellPat, apellMat, edad, telefono = pasajero
                    self.ui.QtableWidget_pasajeros.insertRow(fila_idx)
                    
                    item_numero = QTableWidgetItem(str(numero))
                    item_numero.setTextAlignment(Qt.AlignCenter)
                    item_numero.setFont(font_bold)
                    self.ui.QtableWidget_pasajeros.setItem(fila_idx, 0, item_numero)
                    
                    item_nombre_completo = QTableWidgetItem(f"{nombre} {apellPat} {apellMat}")
                    item_nombre_completo.setTextAlignment(Qt.AlignCenter)
                    item_nombre_completo.setFont(font_bold)
                    self.ui.QtableWidget_pasajeros.setItem(fila_idx, 1, item_nombre_completo)
                    
                    item_edad = QTableWidgetItem(str(edad))
                    item_edad.setTextAlignment(Qt.AlignCenter)
                    item_edad.setFont(font_bold)
                    self.ui.QtableWidget_pasajeros.setItem(fila_idx, 2, item_edad)
                    
                    item_telefono = QTableWidgetItem(telefono)
                    item_telefono.setTextAlignment(Qt.AlignCenter)
                    item_telefono.setFont(font_bold)
                    self.ui.QtableWidget_pasajeros.setItem(fila_idx, 3, item_telefono)
                    
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al cargar pasajeros dashboard: {e}")

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
        
        unique_dates = sorted(list(set([corrida[1].strftime("%Y-%m-%d") for corrida in corridas_data])))
        for date_str in unique_dates:
            self.ui.comboBox_bfecha.addItem(date_str)

    def _display_corridas_in_table(self, corridas_to_display):
        self.ui.QtableWidget_corridasact.setRowCount(0)

        font_bold = QFont()
        font_bold.setBold(True)
        
        if corridas_to_display:
            for fila_idx, corrida in enumerate(corridas_to_display):
                numero, fecha, hora_salida, ruta = corrida
                self.ui.QtableWidget_corridasact.insertRow(fila_idx)
                
                item_numero = QTableWidgetItem(str(numero))
                item_numero.setTextAlignment(Qt.AlignCenter)
                item_numero.setFont(font_bold)
                self.ui.QtableWidget_corridasact.setItem(fila_idx, 0, item_numero)
                
                item_fecha = QTableWidgetItem(fecha.strftime("%Y-%m-%d"))
                item_fecha.setTextAlignment(Qt.AlignCenter)
                item_fecha.setFont(font_bold)
                self.ui.QtableWidget_corridasact.setItem(fila_idx, 1, item_fecha)
                
                item_hora_salida = QTableWidgetItem(str(hora_salida).split('.')[0])
                item_hora_salida.setTextAlignment(Qt.AlignCenter)
                item_hora_salida.setFont(font_bold)
                self.ui.QtableWidget_corridasact.setItem(fila_idx, 2, item_hora_salida)
                
                item_ruta = QTableWidgetItem(ruta)
                item_ruta.setTextAlignment(Qt.AlignCenter)
                item_ruta.setFont(font_bold)
                self.ui.QtableWidget_corridasact.setItem(fila_idx, 3, item_ruta)

    def _filter_corridas_by_fecha(self):
        selected_text = self.ui.comboBox_bfecha.currentText()
        corridas_to_display = []
        if selected_text == "Todas las fechas":
            corridas_to_display = self.all_corridas_data
        else:
            corridas_to_display = [corrida for corrida in self.all_corridas_data if corrida[1].strftime("%Y-%m-%d") == selected_text]

        # Sort the corridas_to_display by hora_salida (which is at index 2 in the tuple)
        corridas_to_display.sort(key=lambda x: x[2])
        self._display_corridas_in_table(corridas_to_display)

    def cargar_operadores_dashboard(self):
        try:
            operadores_data = self.controlador.obtener_operadores_con_corridas_dashboard()
            self.ui.QtableWidget_operadores.setRowCount(0)

            font_bold = QFont()
            font_bold.setBold(True)
            
            last_operator_numero = None

            if operadores_data:
                for fila_idx, operador in enumerate(operadores_data):
                    numero, nombre_completo, ruta_corrida, fecha_corrida = operador
                    self.ui.QtableWidget_operadores.insertRow(fila_idx)
                    
                    # Display operator number and name only if it's a new operator
                    if numero != last_operator_numero:
                        item_numero = QTableWidgetItem(str(numero))
                        item_numero.setTextAlignment(Qt.AlignCenter)
                        item_numero.setFont(font_bold)
                        self.ui.QtableWidget_operadores.setItem(fila_idx, 0, item_numero)
                        
                        item_nombre_completo = QTableWidgetItem(nombre_completo)
                        item_nombre_completo.setTextAlignment(Qt.AlignCenter)
                        item_nombre_completo.setFont(font_bold)
                        self.ui.QtableWidget_operadores.setItem(fila_idx, 1, item_nombre_completo)
                        last_operator_numero = numero
                    else:
                        # For repeated operators, leave the cells empty
                        self.ui.QtableWidget_operadores.setItem(fila_idx, 0, QTableWidgetItem(""))
                        self.ui.QtableWidget_operadores.setItem(fila_idx, 1, QTableWidgetItem(""))
                    
                    item_ruta = QTableWidgetItem(ruta_corrida)
                    item_ruta.setTextAlignment(Qt.AlignCenter)
                    item_ruta.setFont(font_bold)
                    self.ui.QtableWidget_operadores.setItem(fila_idx, 2, item_ruta)
                    
                    item_fecha = QTableWidgetItem(str(fecha_corrida))
                    item_fecha.setTextAlignment(Qt.AlignCenter)
                    item_fecha.setFont(font_bold)
                    self.ui.QtableWidget_operadores.setItem(fila_idx, 3, item_fecha)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al cargar operadores dashboard: {e}")