from PySide6.QtWidgets import QWidget
from vista.empresa.pantalla_operadorescorridas_ui import Ui_pantalla_operadorescorridas

class PantallaOperadoresCorridas(QWidget):
    def __init__(self, app_manager=None, another_param=None):
        super().__init__()
        self.app_manager = app_manager
        self.ui = Ui_pantalla_operadorescorridas()
        self.ui.setupUi(self)
import os
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, Qt

class PantallaOperadoresCorridas(QWidget):
    def __init__(self, controlador, operator_id=None, parent=None):
        super().__init__(parent)
        self.controlador = controlador
        self.operator_id = operator_id

        # Crear una instancia del loader
        loader = QUiLoader()

        # Esto construye la ruta correcta sin importar desde donde se ejecute el script
        path = os.path.join(os.path.dirname(__file__),"pantalla_operadorescorridas.ui")
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
        
        if self.operator_id:
            self.cargar_datos()

    def cargar_datos(self):
        if not self.operator_id:
            print("No operator ID provided.")
            return

        print(f"Loading data for operator ID: {self.operator_id}")
        corridas = self.controlador.obtener_todas_las_corridas_detalladas(self.operator_id)
        print(f"Data returned from controller: {corridas}")
        
        if not corridas:
            self.ui.QtableWidget_corridas.setRowCount(0)
            return

        self.ui.QtableWidget_corridas.setRowCount(len(corridas))
        
        self.ui.label_estatico_operador.setText(corridas[0]['nombre_operador'])

        for row_index, corrida in enumerate(corridas):
            # "numero_viaje"
            self.ui.QtableWidget_corridas.setItem(row_index, 0, QTableWidgetItem(str(corrida['numero_viaje'])))
            # "fecha_hora_salida"
            self.ui.QtableWidget_corridas.setItem(row_index, 1, QTableWidgetItem(corrida['fecha_hora_salida']))
            # "fecha_hora_llegada"
            self.ui.QtableWidget_corridas.setItem(row_index, 2, QTableWidgetItem(corrida['fecha_hora_llegada']))
            # "ciudad_origen"
            self.ui.QtableWidget_corridas.setItem(row_index, 3, QTableWidgetItem(corrida['ciudad_origen']))
            # "ciudad_destino"
            self.ui.QtableWidget_corridas.setItem(row_index, 4, QTableWidgetItem(corrida['ciudad_destino']))
            # "autobus_numero"
            self.ui.QtableWidget_corridas.setItem(row_index, 5, QTableWidgetItem(str(corrida['autobus_numero'])))
            # "cantidad_pasajeros"
            self.ui.QtableWidget_corridas.setItem(row_index, 6, QTableWidgetItem(str(corrida['cantidad_pasajeros'])))
            
            for col_index in range(7):
                item = self.ui.QtableWidget_corridas.item(row_index, col_index)
                if item:
                    item.setTextAlignment(Qt.AlignCenter)
