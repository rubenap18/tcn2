# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pasajerosWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_pagina_pasajeros(object):
    def setupUi(self, pagina_pasajeros):
        if not pagina_pasajeros.objectName():
            pagina_pasajeros.setObjectName(u"pagina_pasajeros")
        pagina_pasajeros.resize(424, 530)
        pagina_pasajeros.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_estatico_titulo = QLabel(pagina_pasajeros)
        self.label_estatico_titulo.setObjectName(u"label_estatico_titulo")
        self.label_estatico_titulo.setGeometry(QRect(90, 20, 241, 31))
        font = QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setItalic(True)
        self.label_estatico_titulo.setFont(font)
        self.boton_agregar = QPushButton(pagina_pasajeros)
        self.boton_agregar.setObjectName(u"boton_agregar")
        self.boton_agregar.setGeometry(QRect(180, 470, 171, 41))
        font1 = QFont()
        font1.setBold(True)
        self.boton_agregar.setFont(font1)
        self.boton_agregar.setStyleSheet(u"QPushButton{\n"
"	background: #1061C4;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 20px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #0D4FAB;    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0A3F8A;     \n"
"}")
        self.boton_cancelar = QPushButton(pagina_pasajeros)
        self.boton_cancelar.setObjectName(u"boton_cancelar")
        self.boton_cancelar.setGeometry(QRect(70, 470, 91, 41))
        self.boton_cancelar.setFont(font1)
        self.boton_cancelar.setStyleSheet(u"QPushButton{\n"
"	background: #FF6A36;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 20px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #E85F30;   /* Naranja m\u00e1s oscuro */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #CC532A;   /* M\u00e1s oscuro para click */\n"
"}")
        self.layoutWidget = QWidget(pagina_pasajeros)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(70, 60, 281, 380))
        self.Layout_operadores = QVBoxLayout(self.layoutWidget)
        self.Layout_operadores.setObjectName(u"Layout_operadores")
        self.Layout_operadores.setContentsMargins(0, 0, 0, 0)
        self.label_estatico_nombre = QLabel(self.layoutWidget)
        self.label_estatico_nombre.setObjectName(u"label_estatico_nombre")
        font2 = QFont()
        font2.setPointSize(12)
        self.label_estatico_nombre.setFont(font2)

        self.Layout_operadores.addWidget(self.label_estatico_nombre)

        self.lineEdit_nombre = QLineEdit(self.layoutWidget)
        self.lineEdit_nombre.setObjectName(u"lineEdit_nombre")
        self.lineEdit_nombre.setMinimumSize(QSize(0, 32))
        self.lineEdit_nombre.setMaximumSize(QSize(16777215, 24))
        font3 = QFont()
        self.lineEdit_nombre.setFont(font3)
        self.lineEdit_nombre.setStyleSheet(u"QLineEdit {\n"
"    background-color: ;\n"
"	color: rgb(255, 255, 255);\n"
"    border: 1px solid #dcdfe6;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-size: 13px;\n"
"    color: #606266;\n"
"    min-height: 18px;\n"
"}")

        self.Layout_operadores.addWidget(self.lineEdit_nombre)

        self.label_estatico_apellidop = QLabel(self.layoutWidget)
        self.label_estatico_apellidop.setObjectName(u"label_estatico_apellidop")
        self.label_estatico_apellidop.setFont(font2)

        self.Layout_operadores.addWidget(self.label_estatico_apellidop)

        self.lineEdit_apellidop = QLineEdit(self.layoutWidget)
        self.lineEdit_apellidop.setObjectName(u"lineEdit_apellidop")
        self.lineEdit_apellidop.setMinimumSize(QSize(0, 32))
        self.lineEdit_apellidop.setMaximumSize(QSize(16777215, 24))
        self.lineEdit_apellidop.setFont(font3)
        self.lineEdit_apellidop.setStyleSheet(u"QLineEdit {\n"
"    background-color: ;\n"
"	color: rgb(255, 255, 255);\n"
"    border: 1px solid #dcdfe6;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-size: 13px;\n"
"    color: #606266;\n"
"    min-height: 18px;\n"
"}\n"
"")

        self.Layout_operadores.addWidget(self.lineEdit_apellidop)

        self.label_estatico_apellidom = QLabel(self.layoutWidget)
        self.label_estatico_apellidom.setObjectName(u"label_estatico_apellidom")
        self.label_estatico_apellidom.setFont(font2)

        self.Layout_operadores.addWidget(self.label_estatico_apellidom)

        self.lineEdit_apellidom = QLineEdit(self.layoutWidget)
        self.lineEdit_apellidom.setObjectName(u"lineEdit_apellidom")
        self.lineEdit_apellidom.setMinimumSize(QSize(0, 32))
        self.lineEdit_apellidom.setMaximumSize(QSize(16777215, 24))
        self.lineEdit_apellidom.setFont(font3)
        self.lineEdit_apellidom.setStyleSheet(u"QLineEdit {\n"
"    background-color: ;\n"
"	color: rgb(255, 255, 255);\n"
"    border: 1px solid #dcdfe6;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-size: 13px;\n"
"    color: #606266;\n"
"    min-height: 18px;\n"
"}\n"
"")

        self.Layout_operadores.addWidget(self.lineEdit_apellidom)

        self.label_estatico_telefono = QLabel(self.layoutWidget)
        self.label_estatico_telefono.setObjectName(u"label_estatico_telefono")
        self.label_estatico_telefono.setFont(font2)

        self.Layout_operadores.addWidget(self.label_estatico_telefono)

        self.lineEdit_telefono = QLineEdit(self.layoutWidget)
        self.lineEdit_telefono.setObjectName(u"lineEdit_telefono")
        self.lineEdit_telefono.setMinimumSize(QSize(0, 32))
        self.lineEdit_telefono.setMaximumSize(QSize(16777215, 24))
        self.lineEdit_telefono.setFont(font3)
        self.lineEdit_telefono.setStyleSheet(u"QLineEdit {\n"
"    background-color: ;\n"
"	color: rgb(255, 255, 255);\n"
"    border: 1px solid #dcdfe6;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-size: 13px;\n"
"    color: #606266;\n"
"    min-height: 18px;\n"
"}")

        self.Layout_operadores.addWidget(self.lineEdit_telefono)

        self.label_estatico_fechan = QLabel(self.layoutWidget)
        self.label_estatico_fechan.setObjectName(u"label_estatico_fechan")
        self.label_estatico_fechan.setFont(font2)

        self.Layout_operadores.addWidget(self.label_estatico_fechan)

        self.dateEdit_fechanacimiento = QDateEdit(self.layoutWidget)
        self.dateEdit_fechanacimiento.setObjectName(u"dateEdit_fechanacimiento")
        self.dateEdit_fechanacimiento.setMinimumSize(QSize(0, 32))
        self.dateEdit_fechanacimiento.setMaximumSize(QSize(16777215, 24))
        self.dateEdit_fechanacimiento.setFont(font3)
        self.dateEdit_fechanacimiento.setStyleSheet(u"\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #dcdfe6;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-size: 13px;\n"
"    color: #606266;\n"
"    min-height: 18px;\n"
"")
        self.dateEdit_fechanacimiento.setMaximumDateTime(QDateTime(QDate(2026, 12, 31), QTime(23, 59, 59)))
        self.dateEdit_fechanacimiento.setMaximumDate(QDate(2026, 12, 31))
        self.dateEdit_fechanacimiento.setCalendarPopup(False)

        self.Layout_operadores.addWidget(self.dateEdit_fechanacimiento)


        self.retranslateUi(pagina_pasajeros)

        QMetaObject.connectSlotsByName(pagina_pasajeros)
    # setupUi

    def retranslateUi(self, pagina_pasajeros):
        pagina_pasajeros.setWindowTitle(QCoreApplication.translate("pagina_pasajeros", u"Registrate", None))
        self.label_estatico_titulo.setText(QCoreApplication.translate("pagina_pasajeros", u"Ingresa tus datos", None))
        self.boton_agregar.setText(QCoreApplication.translate("pagina_pasajeros", u"Aceptar", None))
        self.boton_cancelar.setText(QCoreApplication.translate("pagina_pasajeros", u"Cancelar", None))
        self.label_estatico_nombre.setText(QCoreApplication.translate("pagina_pasajeros", u"Nombre", None))
        self.lineEdit_nombre.setInputMask(QCoreApplication.translate("pagina_pasajeros", u">A<AAAAAAAAAAAAAA", None))
        self.label_estatico_apellidop.setText(QCoreApplication.translate("pagina_pasajeros", u"Apellido Parterno", None))
        self.lineEdit_apellidop.setInputMask(QCoreApplication.translate("pagina_pasajeros", u">A<AAAAAAAAAAAAAA", None))
        self.label_estatico_apellidom.setText(QCoreApplication.translate("pagina_pasajeros", u"Apellido Materno", None))
        self.lineEdit_apellidom.setInputMask(QCoreApplication.translate("pagina_pasajeros", u">A<AAAAAAAAAAAAAA", None))
        self.label_estatico_telefono.setText(QCoreApplication.translate("pagina_pasajeros", u"Telefono", None))
        self.lineEdit_telefono.setInputMask(QCoreApplication.translate("pagina_pasajeros", u"9999999999", None))
        self.label_estatico_fechan.setText(QCoreApplication.translate("pagina_pasajeros", u"Fecha de nacimiento", None))
    # retranslateUi

