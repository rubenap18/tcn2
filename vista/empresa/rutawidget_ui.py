# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rutawidget.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_pagina_rutas(object):
    def setupUi(self, pagina_rutas):
        if not pagina_rutas.objectName():
            pagina_rutas.setObjectName(u"pagina_rutas")
        pagina_rutas.resize(270, 350)
        pagina_rutas.setMinimumSize(QSize(270, 350))
        pagina_rutas.setMaximumSize(QSize(270, 350))
        pagina_rutas.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.layoutWidget = QWidget(pagina_rutas)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 70, 211, 60))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_estatico_origen = QLabel(self.layoutWidget)
        self.label_estatico_origen.setObjectName(u"label_estatico_origen")
        font = QFont()
        font.setPointSize(12)
        self.label_estatico_origen.setFont(font)

        self.verticalLayout.addWidget(self.label_estatico_origen)

        self.ComboBox_origen = QComboBox(self.layoutWidget)
        self.ComboBox_origen.setObjectName(u"ComboBox_origen")
        self.ComboBox_origen.setStyleSheet(u"QComboBox {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #dcdfe6;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-size: 13px;\n"
"    color: #606266;\n"
"    min-height: 18px;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border-color: #c0c4cc;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border-color: #409eff;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"    width: 25px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    border-left: 4px solid transparent;\n"
"    border-right: 4px solid transparent;\n"
"    border-top: 4px solid #909399;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #dcdfe6;\n"
"    border-radius: 6px;\n"
"    background-color: white;\n"
"    outline: none;\n"
"    selection-background-color: #409eff;\n"
"    selection-color: white;\n"
"    /* ELIMINA CUALQUIER cursor: ...; DE AQU\u00cd */\n"
"}")

        self.verticalLayout.addWidget(self.ComboBox_origen)

        self.layoutWidget_2 = QWidget(pagina_rutas)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(30, 140, 211, 60))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_estatico_destino = QLabel(self.layoutWidget_2)
        self.label_estatico_destino.setObjectName(u"label_estatico_destino")
        self.label_estatico_destino.setFont(font)

        self.verticalLayout_2.addWidget(self.label_estatico_destino)

        self.ComboBox_destino = QComboBox(self.layoutWidget_2)
        self.ComboBox_destino.setObjectName(u"ComboBox_destino")
        self.ComboBox_destino.setStyleSheet(u"QComboBox {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #dcdfe6;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-size: 13px;\n"
"    color: #606266;\n"
"    min-height: 18px;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border-color: #c0c4cc;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border-color: #409eff;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"    width: 25px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    border-left: 4px solid transparent;\n"
"    border-right: 4px solid transparent;\n"
"    border-top: 4px solid #909399;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #dcdfe6;\n"
"    border-radius: 6px;\n"
"    background-color: white;\n"
"    outline: none;\n"
"    selection-background-color: #409eff;\n"
"    selection-color: white;\n"
"    /* ELIMINA CUALQUIER cursor: ...; DE AQU\u00cd */\n"
"}")

        self.verticalLayout_2.addWidget(self.ComboBox_destino)

        self.boton_agregar = QPushButton(pagina_rutas)
        self.boton_agregar.setObjectName(u"boton_agregar")
        self.boton_agregar.setGeometry(QRect(110, 300, 141, 24))
        font1 = QFont()
        font1.setBold(True)
        self.boton_agregar.setFont(font1)
        self.boton_agregar.setStyleSheet(u"QPushButton{\n"
"	background: #1061C4;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"}")
        self.boton_cancelar = QPushButton(pagina_rutas)
        self.boton_cancelar.setObjectName(u"boton_cancelar")
        self.boton_cancelar.setGeometry(QRect(20, 300, 81, 24))
        self.boton_cancelar.setFont(font1)
        self.boton_cancelar.setStyleSheet(u"QPushButton{\n"
"	background: #FF6A36;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"}")
        self.layoutWidget_3 = QWidget(pagina_rutas)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(30, 210, 211, 66))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_estatica_distancia = QLabel(self.layoutWidget_3)
        self.label_estatica_distancia.setObjectName(u"label_estatica_distancia")
        self.label_estatica_distancia.setFont(font)

        self.verticalLayout_3.addWidget(self.label_estatica_distancia)

        self.txt_distancia = QLineEdit(self.layoutWidget_3)
        self.txt_distancia.setObjectName(u"txt_distancia")
        self.txt_distancia.setStyleSheet(u"QLineEdit {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #dcdfe6;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-size: 13px;\n"
"    color: #606266;\n"
"    min-height: 18px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border-color: #c0c4cc;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: #409eff;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #f5f7fa;\n"
"    color: #c0c4cc;\n"
"    border-color: #e4e7ed;\n"
"}\n"
"\n"
"QLineEdit:read-only {\n"
"    background-color: #f5f7fa;\n"
"    color: #909399;\n"
"}")

        self.verticalLayout_3.addWidget(self.txt_distancia)

        self.label_estatico_titulo = QLabel(pagina_rutas)
        self.label_estatico_titulo.setObjectName(u"label_estatico_titulo")
        self.label_estatico_titulo.setGeometry(QRect(10, 20, 251, 31))
        font2 = QFont()
        font2.setPointSize(21)
        font2.setBold(True)
        font2.setItalic(True)
        self.label_estatico_titulo.setFont(font2)

        self.retranslateUi(pagina_rutas)

        QMetaObject.connectSlotsByName(pagina_rutas)
    # setupUi

    def retranslateUi(self, pagina_rutas):
        pagina_rutas.setWindowTitle(QCoreApplication.translate("pagina_rutas", u"Form", None))
        self.label_estatico_origen.setText(QCoreApplication.translate("pagina_rutas", u"Origen", None))
        self.label_estatico_destino.setText(QCoreApplication.translate("pagina_rutas", u"Destino", None))
        self.boton_agregar.setText(QCoreApplication.translate("pagina_rutas", u"A\u00f1adir Ruta", None))
        self.boton_cancelar.setText(QCoreApplication.translate("pagina_rutas", u"Cancelar", None))
        self.label_estatica_distancia.setText(QCoreApplication.translate("pagina_rutas", u"Distancia", None))
        self.txt_distancia.setInputMask(QCoreApplication.translate("pagina_rutas", u"00000", None))
        self.label_estatico_titulo.setText(QCoreApplication.translate("pagina_rutas", u"A\u00f1adir nueva ruta", None))
    # retranslateUi

