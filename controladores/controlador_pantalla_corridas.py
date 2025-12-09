from PySide6.QtWidgets import QTableWidgetItem, QTableWidget, QLineEdit, QComboBox, QPushButton, QDialog, QMessageBox
from controladores.controlador_corrida_dialog import ControladorCorridaDialog
from controladores.controlador_actualizar_corrida_dialog import ControladorActualizarCorridaDialog # New Import
from controladores.controlador_actualizar_corr_estado_dialog import ControladorActualizarCorrEstadoDialog # New Import

class ControladorPantallaCorridas:
    def __init__(self, corrida_dao):
        self.corrida_dao = corrida_dao
        self.vista = None
        self.tabla_corridas = None 
        self.todas_las_corridas = [] # Store all corridas

        # Filter states
        self.filtro_numero_corrida = ""
        self.filtro_origen = ""
        self.filtro_destino = "" # New: Filter state for destination

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
            "Matrícula", "Asientos", "Boletos Vendidos"
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
            self.tabla_corridas.setItem(row_num, 0, QTableWidgetItem(str(corrida['numero_viaje'])))
            self.tabla_corridas.setItem(row_num, 1, QTableWidgetItem(corrida['ciudad_origen']))
            self.tabla_corridas.setItem(row_num, 2, QTableWidgetItem(corrida['ciudad_destino']))
            self.tabla_corridas.setItem(row_num, 3, QTableWidgetItem(str(corrida['distancia'])))
            self.tabla_corridas.setItem(row_num, 4, QTableWidgetItem(str(corrida['fecha_hora_salida'])))
            self.tabla_corridas.setItem(row_num, 5, QTableWidgetItem(corrida['nombre_operador']))
            self.tabla_corridas.setItem(row_num, 6, QTableWidgetItem(str(corrida['autobus_numero'])))
            self.tabla_corridas.setItem(row_num, 7, QTableWidgetItem(corrida['matricula']))
            self.tabla_corridas.setItem(row_num, 8, QTableWidgetItem(str(corrida['cantidad_asientos'])))
            self.tabla_corridas.setItem(row_num, 9, QTableWidgetItem(str(corrida['boletos_vendidos'])))

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