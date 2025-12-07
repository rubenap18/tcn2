# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pantalla_contactanos.ui'
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

class Ui_pagina_contactanos(object):
    def setupUi(self, pagina_contactanos):
        if not pagina_contactanos.objectName():
            pagina_contactanos.setObjectName(u"pagina_contactanos")
        pagina_contactanos.resize(1920, 1080)
        pagina_contactanos.setMinimumSize(QSize(1920, 1080))
        pagina_contactanos.setMaximumSize(QSize(1920, 1080))
        pagina_contactanos.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.logo_label = QLabel(pagina_contactanos)
        self.logo_label.setObjectName(u"logo_label")
        self.logo_label.setGeometry(QRect(60, 70, 441, 131))
        self.logo_label.setStyleSheet(u"border:none")
        self.logo_label.setPixmap(QPixmap(u"recursos_recursos usuario/LOGOJPG.jpg"))
        self.logo_label.setScaledContents(True)
        self.logo_label.setWordWrap(False)
        self.destinos_pushButton = QPushButton(pagina_contactanos)
        self.destinos_pushButton.setObjectName(u"destinos_pushButton")
        self.destinos_pushButton.setGeometry(QRect(1340, 60, 241, 91))
        font = QFont()
        font.setBold(True)
        self.destinos_pushButton.setFont(font)
        self.destinos_pushButton.setStyleSheet(u"QPushButton{\n"
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
        self.destinos_pushButton.setIconSize(QSize(30, 30))
        self.reservaciones_pushButton = QPushButton(pagina_contactanos)
        self.reservaciones_pushButton.setObjectName(u"reservaciones_pushButton")
        self.reservaciones_pushButton.setGeometry(QRect(1080, 70, 231, 71))
        font1 = QFont()
        font1.setBold(True)
        font1.setUnderline(True)
        self.reservaciones_pushButton.setFont(font1)
        self.reservaciones_pushButton.setStyleSheet(u"QPushButton{\n"
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
        self.reservaciones_pushButton.setIconSize(QSize(30, 30))
        self.viajar_pushButton = QPushButton(pagina_contactanos)
        self.viajar_pushButton.setObjectName(u"viajar_pushButton")
        self.viajar_pushButton.setGeometry(QRect(1620, 60, 241, 91))
        self.viajar_pushButton.setFont(font)
        self.viajar_pushButton.setStyleSheet(u"QPushButton{\n"
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
        self.viajar_pushButton.setIconSize(QSize(30, 30))
        self.destinos_label_2 = QLabel(pagina_contactanos)
        self.destinos_label_2.setObjectName(u"destinos_label_2")
        self.destinos_label_2.setGeometry(QRect(80, 210, 581, 71))
        font2 = QFont()
        font2.setPointSize(59)
        font2.setBold(True)
        font2.setItalic(True)
        self.destinos_label_2.setFont(font2)
        self.label_17 = QLabel(pagina_contactanos)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(100, 470, 71, 71))
        self.label_17.setPixmap(QPixmap(u"recursos_recursos usuario/facebook.png"))
        self.label_17.setScaledContents(True)
        self.label_17.setWordWrap(False)
        self.label_18 = QLabel(pagina_contactanos)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(100, 580, 71, 71))
        self.label_18.setPixmap(QPixmap(u"recursos_recursos usuario/gmail.png"))
        self.label_18.setScaledContents(True)
        self.label_16 = QLabel(pagina_contactanos)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(100, 365, 71, 71))
        self.label_16.setPixmap(QPixmap(u"recursos_recursos usuario/instagram.png"))
        self.label_16.setScaledContents(True)
        self.contactanos_instagram = QLabel(pagina_contactanos)
        self.contactanos_instagram.setObjectName(u"contactanos_instagram")
        self.contactanos_instagram.setGeometry(QRect(210, 350, 271, 101))
        self.contactanos_instagram.setFont(font2)
        self.contactanos_facebook = QLabel(pagina_contactanos)
        self.contactanos_facebook.setObjectName(u"contactanos_facebook")
        self.contactanos_facebook.setGeometry(QRect(210, 460, 271, 101))
        self.contactanos_facebook.setFont(font2)
        self.label_15 = QLabel(pagina_contactanos)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(1080, 330, 711, 451))
        self.label_15.setPixmap(QPixmap(u"recursos_recursos usuario/irizar i6 naranja.png"))
        self.contactanos_instagram_5 = QLabel(pagina_contactanos)
        self.contactanos_instagram_5.setObjectName(u"contactanos_instagram_5")
        self.contactanos_instagram_5.setGeometry(QRect(480, 700, 451, 81))
        self.contactanos_instagram_5.setFont(font2)
        self.contactanos_instagram_2 = QLabel(pagina_contactanos)
        self.contactanos_instagram_2.setObjectName(u"contactanos_instagram_2")
        self.contactanos_instagram_2.setGeometry(QRect(470, 350, 461, 101))
        self.contactanos_instagram_2.setFont(font2)
        self.contactanos_instagram_3 = QLabel(pagina_contactanos)
        self.contactanos_instagram_3.setObjectName(u"contactanos_instagram_3")
        self.contactanos_instagram_3.setGeometry(QRect(460, 470, 441, 81))
        self.contactanos_instagram_3.setFont(font2)
        self.contactanos_whatsapp = QLabel(pagina_contactanos)
        self.contactanos_whatsapp.setObjectName(u"contactanos_whatsapp")
        self.contactanos_whatsapp.setGeometry(QRect(210, 690, 271, 101))
        self.contactanos_whatsapp.setFont(font2)
        self.contactanos_correo = QLabel(pagina_contactanos)
        self.contactanos_correo.setObjectName(u"contactanos_correo")
        self.contactanos_correo.setGeometry(QRect(210, 570, 191, 101))
        self.contactanos_correo.setFont(font2)
        self.label_19 = QLabel(pagina_contactanos)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(100, 710, 71, 71))
        self.label_19.setPixmap(QPixmap(u"recursos/recursos_usuario/whatsapp.png"))
        self.label_19.setScaledContents(True)
        self.salir_pushButton_5 = QPushButton(pagina_contactanos)
        self.salir_pushButton_5.setObjectName(u"salir_pushButton_5")
        self.salir_pushButton_5.setGeometry(QRect(1790, 170, 71, 61))
        self.salir_pushButton_5.setFont(font)
        self.salir_pushButton_5.setStyleSheet(u"QPushButton{\n"
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
        icon.addFile(u"recursos/recursos empresa/volver.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.salir_pushButton_5.setIcon(icon)
        self.salir_pushButton_5.setIconSize(QSize(35, 35))
        self.contactanos_instagram_4 = QLabel(pagina_contactanos)
        self.contactanos_instagram_4.setObjectName(u"contactanos_instagram_4")
        self.contactanos_instagram_4.setGeometry(QRect(410, 580, 501, 81))
        self.contactanos_instagram_4.setFont(font2)

        self.retranslateUi(pagina_contactanos)

        QMetaObject.connectSlotsByName(pagina_contactanos)
    # setupUi

    def retranslateUi(self, pagina_contactanos):
        pagina_contactanos.setWindowTitle(QCoreApplication.translate("pagina_contactanos", u"Form", None))
        self.logo_label.setText("")
        self.destinos_pushButton.setText(QCoreApplication.translate("pagina_contactanos", u"Destinos", None))
        self.reservaciones_pushButton.setText(QCoreApplication.translate("pagina_contactanos", u"Reservaciones", None))
        self.viajar_pushButton.setText(QCoreApplication.translate("pagina_contactanos", u"VIAJAR", None))
        self.destinos_label_2.setText(QCoreApplication.translate("pagina_contactanos", u"contactanos", None))
        self.label_17.setText("")
        self.label_18.setText("")
        self.label_16.setText("")
        self.contactanos_instagram.setText(QCoreApplication.translate("pagina_contactanos", u"<html><head/><body><p><span style=\" font-size:36pt; font-style:normal;\">Instagram:</span></p></body></html>", None))
        self.contactanos_facebook.setText(QCoreApplication.translate("pagina_contactanos", u"<html><head/><body><p><span style=\" font-size:36pt; font-style:normal;\">Facebook:</span></p></body></html>", None))
        self.label_15.setText("")
        self.contactanos_instagram_5.setText(QCoreApplication.translate("pagina_contactanos", u"<html><head/><body><p><span style=\" font-size:36pt; font-weight:400; font-style:normal;\">+52 663 380 8400</span></p></body></html>", None))
        self.contactanos_instagram_2.setText(QCoreApplication.translate("pagina_contactanos", u"<html><head/><body><p><span style=\" font-size:36pt; font-weight:400; font-style:normal;\">@tcn_bajacalifornia</span></p></body></html>", None))
        self.contactanos_instagram_3.setText(QCoreApplication.translate("pagina_contactanos", u"<html><head/><body><p><span style=\" font-size:36pt; font-weight:400; font-style:normal;\">TCN Baja California</span></p></body></html>", None))
        self.contactanos_whatsapp.setText(QCoreApplication.translate("pagina_contactanos", u"<html><head/><body><p><span style=\" font-size:36pt; font-style:normal;\">Whatsapp:</span></p></body></html>", None))
        self.contactanos_correo.setText(QCoreApplication.translate("pagina_contactanos", u"<html><head/><body><p><span style=\" font-size:36pt; font-style:normal;\">Correo:</span></p></body></html>", None))
        self.label_19.setText("")
        self.salir_pushButton_5.setText("")
        self.contactanos_instagram_4.setText(QCoreApplication.translate("pagina_contactanos", u"<html><head/><body><p><span style=\" font-size:36pt; font-weight:400; font-style:normal;\">informacion@tcn.com</span></p></body></html>", None))
    # retranslateUi

