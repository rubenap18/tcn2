# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pantalla_blog.ui'
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

class Ui_pantalla_blog(object):
    def setupUi(self, pantalla_blog):
        if not pantalla_blog.objectName():
            pantalla_blog.setObjectName(u"pantalla_blog")
        pantalla_blog.resize(1920, 1080)
        pantalla_blog.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.boton_regresar = QPushButton(pantalla_blog)
        self.boton_regresar.setObjectName(u"boton_regresar")
        self.boton_regresar.setGeometry(QRect(1790, 170, 71, 61))
        font = QFont()
        font.setBold(True)
        self.boton_regresar.setFont(font)
        self.boton_regresar.setStyleSheet(u"QPushButton{\n"
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
        icon.addFile(u"recursos/recursos_empresa/volver.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_regresar.setIcon(icon)
        self.boton_regresar.setIconSize(QSize(35, 35))
        self.boton_destinos = QPushButton(pantalla_blog)
        self.boton_destinos.setObjectName(u"boton_destinos")
        self.boton_destinos.setGeometry(QRect(1340, 60, 241, 91))
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
        self.label_estatico_eventos = QLabel(pantalla_blog)
        self.label_estatico_eventos.setObjectName(u"label_estatico_eventos")
        self.label_estatico_eventos.setGeometry(QRect(760, 480, 451, 101))
        font1 = QFont()
        font1.setPointSize(30)
        font1.setBold(True)
        font1.setItalic(True)
        self.label_estatico_eventos.setFont(font1)
        self.label_estatico_eventos.setAlignment(Qt.AlignCenter)
        self.label_estatico_rutasdes = QLabel(pantalla_blog)
        self.label_estatico_rutasdes.setObjectName(u"label_estatico_rutasdes")
        self.label_estatico_rutasdes.setGeometry(QRect(140, 500, 451, 101))
        self.label_estatico_rutasdes.setFont(font1)
        self.label_estatico_rutasdes.setAlignment(Qt.AlignCenter)
        self.label_estatico_bienvenido = QLabel(pantalla_blog)
        self.label_estatico_bienvenido.setObjectName(u"label_estatico_bienvenido")
        self.label_estatico_bienvenido.setGeometry(QRect(160, 80, 701, 101))
        font2 = QFont()
        font2.setPointSize(59)
        font2.setBold(True)
        font2.setItalic(True)
        self.label_estatico_bienvenido.setFont(font2)
        self.label_estatico_consejos = QLabel(pantalla_blog)
        self.label_estatico_consejos.setObjectName(u"label_estatico_consejos")
        self.label_estatico_consejos.setGeometry(QRect(1010, 830, 481, 101))
        self.label_estatico_consejos.setFont(font1)
        self.label_estatico_consejos.setAlignment(Qt.AlignCenter)
        self.boton_reservaciones = QPushButton(pantalla_blog)
        self.boton_reservaciones.setObjectName(u"boton_reservaciones")
        self.boton_reservaciones.setGeometry(QRect(1080, 70, 231, 71))
        font3 = QFont()
        font3.setBold(True)
        font3.setUnderline(True)
        self.boton_reservaciones.setFont(font3)
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
        self.label_estatico_destinos = QLabel(pantalla_blog)
        self.label_estatico_destinos.setObjectName(u"label_estatico_destinos")
        self.label_estatico_destinos.setGeometry(QRect(420, 830, 451, 101))
        self.label_estatico_destinos.setFont(font1)
        self.label_estatico_destinos.setAlignment(Qt.AlignCenter)
        self.boton_viajar = QPushButton(pantalla_blog)
        self.boton_viajar.setObjectName(u"boton_viajar")
        self.boton_viajar.setGeometry(QRect(1620, 60, 241, 91))
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
        self.label_estatico_notcias = QLabel(pantalla_blog)
        self.label_estatico_notcias.setObjectName(u"label_estatico_notcias")
        self.label_estatico_notcias.setGeometry(QRect(1350, 510, 451, 101))
        self.label_estatico_notcias.setFont(font1)
        self.label_estatico_notcias.setAlignment(Qt.AlignCenter)
        self.label_imagenes_noticias = QLabel(pantalla_blog)
        self.label_imagenes_noticias.setObjectName(u"label_imagenes_noticias")
        self.label_imagenes_noticias.setGeometry(QRect(1410, 290, 331, 191))
        self.label_imagenes_noticias.setPixmap(QPixmap(u"recursos/recursos_usuario/carretera-escenica-palya-saldamando-1024x768.jpg"))
        self.label_imagenes_noticias.setScaledContents(True)
        self.label_imagen_eventos = QLabel(pantalla_blog)
        self.label_imagen_eventos.setObjectName(u"label_imagen_eventos")
        self.label_imagen_eventos.setGeometry(QRect(830, 290, 321, 191))
        self.label_imagen_eventos.setPixmap(QPixmap(u"recursos/recursos_usuario/provino-1-1-1200x783.jpg"))
        self.label_imagen_eventos.setScaledContents(True)
        self.label_imagen_rutas = QLabel(pantalla_blog)
        self.label_imagen_rutas.setObjectName(u"label_imagen_rutas")
        self.label_imagen_rutas.setGeometry(QRect(220, 310, 281, 181))
        self.label_imagen_rutas.setPixmap(QPixmap(u"recursos/recursos_usuario/ensenada_2.jpg"))
        self.label_imagen_destinos = QLabel(pantalla_blog)
        self.label_imagen_destinos.setObjectName(u"label_imagen_destinos")
        self.label_imagen_destinos.setGeometry(QRect(480, 630, 321, 191))
        self.label_imagen_destinos.setPixmap(QPixmap(u"recursos/recursos_usuario/tecate_2.jpg"))
        self.label_imagen_destinos.setScaledContents(True)
        self.label_imagen_consejos = QLabel(pantalla_blog)
        self.label_imagen_consejos.setObjectName(u"label_imagen_consejos")
        self.label_imagen_consejos.setGeometry(QRect(1100, 630, 321, 191))
        self.label_imagen_consejos.setPixmap(QPixmap(u"recursos/recursos_usuario/viajar-en-autobus-busolinea.jpg"))
        self.label_imagen_consejos.setScaledContents(True)

        self.retranslateUi(pantalla_blog)

        QMetaObject.connectSlotsByName(pantalla_blog)
    # setupUi

    def retranslateUi(self, pantalla_blog):
        pantalla_blog.setWindowTitle(QCoreApplication.translate("pantalla_blog", u"Form", None))
        self.boton_regresar.setText("")
        self.boton_destinos.setText(QCoreApplication.translate("pantalla_blog", u"Destinos", None))
        self.label_estatico_eventos.setText(QCoreApplication.translate("pantalla_blog", u"Eventos y temporadas", None))
        self.label_estatico_rutasdes.setText(QCoreApplication.translate("pantalla_blog", u"Rutas destacadas de\n"
"la region", None))
        self.label_estatico_bienvenido.setText(QCoreApplication.translate("pantalla_blog", u"\u00a1Bievenido a TCN!", None))
        self.label_estatico_consejos.setText(QCoreApplication.translate("pantalla_blog", u"Consejos Espec\u00edficos de\n"
"Viaje", None))
        self.boton_reservaciones.setText(QCoreApplication.translate("pantalla_blog", u"Reservaciones", None))
        self.label_estatico_destinos.setText(QCoreApplication.translate("pantalla_blog", u"Destinos Tur\u00edsticos\n"
"Locales", None))
        self.boton_viajar.setText(QCoreApplication.translate("pantalla_blog", u"VIAJAR", None))
        self.label_estatico_notcias.setText(QCoreApplication.translate("pantalla_blog", u"Noticias Locales de\n"
"Transporte", None))
        self.label_imagenes_noticias.setText("")
        self.label_imagen_eventos.setText("")
        self.label_imagen_rutas.setText("")
        self.label_imagen_destinos.setText("")
        self.label_imagen_consejos.setText("")
    # retranslateUi

