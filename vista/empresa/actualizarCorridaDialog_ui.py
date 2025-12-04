# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'actualizarCorridaDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 250)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(16, 111, 365, 80))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_15 = QLabel(self.layoutWidget)
        self.label_15.setObjectName(u"label_15")
        font = QFont()
        font.setPointSize(11)
        self.label_15.setFont(font)

        self.verticalLayout_2.addWidget(self.label_15)

        self.comboBox_operadorCorrida = QComboBox(self.layoutWidget)
        self.comboBox_operadorCorrida.setObjectName(u"comboBox_operadorCorrida")

        self.verticalLayout_2.addWidget(self.comboBox_operadorCorrida)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(-10, 80, 741, 20))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 0, 511, 81))
        font1 = QFont()
        font1.setPointSize(27)
        font1.setBold(True)
        self.label.setFont(font1)
        self.boton_cancelarActualizacion = QPushButton(Form)
        self.boton_cancelarActualizacion.setObjectName(u"boton_cancelarActualizacion")
        self.boton_cancelarActualizacion.setGeometry(QRect(290, 200, 91, 31))
        font2 = QFont()
        font2.setBold(True)
        self.boton_cancelarActualizacion.setFont(font2)
        self.boton_cancelarActualizacion.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(237, 51, 59);\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(191, 41, 49);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color: rgb(141, 30, 36);\n"
"}")
        self.boton_actualizarCorrida = QPushButton(Form)
        self.boton_actualizarCorrida.setObjectName(u"boton_actualizarCorrida")
        self.boton_actualizarCorrida.setGeometry(QRect(180, 200, 101, 31))
        self.boton_actualizarCorrida.setFont(font2)
        self.boton_actualizarCorrida.setStyleSheet(u"QPushButton{\n"
"	background: #1061C4;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 6px;\n"
"	font-weight: bold;\n"
"	font-size:15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0D4FAB;    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0A3F8A;     \n"
"}")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Actualizar Corrida", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Operador", None))
        self.comboBox_operadorCorrida.setPlaceholderText(QCoreApplication.translate("Form", u"Operador", None))
        self.label.setText(QCoreApplication.translate("Form", u"Actualizar corrida", None))
        self.boton_cancelarActualizacion.setText(QCoreApplication.translate("Form", u"Cancelar", None))
        self.boton_actualizarCorrida.setText(QCoreApplication.translate("Form", u"Actualizar corrida", None))
    # retranslateUi

