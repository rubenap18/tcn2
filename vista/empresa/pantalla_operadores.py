import os
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QDialog, QHeaderView, QVBoxLayout, QAbstractItemView, QLineEdit, QPushButton, QLabel, QApplication, QDateEdit
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, Qt, QDate
from PySide6.QtGui import QFont # Agregado
 # Se añadió QDate aquí

from datetime import date # Importar date para manejar fechas
from utilidades.validaciones import Validaciones # Asumiendo esta importación
from vista.empresa.operadoresWidget import OperadoresWidget # Agregado
# from .operador_dialog_ui import OperadorDialogUI # Asumiendo que OperadorDialogUI viene de un archivo Python generado
# O si es una clase definida en otro lugar:
# class OperadorDialogUI(object):
#    def setupUi(self, Dialog):
#        # ... implementacion del UI aquí ...
# Esto será un placeholder por ahora, ya que no encontré la definición.




class PantallaOperadores(QWidget):
    def __init__(self, controlador_operadores, app_manager, parent=None):
        super().__init__(parent)
        self.controlador_operadores = controlador_operadores
        self.app_manager = app_manager # Se asume que app_manager es necesario para otras interacciones
        
        self.ui = self.load_ui("pantalla_operadores.ui")
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.ui)
        self.setLayout(layout)

        # Configurar la tabla de operadores
        self.ui.QTableWidget_operadores.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.QTableWidget_operadores.setEditTriggers(QAbstractItemView.NoEditTriggers) # Hacerla no editable
        self.ui.QTableWidget_operadores.setSelectionBehavior(QAbstractItemView.SelectRows) # Hacerla seleccionable
        
        # Conectar señales y cargar datos iniciales
        self.ui.boton_agregaroperadores.clicked.connect(self.abrir_dialogo_agregar_operador) 
        self.ui.boton_editaroperadores.clicked.connect(self.editar_operador_seleccionado) 
        self.ui.lineEdit_boperadores.textChanged.connect(self.buscar_operadores) 
        
        self.cargar_operadores_desde_bd()

    def load_ui(self, filename):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), filename)
        ui_file = QFile(path)
        if not ui_file.open(QIODevice.ReadOnly):
            raise IOError(f"No se puede abrir el archivo UI: {path}")
        widget = loader.load(ui_file, self)
        ui_file.close()
        return widget

    'Funciones de operadores'
    def cargar_operadores_desde_bd(self):
        try:
            font_bold = QFont()
            font_bold.setBold(True)

            operadores = self.controlador_operadores.obtener_todos() 
            self.ui.QTableWidget_operadores.setRowCount(0)
            
            for fila_idx, operador in enumerate(operadores):
                self.ui.QTableWidget_operadores.insertRow(fila_idx)
                
                # Centrar los ítems de la tabla y poner en negritas
                item_numero = QTableWidgetItem(str(operador.get_numero()))
                item_numero.setTextAlignment(Qt.AlignCenter)
                item_numero.setFont(font_bold)
                self.ui.QTableWidget_operadores.setItem(fila_idx, 0, item_numero)
                
                item_nombre = QTableWidgetItem(operador.get_nombre_completo())
                item_nombre.setTextAlignment(Qt.AlignCenter)
                item_nombre.setFont(font_bold)
                self.ui.QTableWidget_operadores.setItem(fila_idx, 1, item_nombre)
                
                item_fechaNac = QTableWidgetItem(str(operador.get_fechaNac()))
                item_fechaNac.setTextAlignment(Qt.AlignCenter)
                item_fechaNac.setFont(font_bold)
                self.ui.QTableWidget_operadores.setItem(fila_idx, 2, item_fechaNac)
                
                item_telefono = QTableWidgetItem(operador.get_telefono())
                item_telefono.setTextAlignment(Qt.AlignCenter)
                item_telefono.setFont(font_bold)
                self.ui.QTableWidget_operadores.setItem(fila_idx, 3, item_telefono)
                
                item_fechaContrato = QTableWidgetItem(str(operador.get_fechaContrato()))
                item_fechaContrato.setTextAlignment(Qt.AlignCenter)
                item_fechaContrato.setFont(font_bold)
                self.ui.QTableWidget_operadores.setItem(fila_idx, 4, item_fechaContrato)
                
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudieron cargar los operadores: {e}")

    def _attempt_add_operador(self, dialogo, operadores_widget_instance):
        nombre = operadores_widget_instance.get_nombre_lineEdit().text().strip()
        apellPat = operadores_widget_instance.get_apellidop_lineEdit().text().strip()
        apellMat = operadores_widget_instance.get_apellidom_lineEdit().text().strip()
        telefono = operadores_widget_instance.get_telefono_lineEdit().text().strip()
        fechaNac = operadores_widget_instance.get_fechanacimiento_dateEdit().date().toString("yyyy-MM-dd")
        fechaContrato = operadores_widget_instance.get_fechacontrato_dateEdit().date().toString("yyyy-MM-dd")
        
        if self.controlador_operadores.insertar_operador(dialogo, nombre, apellPat, apellMat, fechaNac, telefono, fechaContrato):
            QMessageBox.information(self, "Éxito", "Operador agregado correctamente.")
            self.cargar_operadores_desde_bd()
            dialogo.accept() # Close the dialog only if successful
        # If validation fails, the controller already showed the QMessageBox, and we do nothing here, leaving the dialog open.

    def abrir_dialogo_agregar_operador(self):
        try:
            dialogo = QDialog(self)
            operadores_widget_instance = OperadoresWidget(dialogo)
            
            layout = QVBoxLayout(dialogo)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.addWidget(operadores_widget_instance)
            dialogo.setLayout(layout)
            dialogo.setWindowTitle("Nuevo Operador")

            dialogo.setFixedSize(424, 530) # Tamaño fijo
            
            # Connect the "Agregar" button to our custom handler
            operadores_widget_instance.get_agregar_button().clicked.connect(lambda: self._attempt_add_operador(dialogo, operadores_widget_instance))
            operadores_widget_instance.get_cancelar_button().clicked.connect(dialogo.reject) 
            
            # Establecer el título del Label en el diálogo
            label_titulo = operadores_widget_instance.get_title_label()
            if label_titulo:
                label_titulo.setText("Añadir nuevo operador") # Texto por defecto del UI
                label_titulo.setAlignment(Qt.AlignCenter)

            dialogo.exec() # Show the dialog as modal, but it only closes on accept() or reject()
                        
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al abrir diálogo operador: {e}") 
            print(f"Error al abrir diálogo operador: {e}")

    def editar_operador_seleccionado(self):
        try:
            fila_seleccionada = self.ui.QTableWidget_operadores.currentRow()
            
            if fila_seleccionada == -1:
                QMessageBox.warning(self, "Advertencia", "Selecciona un operador para editar")
                return
            
            numero_item = self.ui.QTableWidget_operadores.item(fila_seleccionada, 0)
            if not numero_item:
                return
                
            numero_operador = numero_item.text()
            self.abrir_dialogo_editar_operador(numero_operador)
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al editar operador: {e}") # Usar QMessageBox
            print(f"Error al editar operador: {e}")

    def _attempt_edit_operador(self, dialogo, operadores_widget_instance, numero_operador_int):
        nombre = operadores_widget_instance.get_nombre_lineEdit().text().strip()
        apellPat = operadores_widget_instance.get_apellidop_lineEdit().text().strip()
        apellMat = operadores_widget_instance.get_apellidom_lineEdit().text().strip()
        telefono = operadores_widget_instance.get_telefono_lineEdit().text().strip()
        fechaNac = operadores_widget_instance.get_fechanacimiento_dateEdit().date().toString("yyyy-MM-dd")
        fechaContrato = operadores_widget_instance.get_fechacontrato_dateEdit().date().toString("yyyy-MM-dd")
        
        if self.controlador_operadores.actualizar_operador(dialogo, numero_operador_int, nombre, apellPat, apellMat, fechaNac, telefono, fechaContrato):
            QMessageBox.information(self, "Éxito", "Operador actualizado correctamente.")
            self.cargar_operadores_desde_bd()
            dialogo.accept() # Close the dialog only if successful
        # If validation fails, the controller already showed the QMessageBox, and we do nothing here, leaving the dialog open.


    def abrir_dialogo_editar_operador(self, numero_operador):
        try:
            # validador = Validaciones() # No longer needed
            
            operadores = self.controlador_operadores.obtener_todos() 
            operador_actual = None
            
            numero_operador_int = int(numero_operador)
            
            for operador in operadores:
                if operador.get_numero() == numero_operador_int:
                    operador_actual = operador
                    break
            
            if not operador_actual:
                QMessageBox.warning(self, "Advertencia", "Operador no encontrado para editar.")
                return
                
            dialogo = QDialog(self)
            operadores_widget_instance = OperadoresWidget(dialogo)
            
            layout = QVBoxLayout(dialogo)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.addWidget(operadores_widget_instance)
            dialogo.setLayout(layout)

            dialogo.setFixedSize(424, 530) # Tamaño fijo

            dialogo.setWindowTitle("Editar Operador")
            
            # Establecer el título del Label en el diálogo
            label_titulo = operadores_widget_instance.get_title_label()
            if label_titulo:
                label_titulo.setText("Editar Operador") 
                label_titulo.setAlignment(Qt.AlignCenter) 

            # Llenar con datos actuales usando getters
            operadores_widget_instance.get_nombre_lineEdit().setText(operador_actual.get_nombre())
            operadores_widget_instance.get_apellidop_lineEdit().setText(operador_actual.get_apellPat())
            operadores_widget_instance.get_apellidom_lineEdit().setText(operador_actual.get_apellMat())
            operadores_widget_instance.get_telefono_lineEdit().setText(operador_actual.get_telefono())
            
            # Convertir fechas usando getters y deshabilitar
            fechaNac = operador_actual.get_fechaNac()
            if isinstance(fechaNac, date):
                operadores_widget_instance.get_fechanacimiento_dateEdit().setDate(QDate(fechaNac.year, fechaNac.month, fechaNac.day))
            else:
                operadores_widget_instance.get_fechanacimiento_dateEdit().setDate(QDate.currentDate())
            operadores_widget_instance.get_fechanacimiento_dateEdit().setEnabled(False) # Deshabilitar

            fechaContrato = operador_actual.get_fechaContrato()
            if isinstance(fechaContrato, date):
                operadores_widget_instance.get_fechacontrato_dateEdit().setDate(QDate(fechaContrato.year, fechaContrato.month, fechaContrato.day))
            else:
                operadores_widget_instance.get_fechacontrato_dateEdit().setDate(QDate.currentDate())
            operadores_widget_instance.get_fechacontrato_dateEdit().setEnabled(False) # Deshabilitar
            
            # Connect the "Actualizar" button to our custom handler
            operadores_widget_instance.get_agregar_button().clicked.connect(lambda: self._attempt_edit_operador(dialogo, operadores_widget_instance, numero_operador_int))
            operadores_widget_instance.get_cancelar_button().clicked.connect(dialogo.reject) 
            operadores_widget_instance.get_agregar_button().setText("Actualizar Operador")  
            
            dialogo.exec() # Show the dialog as modal, but it only closes on accept() or reject()
                    
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al abrir diálogo de edición operador: {e}") 
            print(f"Error al abrir diálogo de edición operador: {e}")

    def buscar_operadores(self):
        'Buscar operadores según el texto en el QLineEdit'
        try:
            font_bold = QFont()
            font_bold.setBold(True)

            criterio = self.ui.lineEdit_boperadores.text().strip()  
            
            if not criterio:
                self.cargar_operadores_desde_bd()
                return
            
            resultados = self.controlador_operadores.buscar_operadores(criterio)
            self.ui.QTableWidget_operadores.setRowCount(0)
            
            for fila_idx, operador in enumerate(resultados):
                numero = operador.get_numero()
                nombre_completo = operador.get_nombre_completo()
                fechaNac = operador.get_fechaNac()
                telefono = operador.get_telefono()
                fechaContrato = operador.get_fechaContrato()
                
                self.ui.QTableWidget_operadores.insertRow(fila_idx)
                
                item_numero = QTableWidgetItem(str(numero))
                item_numero.setTextAlignment(Qt.AlignCenter)
                item_numero.setFont(font_bold)
                self.ui.QTableWidget_operadores.setItem(fila_idx, 0, item_numero)
                
                item_nombre_completo = QTableWidgetItem(nombre_completo)
                item_nombre_completo.setTextAlignment(Qt.AlignCenter)
                item_nombre_completo.setFont(font_bold)
                self.ui.QTableWidget_operadores.setItem(fila_idx, 1, item_nombre_completo)
                
                item_fechaNac = QTableWidgetItem(str(fechaNac))
                item_fechaNac.setTextAlignment(Qt.AlignCenter)
                item_fechaNac.setFont(font_bold)
                self.ui.QTableWidget_operadores.setItem(fila_idx, 2, item_fechaNac)
                
                item_telefono = QTableWidgetItem(telefono)
                item_telefono.setTextAlignment(Qt.AlignCenter)
                item_telefono.setFont(font_bold)
                self.ui.QTableWidget_operadores.setItem(fila_idx, 3, item_telefono)
                
                item_fechaContrato = QTableWidgetItem(str(fechaContrato))
                item_fechaContrato.setTextAlignment(Qt.AlignCenter)
                item_fechaContrato.setFont(font_bold)
                self.ui.QTableWidget_operadores.setItem(fila_idx, 4, item_fechaContrato)
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al buscar operadores: {e}") # Usar QMessageBox
            print(f"Error al buscar operadores: {e}")