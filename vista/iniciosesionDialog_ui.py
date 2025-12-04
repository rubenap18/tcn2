# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'iniciosesionDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(934, 700)
        self.label_estatico_sincuenta = QLabel(Form)
        self.label_estatico_sincuenta.setObjectName(u"label_estatico_sincuenta")
        self.label_estatico_sincuenta.setGeometry(QRect(470, 620, 131, 21))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        self.label_estatico_sincuenta.setFont(font)
        self.label_imagen_identificate = QLabel(Form)
        self.label_imagen_identificate.setObjectName(u"label_imagen_identificate")
        self.label_imagen_identificate.setGeometry(QRect(0, 0, 451, 721))
        self.label_imagen_identificate.setPixmap(QPixmap(u"recursos/recursos_usuario/image(4).png"))
        self.lineEdit_contrasena = QLineEdit(Form)
        self.lineEdit_contrasena.setObjectName(u"lineEdit_contrasena")
        self.lineEdit_contrasena.setGeometry(QRect(480, 390, 401, 32))
        self.lineEdit_contrasena.setMinimumSize(QSize(0, 32))
        self.lineEdit_contrasena.setMaximumSize(QSize(16777215, 24))
        font1 = QFont()
        self.lineEdit_contrasena.setFont(font1)
        self.lineEdit_contrasena.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(246, 245, 244);\n"
"    border: 1px solid #dcdfe6;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-size: 13px;\n"
"    color: #606266;\n"
"    min-height: 18px;\n"
"}\n"
"")
        self.lineEdit_contrasena.setEchoMode(QLineEdit.EchoMode.Password)
        self.label_estatico_telefono = QLabel(Form)
        self.label_estatico_telefono.setObjectName(u"label_estatico_telefono")
        self.label_estatico_telefono.setGeometry(QRect(480, 260, 111, 31))
        font2 = QFont()
        font2.setPointSize(18)
        self.label_estatico_telefono.setFont(font2)
        self.boton_invitado = QPushButton(Form)
        self.boton_invitado.setObjectName(u"boton_invitado")
        self.boton_invitado.setGeometry(QRect(550, 530, 261, 31))
        font3 = QFont()
        font3.setBold(True)
        font3.setUnderline(True)
        self.boton_invitado.setFont(font3)
        self.boton_invitado.setStyleSheet(u"QPushButton{\n"
"	background: white;\n"
"	color:#00000;\n"
"	border:none;\n"
"	border-radius: 15px;\n"
"	font-weight: bold;\n"
"	font-size: 14px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(222, 221, 218);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(192, 191, 188);\n"
"}")
        self.label_estatico_identificatetxt = QLabel(Form)
        self.label_estatico_identificatetxt.setObjectName(u"label_estatico_identificatetxt")
        self.label_estatico_identificatetxt.setGeometry(QRect(470, 150, 411, 41))
        font4 = QFont()
        font4.setPointSize(13)
        self.label_estatico_identificatetxt.setFont(font4)
        self.label_estatico_identificatetxt.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_estatico_identificatetxt.setWordWrap(True)
        self.boton_registrate = QPushButton(Form)
        self.boton_registrate.setObjectName(u"boton_registrate")
        self.boton_registrate.setGeometry(QRect(610, 610, 131, 41))
        font5 = QFont()
        font5.setBold(True)
        self.boton_registrate.setFont(font5)
        self.boton_registrate.setStyleSheet(u"QPushButton{\n"
"	background: white;\n"
"	color:#1061C4;\n"
"	border: 2px solid #1061C4;\n"
"	border-radius: 15px;\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #0D4FAB;    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0A3F8A;     \n"
"}")
        self.label_estatico_identificate = QLabel(Form)
        self.label_estatico_identificate.setObjectName(u"label_estatico_identificate")
        self.label_estatico_identificate.setGeometry(QRect(470, 90, 411, 41))
        font6 = QFont()
        font6.setPointSize(25)
        font6.setBold(True)
        self.label_estatico_identificate.setFont(font6)
        self.label_estatico_identificate.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_telefono = QLineEdit(Form)
        self.lineEdit_telefono.setObjectName(u"lineEdit_telefono")
        self.lineEdit_telefono.setGeometry(QRect(480, 300, 401, 32))
        self.lineEdit_telefono.setMinimumSize(QSize(0, 32))
        self.lineEdit_telefono.setMaximumSize(QSize(16777215, 24))
        self.lineEdit_telefono.setFont(font1)
        self.lineEdit_telefono.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(246, 245, 244);\n"
"    border: 1px solid #dcdfe6;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-size: 13px;\n"
"    color: #606266;\n"
"    min-height: 18px;\n"
"}\n"
"\n"
"")
        self.label_estatico_contrasena = QLabel(Form)
        self.label_estatico_contrasena.setObjectName(u"label_estatico_contrasena")
        self.label_estatico_contrasena.setGeometry(QRect(480, 349, 141, 31))
        self.label_estatico_contrasena.setFont(font2)
        self.boton_continuar = QPushButton(Form)
        self.boton_continuar.setObjectName(u"boton_continuar")
        self.boton_continuar.setGeometry(QRect(550, 477, 261, 51))
        self.boton_continuar.setFont(font5)
        self.boton_continuar.setStyleSheet(u"QPushButton{\n"
"	background: #1061C4;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 15px;\n"
"	font-weight: bold;\n"
"	font-size: 22px;\n"
"}\n"
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
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_estatico_sincuenta.setText(QCoreApplication.translate("Form", u"\u00bfAun sin cuenta?", None))
        self.label_imagen_identificate.setText("")
        self.lineEdit_contrasena.setInputMask("")
        self.label_estatico_telefono.setText(QCoreApplication.translate("Form", u"Tel\u00e9fono:", None))
        self.boton_invitado.setText(QCoreApplication.translate("Form", u"Ingresa como invitado", None))
        self.label_estatico_identificatetxt.setText(QCoreApplication.translate("Form", u"Accede para comprar boletos y getionar tus reservaciones de forma mas sencilla.", None))
        self.boton_registrate.setText(QCoreApplication.translate("Form", u"reg\u00edstrate", None))
        self.label_estatico_identificate.setText(QCoreApplication.translate("Form", u"\u00a1Hola, identif\u00edcate!", None))
        self.lineEdit_telefono.setInputMask(QCoreApplication.translate("Form", u"9999999999", None))
        self.label_estatico_contrasena.setText(QCoreApplication.translate("Form", u"Contrase\u00f1a:", None))
        self.boton_continuar.setText(QCoreApplication.translate("Form", u"Continuar", None))
    # retranslateUi

