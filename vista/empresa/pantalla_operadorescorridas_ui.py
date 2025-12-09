# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pantalla_operadorescorridas.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_pantalla_operadorescorridas(object):
    def setupUi(self, pantalla_operadorescorridas):
        if not pantalla_operadorescorridas.objectName():
            pantalla_operadorescorridas.setObjectName(u"pantalla_operadorescorridas")
        pantalla_operadorescorridas.resize(1920, 1080)
        self.label = QLabel(pantalla_operadorescorridas)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(500, 200, 800, 100))
        self.label.setText("Pantalla de Operadores Corridas")
        self.label.setStyleSheet("font-size: 48px; font-weight: bold;")

        self.retranslateUi(pantalla_operadorescorridas)

        QMetaObject.connectSlotsByName(pantalla_operadorescorridas)
    # setupUi

    def retranslateUi(self, pantalla_operadorescorridas):
        pantalla_operadorescorridas.setWindowTitle(QCoreApplication.translate("pantalla_operadorescorridas", u"Pantalla de Operadores Corridas", None))
        self.label.setText(QCoreApplication.translate("pantalla_operadorescorridas", u"Pantalla de Operadores Corridas", None))
        pass
    # retranslateUi