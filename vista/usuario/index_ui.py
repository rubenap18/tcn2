# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'index.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_pagina_inicio(object):
    def setupUi(self, pagina_inicio):
        if not pagina_inicio.objectName():
            pagina_inicio.setObjectName(u"pagina_inicio")
        pagina_inicio.resize(1920, 1080)
        pagina_inicio.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.boton_reservaciones = QPushButton(pagina_inicio)
        self.boton_reservaciones.setObjectName(u"boton_reservaciones")
        self.boton_reservaciones.setGeometry(QRect(1070, 70, 231, 71))
        font = QFont()
        font.setBold(True)
        font.setUnderline(True)
        self.boton_reservaciones.setFont(font)
        self.boton_reservaciones.setStyleSheet(u"QPushButton{\n"
"	background: rgb(255, 255, 255);\n"
"	color:black;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size:25px;\n"
"	text-decoration: underline;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(222, 221, 218);    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(192, 191, 188);     \n"
"}")
        self.boton_reservaciones.setIconSize(QSize(30, 30))
        self.label_estatico_logo = QLabel(pagina_inicio)
        self.label_estatico_logo.setObjectName(u"label_estatico_logo")
        self.label_estatico_logo.setGeometry(QRect(70, 70, 441, 131))
        self.label_estatico_logo.setStyleSheet(u"border:none")
        self.label_estatico_logo.setPixmap(QPixmap(u"../recursos/recursos usuario/LOGOJPG.jpg"))
        self.label_estatico_logo.setScaledContents(True)
        self.label_estatico_logo.setWordWrap(False)
        self.boton_destinos = QPushButton(pagina_inicio)
        self.boton_destinos.setObjectName(u"boton_destinos")
        self.boton_destinos.setGeometry(QRect(1330, 60, 241, 91))
        font1 = QFont()
        font1.setBold(True)
        self.boton_destinos.setFont(font1)
        self.boton_destinos.setStyleSheet(u"QPushButton{\n"
"	background: #1061C4;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size:25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0D4FAB;    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0A3F8A;     \n"
"}")
        self.boton_destinos.setIconSize(QSize(30, 30))
        self.boton_viajar = QPushButton(pagina_inicio)
        self.boton_viajar.setObjectName(u"boton_viajar")
        self.boton_viajar.setGeometry(QRect(1610, 60, 241, 91))
        self.boton_viajar.setFont(font1)
        self.boton_viajar.setStyleSheet(u"QPushButton{\n"
"	background: #FF6A36;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #E85F30;   /* Naranja m\u00e1s oscuro */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #CC532A;   /* M\u00e1s oscuro para click */\n"
"}")
        self.boton_viajar.setIconSize(QSize(30, 30))
        self.boton_nosotros = QPushButton(pagina_inicio)
        self.boton_nosotros.setObjectName(u"boton_nosotros")
        self.boton_nosotros.setGeometry(QRect(1380, 890, 161, 61))
        self.boton_nosotros.setFont(font1)
        self.boton_nosotros.setStyleSheet(u"QPushButton{\n"
"	background: rgb(255, 255, 255);\n"
"	color:black;\n"
"	border: 2px solid #1061C4;\n"
"	color: #1061C4;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size:27px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(222, 221, 218);    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(192, 191, 188);     \n"
"}")
        self.boton_nosotros.setIconSize(QSize(30, 30))
        self.label_estatico_numdestinos = QLabel(pagina_inicio)
        self.label_estatico_numdestinos.setObjectName(u"label_estatico_numdestinos")
        self.label_estatico_numdestinos.setGeometry(QRect(180, 840, 41, 61))
        font2 = QFont()
        font2.setPointSize(46)
        font2.setBold(True)
        font2.setItalic(True)
        self.label_estatico_numdestinos.setFont(font2)
        self.label_estatico_numdestinos.setStyleSheet(u"color: rgb(255, 106, 54);\n"
"border:none;\n"
"")
        self.label_estatico_247 = QLabel(pagina_inicio)
        self.label_estatico_247.setObjectName(u"label_estatico_247")
        self.label_estatico_247.setGeometry(QRect(430, 840, 151, 61))
        self.label_estatico_247.setFont(font2)
        self.label_estatico_247.setStyleSheet(u"border:none;\n"
"color: rgb(255, 106, 54);")
        self.boton_contactanos = QPushButton(pagina_inicio)
        self.boton_contactanos.setObjectName(u"boton_contactanos")
        self.boton_contactanos.setGeometry(QRect(1580, 890, 191, 61))
        font3 = QFont()
        font3.setBold(True)
        font3.setUnderline(False)
        self.boton_contactanos.setFont(font3)
        self.boton_contactanos.setStyleSheet(u"QPushButton{\n"
"	background: rgb(255, 255, 255);\n"
"	color:black;\n"
"	border: 2px solid rgb(255, 106, 54);\n"
"	color: rgb(255, 106, 54);\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size:27px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(222, 221, 218);    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(192, 191, 188);     \n"
"}")
        self.boton_contactanos.setIconSize(QSize(30, 30))
        self.label_estatico_descripcion = QLabel(pagina_inicio)
        self.label_estatico_descripcion.setObjectName(u"label_estatico_descripcion")
        self.label_estatico_descripcion.setGeometry(QRect(110, 490, 621, 111))
        font4 = QFont()
        font4.setPointSize(16)
        font4.setBold(True)
        font4.setItalic(True)
        self.label_estatico_descripcion.setFont(font4)
        self.label_estatico_disponibilidad = QLabel(pagina_inicio)
        self.label_estatico_disponibilidad.setObjectName(u"label_estatico_disponibilidad")
        self.label_estatico_disponibilidad.setGeometry(QRect(370, 910, 271, 51))
        font5 = QFont()
        font5.setPointSize(27)
        font5.setBold(True)
        font5.setItalic(True)
        self.label_estatico_disponibilidad.setFont(font5)
        self.label_estatico_viajatitulo = QLabel(pagina_inicio)
        self.label_estatico_viajatitulo.setObjectName(u"label_estatico_viajatitulo")
        self.label_estatico_viajatitulo.setGeometry(QRect(100, 260, 581, 111))
        font6 = QFont()
        font6.setPointSize(59)
        font6.setBold(True)
        font6.setItalic(True)
        self.label_estatico_viajatitulo.setFont(font6)
        self.label_estatico_nuestroservicios = QPushButton(pagina_inicio)
        self.label_estatico_nuestroservicios.setObjectName(u"label_estatico_nuestroservicios")
        self.label_estatico_nuestroservicios.setGeometry(QRect(100, 600, 351, 71))
        self.label_estatico_nuestroservicios.setFont(font)
        self.label_estatico_nuestroservicios.setStyleSheet(u"QPushButton{\n"
"	background: rgb(255, 255, 255);\n"
"	color:#1061C4;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size:25px;\n"
"	text-decoration: underline;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(222, 221, 218);    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(192, 191, 188);     \n"
"}")
        self.label_estatico_nuestroservicios.setIconSize(QSize(30, 30))
        self.label_estatico_pordescuento = QLabel(pagina_inicio)
        self.label_estatico_pordescuento.setObjectName(u"label_estatico_pordescuento")
        self.label_estatico_pordescuento.setGeometry(QRect(810, 840, 141, 61))
        self.label_estatico_pordescuento.setFont(font2)
        self.label_estatico_pordescuento.setStyleSheet(u"color: rgb(255, 106, 54);")
        self.boton_blog = QPushButton(pagina_inicio)
        self.boton_blog.setObjectName(u"boton_blog")
        self.boton_blog.setGeometry(QRect(1140, 890, 201, 61))
        self.boton_blog.setFont(font1)
        self.boton_blog.setStyleSheet(u"QPushButton{\n"
"	background: rgb(255, 255, 255);\n"
"	color:black;\n"
"	border: 2px solid black;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size:27px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(222, 221, 218);    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(192, 191, 188);     \n"
"}")
        self.boton_blog.setIconSize(QSize(30, 30))
        self.label_estatico_ndestinos = QLabel(pagina_inicio)
        self.label_estatico_ndestinos.setObjectName(u"label_estatico_ndestinos")
        self.label_estatico_ndestinos.setGeometry(QRect(120, 910, 161, 51))
        self.label_estatico_ndestinos.setFont(font5)
        self.label_estatico_pordescripcion = QLabel(pagina_inicio)
        self.label_estatico_pordescripcion.setObjectName(u"label_estatico_pordescripcion")
        self.label_estatico_pordescripcion.setGeometry(QRect(730, 910, 291, 61))
        font7 = QFont()
        font7.setPointSize(19)
        font7.setBold(True)
        font7.setItalic(True)
        font7.setKerning(True)
        self.label_estatico_pordescripcion.setFont(font7)
        self.label_estatico_pordescripcion.setAlignment(Qt.AlignCenter)
        self.label_imagen_camion = QLabel(pagina_inicio)
        self.label_imagen_camion.setObjectName(u"label_imagen_camion")
        self.label_imagen_camion.setGeometry(QRect(920, 230, 941, 481))
        self.label_imagen_camion.setPixmap(QPixmap(u"../recursos/recursos usuario/volvo 9800 blanco.png"))
        self.label_imagen_camion.setScaledContents(True)
        self.label_imagen_camion.setWordWrap(True)
        self.label_imagen_camion.setIndent(2)
        self.label_estatico_bajatitulo = QLabel(pagina_inicio)
        self.label_estatico_bajatitulo.setObjectName(u"label_estatico_bajatitulo")
        self.label_estatico_bajatitulo.setGeometry(QRect(100, 360, 621, 111))
        font8 = QFont()
        font8.setPointSize(60)
        font8.setBold(True)
        font8.setItalic(True)
        self.label_estatico_bajatitulo.setFont(font8)
        self.label_estatico_bajatitulo.setStyleSheet(u"color: rgb(255, 106, 54);\n"
"background-color: rgb(255, 255, 255);")

        self.retranslateUi(pagina_inicio)

        QMetaObject.connectSlotsByName(pagina_inicio)
    # setupUi

    def retranslateUi(self, pagina_inicio):
        pagina_inicio.setWindowTitle(QCoreApplication.translate("pagina_inicio", u"Form", None))
        self.boton_reservaciones.setText(QCoreApplication.translate("pagina_inicio", u"Reservaciones", None))
        self.label_estatico_logo.setText("")
        self.boton_destinos.setText(QCoreApplication.translate("pagina_inicio", u"Destinos", None))
        self.boton_viajar.setText(QCoreApplication.translate("pagina_inicio", u"VIAJAR", None))
        self.boton_nosotros.setText(QCoreApplication.translate("pagina_inicio", u"Nosotros", None))
        self.label_estatico_numdestinos.setText(QCoreApplication.translate("pagina_inicio", u"6 ", None))
        self.label_estatico_247.setText(QCoreApplication.translate("pagina_inicio", u"24/7", None))
        self.boton_contactanos.setText(QCoreApplication.translate("pagina_inicio", u"Contactanos", None))
        self.label_estatico_descripcion.setText(QCoreApplication.translate("pagina_inicio", u"Descubre Baja California a tu estilo. Con TCN, elige entre \n"
"nuestras dos categorias de autobus y vive un viaje donde \n"
"la comodidad y tecnologia transforman cada proyecto en \n"
"una experiencia \u00fanica", None))
        self.label_estatico_disponibilidad.setText(QCoreApplication.translate("pagina_inicio", u"Disponibilidad", None))
        self.label_estatico_viajatitulo.setText(QCoreApplication.translate("pagina_inicio", u"Viaja por toda ", None))
        self.label_estatico_nuestroservicios.setText(QCoreApplication.translate("pagina_inicio", u"Conoce nuestros servicios", None))
        self.label_estatico_pordescuento.setText(QCoreApplication.translate("pagina_inicio", u"50%", None))
        self.boton_blog.setText(QCoreApplication.translate("pagina_inicio", u"Nuestro blog", None))
        self.label_estatico_ndestinos.setText(QCoreApplication.translate("pagina_inicio", u"Destinos", None))
        self.label_estatico_pordescripcion.setText(QCoreApplication.translate("pagina_inicio", u"Descuentos para ni\u00f1os \n"
"y adultos mayores", None))
        self.label_imagen_camion.setText("")
        self.label_estatico_bajatitulo.setText(QCoreApplication.translate("pagina_inicio", u"Baja California", None))
    # retranslateUi

