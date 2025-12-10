import os
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QDialog, QHeaderView, QVBoxLayout, QComboBox, QLineEdit, QPushButton, QLabel, QAbstractItemView
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, Qt

from vista.empresa.ciudadWidget import CiudadWidget


class PantallaRutas(QWidget):
    def __init__(self, app_manager, parent=None):
        super().__init__(parent)
        
        self.controlador = app_manager.controlador_prutas
        self.app_manager = app_manager

        # Cargar el archivo .ui
        self.ui = self.load_ui("pantalla_rutas.ui")

        # Crear un layout y añadir el widget cargado
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.ui)
        self.setLayout(layout)

        # Guardar estado
        self.todas_las_rutas = []
        self.ciudades_map = {}

        # Configurar la tabla
        self.ui.QtableWidget_rutas.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.QtableWidget_rutas.setEditTriggers(QAbstractItemView.NoEditTriggers) # Deshabilitar edición de celdas
        self.ui.QtableWidget_rutas.setSelectionBehavior(QAbstractItemView.SelectRows) # Mantener selección por fila

        # Conectar señales a slots
        self.ui.boton_agregaruta.clicked.connect(self.abrir_dialogo_agregar)
        self.ui.boton_editaruta.clicked.connect(self.abrir_dialogo_editar)
        self.ui.boton_ciudades.clicked.connect(self.abrir_widget_ciudades)
        self.ui.comboBox_forigen.currentIndexChanged.connect(self.filtrar_rutas)
        self.ui.comboBox_fdestino.currentIndexChanged.connect(self.filtrar_rutas)
        
        # Cargar datos iniciales
        self.cargar_datos_iniciales()

    def load_ui(self, filename):
        """Carga un archivo .ui dinámicamente y devuelve el widget"""
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), filename)
        ui_file = QFile(path)
        if not ui_file.open(QIODevice.ReadOnly):
            raise IOError(f"No se puede abrir el archivo UI: {path}")
        widget = loader.load(ui_file, self)
        ui_file.close()
        return widget

    def cargar_datos_iniciales(self):
        """Llama al controlador para obtener rutas y ciudades y actualiza la UI"""
        rutas = self.controlador.obtener_todas_las_rutas()
        ciudades_map = self.controlador.obtener_ciudades_map()

        if rutas is False or ciudades_map is False:
            QMessageBox.critical(self, "Error", "No se pudieron cargar los datos iniciales desde la base de datos")
            return

        self.todas_las_rutas = rutas if rutas is not None else []
        self.ciudades_map = ciudades_map if ciudades_map is not None else {}
        
        self.llenar_filtros_ciudades()
        self.mostrar_rutas_en_tabla(self.todas_las_rutas)

    def mostrar_rutas_en_tabla(self, rutas):
        """Puebla la tabla con la lista de rutas proporcionada"""
        self.ui.QtableWidget_rutas.setRowCount(0)
        for fila_idx, ruta in enumerate(rutas):
            self.ui.QtableWidget_rutas.insertRow(fila_idx)
            
            item_codigo = QTableWidgetItem(str(ruta.get_codigo()))
            item_codigo.setTextAlignment(Qt.AlignCenter)
            self.ui.QtableWidget_rutas.setItem(fila_idx, 0, item_codigo)
            
            item_origen = QTableWidgetItem(ruta.get_ciudadorigen())
            item_origen.setTextAlignment(Qt.AlignCenter)
            self.ui.QtableWidget_rutas.setItem(fila_idx, 1, item_origen)
            
            item_destino = QTableWidgetItem(ruta.get_ciudaddestino())
            item_destino.setTextAlignment(Qt.AlignCenter)
            self.ui.QtableWidget_rutas.setItem(fila_idx, 2, item_destino)
            
            item_distancia = QTableWidgetItem(f"{ruta.get_distancia()} km")
            item_distancia.setTextAlignment(Qt.AlignCenter)
            self.ui.QtableWidget_rutas.setItem(fila_idx, 3, item_distancia)

    def llenar_filtros_ciudades(self):
        """Puebla los ComboBox de filtro con ciudades únicas"""
        if not self.todas_las_rutas:
            origenes = []
            destinos = []
        else:
            origenes = sorted(list(set(r.get_ciudadorigen() for r in self.todas_las_rutas)))
            destinos = sorted(list(set(r.get_ciudaddestino() for r in self.todas_las_rutas)))
        
        self.ui.comboBox_forigen.clear()
        self.ui.comboBox_fdestino.clear()
        
        self.ui.comboBox_forigen.addItem("Todos")
        self.ui.comboBox_fdestino.addItem("Todos")
        
        self.ui.comboBox_forigen.addItems(origenes)
        self.ui.comboBox_fdestino.addItems(destinos)

    def filtrar_rutas(self):
        """Filtra las rutas mostradas según la selección de los ComboBox"""
        filtro_origen = self.ui.comboBox_forigen.currentText()
        filtro_destino = self.ui.comboBox_fdestino.currentText()
        
        if not self.todas_las_rutas:
            return
        
        rutas_filtradas = []
        for ruta in self.todas_las_rutas:
            coincide_origen = (filtro_origen == "Todos" or ruta.get_ciudadorigen() == filtro_origen)
            coincide_destino = (filtro_destino == "Todos" or ruta.get_ciudaddestino() == filtro_destino)
            if coincide_origen and coincide_destino:
                rutas_filtradas.append(ruta)
        
        self.mostrar_rutas_en_tabla(rutas_filtradas)

    def _attempt_add_ruta(self, dialogo, widget_dialogo):
        nombre_origen = widget_dialogo.findChild(QComboBox, "ComboBox_origen").currentText()
        nombre_destino = widget_dialogo.findChild(QComboBox, "ComboBox_destino").currentText()
        distancia = widget_dialogo.findChild(QLineEdit, "txt_distancia").text().strip()

        codigo_origen = self.ciudades_map.get(nombre_origen)
        codigo_destino = self.ciudades_map.get(nombre_destino)
        # print(f"DEBUG: Datos para agregar ruta - Origen: {codigo_origen}, Destino: {codigo_destino}, Distancia: {distancia}")

        # print("DEBUG: Calling controlador.agregar_nueva_ruta...")
        result = self.controlador.agregar_nueva_ruta(dialogo, codigo_origen, codigo_destino, distancia)
       

        if result:
            # print("DEBUG: Controlador returned True (success).")
            self.cargar_datos_iniciales()
            QMessageBox.information(self, "Éxito", "Ruta agregada correctamente")
            dialogo.accept() 
        

    def abrir_dialogo_agregar(self):
        """Abre un diálogo para agregar una nueva ruta"""
        try:
            dialogo = QDialog(self)
            
            loader = QUiLoader()
            path = os.path.join(os.path.dirname(__file__), "rutawidget.ui")
            ui_file = QFile(path)
            if not ui_file.open(QIODevice.ReadOnly):
                raise IOError(f"No se puede abrir el archivo de diálogo: {path}")

            widget_dialogo = loader.load(ui_file)
            ui_file.close()

            layout = QVBoxLayout(dialogo)
            layout.addWidget(widget_dialogo)
            dialogo.setWindowTitle("Agregar Nueva Ruta")

            combo_origen = widget_dialogo.findChild(QComboBox, "ComboBox_origen")
            combo_destino = widget_dialogo.findChild(QComboBox, "ComboBox_destino")
            
            nombres_ciudades = sorted(self.ciudades_map.keys())
            combo_origen.addItems(nombres_ciudades)
            combo_destino.addItems(nombres_ciudades)

            widget_dialogo.findChild(QPushButton, "boton_agregar").clicked.connect(lambda: self._attempt_add_ruta(dialogo, widget_dialogo))
            widget_dialogo.findChild(QPushButton, "boton_cancelar").clicked.connect(dialogo.reject)

            dialogo.exec() 
            

        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo abrir el diálogo de agregar: {e}")

    def _attempt_edit_ruta(self, dialogo, widget_dialogo, codigo_ruta):
        nueva_distancia = widget_dialogo.findChild(QLineEdit, "txt_distancia").text().strip()
        
        if self.controlador.actualizar_distancia_ruta(dialogo, codigo_ruta, nueva_distancia):
            self.cargar_datos_iniciales()
            QMessageBox.information(self, "Éxito", "Distancia actualizada correctamente.")
            dialogo.accept()

    def abrir_dialogo_editar(self, numero_operador): 
        """Abre un diálogo para editar la distancia de una ruta seleccionada"""
        fila_seleccionada = self.ui.QtableWidget_rutas.currentRow()
        if fila_seleccionada == -1:
            QMessageBox.warning(self, "Advertencia", "Selecciona una ruta para editar.")
            return

        codigo_ruta = self.ui.QtableWidget_rutas.item(fila_seleccionada, 0).text()
        origen_actual = self.ui.QtableWidget_rutas.item(fila_seleccionada, 1).text()
        destino_actual = self.ui.QtableWidget_rutas.item(fila_seleccionada, 2).text()
        distancia_actual = self.ui.QtableWidget_rutas.item(fila_seleccionada, 3).text().replace(" km", "")

        try:
            dialogo = QDialog(self)
            
            loader = QUiLoader()
            path = os.path.join(os.path.dirname(__file__), "rutawidget.ui")
            ui_file = QFile(path)
            if not ui_file.open(QIODevice.ReadOnly):
                raise IOError(f"No se pudo abrir el archivo de diálogo: {path}")

            widget_dialogo = loader.load(ui_file)
            ui_file.close()

            layout = QVBoxLayout(dialogo)
            layout.addWidget(widget_dialogo)
            dialogo.setWindowTitle(f"Editar Distancia - {origen_actual} a {destino_actual}")

            # Establecer el título del Label en el diálogo
            label_titulo = widget_dialogo.findChild(QLabel, "label_estatico_titulo")
            if label_titulo:
                label_titulo.setText("Editar Ruta")
                label_titulo.setAlignment(Qt.AlignCenter) # Centrar el texto

            combo_origen = widget_dialogo.findChild(QComboBox, "ComboBox_origen")
            combo_destino = widget_dialogo.findChild(QComboBox, "ComboBox_destino")
            line_distancia = widget_dialogo.findChild(QLineEdit, "txt_distancia") 
            
            # Limpiar ComboBox y establecer el texto actual
            combo_origen.clear()
            combo_origen.addItem(origen_actual)
            combo_origen.setCurrentText(origen_actual) # Asegura que esté seleccionado si no es el primer elemento
            combo_origen.setEnabled(False)

            combo_destino.clear()
            combo_destino.addItem(destino_actual)
            combo_destino.setCurrentText(destino_actual) # Asegura que esté seleccionado si no es el primer elemento
            combo_destino.setEnabled(False)

            line_distancia.setText(distancia_actual)
            
            boton_actualizar = widget_dialogo.findChild(QPushButton, "boton_agregar")
            boton_actualizar.setText("Actualizar Ruta") # Cambiar a "Actualizar Ruta"
            boton_actualizar.clicked.connect(lambda: self._attempt_edit_ruta(dialogo, widget_dialogo, codigo_ruta))
            widget_dialogo.findChild(QPushButton, "boton_cancelar").clicked.connect(dialogo.reject)

            dialogo.exec()
        
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo abrir el diálogo de edición: {e}")

    def abrir_widget_ciudades(self):
        """Abre el widget para administrar las ciudades como un diálogo"""
        try:
            dialogo_ciudades = QDialog(self)
            dialogo_ciudades.setWindowTitle("Administrar Ciudades")
            
            # Crear una instancia de CiudadWidget pasándole el controlador y el diálogo como parent
            ciudad_widget_instance = CiudadWidget(self.app_manager, dialogo_ciudades)
            
            # Crear un layout para el diálogo y añadir el CiudadWidget
            layout_dialogo = QVBoxLayout(dialogo_ciudades)
            layout_dialogo.addWidget(ciudad_widget_instance)
            dialogo_ciudades.setLayout(layout_dialogo)
            
            # Establecer tamaño fijo para el diálogo
            dialogo_ciudades.setFixedSize(440, 465)
            
            # Ejecutar el diálogo de forma modal
            dialogo_ciudades.exec()
            
            # Después de cerrar el diálogo, recargar los datos de rutas por si se modificaron ciudades
            self.cargar_datos_iniciales()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo abrir el diálogo de ciudades: {e}")