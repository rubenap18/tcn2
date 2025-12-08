from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtCore import Qt
from vista.compartido.pantalla_viajar_ui import PantallaViajar
from datetime import datetime

class PantallaViajarWidget(QWidget):
    
    def __init__(self, app_manager, parent=None):
        super().__init__(parent)
        self.app_manager = app_manager
        self.controlador = app_manager.controlador_viajar
        self.parent_window = parent
        
        # Configurar UI usando el objeto PantallaViajar
        self.ui = PantallaViajar()
        self.ui.setupUi(self)  # Configurar la UI en este widget
        
        # Variables de estado
        self.corrida_seleccionada = None
        self.num_pasajeros = 0
        
        # Conectar señales
        self.conectar_senales()
        
        # Cargar datos iniciales
        self.cargar_ciudades_origen()
    
    def conectar_senales(self):
        """Conecta las señales de los widgets."""
        self.ui.comboBox_origen.currentTextChanged.connect(self.on_origen_changed)
        self.ui.comboBox_destino.currentTextChanged.connect(self.on_destino_changed)
        self.ui.comboBox_fecha.currentTextChanged.connect(self.on_fecha_changed)
        self.ui.LineEdit_pasajeros.textChanged.connect(self.on_pasajeros_changed)
        self.ui.boton_continuar.clicked.connect(self.on_continuar_clicked)
        self.ui.boton_regresar.clicked.connect(self.on_regresar_clicked)
        self.ui.tableWidget.itemSelectionChanged.connect(self.on_corrida_seleccionada)
    
    def cargar_ciudades_origen(self):
        """Carga las ciudades de origen en el combobox."""
        self.ui.comboBox_origen.clear()
        ciudades = self.controlador.obtener_ciudades_origen()
        
        for ciudad in ciudades:
            self.ui.comboBox_origen.addItem(ciudad['nombre'])
    
    def on_origen_changed(self, ciudad_origen):
        """Cuando cambia la ciudad de origen, cargar destinos."""
        if not ciudad_origen:
            return
        
        self.ui.comboBox_destino.clear()
        self.ui.comboBox_fecha.clear()
        self.ui.tableWidget.setRowCount(0)
        
        ciudades = self.controlador.obtener_ciudades_destino(ciudad_origen)
        
        for ciudad in ciudades:
            self.ui.comboBox_destino.addItem(ciudad['nombre'])
    
    def on_destino_changed(self, ciudad_destino):
        """Cuando cambia el destino, cargar fechas disponibles."""
        ciudad_origen = self.ui.comboBox_origen.currentText()
        
        if not ciudad_origen or not ciudad_destino:
            return
        
        self.ui.comboBox_fecha.clear()
        self.ui.tableWidget.setRowCount(0)
        
        fechas = self.controlador.obtener_fechas_disponibles(ciudad_origen, ciudad_destino)
        
        for fecha in fechas:
            # Formatear la fecha para mostrar
            fecha_str = fecha.strftime('%d/%m/%Y') if hasattr(fecha, 'strftime') else str(fecha)
            self.ui.comboBox_fecha.addItem(fecha_str, fecha)  # Guardar fecha original en userData
    
    def on_fecha_changed(self, fecha_texto):
        """Cuando cambia la fecha, buscar corridas automáticamente."""
        if not fecha_texto:
            return
        
        self.buscar_corridas()
    
    def on_pasajeros_changed(self, texto):
        """Validar número de pasajeros."""
        if texto:
            try:
                self.num_pasajeros = int(texto)
                if self.num_pasajeros <= 0:
                    self.num_pasajeros = 0
            except ValueError:
                self.num_pasajeros = 0
    
    def buscar_corridas(self):
        """Busca y muestra las corridas disponibles."""
        ciudad_origen = self.ui.comboBox_origen.currentText()
        ciudad_destino = self.ui.comboBox_destino.currentText()
        fecha_item = self.ui.comboBox_fecha.currentData()
        num_pasajeros_text = self.ui.LineEdit_pasajeros.text()
        
        # Validaciones
        if not ciudad_origen or not ciudad_destino:
            QMessageBox.warning(self, "Datos incompletos", "Selecciona origen y destino")
            return
        
        if not fecha_item:
            QMessageBox.warning(self, "Datos incompletos", "Selecciona una fecha")
            return
        
        if not num_pasajeros_text or self.num_pasajeros <= 0:
            QMessageBox.warning(self, "Datos incompletos", "Ingresa el número de pasajeros")
            return
        
        # Convertir fecha al formato correcto
        if hasattr(fecha_item, 'strftime'):
            fecha_str = fecha_item.strftime('%Y-%m-%d')
        else:
            fecha_str = str(fecha_item)
        
        # Buscar corridas
        corridas = self.controlador.buscar_corridas(
            ciudad_origen, ciudad_destino, fecha_str, self.num_pasajeros
        )
        
        # Mostrar resultados en la tabla
        self.mostrar_corridas(corridas)
    
    def mostrar_corridas(self, corridas):
        """Muestra las corridas en la tabla."""
        self.ui.tableWidget.setRowCount(0)
        
        if not corridas:
            QMessageBox.information(self, "Sin resultados", 
                                   "No se encontraron corridas disponibles con los criterios seleccionados")
            return
        
        for corrida in corridas:
            row_position = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row_position)
            
            # Columna 0: Número de corrida
            item = QTableWidgetItem(str(corrida['numero_corrida']))
            item.setTextAlignment(Qt.AlignCenter)
            item.setData(Qt.UserRole, corrida)  # Guardar toda la info de la corrida
            self.ui.tableWidget.setItem(row_position, 0, item)
            
            # Columna 1: Ruta
            ruta = f"{corrida['ciudad_origen']} → {corrida['ciudad_destino']}"
            item = QTableWidgetItem(ruta)
            item.setTextAlignment(Qt.AlignCenter)
            self.ui.tableWidget.setItem(row_position, 1, item)
            
            # Columna 2: Autobús
            item = QTableWidgetItem(str(corrida['numero_autobus']))
            item.setTextAlignment(Qt.AlignCenter)
            self.ui.tableWidget.setItem(row_position, 2, item)
            
            # Columna 3: Servicio
            item = QTableWidgetItem(corrida['descripcion_servicio'])
            item.setTextAlignment(Qt.AlignCenter)
            self.ui.tableWidget.setItem(row_position, 3, item)
            
            # Columna 4: Hora de salida
            item = QTableWidgetItem(str(corrida['hora_salida']))
            item.setTextAlignment(Qt.AlignCenter)
            self.ui.tableWidget.setItem(row_position, 4, item)
            
            # Columna 5: Hora de llegada
            item = QTableWidgetItem(str(corrida['hora_llegada']))
            item.setTextAlignment(Qt.AlignCenter)
            self.ui.tableWidget.setItem(row_position, 5, item)
            
            # Columna 6: Lugares disponibles
            item = QTableWidgetItem(str(corrida['lugares_disponibles']))
            item.setTextAlignment(Qt.AlignCenter)
            self.ui.tableWidget.setItem(row_position, 6, item)
            
            # Columna 7: Precio
            precio_formateado = f"${corrida['precio']:.2f}"
            item = QTableWidgetItem(precio_formateado)
            item.setTextAlignment(Qt.AlignCenter)
            self.ui.tableWidget.setItem(row_position, 7, item)
    
    def on_corrida_seleccionada(self):
        """Cuando se selecciona una corrida de la tabla."""
        selected_items = self.ui.tableWidget.selectedItems()
        if selected_items:
            # Obtener la corrida del primer item de la fila seleccionada
            row = selected_items[0].row()
            item_corrida = self.ui.tableWidget.item(row, 0)
            self.corrida_seleccionada = item_corrida.data(Qt.UserRole)
    
    def on_continuar_clicked(self):
        """Cuando se presiona el botón continuar."""
        if not self.corrida_seleccionada:
            QMessageBox.warning(self, "Selección requerida", 
                              "Por favor selecciona una corrida de la tabla")
            return
        
        if self.num_pasajeros <= 0:
            QMessageBox.warning(self, "Datos incompletos", 
                              "Ingresa el número de pasajeros")
            return
        
        # Validar que haya suficientes lugares
        if self.corrida_seleccionada['lugares_disponibles'] < self.num_pasajeros:
            QMessageBox.warning(self, "Sin disponibilidad", 
                              f"Solo hay {self.corrida_seleccionada['lugares_disponibles']} lugares disponibles")
            return
        
        # Importar aquí para evitar importación circular
        from vista.compartido.seleccionAsientoDialog import SeleccionAsientoDialog
        
        # Abrir diálogo de selección de asientos
        dialog = SeleccionAsientoDialog(
            self.app_manager,
            self.corrida_seleccionada,
            self.num_pasajeros,
            self
        )
        
        resultado = dialog.exec()
        
        # Si el usuario completó la compra, regresar al index
        if resultado == dialog.COMPRA_EXITOSA:
            self.on_regresar_clicked()
    
    def on_regresar_clicked(self):
        """Cuando se presiona el botón regresar."""
        # Cerrar esta ventana y volver al parent
        self.close()