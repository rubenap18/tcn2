import os
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QDateEdit, QPushButton, QLabel
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, Qt

class OperadoresWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "operadoresWidget.ui")
        ui_file = QFile(path)
        if not ui_file.open(QIODevice.ReadOnly):
            raise IOError(f"No se puede abrir el archivo UI: {path}")
        loader.load(ui_file, self) # Carga el UI directamente en 'self'
        ui_file.close()

        
    # Métodos para acceder a los widgets
    def get_nombre_lineEdit(self):
        return self.findChild(QLineEdit, "lineEdit_nombre")

    def get_apellidop_lineEdit(self):
        return self.findChild(QLineEdit, "lineEdit_apellidop")

    def get_apellidom_lineEdit(self):
        return self.findChild(QLineEdit, "lineEdit_apellidom")

    def get_telefono_lineEdit(self):
        return self.findChild(QLineEdit, "lineEdit_telefono")

    def get_fechanacimiento_dateEdit(self):
        return self.findChild(QDateEdit, "dateEdit_fechanacimiento")

    def get_fechacontrato_dateEdit(self):
        return self.findChild(QDateEdit, "dateEdit_fechacontrato")

    def get_agregar_button(self):
        return self.findChild(QPushButton, "boton_agregar")

    def get_cancelar_button(self):
        return self.findChild(QPushButton, "boton_cancelar")

    def get_title_label(self):
        return self.findChild(QLabel, "label_estatico_titulo")
