# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pantalla_catalogodestinos.ui'
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

class Ui_pagina_catdestinos(object):
    def setupUi(self, pagina_catdestinos):
        if not pagina_catdestinos.objectName():
            pagina_catdestinos.setObjectName(u"pagina_catdestinos")
        pagina_catdestinos.resize(1920, 1080)
        pagina_catdestinos.setMinimumSize(QSize(1920, 1080))
        pagina_catdestinos.setMaximumSize(QSize(1920, 16777215))
        pagina_catdestinos.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_imagen_logo = QLabel(pagina_catdestinos)
        self.label_imagen_logo.setObjectName(u"label_imagen_logo")
        self.label_imagen_logo.setGeometry(QRect(60, 60, 441, 111))
        self.label_imagen_logo.setStyleSheet(u"border:none")
        self.label_imagen_logo.setPixmap(QPixmap(u"../recursos/recursos empresa/LOGOJPG.jpg"))
        self.label_imagen_logo.setScaledContents(True)
        self.label_imagen_logo.setWordWrap(False)
        self.boton_destinos = QPushButton(pagina_catdestinos)
        self.boton_destinos.setObjectName(u"boton_destinos")
        self.boton_destinos.setGeometry(QRect(1350, 60, 241, 91))
        font = QFont()
        font.setBold(True)
        self.boton_destinos.setFont(font)
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
        self.boton_reservaciones = QPushButton(pagina_catdestinos)
        self.boton_reservaciones.setObjectName(u"boton_reservaciones")
        self.boton_reservaciones.setGeometry(QRect(1090, 70, 231, 71))
        font1 = QFont()
        font1.setBold(True)
        font1.setUnderline(True)
        self.boton_reservaciones.setFont(font1)
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
        self.boton_viajar = QPushButton(pagina_catdestinos)
        self.boton_viajar.setObjectName(u"boton_viajar")
        self.boton_viajar.setGeometry(QRect(1630, 60, 241, 91))
        self.boton_viajar.setFont(font)
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
        self.label_imagen_mexicali = QLabel(pagina_catdestinos)
        self.label_imagen_mexicali.setObjectName(u"label_imagen_mexicali")
        self.label_imagen_mexicali.setGeometry(QRect(630, 340, 231, 121))
        self.label_imagen_mexicali.setPixmap(QPixmap(u"../recursos/recursos usuario/mexicali.png"))
        self.label_imagen_mexicali.setScaledContents(True)
        self.label_estatico_sanfelipe = QLabel(pagina_catdestinos)
        self.label_estatico_sanfelipe.setObjectName(u"label_estatico_sanfelipe")
        self.label_estatico_sanfelipe.setGeometry(QRect(1510, 360, 251, 61))
        font2 = QFont()
        font2.setPointSize(35)
        font2.setBold(True)
        font2.setItalic(True)
        self.label_estatico_sanfelipe.setFont(font2)
        self.label_estatico_sanfelipe.setStyleSheet(u"color: rgb(16, 97, 196);")
        self.label_estatico_sqdescripcion = QLabel(pagina_catdestinos)
        self.label_estatico_sqdescripcion.setObjectName(u"label_estatico_sqdescripcion")
        self.label_estatico_sqdescripcion.setGeometry(QRect(1480, 750, 311, 171))
        font3 = QFont()
        font3.setPointSize(18)
        font3.setBold(True)
        font3.setItalic(True)
        self.label_estatico_sqdescripcion.setFont(font3)
        self.label_estatico_sqdescripcion.setAlignment(Qt.AlignCenter)
        self.label_estatico_sqdescripcion.setWordWrap(True)
        self.label_imagen_tecate = QLabel(pagina_catdestinos)
        self.label_imagen_tecate.setObjectName(u"label_imagen_tecate")
        self.label_imagen_tecate.setGeometry(QRect(30, 670, 211, 121))
        self.label_imagen_tecate.setPixmap(QPixmap(u"../recursos/recursos usuario/tecate.png"))
        self.label_imagen_tecate.setScaledContents(True)
        self.label_imagen_ensenada = QLabel(pagina_catdestinos)
        self.label_imagen_ensenada.setObjectName(u"label_imagen_ensenada")
        self.label_imagen_ensenada.setGeometry(QRect(630, 670, 231, 121))
        self.label_imagen_ensenada.setPixmap(QPixmap(u"../recursos/recursos usuario/ensenada_2.jpg"))
        self.label_imagen_ensenada.setScaledContents(True)
        self.label_estatico_sanquintin = QLabel(pagina_catdestinos)
        self.label_estatico_sanquintin.setObjectName(u"label_estatico_sanquintin")
        self.label_estatico_sanquintin.setGeometry(QRect(1500, 690, 271, 61))
        self.label_estatico_sanquintin.setFont(font2)
        self.label_estatico_sanquintin.setStyleSheet(u"color: rgb(16, 97, 196);")
        self.label_estatico_mexicali = QLabel(pagina_catdestinos)
        self.label_estatico_mexicali.setObjectName(u"label_estatico_mexicali")
        self.label_estatico_mexicali.setGeometry(QRect(940, 360, 201, 61))
        self.label_estatico_mexicali.setFont(font2)
        self.label_estatico_mexicali.setStyleSheet(u"color: rgb(16, 97, 196);")
        self.label_imagen_mexicali2 = QLabel(pagina_catdestinos)
        self.label_imagen_mexicali2.setObjectName(u"label_imagen_mexicali2")
        self.label_imagen_mexicali2.setGeometry(QRect(630, 470, 231, 141))
        self.label_imagen_mexicali2.setPixmap(QPixmap(u"../recursos/recursos usuario/mexicali_2.jfif"))
        self.label_imagen_mexicali2.setScaledContents(True)
        self.label_estatico_ensdescripcion = QLabel(pagina_catdestinos)
        self.label_estatico_ensdescripcion.setObjectName(u"label_estatico_ensdescripcion")
        self.label_estatico_ensdescripcion.setGeometry(QRect(890, 740, 301, 181))
        self.label_estatico_ensdescripcion.setFont(font3)
        self.label_estatico_ensdescripcion.setAlignment(Qt.AlignCenter)
        self.label_estatico_ensdescripcion.setWordWrap(True)
        self.label_imagen_tijuana2 = QLabel(pagina_catdestinos)
        self.label_imagen_tijuana2.setObjectName(u"label_imagen_tijuana2")
        self.label_imagen_tijuana2.setGeometry(QRect(30, 470, 201, 131))
        self.label_imagen_tijuana2.setPixmap(QPixmap(u"../recursos/recursos usuario/mx_tijuana-mexico.jpg"))
        self.label_imagen_tijuana2.setScaledContents(True)
        self.label_estatico_rijdescripcion = QLabel(pagina_catdestinos)
        self.label_estatico_rijdescripcion.setObjectName(u"label_estatico_rijdescripcion")
        self.label_estatico_rijdescripcion.setGeometry(QRect(280, 440, 321, 151))
        self.label_estatico_rijdescripcion.setFont(font3)
        self.label_estatico_rijdescripcion.setAlignment(Qt.AlignCenter)
        self.label_estatico_rijdescripcion.setWordWrap(True)
        self.boton_regresas = QPushButton(pagina_catdestinos)
        self.boton_regresas.setObjectName(u"boton_regresas")
        self.boton_regresas.setGeometry(QRect(1800, 180, 71, 61))
        self.boton_regresas.setFont(font)
        self.boton_regresas.setStyleSheet(u"QPushButton{\n"
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
        icon = QIcon()
        icon.addFile(u"../recursos/recursos empresa/volver.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_regresas.setIcon(icon)
        self.boton_regresas.setIconSize(QSize(35, 35))
        self.label_estatico_titulo2 = QLabel(pagina_catdestinos)
        self.label_estatico_titulo2.setObjectName(u"label_estatico_titulo2")
        self.label_estatico_titulo2.setGeometry(QRect(820, 180, 451, 96))
        font4 = QFont()
        font4.setPointSize(59)
        font4.setBold(True)
        font4.setItalic(True)
        self.label_estatico_titulo2.setFont(font4)
        self.label_estatico_titulo2.setStyleSheet(u"color: rgb(16, 97, 196);")
        self.label_estatico_tijuana = QLabel(pagina_catdestinos)
        self.label_estatico_tijuana.setObjectName(u"label_estatico_tijuana")
        self.label_estatico_tijuana.setGeometry(QRect(350, 360, 191, 61))
        self.label_estatico_tijuana.setFont(font2)
        self.label_estatico_tijuana.setStyleSheet(u"color: rgb(16, 97, 196);")
        self.label_estatico_tecdescripion = QLabel(pagina_catdestinos)
        self.label_estatico_tecdescripion.setObjectName(u"label_estatico_tecdescripion")
        self.label_estatico_tecdescripion.setGeometry(QRect(270, 750, 321, 151))
        self.label_estatico_tecdescripion.setFont(font3)
        self.label_estatico_tecdescripion.setLayoutDirection(Qt.LeftToRight)
        self.label_estatico_tecdescripion.setAlignment(Qt.AlignCenter)
        self.label_estatico_tecdescripion.setWordWrap(True)
        self.label_imagen_tijuana = QLabel(pagina_catdestinos)
        self.label_imagen_tijuana.setObjectName(u"label_imagen_tijuana")
        self.label_imagen_tijuana.setGeometry(QRect(20, 340, 231, 121))
        self.label_imagen_tijuana.setPixmap(QPixmap(u"../recursos/recursos usuario/Tijuana.png"))
        self.label_imagen_tijuana.setScaledContents(True)
        self.label_estatico_ensenada = QLabel(pagina_catdestinos)
        self.label_estatico_ensenada.setObjectName(u"label_estatico_ensenada")
        self.label_estatico_ensenada.setGeometry(QRect(920, 690, 241, 61))
        self.label_estatico_ensenada.setFont(font2)
        self.label_estatico_ensenada.setStyleSheet(u"color: rgb(16, 97, 196);")
        self.label_imagen_sanfelipe = QLabel(pagina_catdestinos)
        self.label_imagen_sanfelipe.setObjectName(u"label_imagen_sanfelipe")
        self.label_imagen_sanfelipe.setGeometry(QRect(1220, 340, 231, 131))
        self.label_imagen_sanfelipe.setPixmap(QPixmap(u"../recursos/recursos usuario/San Felipe_2.jpg"))
        self.label_imagen_sanfelipe.setScaledContents(True)
        self.label_imagen_sanquintin_2 = QLabel(pagina_catdestinos)
        self.label_imagen_sanquintin_2.setObjectName(u"label_imagen_sanquintin_2")
        self.label_imagen_sanquintin_2.setGeometry(QRect(1220, 810, 231, 131))
        self.label_imagen_sanquintin_2.setPixmap(QPixmap(u"../recursos/recursos usuario/san quintin_2.jpg"))
        self.label_imagen_sanquintin_2.setScaledContents(True)
        self.label_imagen_sanfelipe_2 = QLabel(pagina_catdestinos)
        self.label_imagen_sanfelipe_2.setObjectName(u"label_imagen_sanfelipe_2")
        self.label_imagen_sanfelipe_2.setGeometry(QRect(1220, 480, 231, 131))
        self.label_imagen_sanfelipe_2.setPixmap(QPixmap(u"../recursos/recursos usuario/San felipe.jpg"))
        self.label_imagen_sanfelipe_2.setScaledContents(True)
        self.label_estatico_sfdescripcion = QLabel(pagina_catdestinos)
        self.label_estatico_sfdescripcion.setObjectName(u"label_estatico_sfdescripcion")
        self.label_estatico_sfdescripcion.setGeometry(QRect(1470, 430, 321, 171))
        self.label_estatico_sfdescripcion.setFont(font3)
        self.label_estatico_sfdescripcion.setAlignment(Qt.AlignCenter)
        self.label_estatico_sfdescripcion.setWordWrap(True)
        self.label_estatico_tecate = QLabel(pagina_catdestinos)
        self.label_estatico_tecate.setObjectName(u"label_estatico_tecate")
        self.label_estatico_tecate.setGeometry(QRect(350, 690, 191, 61))
        self.label_estatico_tecate.setFont(font2)
        self.label_estatico_tecate.setStyleSheet(u"color: rgb(16, 97, 196);")
        self.label_estatico_titulo1 = QLabel(pagina_catdestinos)
        self.label_estatico_titulo1.setObjectName(u"label_estatico_titulo1")
        self.label_estatico_titulo1.setGeometry(QRect(70, 180, 752, 96))
        self.label_estatico_titulo1.setFont(font4)
        self.label_imagen_sanquintin = QLabel(pagina_catdestinos)
        self.label_imagen_sanquintin.setObjectName(u"label_imagen_sanquintin")
        self.label_imagen_sanquintin.setGeometry(QRect(1220, 670, 231, 121))
        self.label_imagen_sanquintin.setPixmap(QPixmap(u"../recursos/recursos usuario/san quintin.png"))
        self.label_imagen_sanquintin.setScaledContents(True)
        self.label_imagen_tecate2 = QLabel(pagina_catdestinos)
        self.label_imagen_tecate2.setObjectName(u"label_imagen_tecate2")
        self.label_imagen_tecate2.setGeometry(QRect(30, 820, 211, 121))
        self.label_imagen_tecate2.setPixmap(QPixmap(u"../recursos/recursos usuario/tecate_2.jpg"))
        self.label_imagen_tecate2.setScaledContents(True)
        self.label_imagen_ensenada2 = QLabel(pagina_catdestinos)
        self.label_imagen_ensenada2.setObjectName(u"label_imagen_ensenada2")
        self.label_imagen_ensenada2.setGeometry(QRect(630, 800, 231, 141))
        self.label_imagen_ensenada2.setPixmap(QPixmap(u"../recursos/recursos usuario/678ff539bdbb722906d176f8_ENS_Malecon 1 Large.jpeg"))
        self.label_imagen_ensenada2.setScaledContents(True)
        self.label_estatico_mexdescripcion = QLabel(pagina_catdestinos)
        self.label_estatico_mexdescripcion.setObjectName(u"label_estatico_mexdescripcion")
        self.label_estatico_mexdescripcion.setGeometry(QRect(880, 420, 321, 171))
        self.label_estatico_mexdescripcion.setFont(font3)
        self.label_estatico_mexdescripcion.setAlignment(Qt.AlignCenter)
        self.label_estatico_mexdescripcion.setWordWrap(True)

        self.retranslateUi(pagina_catdestinos)

        QMetaObject.connectSlotsByName(pagina_catdestinos)
    # setupUi

    def retranslateUi(self, pagina_catdestinos):
        pagina_catdestinos.setWindowTitle(QCoreApplication.translate("pagina_catdestinos", u"Form", None))
        self.label_imagen_logo.setText("")
        self.boton_destinos.setText(QCoreApplication.translate("pagina_catdestinos", u"Destinos", None))
        self.boton_reservaciones.setText(QCoreApplication.translate("pagina_catdestinos", u"Reservaciones", None))
        self.boton_viajar.setText(QCoreApplication.translate("pagina_catdestinos", u"VIAJAR", None))
        self.label_imagen_mexicali.setText("")
        self.label_estatico_sanfelipe.setText(QCoreApplication.translate("pagina_catdestinos", u"San Felipe", None))
        self.label_estatico_sqdescripcion.setText(QCoreApplication.translate("pagina_catdestinos", u"Posee un gran vi\u00f1edo, donde puedes degustar los mejores vinos del pa\u00eds, adem\u00e1s de navegar entre sus humedales.", None))
        self.label_imagen_tecate.setText("")
        self.label_imagen_ensenada.setText("")
        self.label_estatico_sanquintin.setText(QCoreApplication.translate("pagina_catdestinos", u"San Quintin", None))
        self.label_estatico_mexicali.setText(QCoreApplication.translate("pagina_catdestinos", u"Mexicali", None))
        self.label_imagen_mexicali2.setText("")
        self.label_estatico_ensdescripcion.setText(QCoreApplication.translate("pagina_catdestinos", u"Conoce el puerto m\u00e1s colorido del estado, atrap\u00e1ndote con su malec\u00f3n y con la bufadora.", None))
        self.label_imagen_tijuana2.setText("")
        self.label_estatico_rijdescripcion.setText(QCoreApplication.translate("pagina_catdestinos", u"Descubre la ciudad\n"
"m\u00e1s importante de Baja California, llena de colores representativos y con una vida nocturna activa.", None))
        self.boton_regresas.setText("")
        self.label_estatico_titulo2.setText(QCoreApplication.translate("pagina_catdestinos", u"Destinos", None))
        self.label_estatico_tijuana.setText(QCoreApplication.translate("pagina_catdestinos", u"Tijuana", None))
        self.label_estatico_tecdescripion.setText(QCoreApplication.translate("pagina_catdestinos", u" El \u00fanico pueblo m\u00e1gico fronterizo, hogar del mejor pan y la mejor cerveza de toda la pen\u00ednsula", None))
        self.label_imagen_tijuana.setText("")
        self.label_estatico_ensenada.setText(QCoreApplication.translate("pagina_catdestinos", u"Ensenada", None))
        self.label_imagen_sanfelipe.setText("")
        self.label_imagen_sanquintin_2.setText("")
        self.label_imagen_sanfelipe_2.setText("")
        self.label_estatico_sfdescripcion.setText(QCoreApplication.translate("pagina_catdestinos", u"Uno de los puertos m\u00e1s tur\u00edsticos del estado, con un ambiente c\u00e1lido y tranquilo, siempre es recomendable probar el agua de sus playas.", None))
        self.label_estatico_tecate.setText(QCoreApplication.translate("pagina_catdestinos", u"Tecate", None))
        self.label_estatico_titulo1.setText(QCoreApplication.translate("pagina_catdestinos", u"Descubre nuestros", None))
        self.label_imagen_sanquintin.setText("")
        self.label_imagen_tecate2.setText("")
        self.label_imagen_ensenada2.setText("")
        self.label_estatico_mexdescripcion.setText(QCoreApplication.translate("pagina_catdestinos", u" Conoce la capital de Baja California, la ciudad que atrap\u00f3 el sol. Con un valle imponente y una tradici\u00f3n beisbolera", None))
    # retranslateUi

