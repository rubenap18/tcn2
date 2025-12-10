from PySide6.QtWidgets import QTableWidgetItem, QTableWidget, QLineEdit, QComboBox, QPushButton, QDialog, QMessageBox
from PySide6.QtCore import Qt
from controladores.controlador_corrida_dialog import ControladorCorridaDialog
from controladores.controlador_actualizar_corrida_dialog import ControladorActualizarCorridaDialog # New Import
from controladores.controlador_actualizar_corr_estado_dialog import ControladorActualizarCorrEstadoDialog # New Import

class ControladorPantallaCorridas:
    def __init__(self, corrida_dao):
        self.corrida_dao = corrida_dao
        self.vista = None
        self.tabla_corridas = None 
        self.todas_las_corridas = [] 

        # Filter states
        self.filtro_numero_corrida = ""
        self.filtro_origen = ""
        self.filtro_destino = "" 

    def set_vista(self, vista_corridas):
        self.vista = vista_corridas
        self._setup_ui()

    def _setup_ui(self):
        self.tabla_corridas = self.vista.ui.findChild(QTableWidget, 'QtableWidget_corridas')
        
        if self.tabla_corridas is None:
            print("Error: QtableWidget_corridas not found in the UI. Make sure the name is exactly 'QtableWidget_corridas' (case-sensitive).")
            return
        
        # Find and connect lineEdit_buscarNumCorr
        self.lineEdit_buscarNumCorr = self.vista.ui.findChild(QLineEdit, 'lineEdit_buscarNumCorr')
        if self.lineEdit_buscarNumCorr:
            self.lineEdit_buscarNumCorr.textChanged.connect(self._on_numero_corrida_text_changed)
        else:
            print("Error: lineEdit_buscarNumCorr not found in the UI.")
        
        # Find and connect comboBox_filtroOrigenCorr
        self.comboBox_filtroOrigenCorr = self.vista.ui.findChild(QComboBox, 'comboBox_filtroOrigenCorr')
        if self.comboBox_filtroOrigenCorr:
            self.comboBox_filtroOrigenCorr.currentIndexChanged.connect(self._on_filtro_origen_changed)
        else:
            print("Error: comboBox_filtroOrigenCorr not found in the UI.")
        
        # New: Find and connect comboBox_filtroDestinoCorr
        self.comboBox_filtroDestinoCorr = self.vista.ui.findChild(QComboBox, 'comboBox_filtroDestinoCorr')
        if self.comboBox_filtroDestinoCorr:
            self.comboBox_filtroDestinoCorr.currentIndexChanged.connect(self._on_filtro_destino_changed)
        else:
            print("Error: comboBox_filtroDestinoCorr not found in the UI.")

        # Connect boton_anadirCorr
        self.boton_anadirCorr = self.vista.ui.findChild(QPushButton, 'boton_anadirCorr')
        if self.boton_anadirCorr:
            self.boton_anadirCorr.clicked.connect(self._abrir_corrida_dialog)
        else:
            print("Error: boton_anadirCorr not found in the UI.")

        # Connect boton_actualizarCorr (New connection)
        self.boton_actualizarCorr = self.vista.ui.findChild(QPushButton, 'boton_actualizarCorr')
        if self.boton_actualizarCorr:
            self.boton_actualizarCorr.clicked.connect(self._abrir_actualizar_corrida_dialog)
        else:
            print("Error: boton_actualizarCorr not found in the UI.")

        # Connect boton_estadoCorr (New connection)
        self.boton_estadoCorr = self.vista.ui.findChild(QPushButton, 'boton_estadoCorr')
        if self.boton_estadoCorr:
            self.boton_estadoCorr.clicked.connect(self._abrir_actualizar_corr_estado_dialog)
        else:
            print("Error: boton_estadoCorr not found in the UI.")


        self.tabla_corridas.setColumnCount(10)
        self.tabla_corridas.setHorizontalHeaderLabels([
            "Corrida", "Origen", "Destino", "Distancia",
            "Fecha y Hora de Salida", "Operador", "Autobus", # Changed "Número Autobús" to "Autobus"
            "Matrícula", "Asientos", "Pasajeros"
        ])
        self.tabla_corridas.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tabla_corridas.verticalHeader().setVisible(False)
        
        # Adjust column widths (increased space)
        self.tabla_corridas.setColumnWidth(0, 120)  # Número de Viaje
        self.tabla_corridas.setColumnWidth(1, 140)  # Origen
        self.tabla_corridas.setColumnWidth(2, 140)  # Destino
        self.tabla_corridas.setColumnWidth(3, 100)  # Distancia
        self.tabla_corridas.setColumnWidth(4, 220)  # Fecha y Hora de Salida (more space)
        self.tabla_corridas.setColumnWidth(5, 220)  # Operador (more space)
        self.tabla_corridas.setColumnWidth(6, 120)  # Autobus
        self.tabla_corridas.setColumnWidth(7, 120)  # Matrícula
        self.tabla_corridas.setColumnWidth(8, 120)  # Asientos
        self.tabla_corridas.setColumnWidth(9, 120)  # Boletos Vendidos
        
        self._cargar_todas_las_corridas() # Call this to load data on init and store it

    def _abrir_corrida_dialog(self):
        dialog = ControladorCorridaDialog(self.vista)
        dialog.exec()
        # After the dialog closes, refresh the corridas table to show any new additions
        self._cargar_todas_las_corridas()

    def _abrir_actualizar_corrida_dialog(self):
        selected_row = self.tabla_corridas.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self.vista, "Selección Requerida", "Por favor, seleccione una corrida de la tabla para actualizar.")
            return

        # Get numero_viaje from the selected row
        numero_viaje_selected = int(self.tabla_corridas.item(selected_row, 0).text())
        
        # Find the complete corrida_data from self.todas_las_corridas
        corrida_to_update = None
        for corrida in self.todas_las_corridas:
            if corrida['numero_viaje'] == numero_viaje_selected:
                corrida_to_update = corrida
                break

        if corrida_to_update is None:
            QMessageBox.critical(self.vista, "Error", "No se encontró la corrida seleccionada en los datos internos.")
            return

        dialog = ControladorActualizarCorridaDialog(corrida_data=corrida_to_update) # Removed self.vista as parent
        dialog.exec()
        self._cargar_todas_las_corridas()

    def _abrir_actualizar_corr_estado_dialog(self):
        selected_row = self.tabla_corridas.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self.vista, "Selección Requerida", "Por favor, seleccione una corrida de la tabla para actualizar su estado.")
            return

        # Get numero_viaje from the selected row
        numero_viaje_selected = int(self.tabla_corridas.item(selected_row, 0).text())
        
        # Find the complete corrida_data from self.todas_las_corridas
        corrida_to_update = None
        for corrida in self.todas_las_corridas:
            if corrida['numero_viaje'] == numero_viaje_selected:
                corrida_to_update = corrida
                break

        if corrida_to_update is None:
            QMessageBox.critical(self.vista, "Error", "No se encontró la corrida seleccionada en los datos internos.")
            return

        controlador_dialogo = ControladorActualizarCorrEstadoDialog(self.corrida_dao, self.vista)
        controlador_dialogo.mostrar_dialogo(corrida_data=corrida_to_update)
        self._cargar_todas_las_corridas() # Refresh table after dialog closes

    def _cargar_todas_las_corridas(self):
        # Fetch and store all corridas
        self.todas_las_corridas = self.corrida_dao.obtener_todas_las_corridas_detalladas()
        self._aplicar_filtros() # Apply filters (initially none)

    def _actualizar_tabla(self, corridas_a_mostrar):
        if self.tabla_corridas is None:
            print("Error: Tabla de corridas no inicializada.")
            return

        self.tabla_corridas.setRowCount(0) # Clear existing data
        
        for row_num, corrida in enumerate(corridas_a_mostrar):
            self.tabla_corridas.insertRow(row_num)
            item_numero_viaje = QTableWidgetItem(str(corrida['numero_viaje']))
            item_numero_viaje.setTextAlignment(Qt.AlignCenter)
            self.tabla_corridas.setItem(row_num, 0, item_numero_viaje)
            
            item_origen = QTableWidgetItem(corrida['ciudad_origen'])
            item_origen.setTextAlignment(Qt.AlignCenter)
            self.tabla_corridas.setItem(row_num, 1, item_origen)
            
            item_destino = QTableWidgetItem(corrida['ciudad_destino'])
            item_destino.setTextAlignment(Qt.AlignCenter)
            self.tabla_corridas.setItem(row_num, 2, item_destino)
            
            item_distancia = QTableWidgetItem(str(corrida['distancia']))
            item_distancia.setTextAlignment(Qt.AlignCenter)
            self.tabla_corridas.setItem(row_num, 3, item_distancia)
            
            item_fecha_hora_salida = QTableWidgetItem(str(corrida['fecha_hora_salida']))
            item_fecha_hora_salida.setTextAlignment(Qt.AlignCenter)
            self.tabla_corridas.setItem(row_num, 4, item_fecha_hora_salida)
            
            item_nombre_operador = QTableWidgetItem(corrida['nombre_operador'])
            item_nombre_operador.setTextAlignment(Qt.AlignCenter)
            self.tabla_corridas.setItem(row_num, 5, item_nombre_operador)
            
            item_autobus_numero = QTableWidgetItem(str(corrida['autobus_numero']))
            item_autobus_numero.setTextAlignment(Qt.AlignCenter)
            self.tabla_corridas.setItem(row_num, 6, item_autobus_numero)
            
            item_matricula = QTableWidgetItem(corrida['matricula'])
            item_matricula.setTextAlignment(Qt.AlignCenter)
            self.tabla_corridas.setItem(row_num, 7, item_matricula)
            
            item_cantidad_asientos = QTableWidgetItem(str(corrida['cantidad_asientos']))
            item_cantidad_asientos.setTextAlignment(Qt.AlignCenter)
            self.tabla_corridas.setItem(row_num, 8, item_cantidad_asientos)
            
            item_boletos_vendidos = QTableWidgetItem(str(corrida['boletos_vendidos']))
            item_boletos_vendidos.setTextAlignment(Qt.AlignCenter)
            self.tabla_corridas.setItem(row_num, 9, item_boletos_vendidos)

    def _on_numero_corrida_text_changed(self, texto_busqueda):
        self.filtro_numero_corrida = texto_busqueda
        self._aplicar_filtros()

    def _on_filtro_origen_changed(self, index):
        if self.comboBox_filtroOrigenCorr:
            self.filtro_origen = self.comboBox_filtroOrigenCorr.currentText()
            # If "TODOS" or an empty string is selected, treat it as no filter
            if self.filtro_origen == "TODOS" or self.filtro_origen == "":
                self.filtro_origen = ""
            self._aplicar_filtros()

    # New: Method to handle changes in destination combobox
    def _on_filtro_destino_changed(self, index):
        if self.comboBox_filtroDestinoCorr:
            self.filtro_destino = self.comboBox_filtroDestinoCorr.currentText()
            # If "TODOS" or an empty string is selected, treat it as no filter
            if self.filtro_destino == "TODOS" or self.filtro_destino == "":
                self.filtro_destino = ""
            self._aplicar_filtros()

    def _aplicar_filtros(self):
        corridas_filtradas = self.todas_las_corridas

        # Apply numero_corrida filter
        if self.filtro_numero_corrida:
            try:
                numero_corrida_buscado = int(self.filtro_numero_corrida)
                corridas_filtradas = [
                    corrida for corrida in corridas_filtradas
                    if corrida['numero_viaje'] == numero_corrida_buscado
                ]
            except ValueError:
                corridas_filtradas = [] # No matches if input is not a valid number
        
        # Apply origen filter
        if self.filtro_origen:
            corridas_filtradas = [
                corrida for corrida in corridas_filtradas
                if corrida['ciudad_origen'] == self.filtro_origen
            ]

        # New: Apply destino filter
        if self.filtro_destino:
            corridas_filtradas = [
                corrida for corrida in corridas_filtradas
                if corrida['ciudad_destino'] == self.filtro_destino
            ]
        
        self._actualizar_tabla(corridas_filtradas)
    
    def obtener_informacion_corrida_para_asientos(self, numero_corrida):
        """
        NUEVO MÉTODO: Obtiene la información completa de una corrida para mostrar en el diálogo de asientos.
        
        Args:
            numero_corrida (int): Número de la corrida
            
        Returns:
            dict: Diccionario con la información de la corrida o None si no se encuentra
        """
        # Buscar en las corridas ya cargadas
        for corrida in self.todas_las_corridas:
            if corrida['numero_viaje'] == numero_corrida:
                # Retornar formato compatible con el diálogo de asientos
                return {
                    'numero_corrida': corrida['numero_viaje'],
                    'numero_autobus': corrida['autobus_numero'],
                    'ciudad_origen': corrida['ciudad_origen'],
                    'ciudad_destino': corrida['ciudad_destino'],
                    'fecha': corrida['fecha_hora_salida'].split()[0] if ' ' in str(corrida['fecha_hora_salida']) else corrida['fecha_hora_salida'],
                    'hora_salida': corrida['fecha_hora_salida'].split()[1] if ' ' in str(corrida['fecha_hora_salida']) else ''
                }
        
        # Si no está en las corridas cargadas, buscar en la BD
        try:
            corridas = self.corrida_dao.obtener_todas_las_corridas_detalladas()
            for corrida in corridas:
                if corrida['numero_viaje'] == numero_corrida:
                    return {
                        'numero_corrida': corrida['numero_viaje'],
                        'numero_autobus': corrida['autobus_numero'],
                        'ciudad_origen': corrida['ciudad_origen'],
                        'ciudad_destino': corrida['ciudad_destino'],
                        'fecha': corrida['fecha_hora_salida'].split()[0] if ' ' in str(corrida['fecha_hora_salida']) else corrida['fecha_hora_salida'],
                        'hora_salida': corrida['fecha_hora_salida'].split()[1] if ' ' in str(corrida['fecha_hora_salida']) else ''
                    }
        except Exception as e:
            print(f"Error al buscar corrida en BD: {e}")
        
        return None