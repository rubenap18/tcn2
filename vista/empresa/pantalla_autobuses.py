# vista/empresa/pantalla_autobuses.py

from PySide6.QtWidgets import QWidget
from vista.empresa.pantalla_autobuses_ui import Ui_pantalla_autobuses
from controladores.controlador_pantalla_autobuses import ControladorPantallaAutobuses

class PantallaAutobuses(QWidget):
    def __init__(self, controlador_pa):
        super().__init__()
        self.controlador = controlador_pa
        self.ui = Ui_pantalla_autobuses()
        self.ui.setupUi(self)
        
        # Configurar la UI usando el controlador
        self.controlador.setup_ui(self, self.ui)