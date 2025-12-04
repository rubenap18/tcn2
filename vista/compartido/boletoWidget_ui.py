# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'boletoWidget.ui'
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

class BoletoWidget(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(568, 864)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(-20, 0, 591, 871))
        self.widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_imagen_logo = QLabel(self.widget)
        self.label_imagen_logo.setObjectName(u"label_imagen_logo")
        self.label_imagen_logo.setGeometry(QRect(170, 20, 261, 71))
        font = QFont()
        font.setPointSize(25)
        self.label_imagen_logo.setFont(font)
        self.label_imagen_logo.setStyleSheet(u"")
        self.label_imagen_logo.setPixmap(QPixmap(u"../../recursos/recursos_usuario/LOGOPNG.png"))
        self.label_imagen_logo.setScaledContents(True)
        self.label_imagen_logo.setAlignment(Qt.AlignCenter)
        self.label_estatico_viaje = QLabel(self.widget)
        self.label_estatico_viaje.setObjectName(u"label_estatico_viaje")
        self.label_estatico_viaje.setGeometry(QRect(120, 120, 64, 34))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(False)
        font1.setItalic(True)
        self.label_estatico_viaje.setFont(font1)
        self.label_estatico_viaje.setStyleSheet(u"border:none\n"
"\n"
"")
        self.label_dinamico_viaje = QLabel(self.widget)
        self.label_dinamico_viaje.setObjectName(u"label_dinamico_viaje")
        self.label_dinamico_viaje.setGeometry(QRect(120, 160, 68, 34))
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setItalic(True)
        self.label_dinamico_viaje.setFont(font2)
        self.label_dinamico_viaje.setStyleSheet(u"border:none\n"
"\n"
"")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 320, 581, 121))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: rgb(246, 245, 244);")
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_dinamico_origen = QLabel(self.widget)
        self.label_dinamico_origen.setObjectName(u"label_dinamico_origen")
        self.label_dinamico_origen.setGeometry(QRect(110, 380, 91, 34))
        self.label_dinamico_origen.setFont(font2)
        self.label_dinamico_origen.setStyleSheet(u"border:none;\n"
"background-color: rgb(246, 245, 244);\n"
"color:#1061C4;\n"
"\n"
"")
        self.label_estatico_origen = QLabel(self.widget)
        self.label_estatico_origen.setObjectName(u"label_estatico_origen")
        self.label_estatico_origen.setGeometry(QRect(110, 340, 91, 34))
        self.label_estatico_origen.setFont(font1)
        self.label_estatico_origen.setStyleSheet(u"border:none;\n"
"background-color: rgb(246, 245, 244);")
        self.label_dinamico_destino = QLabel(self.widget)
        self.label_dinamico_destino.setObjectName(u"label_dinamico_destino")
        self.label_dinamico_destino.setGeometry(QRect(420, 380, 101, 34))
        self.label_dinamico_destino.setFont(font2)
        self.label_dinamico_destino.setStyleSheet(u"border:none;\n"
"background-color: rgb(246, 245, 244);\n"
"color:#1061C4;\n"
"\n"
"")
        self.label_estatico_destino = QLabel(self.widget)
        self.label_estatico_destino.setObjectName(u"label_estatico_destino")
        self.label_estatico_destino.setGeometry(QRect(420, 340, 101, 34))
        self.label_estatico_destino.setFont(font1)
        self.label_estatico_destino.setStyleSheet(u"border:none;\n"
"background-color: rgb(246, 245, 244);")
        self.label_dinamico_numboleto = QLabel(self.widget)
        self.label_dinamico_numboleto.setObjectName(u"label_dinamico_numboleto")
        self.label_dinamico_numboleto.setGeometry(QRect(400, 160, 131, 34))
        self.label_dinamico_numboleto.setFont(font2)
        self.label_dinamico_numboleto.setStyleSheet(u"border:none;\n"
"color:#1061C4;\n"
"\n"
"\n"
"\n"
"")
        self.label_dinamico_numboleto.setAlignment(Qt.AlignCenter)
        self.label_estatico_numboleto = QLabel(self.widget)
        self.label_estatico_numboleto.setObjectName(u"label_estatico_numboleto")
        self.label_estatico_numboleto.setGeometry(QRect(400, 120, 131, 34))
        self.label_estatico_numboleto.setFont(font1)
        self.label_estatico_numboleto.setStyleSheet(u"border:none\n"
"\n"
"")
        self.label_estatico_salida_2 = QLabel(self.widget)
        self.label_estatico_salida_2.setObjectName(u"label_estatico_salida_2")
        self.label_estatico_salida_2.setGeometry(QRect(70, 220, 171, 34))
        self.label_estatico_salida_2.setFont(font1)
        self.label_estatico_salida_2.setStyleSheet(u"border:none\n"
"\n"
"")
        self.label_estatico_salida_2.setAlignment(Qt.AlignCenter)
        self.label_dinamico_salida = QLabel(self.widget)
        self.label_dinamico_salida.setObjectName(u"label_dinamico_salida")
        self.label_dinamico_salida.setGeometry(QRect(70, 260, 171, 34))
        self.label_dinamico_salida.setFont(font2)
        self.label_dinamico_salida.setStyleSheet(u"border:none\n"
"\n"
"")
        self.label_dinamico_salida.setAlignment(Qt.AlignCenter)
        self.label_dinamico_llegada = QLabel(self.widget)
        self.label_dinamico_llegada.setObjectName(u"label_dinamico_llegada")
        self.label_dinamico_llegada.setGeometry(QRect(380, 260, 171, 34))
        self.label_dinamico_llegada.setFont(font2)
        self.label_dinamico_llegada.setStyleSheet(u"border:none\n"
"\n"
"")
        self.label_dinamico_llegada.setAlignment(Qt.AlignCenter)
        self.label_estatico_llegada = QLabel(self.widget)
        self.label_estatico_llegada.setObjectName(u"label_estatico_llegada")
        self.label_estatico_llegada.setGeometry(QRect(380, 220, 171, 34))
        self.label_estatico_llegada.setFont(font1)
        self.label_estatico_llegada.setStyleSheet(u"border:none\n"
"\n"
"")
        self.label_estatico_llegada.setAlignment(Qt.AlignCenter)
        self.label_dinamico_pasajero = QLabel(self.widget)
        self.label_dinamico_pasajero.setObjectName(u"label_dinamico_pasajero")
        self.label_dinamico_pasajero.setGeometry(QRect(100, 500, 421, 34))
        self.label_dinamico_pasajero.setFont(font2)
        self.label_dinamico_pasajero.setStyleSheet(u"border:none\n"
"\n"
"")
        self.label_dinamico_pasajero.setAlignment(Qt.AlignCenter)
        self.label_estatico_pasajero = QLabel(self.widget)
        self.label_estatico_pasajero.setObjectName(u"label_estatico_pasajero")
        self.label_estatico_pasajero.setGeometry(QRect(220, 460, 171, 34))
        self.label_estatico_pasajero.setFont(font1)
        self.label_estatico_pasajero.setStyleSheet(u"border:none\n"
"\n"
"")
        self.label_estatico_pasajero.setAlignment(Qt.AlignCenter)
        self.label_dinamico_numasiento = QLabel(self.widget)
        self.label_dinamico_numasiento.setObjectName(u"label_dinamico_numasiento")
        self.label_dinamico_numasiento.setGeometry(QRect(100, 590, 131, 34))
        self.label_dinamico_numasiento.setFont(font2)
        self.label_dinamico_numasiento.setStyleSheet(u"border:none;\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.label_dinamico_numasiento.setAlignment(Qt.AlignCenter)
        self.label_estatico_numasientos = QLabel(self.widget)
        self.label_estatico_numasientos.setObjectName(u"label_estatico_numasientos")
        self.label_estatico_numasientos.setGeometry(QRect(100, 550, 141, 34))
        self.label_estatico_numasientos.setFont(font1)
        self.label_estatico_numasientos.setStyleSheet(u"border:none\n"
"\n"
"")
        self.label_dinamico_tipopasajero = QLabel(self.widget)
        self.label_dinamico_tipopasajero.setObjectName(u"label_dinamico_tipopasajero")
        self.label_dinamico_tipopasajero.setGeometry(QRect(90, 690, 141, 34))
        self.label_dinamico_tipopasajero.setFont(font2)
        self.label_dinamico_tipopasajero.setStyleSheet(u"border:none;\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.label_dinamico_tipopasajero.setAlignment(Qt.AlignCenter)
        self.label_estatico_tipopasajero = QLabel(self.widget)
        self.label_estatico_tipopasajero.setObjectName(u"label_estatico_tipopasajero")
        self.label_estatico_tipopasajero.setGeometry(QRect(90, 660, 141, 34))
        self.label_estatico_tipopasajero.setFont(font1)
        self.label_estatico_tipopasajero.setStyleSheet(u"border:none\n"
"\n"
"")
        self.label_estatico_tipopasajero.setAlignment(Qt.AlignCenter)
        self.label_estatico_precioboleto = QLabel(self.widget)
        self.label_estatico_precioboleto.setObjectName(u"label_estatico_precioboleto")
        self.label_estatico_precioboleto.setGeometry(QRect(320, 550, 81, 34))
        self.label_estatico_precioboleto.setFont(font1)
        self.label_estatico_precioboleto.setStyleSheet(u"border:none\n"
"\n"
"")
        self.label_estatico_precioboleto.setAlignment(Qt.AlignCenter)
        self.label_dinamico_precioboleto = QLabel(self.widget)
        self.label_dinamico_precioboleto.setObjectName(u"label_dinamico_precioboleto")
        self.label_dinamico_precioboleto.setGeometry(QRect(410, 550, 121, 34))
        self.label_dinamico_precioboleto.setFont(font2)
        self.label_dinamico_precioboleto.setStyleSheet(u"border:none;\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.label_dinamico_precioboleto.setAlignment(Qt.AlignCenter)
        self.label_estatico_descuento = QLabel(self.widget)
        self.label_estatico_descuento.setObjectName(u"label_estatico_descuento")
        self.label_estatico_descuento.setGeometry(QRect(270, 600, 141, 34))
        self.label_estatico_descuento.setFont(font1)
        self.label_estatico_descuento.setStyleSheet(u"border:none\n"
"\n"
"")
        self.label_estatico_descuento.setAlignment(Qt.AlignCenter)
        self.label_dinamico_pordescuento = QLabel(self.widget)
        self.label_dinamico_pordescuento.setObjectName(u"label_dinamico_pordescuento")
        self.label_dinamico_pordescuento.setGeometry(QRect(410, 600, 121, 34))
        self.label_dinamico_pordescuento.setFont(font2)
        self.label_dinamico_pordescuento.setStyleSheet(u"border:none;\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.label_dinamico_pordescuento.setAlignment(Qt.AlignCenter)
        self.label_estatico_total = QLabel(self.widget)
        self.label_estatico_total.setObjectName(u"label_estatico_total")
        self.label_estatico_total.setGeometry(QRect(330, 690, 71, 34))
        self.label_estatico_total.setFont(font1)
        self.label_estatico_total.setStyleSheet(u"border:none\n"
"\n"
"")
        self.label_estatico_total.setAlignment(Qt.AlignCenter)
        self.label_dinamico_total = QLabel(self.widget)
        self.label_dinamico_total.setObjectName(u"label_dinamico_total")
        self.label_dinamico_total.setGeometry(QRect(410, 690, 121, 34))
        self.label_dinamico_total.setFont(font2)
        self.label_dinamico_total.setStyleSheet(u"border:none;\n"
"color:#1061C4;\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.label_dinamico_total.setAlignment(Qt.AlignCenter)
        self.label_dinamico_descuento = QLabel(self.widget)
        self.label_dinamico_descuento.setObjectName(u"label_dinamico_descuento")
        self.label_dinamico_descuento.setGeometry(QRect(410, 640, 121, 34))
        self.label_dinamico_descuento.setFont(font2)
        self.label_dinamico_descuento.setStyleSheet(u"border:none;\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.label_dinamico_descuento.setAlignment(Qt.AlignCenter)
        self.boton_siguiente = QPushButton(self.widget)
        self.boton_siguiente.setObjectName(u"boton_siguiente")
        self.boton_siguiente.setGeometry(QRect(350, 790, 201, 51))
        self.boton_siguiente.setStyleSheet(u"QPushButton {\n"
"    background-color: #1877F2;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    padding: 10px 20px;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"    font-family: \"Helvetica Neue\", Arial, sans-serif;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #166FE5;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #145BCC;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #8BB5F8;\n"
"    color: #E0E0E0;\n"
"}")
        self.boton_anterior = QPushButton(self.widget)
        self.boton_anterior.setObjectName(u"boton_anterior")
        self.boton_anterior.setGeometry(QRect(60, 790, 201, 51))
        self.boton_anterior.setStyleSheet(u"QPushButton {\n"
"    background-color: #FF9800;\n"
"    color: white;\n"
"    border: 2px solid #F57C00;\n"
"    border-radius: 8px;\n"
"    padding: 8px 16px;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #F57C00;\n"
"    border: 2px solid #E65100;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E65100;\n"
"    border: 2px solid #BF360C;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #FFCC80;\n"
"    color: #E0E0E0;\n"
"    border: 2px solid #FFB74D;\n"
"}")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_imagen_logo.setText("")
        self.label_estatico_viaje.setText(QCoreApplication.translate("Form", u"Viaje", None))
        self.label_dinamico_viaje.setText(QCoreApplication.translate("Form", u"Viaje", None))
        self.label_2.setText("")
        self.label_dinamico_origen.setText(QCoreApplication.translate("Form", u"Origen", None))
        self.label_estatico_origen.setText(QCoreApplication.translate("Form", u"Origen", None))
        self.label_dinamico_destino.setText(QCoreApplication.translate("Form", u"Destino", None))
        self.label_estatico_destino.setText(QCoreApplication.translate("Form", u"Destino", None))
        self.label_dinamico_numboleto.setText(QCoreApplication.translate("Form", u"3", None))
        self.label_estatico_numboleto.setText(QCoreApplication.translate("Form", u"No.Boleto", None))
        self.label_estatico_salida_2.setText(QCoreApplication.translate("Form", u"Salida", None))
        self.label_dinamico_salida.setText(QCoreApplication.translate("Form", u"Salida", None))
        self.label_dinamico_llegada.setText(QCoreApplication.translate("Form", u"Llegada", None))
        self.label_estatico_llegada.setText(QCoreApplication.translate("Form", u"Llegada", None))
        self.label_dinamico_pasajero.setText(QCoreApplication.translate("Form", u"juan manuel hernandez medina", None))
        self.label_estatico_pasajero.setText(QCoreApplication.translate("Form", u"Pasajero", None))
        self.label_dinamico_numasiento.setText(QCoreApplication.translate("Form", u"texto", None))
        self.label_estatico_numasientos.setText(QCoreApplication.translate("Form", u"No.Asiento", None))
        self.label_dinamico_tipopasajero.setText(QCoreApplication.translate("Form", u"texto", None))
        self.label_estatico_tipopasajero.setText(QCoreApplication.translate("Form", u"Tipo", None))
        self.label_estatico_precioboleto.setText(QCoreApplication.translate("Form", u"Boleto", None))
        self.label_dinamico_precioboleto.setText(QCoreApplication.translate("Form", u"texto", None))
        self.label_estatico_descuento.setText(QCoreApplication.translate("Form", u"decuento", None))
        self.label_dinamico_pordescuento.setText(QCoreApplication.translate("Form", u"texto", None))
        self.label_estatico_total.setText(QCoreApplication.translate("Form", u"Total", None))
        self.label_dinamico_total.setText(QCoreApplication.translate("Form", u"texto", None))
        self.label_dinamico_descuento.setText(QCoreApplication.translate("Form", u"texto", None))
        self.boton_siguiente.setText(QCoreApplication.translate("Form", u"Siguiente", None))
        self.boton_anterior.setText(QCoreApplication.translate("Form", u"Anterior", None))
    # retranslateUi

