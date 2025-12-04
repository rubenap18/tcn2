# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'IngresarDatosPasajeroDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class IngresarDatosPasajeroDialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(630, 566)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 611, 71))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 130, 122, 39))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 190, 219, 39))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 250, 248, 39))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 310, 290, 39))
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 370, 102, 39))
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 420, 141, 39))
        self.lineEdit_ingresarNombre = QLineEdit(Dialog)
        self.lineEdit_ingresarNombre.setObjectName(u"lineEdit_ingresarNombre")
        self.lineEdit_ingresarNombre.setGeometry(QRect(160, 130, 441, 41))
        self.lineEdit_ingresarPrimerApellido = QLineEdit(Dialog)
        self.lineEdit_ingresarPrimerApellido.setObjectName(u"lineEdit_ingresarPrimerApellido")
        self.lineEdit_ingresarPrimerApellido.setGeometry(QRect(250, 190, 351, 41))
        self.lineEdit_ingresarSegundoApellido = QLineEdit(Dialog)
        self.lineEdit_ingresarSegundoApellido.setObjectName(u"lineEdit_ingresarSegundoApellido")
        self.lineEdit_ingresarSegundoApellido.setGeometry(QRect(280, 250, 321, 41))
        self.dateEdit_fechaNacimientoPasajero = QDateEdit(Dialog)
        self.dateEdit_fechaNacimientoPasajero.setObjectName(u"dateEdit_fechaNacimientoPasajero")
        self.dateEdit_fechaNacimientoPasajero.setGeometry(QRect(320, 310, 221, 41))
        self.lineEdit_ingresarCorreo = QLineEdit(Dialog)
        self.lineEdit_ingresarCorreo.setObjectName(u"lineEdit_ingresarCorreo")
        self.lineEdit_ingresarCorreo.setGeometry(QRect(180, 370, 421, 41))
        self.lineEdit_ingresarTelefono = QLineEdit(Dialog)
        self.lineEdit_ingresarTelefono.setObjectName(u"lineEdit_ingresarTelefono")
        self.lineEdit_ingresarTelefono.setGeometry(QRect(180, 420, 421, 41))
        self.boton_continuar = QPushButton(Dialog)
        self.boton_continuar.setObjectName(u"boton_continuar")
        self.boton_continuar.setGeometry(QRect(330, 500, 161, 51))
        self.boton_continuar.setStyleSheet(u"QPushButton {\n"
"    background-color: #1877F2;  /* Azul de Facebook */\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 8px 16px;\n"
"    border-radius: 6px;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"	background-color: rgb(0, 59, 176);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1458B8;  /* Azul m\u00e1s oscuro al presionar */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #CCCCCC;  /* Gris cuando est\u00e1 deshabilitado */\n"
"    color: #666666;\n"
"}")
        self.boton_continuar_2 = QPushButton(Dialog)
        self.boton_continuar_2.setObjectName(u"boton_continuar_2")
        self.boton_continuar_2.setGeometry(QRect(120, 500, 161, 51))
        self.boton_continuar_2.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 170, 0);\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 8px 16px;\n"
"    border-radius: 6px;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"	background-color: rgb(167, 111, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1458B8;  /* Azul m\u00e1s oscuro al presionar */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #CCCCCC;  /* Gris cuando est\u00e1 deshabilitado */\n"
"    color: #666666;\n"
"}")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:700; font-style:italic;\">Ingresar datos del pasajero</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:700;\">Nombre:</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:700;\">Primer apellido:</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:700;\">Segundo apellido:</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:700;\">Fecha de nacimiento:</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:700;\">Correo:</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:700;\">Tel\u00e9fono:</span></p></body></html>", None))
        self.boton_continuar.setText(QCoreApplication.translate("Dialog", u"Continuar", None))
        self.boton_continuar_2.setText(QCoreApplication.translate("Dialog", u"Regresar", None))
    # retranslateUi

