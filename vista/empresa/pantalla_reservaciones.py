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
        self.app_manager = app_manager  # NUEVO - Para acceder a MostrarBoletosDialog

        # Crear una instancia del loader
        loader = QUiLoader()

        # Esto construye la ruta correcta sin importar desde donde se ejecute el script
        path = os.path.join(os.path.dirname(__file__),"pantalla_reservaciones.ui")
        ui_file = QFile(path)

        # 3. Abrir el archivo.
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Error: No se puede abrir el archivo UI en: {path}")
            # Si no se carga el UI, no tiene sentido continuar
            return

        # 4. Cargar el UI. El loader devuelve un NUEVO WIDGET.
        self.ui = loader.load(ui_file, self)
        ui_file.close()
        
        # 5. Crear un layout para nuestro QDialog.
        #    El QWidget está vacío por defecto, necesitamos un layout para organizar su contenido.
        layout = QVBoxLayout()

        # 6. Añadir el widget que cargamos (self.ui) al layout.
        layout.addWidget(self.ui)

        # 7. Establecer el layout en nuestro QDialog. Ahora el contenido del .ui es visible.
        self.setLayout(layout)

        # Opcional: Ajustar el tamaño del diálogo al contenido del UI
        self.resize(self.ui.size())
        self.setContentsMargins(0,0,0,0)

        #Obteniendo componentes del .ui
        self.boton_crear_reservacion = self.ui.findChild(QPushButton,'boton_crear_reservacion')
        self.boton_editar_reservacion = self.ui.findChild(QPushButton,'boton_editar_reservacion')
        self.boton_buscar = self.ui.findChild(QPushButton,'boton_buscar')
        self.boton_mostrarboleto = self.ui.findChild(QPushButton,'boton_mostrarboleto')  # NUEVO

        self.line_edit_buscar_reservacion = self.ui.findChild(QLineEdit,'lineEdit_buscar')
        self.combo_box_filtro = self.ui.findChild(QComboBox,'comboBox_filtros')

        self.table_widget = self.ui.findChild(QTableWidget,'tabla_reservaciones')

        # Si el boton crear reservacion fue recuperado as True, entonces ejecuata el metodo determinado.
        if self.boton_crear_reservacion:
            self.boton_crear_reservacion.clicked.connect(self.filtrarPorComboBox)

        # Si el boton editar fue recuperado as True, entonces ejecuata el metodo determinado.
        if self.boton_editar_reservacion:
            self.boton_editar_reservacion.clicked.connect(self.editarReservacion)

        # NUEVO - Conectar botón mostrar boleto
        if self.boton_mostrarboleto:
            self.boton_mostrarboleto.clicked.connect(self.mostrar_boletos_reservacion)

        if self.combo_box_filtro:
            self.combo_box_filtro.currentIndexChanged.connect(self.filtrarPorComboBox)

        if self.boton_buscar:
            self.boton_buscar.clicked.connect(self.buscarPorCorrida)


        self.llenarTablaAlInicio()

    def crearReservacion(self):
        pass

    def buscarPorCorrida(self):
        num_corrida = str(self.line_edit_buscar_reservacion.text())
        validacion = Validaciones.validar_id(num_corrida)
        if validacion != num_corrida:
            return QMessageBox.information(self, "Mensaje", validacion)
        corridas = self.controlador.buscarReservacionPorCorrida(num_corrida)
        print('corridas:',corridas)
        if not corridas:
            self.llenarTablaAlInicio()
            return QMessageBox.information(self, "Mensaje", "No se encontraron reservaciones para la corrida ingresada.")
        self.__llenar_tabla_reservaciones(corridas)

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
            print(f"✓ Abriendo boletos para reservación #{numero_reservacion}")
            
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

            # Verificamos si el usuario presionóo "Ok" y si escribio algo
            if ok and texto_busqueda:
                print(f"Buscando '{texto_busqueda}' en el filtro '{filtro_seleccionado}'")
                validacion = Validaciones.validar_ciudad(texto_busqueda)
                
                if Validaciones.validar_ciudad(texto_busqueda) != texto_busqueda:
                    return QMessageBox.information(self, "Mensaje", texto_busqueda)

                if filtro_seleccionado == "Nombre de cliente":
                    # Necesitarías un método en tu controlador para esto
                    # datos_tabla = self.controlador.buscarReservacionPorCliente(texto_busqueda)
                    # self.__llenar_tabla_reservaciones(datos_tabla)
                    pass # A implementar
                elif filtro_seleccionado == "Origen" or filtro_seleccionado == "Destino":
                    
                    datos_tabla = self.controlador.buscarReservacionPorCiudad(texto_busqueda)
                    self.__llenar_tabla_reservaciones(datos_tabla)
            else:
                # El usuario cancelo o no ingreso texto se recarga la tabla original o no hace nada
                print("Busqueda cancelada por el usuario.")
                self.llenarTablaAlInicio()

        elif filtro_seleccionado == "Fecha":
            pass
        

    def llenarTablaAlInicio(self):
        datos_tabla = self.controlador.consultarTodasReservacionesParaTabla()
        self.__llenar_tabla_reservaciones(datos_tabla)

    def __llenar_tabla_reservaciones(self,datos_tabla):
        # columnas = ["Nombre", "Edad", "Ciudad"]
        if datos_tabla == True or datos_tabla == False:
            return
        # Establecer la estructura
        self.table_widget.setRowCount(len(datos_tabla))
        num_columnas = self.table_widget.columnCount()

        num_cols_datos = len(datos_tabla[0])

        if not datos_tabla:
            self.table_widget.setRowCount(0) # Vacía la tabla si no hay datos
            print("No hay datos para llenar la tabla.")
            return

        for row_index, row_data in enumerate(datos_tabla):
        # Se usa el minimo entre las columnas de los datos y las columnas de la tabla 
        # para evitar errores si las dimensiones no coinciden.
            for col_index in range(min(num_cols_datos, self.table_widget.columnCount())):
                item_data = row_data[col_index]

                # Crear y configurar el ítem
                item = QTableWidgetItem(str(item_data))

                # 4. Insertar el item en la celda
                self.table_widget.setItem(row_index, col_index, item)

                # Si la columna es la 2 (indice 1), la centramos
                if col_index == 1: 
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)