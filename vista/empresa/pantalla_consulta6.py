# vista/empresa/pantalla_consulta6.py

from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor
from vista.empresa.pantalla_consulta6_ui import Ui_Form

class PantallaConsulta6(QWidget):
    def __init__(self, app_manager=None):
        super().__init__()
        self.app_manager = app_manager
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor('white'))