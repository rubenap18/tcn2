# controladores/controlador_pantalla_autobuses.py

from PySide6.QtWidgets import QMessageBox, QTableWidgetItem, QHeaderView, QWidget, QDialog
from PySide6.QtCore import Qt
from dao.autobus_dao import AutobusDAO
from dao.asiento_dao import AsientoDAO
from dao.marca_modelo_dao import MarcaModeloDAO
from objetos.autobus import Autobus
from vista.empresa.pantalla_autobuses_ui import Ui_pantalla_autobuses
from vista.empresa.registrarAutobusDialog_ui import Ui_Dialog as Ui_RegistrarDialog
from vista.empresa.bajaAutobusDialog_ui import Ui_Dialog as Ui_BajaDialog

class ControladorPantallaAutobuses:
    
    def __init__(self, autobus_dao=None):
        
        if autobus_dao:
            self.autobus_dao = autobus_dao
        else:
            self.autobus_dao = AutobusDAO()
            
        self.asiento_dao = AsientoDAO()
        self.marca_modelo_dao = MarcaModeloDAO()
    
    def setup_ui(self, pantalla_autobuses_widget, ui):
        """Configura la UI de la pantalla de autobuses"""
        self.pantalla = pantalla_autobuses_widget
        self.ui = ui
        
        self.configurar_vista()
    
    def configurar_vista(self):
        """Configura la vista inicial de autobuses"""
        if self.ui:
            # Configurar combobox de filtro
            self.ui.comboBox_tiposAutobus.clear()
            self.ui.comboBox_tiposAutobus.addItems(["TODOS", "PLUS", "PLATINO"])
            
            # Conectar señales
            self.ui.comboBox_tiposAutobus.currentTextChanged.connect(self.filtrar_autobuses)
            self.ui.boton_registrarAutobus.clicked.connect(self.abrir_alta_autobus)
            self.ui.boton_bajaAutobus.clicked.connect(self.abrir_baja_autobus)
            
            # Configurar tabla
            self.configurar_tabla()
            
            # Cargar datos iniciales
            self.cargar_autobuses()
    
    def configurar_tabla(self):
        """Configura la tabla de autobuses"""
        if self.ui:
            # Configurar columnas (sin Estado)
            columnas = ["Número", "Matrícula", "Tipo Servicio", "Marca", "Modelo", "Asientos"]
            self.ui.QtableWidget_autobuses.setColumnCount(len(columnas))
            self.ui.QtableWidget_autobuses.setHorizontalHeaderLabels(columnas)
            
            # Ajustar ancho de columnas específico
            header = self.ui.QtableWidget_autobuses.horizontalHeader()
            
            # Configurar modos de redimensionamiento
            header.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)      # Número
            header.setSectionResizeMode(1, QHeaderView.ResizeMode.Fixed)      # Matrícula
            header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)    # Tipo Servicio
            header.setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)    # Marca
            header.setSectionResizeMode(4, QHeaderView.ResizeMode.Stretch)    # Modelo
            header.setSectionResizeMode(5, QHeaderView.ResizeMode.Fixed)      # Asientos
            
            # Establecer anchos fijos para columnas específicas
            self.ui.QtableWidget_autobuses.setColumnWidth(0, 120)   # Número (más ancho)
            self.ui.QtableWidget_autobuses.setColumnWidth(1, 150)   # Matrícula
            self.ui.QtableWidget_autobuses.setColumnWidth(5, 120)   # Asientos
            
            # Deshabilitar edición de celdas
            self.ui.QtableWidget_autobuses.setEditTriggers(self.ui.QtableWidget_autobuses.EditTrigger.NoEditTriggers)
            
            # Selección por filas completas
            self.ui.QtableWidget_autobuses.setSelectionBehavior(self.ui.QtableWidget_autobuses.SelectionBehavior.SelectRows)
            
            # Ajustar altura de filas para mejor visualización
            self.ui.QtableWidget_autobuses.verticalHeader().setDefaultSectionSize(45)
            
            # Estilo adicional para mejor apariencia
            self.ui.QtableWidget_autobuses.setAlternatingRowColors(True)
            self.ui.QtableWidget_autobuses.setStyleSheet("""
                QTableWidget {
                    gridline-color: #e0e0e0;
                }
                QTableWidget::item {
                    padding: 10px;
                }
            """)
    
    def cargar_autobuses(self, filtro="TODOS"):
        
        try:
            # Obtener autobuses del DAO
            autobuses = self.autobus_dao.obtener_autobuses_activos(filtro)
            
            # Limpiar tabla
            self.ui.QtableWidget_autobuses.setRowCount(0)
            
            # Llenar tabla
            for i, autobus in enumerate(autobuses):
                self.ui.QtableWidget_autobuses.insertRow(i)
                
                # Agregar datos centrados (sin Estado)
                self.agregar_item_tabla(i, 0, str(autobus.get_numero()), True)
                self.agregar_item_tabla(i, 1, autobus.get_matricula(), True)
                self.agregar_item_tabla(i, 2, autobus.get_tipoAutobus(), True)
                self.agregar_item_tabla(i, 3, autobus.get_marca(), True)
                self.agregar_item_tabla(i, 4, autobus.get_modelo(), True)
                self.agregar_item_tabla(i, 5, str(autobus.get_cantAsientos()), True)
                
        except Exception as e:
            QMessageBox.critical(self.pantalla, "Error", f"Error al cargar autobuses: {str(e)}")
    
    def agregar_item_tabla(self, fila, columna, texto, centrar=False):
        
        item = QTableWidgetItem(texto)
        if centrar:
            item.setTextAlignment(Qt.AlignCenter)
        self.ui.QtableWidget_autobuses.setItem(fila, columna, item)
    
    def filtrar_autobuses(self, filtro):
        
        self.cargar_autobuses(filtro)
    
    def abrir_alta_autobus(self):
        
        try:
            # Crear diálogo
            dialog = QDialog(self.pantalla)
            ui = Ui_RegistrarDialog()
            ui.setupUi(dialog)
            
            # Configurar diálogo
            self.configurar_dialogo_alta(ui, dialog)
            
            # Mostrar diálogo
            if dialog.exec():
                # Actualizar tabla si se registró un autobús
                filtro_actual = self.ui.comboBox_tiposAutobus.currentText()
                self.cargar_autobuses(filtro_actual)
                QMessageBox.information(self.pantalla, "Éxito", "Autobús registrado exitosamente")
                
        except Exception as e:
            QMessageBox.critical(self.pantalla, "Error", f"Error al abrir diálogo de alta: {str(e)}")
    
    def configurar_dialogo_alta(self, ui, dialog):
        # Limpiar y configurar comboBox de tipos de servicio (sin TODOS)
        ui.comboBox_tiposdeautobus.clear()
        ui.comboBox_tiposdeautobus.addItems(["PLUS", "PLATINO"])
        
        # Cargar marcas
        marcas = self.marca_modelo_dao.obtener_marcas()
        ui.comboBox_marcaAutobus.clear()
        for marca in marcas:
            ui.comboBox_marcaAutobus.addItem(marca['nombre'], marca['clave'])
    
        # Cargar modelos de la primera marca
        if marcas:
            self.cargar_modelos_dialogo(ui, marcas[0]['clave'])
    
        # Conectar señales
        ui.comboBox_marcaAutobus.currentIndexChanged.connect(
            lambda: self.cargar_modelos_dialogo(ui, ui.comboBox_marcaAutobus.currentData())
        )
        ui.boton_registrarAutobus.clicked.connect(
            lambda: self.registrar_autobus_dialogo(ui, dialog)
        )
    
    def cargar_modelos_dialogo(self, ui, marca_clave):
        
        try:
            modelos = self.marca_modelo_dao.obtener_modelos_por_marca(marca_clave)
            ui.comboBox_modeloAutobus.clear()
            for modelo in modelos:
                ui.comboBox_modeloAutobus.addItem(modelo['nombre'], modelo['clave'])
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Error al cargar modelos: {str(e)}")
    
    def validar_datos_alta(self, ui):
        
        # Obtener valores
        numero_text = ui.lineEdit_numeroAutobus.text()
        matricula = ui.lineEdit_matriculaAutobus.text().strip()
        clave_wifi = ui.lineEdit_claveWIFIAutobus.text().strip()
        tipo_servicio = ui.comboBox_tiposdeautobus.currentText()
        marca = ui.comboBox_marcaAutobus.currentText()
        modelo = ui.comboBox_modeloAutobus.currentText()
        
        # Validar que todos los campos estén llenos
        if not all([numero_text, matricula, clave_wifi, tipo_servicio, marca, modelo]):
            return "Todos los campos son obligatorios"
        
        # Validar número
        try:
            numero = int(numero_text)
        except ValueError:
            return "El número debe ser un valor numérico"
        
        # Validar rango según tipo de servicio
        if tipo_servicio == "PLUS":
            if not (100 <= numero <= 200):
                return "Para servicio PLUS, el número debe estar entre 100 y 200"
        elif tipo_servicio == "PLATINO":
            if not (500 <= numero <= 600):
                return "Para servicio PLATINO, el número debe estar entre 500 y 600"
        else:
            return "Seleccione un tipo de servicio válido"
        
        # Validar matrícula
        if len(matricula) != 6:
            return "La matrícula debe tener exactamente 6 caracteres"
        
        if " " in matricula:
            return "La matrícula no puede contener espacios"
        
        # Validar que matrícula no exista
        if self.autobus_dao.existe_matricula(matricula):
            return "La matrícula ya está registrada"
        
        # Validar que número no exista
        if self.autobus_dao.existe_numero(numero):
            return f"El número {numero} ya está registrado"
        
        # Validar clave WiFi
        if not (8 <= len(clave_wifi) <= 16):
            return "La clave WiFi debe tener entre 8 y 16 caracteres"
        
        return None  # Sin errores
    
    def registrar_autobus_dialogo(self, ui, dialog):
        
        try:
            # Validar datos
            error = self.validar_datos_alta(ui)
            if error:
                QMessageBox.warning(dialog, "Validación", error)
                return
            
            # Crear objeto Autobus
            autobus = Autobus()
            autobus.set_numero(int(ui.lineEdit_numeroAutobus.text()))
            autobus.set_matricula(ui.lineEdit_matriculaAutobus.text().strip())
            autobus.set_claveWIFI(ui.lineEdit_claveWIFIAutobus.text().strip())
            autobus.set_tipoAutobus(ui.comboBox_tiposdeautobus.currentText())
            autobus.set_marca(ui.comboBox_marcaAutobus.currentText())
            autobus.set_modelo(ui.comboBox_modeloAutobus.currentText())
            autobus.set_estado("ACTIVO")
            
            # Registrar autobús en BD
            self.autobus_dao.registrar_autobus(autobus)
            
            # Crear asientos automáticamente
            tipo_servicio = autobus.get_tipoAutobus()
            self.asiento_dao.crear_asientos_autobus(autobus.get_numero(), tipo_servicio)
            
            # Cerrar diálogo
            dialog.accept()
            
        except Exception as e:
            QMessageBox.critical(dialog, "Error", f"Error al registrar autobús: {str(e)}")
    
    def abrir_baja_autobus(self):
        
        try:
            # Crear diálogo
            dialog = QDialog(self.pantalla)
            ui = Ui_BajaDialog()
            ui.setupUi(dialog)
            
            # Configurar diálogo
            self.configurar_dialogo_baja(ui, dialog)
            
            # Mostrar diálogo
            if dialog.exec():
                # Actualizar tabla si se dio de baja un autobús
                filtro_actual = self.ui.comboBox_tiposAutobus.currentText()
                self.cargar_autobuses(filtro_actual)
                QMessageBox.information(self.pantalla, "Éxito", "Autobús dado de baja exitosamente")
                
        except Exception as e:
            QMessageBox.critical(self.pantalla, "Error", f"Error al abrir diálogo de baja: {str(e)}")
    
    def configurar_dialogo_baja(self, ui, dialog):
        
        # Cargar autobuses activos
        try:
            autobuses = self.autobus_dao.obtener_autobuses_activos_para_baja()
            ui.comboBox_numeroAutobus.clear()
            
            for autobus in autobuses:
                texto = f"{autobus['numero']} - {autobus['matricula']}"
                ui.comboBox_numeroAutobus.addItem(texto, autobus['numero'])
            
            # Conectar señales
            ui.comboBox_numeroAutobus.currentIndexChanged.connect(
                lambda: self.mostrar_datos_autobus_dialogo(ui)
            )
            ui.boton_bajaAutobus.clicked.connect(
                lambda: self.dar_baja_autobus_dialogo(ui, dialog)
            )
            
            # Mostrar datos del primer autobús si existe
            if autobuses:
                self.mostrar_datos_autobus_dialogo(ui)
                
        except Exception as e:
            QMessageBox.critical(dialog, "Error", f"Error al cargar autobuses: {str(e)}")
    
    def mostrar_datos_autobus_dialogo(self, ui):
        
        try:
            numero_autobus = ui.comboBox_numeroAutobus.currentData()
            if numero_autobus:
                autobus = self.autobus_dao.obtener_datos_autobus(numero_autobus)
                if autobus:
                    ui.label_mostrarMatricula.setText(autobus.get_matricula())
                    ui.label_mostrarMarca.setText(autobus.get_marca())
                    ui.label_mostrarModelo.setText(autobus.get_modelo())
                    ui.label_mostrarTipoAutobus.setText(autobus.get_tipoAutobus())
                else:
                    self.limpiar_labels_dialogo(ui)
            else:
                self.limpiar_labels_dialogo(ui)
                
        except Exception as e:
            print(f"Error al cargar datos del autobús: {str(e)}")
    
    def limpiar_labels_dialogo(self, ui):
        
        ui.label_mostrarMatricula.setText("")
        ui.label_mostrarMarca.setText("")
        ui.label_mostrarModelo.setText("")
        ui.label_mostrarTipoAutobus.setText("")

    def dar_baja_autobus_dialogo(self, ui, dialog):
        
        try:
            numero_autobus = ui.comboBox_numeroAutobus.currentData()
            if not numero_autobus:
                QMessageBox.warning(dialog, "Advertencia", "Seleccione un autobús")
                return
            
            # Verificar si tiene corridas futuras
            if self.autobus_dao.tiene_corridas_futuras(numero_autobus):
                # Obtener información de las corridas
                corridas = self.autobus_dao.obtener_corridas_futuras(numero_autobus)
                
                # Crear mensaje
                mensaje = f"No se puede dar de baja el autobús {numero_autobus}.\n\n"
                mensaje += "Tiene corridas asignadas para hoy o fechas futuras:\n\n"
                
                for corrida in corridas:
                    mensaje += f"• Corrida {corrida['numero']}: {corrida['fecha']} "
                    mensaje += f"({corrida['hora_salida']} - {corrida['hora_llegada']}) "
                    mensaje += f"Ruta: {corrida['ruta']}\n"
                
                if len(corridas) >= 5:
                    mensaje += "\n... y más corridas.\n"
                
                mensaje += "\nDebe cancelar o reasignar estas corridas primero."
                
                QMessageBox.warning(dialog, "No se puede dar de baja", mensaje)
                return
            
            # Si no tiene corridas, proceder con la baja
            confirmacion = QMessageBox.question(
                dialog,
                "Confirmar baja",
                f"¿Está seguro de dar de baja el autobús {numero_autobus}?\n\n"
                "El autobús NO tiene corridas asignadas para hoy ni fechas futuras.\n"
                "Esta acción cambiará el estado a INACTIVO.",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            
            if confirmacion == QMessageBox.StandardButton.Yes:
                exito, mensaje_error = self.autobus_dao.dar_baja_autobus(numero_autobus)
                if exito:
                    QMessageBox.information(dialog, "Éxito", f"Autobús {numero_autobus} dado de baja exitosamente")
                    dialog.accept()
                else:
                    QMessageBox.warning(dialog, "Error", mensaje_error)
                        
        except Exception as e:
            QMessageBox.critical(dialog, "Error", f"Error al dar de baja autobús: {str(e)}")