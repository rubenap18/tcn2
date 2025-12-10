#imports de pyside
import os
from PySide6.QtWidgets import (QApplication, QMainWindow, QStackedWidget, QWidget,QVBoxLayout,
                            QDialog, QPushButton, QLineEdit, QLabel, QMessageBox, QTableWidget,
                            QTableWidgetItem, QComboBox, QInputDialog)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, QCoreApplication, Qt
from PySide6.QtGui import QCloseEvent
from utilidades.validaciones import Validaciones


class PantallaReservaciones(QWidget):

    def __init__(self, controlador, app_manager, parent=None):
        super().__init__(parent)
        self.controlador = controlador
        self.app_manager = app_manager  # Para acceder a MostrarBoletosDialog

        # Crear una instancia del loader
        loader = QUiLoader()

        # Construye la ruta correcta sin importar desde donde se ejecute el script
        path = os.path.join(os.path.dirname(__file__),"pantalla_reservaciones.ui")
        ui_file = QFile(path)

        # Abrir el archivo
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Error: No se puede abrir el archivo UI en: {path}")
            # Si no se carga el UI, no tiene sentido continuar
            return

        # Cargar el UI, el loader devuelve un NUEVO WIDGET
        self.ui = loader.load(ui_file, self)
        ui_file.close()
        
        # Crear un layout para nuestro QDialog.
        # El QWidget está vacío por defecto, necesitamos un layout para organizar su contenido.
        layout = QVBoxLayout()

        # Añadir el widget que cargamos (self.ui) al layout.
        layout.addWidget(self.ui)

        # Establecer el layout en nuestro QDialog. Ahora el contenido del .ui es visible.
        self.setLayout(layout)

        # Ajustar el tamaño del diálogo al contenido del UI
        self.resize(self.ui.size())
        self.setContentsMargins(0,0,0,0)

        # Obtener componentes del .ui
        self.boton_crear_reservacion = self.ui.findChild(QPushButton,'boton_crear_reservacion')
        self.boton_editar_reservacion = self.ui.findChild(QPushButton,'boton_editar_reservacion')
        self.boton_buscar = self.ui.findChild(QPushButton,'boton_buscar')
        self.boton_buscar_2 = self.ui.findChild(QPushButton,'boton_buscar_2')  # NUEVO - Búsqueda por nombre
        self.boton_mostrarboleto = self.ui.findChild(QPushButton,'boton_mostrarboleto')
        self.boton_actualizar = self.ui.findChild(QPushButton,'boton_actualizar')  # NUEVO - Actualizar tabla

        self.line_edit_buscar_reservacion = self.ui.findChild(QLineEdit,'lineEdit_buscar')
        self.line_edit_buscar_nombre_pasajero = self.ui.findChild(QLineEdit,'lineEdit_buscarPorNombrePasajero')  # NUEVO
        self.combo_box_filtro = self.ui.findChild(QComboBox,'comboBox_filtros')

        self.table_widget = self.ui.findChild(QTableWidget,'tabla_reservaciones')

        # Centrar los encabezados de las columnas
        if self.table_widget:
            header = self.table_widget.horizontalHeader()
            for i in range(self.table_widget.columnCount()):
                item = self.table_widget.horizontalHeaderItem(i)
                if item:
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

        # Si el boton crear reservacion fue recuperado as True, entonces ejecuata el metodo determinado.
        if self.boton_crear_reservacion:
            self.boton_crear_reservacion.clicked.connect(self.filtrarPorComboBox)

        # Si el boton editar fue recuperado as True, entonces ejecuata el metodo determinado.
        if self.boton_editar_reservacion:
            self.boton_editar_reservacion.clicked.connect(self.editarReservacion)

        # Conectar botón mostrar boleto
        if self.boton_mostrarboleto:
            self.boton_mostrarboleto.clicked.connect(self.mostrar_boletos_reservacion)

        if self.combo_box_filtro:
            self.combo_box_filtro.currentIndexChanged.connect(self.filtrarPorComboBox)

        if self.boton_buscar:
            self.boton_buscar.clicked.connect(self.buscarPorCorrida)

        # Conectar botón de búsqueda por nombre de pasajero
        if self.boton_buscar_2:
            self.boton_buscar_2.clicked.connect(self.buscarPorNombrePasajero)

        # Conectar botón actualizar para recargar toda la tabla
        if self.boton_actualizar:
            self.boton_actualizar.clicked.connect(self.actualizarTabla)

        self.llenarTablaAlInicio()

    def crearReservacion(self):
        pass

    def buscarPorCorrida(self):
        """Busca reservaciones por número de corrida"""
        num_corrida = str(self.line_edit_buscar_reservacion.text())
        validacion = Validaciones.validar_id(num_corrida)
        if validacion != num_corrida:
            return QMessageBox.information(self, "Mensaje", validacion)
        corridas = self.controlador.buscarReservacionPorCorrida(num_corrida)
        if not corridas:
            self.llenarTablaAlInicio()
            return QMessageBox.information(self, "Mensaje", "No se encontraron reservaciones para la corrida ingresada.")
        self.__llenar_tabla_reservaciones(corridas)

    def buscarPorNombrePasajero(self):
        """
        NUEVO MÉTODO: Busca reservaciones por nombre del pasajero.
        Se activa al hacer clic en boton_buscar_2.
        """
        nombre_pasajero = self.line_edit_buscar_nombre_pasajero.text().strip()
        
        # Validar que se haya ingresado algo
        if not nombre_pasajero:
            QMessageBox.warning(
                self, 
                "Campo vacío", 
                "Por favor, ingresa el nombre del pasajero a buscar."
            )
            return
        
        # Validar longitud mínima (al menos 2 caracteres)
        if len(nombre_pasajero) < 2:
            QMessageBox.warning(
                self,
                "Búsqueda inválida",
                "Por favor, ingresa al menos 2 caracteres para buscar."
            )
            return
        
        try:
            # Buscar en el controlador
            reservaciones = self.controlador.buscarReservacionPorNombrePasajero(nombre_pasajero)
            
            if reservaciones is False:
                QMessageBox.warning(
                    self,
                    "Error de validación",
                    "El nombre ingresado no es válido."
                )
                return
            
            if not reservaciones:
                self.llenarTablaAlInicio()
                QMessageBox.information(
                    self,
                    "Sin resultados",
                    f"No se encontraron reservaciones para el pasajero: '{nombre_pasajero}'"
                )
                return
            
            # Llenar la tabla con los resultados
            self.__llenar_tabla_reservaciones(reservaciones)
            
            # Mostrar mensaje de éxito
            QMessageBox.information(
                self,
                "Búsqueda exitosa",
                f"Se encontraron {len(reservaciones)} reservación(es) para: '{nombre_pasajero}'"
            )
            
        except Exception as e:
            print(f"Error al buscar por nombre de pasajero: {e}")
            QMessageBox.critical(
                self,
                "Error",
                f"Ocurrió un error al buscar las reservaciones:\n{str(e)}"
            )

    def actualizarTabla(self):
        """
        NUEVO MÉTODO: Actualiza la tabla cargando todas las reservaciones de nuevo.
        Se activa al hacer clic en boton_actualizar.
        También limpia los campos de búsqueda.
        """
        try:
            # Limpiar campos de búsqueda
            if self.line_edit_buscar_reservacion:
                self.line_edit_buscar_reservacion.clear()
            
            if self.line_edit_buscar_nombre_pasajero:
                self.line_edit_buscar_nombre_pasajero.clear()
            
            # Recargar todas las reservaciones
            self.llenarTablaAlInicio()
            
            print("Tabla de reservaciones actualizada exitosamente")
            
        except Exception as e:
            print(f"Error al actualizar la tabla: {e}")
            QMessageBox.critical(
                self,
                "Error",
                f"Ocurrió un error al actualizar la tabla:\n{str(e)}"
            )

    def editarReservacion(self):
        """
        Obtiene los datos de la fila que está actualmente seleccionada o enfocada.
        Retorna una lista con el contenido de cada celda de esa fila.
        """

        tabla = self.table_widget  # Se Asume que 'self.tableWidget' es tu QTableWidget

        # 1. Obtener el indice de la fila actualmente seleccionada/enfocada
        fila_actual = tabla.currentRow()

        # 2. Verificar si hay alguna fila seleccionada (-1 si no hay)
        if fila_actual < 0:
            print("No hay ninguna fila actualmente seleccionada o enfocada.")
            return None  # Retorna None si no hay selección

        # 3. Obtener la cantidad de columnas de la tabla (Método clave)
        num_columnas = tabla.columnCount()

        datos_fila = []

        # 4. Iterar sobre las columnas de la fila actual para extraer los datos
        for col_index in range(num_columnas):

            # Obtener el QTableWidgetItem en la posición (fila, columna)
            item = tabla.item(fila_actual, col_index)

            if item is not None:
                # Extraer el texto del QTableWidgetItem (Método clave)
                dato = item.text()
                datos_fila.append(dato)
            else:
                # Manejar celdas vacías si es posible
                datos_fila.append("")

        print(f"Datos de la fila {fila_actual}: {datos_fila}")
        return datos_fila

    def mostrar_boletos_reservacion(self):
        """
        Muestra los boletos de la reservación seleccionada.
        Obtiene el número de reservación directamente de la columna 0
        """
        # Obtener la fila seleccionada
        fila_actual = self.table_widget.currentRow()
        
        if fila_actual < 0:
            QMessageBox.warning(
                self,
                "Sin selección",
                "Por favor, selecciona una reservación de la tabla para ver sus boletos."
            )
            return
        
        # Obtener el número de reservación directamente de la columna 0
        item_numero_reservacion = self.table_widget.item(fila_actual, 0)
        
        if not item_numero_reservacion:
            QMessageBox.warning(
                self,
                "Error",
                "No se pudo obtener el número de reservación."
            )
            return
        
        try:
            numero_reservacion = int(item_numero_reservacion.text())
            print(f"Abriendo boletos para reservación #{numero_reservacion}")
            
            # Abrir el diálogo de boletos directamente
            from vista.compartido.mostrarBoletosDialog import MostrarBoletosDialog
            
            dialog = MostrarBoletosDialog(
                self.app_manager,
                numero_reservacion,
                self
            )
            dialog.exec()
            
        except ValueError:
            # Solo mostrar error si realmente hay un problema al convertir a int
            QMessageBox.warning(
                self,
                "Error",
                "El número de reservación no es válido."
            )
            return
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"No se pudieron cargar los boletos:\n{str(e)}"
            )
            print(f"Error al abrir diálogo de boletos: {e}")
            import traceback
            traceback.print_exc()

    def filtrarPorComboBox(self):
        filtro_seleccionado = self.combo_box_filtro.currentText()
        if filtro_seleccionado == "Reservaciones Activas":
            if True:
                pass
        elif filtro_seleccionado == "Reservaciones Pendientes":
            pass

        elif filtro_seleccionado in ["Nombre de cliente", "Origen", "Destino"]:
            # Titulo y etiqueta del dialogo
            titulo_dialogo = f"Buscar por {filtro_seleccionado}"
            etiqueta_dialogo = f"Ingrese el {filtro_seleccionado.lower()} a buscar:"

            # Llamamos al QInputDialog.getText()
            texto_busqueda, ok = QInputDialog.getText(self, titulo_dialogo, etiqueta_dialogo)

            # Verificamos si el usuario presionó "Ok" y si escribe algo
            if ok and texto_busqueda:
                validacion = Validaciones.validar_ciudad(texto_busqueda)
                
                if Validaciones.validar_ciudad(texto_busqueda) != texto_busqueda:
                    return QMessageBox.information(self, "Mensaje", texto_busqueda)

                if filtro_seleccionado == "Nombre de cliente":
                    pass # A implementar
                elif filtro_seleccionado == "Origen" or filtro_seleccionado == "Destino":
                    
                    datos_tabla = self.controlador.buscarReservacionPorCiudad(texto_busqueda)
                    self.__llenar_tabla_reservaciones(datos_tabla)
            else:
                # El usuario cancelo o no ingreso texto o no hace nada
                print("Busqueda cancelada por el usuario")
                self.llenarTablaAlInicio()

        elif filtro_seleccionado == "Fecha":
            pass
        

    def llenarTablaAlInicio(self):
        """Carga todas las reservaciones al iniciar la pantalla"""
        datos_tabla = self.controlador.consultarTodasReservacionesParaTabla()
        self.__llenar_tabla_reservaciones(datos_tabla)

    def __llenar_tabla_reservaciones(self, datos_tabla):
        """
        ACTUALIZADO: Llena la tabla de reservaciones con las 8 columnas requeridas.
        IMPORTANTE: Ahora centra el texto en TODAS las celdas.
        
        Estructura de datos esperada (8 columnas):
        0. Núm. Reservación
        1. Fecha Reservación
        2. Nombre Cliente (completo)
        3. Ciudad Origen
        4. Ciudad Destino
        5. Fecha y Hora Salida (combinadas)
        6. Cant. Pasajeros
        7. Fecha Límite Pago
        """
        # Validar datos de entrada
        if datos_tabla == True or datos_tabla == False:
            return
        
        if not datos_tabla:
            self.table_widget.setRowCount(0)
            print("No hay datos para llenar la tabla")
            return

        # Configurar número de filas
        self.table_widget.setRowCount(len(datos_tabla))
        
        # Llenar la tabla
        for row_index, row_data in enumerate(datos_tabla):
            # Iterar sobre cada columna (máximo 8 columnas según la tabla)
            for col_index in range(min(len(row_data), self.table_widget.columnCount())):
                item_data = row_data[col_index]
                
                # Crear el ítem
                item = QTableWidgetItem(str(item_data))
                
                # CENTRAR TEXTO EN TODAS LAS CELDAS
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                
                # Insertar el ítem en la celda
                self.table_widget.setItem(row_index, col_index, item)