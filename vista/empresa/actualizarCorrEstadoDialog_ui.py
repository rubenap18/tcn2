# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'actualizarCorrEstadoDialog.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(438, 298)
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 60, 421, 20))
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 0, 511, 81))
        font = QFont()
        font.setPointSize(27)
        font.setBold(True)
        self.label_5.setFont(font)
        self.comboBox_estadoCorrida = QComboBox(Form)
        self.comboBox_estadoCorrida.addItem("")
        self.comboBox_estadoCorrida.addItem("")
        self.comboBox_estadoCorrida.setObjectName(u"comboBox_estadoCorrida")
        self.comboBox_estadoCorrida.setGeometry(QRect(20, 196, 181, 24))
        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(-20, 80, 741, 20))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 170, 91, 20))
        font1 = QFont()
        font1.setPointSize(11)
        self.label_8.setFont(font1)
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 114, 71, 20))
        self.label_7.setFont(font1)
        self.boton_actualizar = QPushButton(Form)
        self.boton_actualizar.setObjectName(u"boton_actualizar")
        self.boton_actualizar.setGeometry(QRect(220, 260, 101, 31))
        font2 = QFont()
        font2.setBold(True)
        self.boton_actualizar.setFont(font2)
        self.boton_actualizar.setStyleSheet(u"QPushButton{\n"
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
        self.lineEdit_numeroCorrida = QLineEdit(Form)
        self.lineEdit_numeroCorrida.setObjectName(u"lineEdit_numeroCorrida")
        self.lineEdit_numeroCorrida.setGeometry(QRect(20, 140, 181, 22))
        self.lineEdit_numeroCorrida.setMaxLength(4)
        self.label_estadoActual = QLabel(Form)
        self.label_estadoActual.setObjectName(u"label_estadoActual")
        self.label_estadoActual.setGeometry(QRect(220, 140, 200, 22))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.label_estadoActual.setFont(font3)
        self.boton_cancelar = QPushButton(Form)
        self.boton_cancelar.setObjectName(u"boton_cancelar")
        self.boton_cancelar.setGeometry(QRect(330, 260, 91, 31))
        self.boton_cancelar.setFont(font2)
        self.boton_cancelar.setStyleSheet(u"QPushButton{\n"
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

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Por favor, ingresa el n\u00famero de corrida a la que quieres cambiar su estado", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Actualizar estado", None))
        self.comboBox_estadoCorrida.setItemText(0, QCoreApplication.translate("Form", u"ACTIVA", None))
        self.comboBox_estadoCorrida.setItemText(1, QCoreApplication.translate("Form", u"INACTIVA", None))

        self.comboBox_estadoCorrida.setPlaceholderText(QCoreApplication.translate("Form", u"Estado", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Estado", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"N\u00famero", None))
        self.boton_actualizar.setText(QCoreApplication.translate("Form", u"Actualizar", None))
        self.lineEdit_numeroCorrida.setText("")
        self.lineEdit_numeroCorrida.setPlaceholderText(QCoreApplication.translate("Form", u"N\u00famero", None))
        self.label_estadoActual.setText(QCoreApplication.translate("Form", u"Estado Actual: N/A", None))
        self.boton_cancelar.setText(QCoreApplication.translate("Form", u"Cancelar", None))
    # retranslateUi

