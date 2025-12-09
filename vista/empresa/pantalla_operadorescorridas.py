from PySide6.QtWidgets import QWidget
from vista.empresa.pantalla_operadorescorridas_ui import Ui_pantalla_operadorescorridas

class PantallaOperadoresCorridas(QWidget):
    def __init__(self, app_manager=None, another_param=None):
        super().__init__()
        self.app_manager = app_manager
        self.ui = Ui_pantalla_operadorescorridas()
        self.ui.setupUi(self)