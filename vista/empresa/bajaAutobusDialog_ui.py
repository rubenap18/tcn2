# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bajaAutobusDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(394, 505)
        Dialog.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_estatico_titulo_2 = QLabel(Dialog)
        self.label_estatico_titulo_2.setObjectName(u"label_estatico_titulo_2")
        self.label_estatico_titulo_2.setGeometry(QRect(30, 10, 331, 51))
        self.label_estatico_numerodeautobus = QLabel(Dialog)
        self.label_estatico_numerodeautobus.setObjectName(u"label_estatico_numerodeautobus")
        self.label_estatico_numerodeautobus.setGeometry(QRect(40, 100, 121, 61))
        self.comboBox_numeroAutobus = QComboBox(Dialog)
        self.comboBox_numeroAutobus.setObjectName(u"comboBox_numeroAutobus")
        self.comboBox_numeroAutobus.setGeometry(QRect(160, 110, 161, 41))
        self.comboBox_numeroAutobus.setStyleSheet(u"QComboBox {\n"
"    border: 2px solid #1877f2;  /* Borde azul de Facebook */\n"
"    border-radius: 6px;\n"
"    padding: 8px 12px;\n"
"    font-size: 14px;\n"
"    background-color: white;\n"
"    color: #333333;\n"
"    min-width: 100px;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 2px solid #166fe5;  /* Azul m\u00e1s oscuro al hacer hover */\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid #1877f2;\n"
"    background-color: #f8f9fa;  /* Fondo ligeramente m\u00e1s claro al enfocar */\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    border-left: 1px solid #dddfe2;\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    border-left: 4px solid transparent;\n"
"    border-right: 4px solid transparent;\n"
"    border-top: 4px solid #1877f2;\n"
"    width: 0px;\n"
"    height: 0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow:"
                        "hover {\n"
"    border-top: 4px solid #166fe5;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 2px solid #1877f2;\n"
"    border-radius: 6px;\n"
"    background-color: white;\n"
"    selection-background-color: #1877f2;\n"
"    selection-color: white;\n"
"    outline: none;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    padding: 8px 12px;\n"
"    border: none;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #f0f2f5;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    background-color: #1877f2;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"    border: 2px solid #cccccc;\n"
"    background-color: #f5f5f5;\n"
"    color: #999999;\n"
"}\n"
"\n"
"QComboBox::down-arrow:disabled {\n"
"    border-top: 4px solid #cccccc;\n"
"}")
        self.label_estatico_matricula = QLabel(Dialog)
        self.label_estatico_matricula.setObjectName(u"label_estatico_matricula")
        self.label_estatico_matricula.setGeometry(QRect(30, 180, 121, 51))
        self.label_estatico_titulo_7 = QLabel(Dialog)
        self.label_estatico_titulo_7.setObjectName(u"label_estatico_titulo_7")
        self.label_estatico_titulo_7.setGeometry(QRect(50, 350, 101, 61))
        self.label_estatico_titulo_4 = QLabel(Dialog)
        self.label_estatico_titulo_4.setObjectName(u"label_estatico_titulo_4")
        self.label_estatico_titulo_4.setGeometry(QRect(50, 290, 101, 61))
        self.label_estatico_marca = QLabel(Dialog)
        self.label_estatico_marca.setObjectName(u"label_estatico_marca")
        self.label_estatico_marca.setGeometry(QRect(70, 230, 91, 61))
        self.boton_bajaAutobus = QPushButton(Dialog)
        self.boton_bajaAutobus.setObjectName(u"boton_bajaAutobus")
        self.boton_bajaAutobus.setGeometry(QRect(130, 430, 151, 51))
        self.boton_bajaAutobus.setStyleSheet(u"QPushButton {\n"
"    background-color: #1877f2;  /* Azul de Facebook */\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    padding: 8px 16px;\n"
"    border-radius: 6px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #166fe5;  /* Azul m\u00e1s oscuro al hacer hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #145dbf;  /* Azul a\u00fan m\u00e1s oscuro al presionar */\n"
"}")
        self.label_mostrarMatricula = QLabel(Dialog)
        self.label_mostrarMatricula.setObjectName(u"label_mostrarMatricula")
        self.label_mostrarMatricula.setGeometry(QRect(160, 180, 201, 51))
        self.label_mostrarMatricula.setStyleSheet(u"/* Bot\u00f3n estilo Facebook */\n"
"QPushButton {\n"
"    background-color: #1877f2;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    padding: 8px 16px;\n"
"    border-radius: 6px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #166fe5;\n"
"}\n"
"\n"
"/* LineEdit con borde azul */\n"
"QLineEdit {\n"
"    border: 2px solid #1877f2;\n"
"    border-radius: 6px;\n"
"    padding: 8px 12px;\n"
"    font-size: 14px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #1877f2;\n"
"    background-color: #f8f9fa;\n"
"}\n"
"\n"
"/* ComboBox con borde azul */\n"
"QComboBox {\n"
"    border: 2px solid #1877f2;\n"
"    border-radius: 6px;\n"
"    padding: 8px 12px;\n"
"    font-size: 14px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    border-left: 4px solid transparent;\n"
"    border-right: 4px solid transparent;\n"
"    border-top: 4px solid #1877f2;\n"
"}\n"
"\n"
"/* Label azul F"
                        "acebook */\n"
"QLabel {\n"
"    color: #1877f2;\n"
"    font-size: 15px;\n"
"    font-weight: normal;\n"
"    background-color: transparent;\n"
"}")
        self.label_mostrarMarca = QLabel(Dialog)
        self.label_mostrarMarca.setObjectName(u"label_mostrarMarca")
        self.label_mostrarMarca.setGeometry(QRect(160, 240, 201, 41))
        self.label_mostrarMarca.setStyleSheet(u"/* Bot\u00f3n estilo Facebook */\n"
"QPushButton {\n"
"    background-color: #1877f2;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    padding: 8px 16px;\n"
"    border-radius: 6px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #166fe5;\n"
"}\n"
"\n"
"/* LineEdit con borde azul */\n"
"QLineEdit {\n"
"    border: 2px solid #1877f2;\n"
"    border-radius: 6px;\n"
"    padding: 8px 12px;\n"
"    font-size: 14px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #1877f2;\n"
"    background-color: #f8f9fa;\n"
"}\n"
"\n"
"/* ComboBox con borde azul */\n"
"QComboBox {\n"
"    border: 2px solid #1877f2;\n"
"    border-radius: 6px;\n"
"    padding: 8px 12px;\n"
"    font-size: 14px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    border-left: 4px solid transparent;\n"
"    border-right: 4px solid transparent;\n"
"    border-top: 4px solid #1877f2;\n"
"}\n"
"\n"
"/* Label azul F"
                        "acebook */\n"
"QLabel {\n"
"    color: #1877f2;\n"
"    font-size: 15px;\n"
"    font-weight: normal;\n"
"    background-color: transparent;\n"
"}")
        self.label_mostrarModelo = QLabel(Dialog)
        self.label_mostrarModelo.setObjectName(u"label_mostrarModelo")
        self.label_mostrarModelo.setGeometry(QRect(160, 300, 201, 41))
        self.label_mostrarModelo.setStyleSheet(u"/* Bot\u00f3n estilo Facebook */\n"
"QPushButton {\n"
"    background-color: #1877f2;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    padding: 8px 16px;\n"
"    border-radius: 6px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #166fe5;\n"
"}\n"
"\n"
"/* LineEdit con borde azul */\n"
"QLineEdit {\n"
"    border: 2px solid #1877f2;\n"
"    border-radius: 6px;\n"
"    padding: 8px 12px;\n"
"    font-size: 14px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #1877f2;\n"
"    background-color: #f8f9fa;\n"
"}\n"
"\n"
"/* ComboBox con borde azul */\n"
"QComboBox {\n"
"    border: 2px solid #1877f2;\n"
"    border-radius: 6px;\n"
"    padding: 8px 12px;\n"
"    font-size: 14px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    border-left: 4px solid transparent;\n"
"    border-right: 4px solid transparent;\n"
"    border-top: 4px solid #1877f2;\n"
"}\n"
"\n"
"/* Label azul F"
                        "acebook */\n"
"QLabel {\n"
"    color: #1877f2;\n"
"    font-size: 15px;\n"
"    font-weight: normal;\n"
"    background-color: transparent;\n"
"}")
        self.label_mostrarTipoAutobus = QLabel(Dialog)
        self.label_mostrarTipoAutobus.setObjectName(u"label_mostrarTipoAutobus")
        self.label_mostrarTipoAutobus.setGeometry(QRect(160, 360, 201, 41))
        self.label_mostrarTipoAutobus.setStyleSheet(u"/* Bot\u00f3n estilo Facebook */\n"
"QPushButton {\n"
"    background-color: #1877f2;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    padding: 8px 16px;\n"
"    border-radius: 6px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #166fe5;\n"
"}\n"
"\n"
"/* LineEdit con borde azul */\n"
"QLineEdit {\n"
"    border: 2px solid #1877f2;\n"
"    border-radius: 6px;\n"
"    padding: 8px 12px;\n"
"    font-size: 14px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #1877f2;\n"
"    background-color: #f8f9fa;\n"
"}\n"
"\n"
"/* ComboBox con borde azul */\n"
"QComboBox {\n"
"    border: 2px solid #1877f2;\n"
"    border-radius: 6px;\n"
"    padding: 8px 12px;\n"
"    font-size: 14px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    border-left: 4px solid transparent;\n"
"    border-right: 4px solid transparent;\n"
"    border-top: 4px solid #1877f2;\n"
"}\n"
"\n"
"/* Label azul F"
                        "acebook */\n"
"QLabel {\n"
"    color: #1877f2;\n"
"    font-size: 15px;\n"
"    font-weight: normal;\n"
"    background-color: transparent;\n"
"}")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_estatico_titulo_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:700; font-style:italic;\">Dar de baja</span></p></body></html>", None))
        self.label_estatico_numerodeautobus.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">N\u00famero:</span></p></body></html>", None))
        self.label_estatico_matricula.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">Matr\u00edcula:</span></p></body></html>", None))
        self.label_estatico_titulo_7.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">Servicio:</span></p></body></html>", None))
        self.label_estatico_titulo_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">Modelo:</span></p></body></html>", None))
        self.label_estatico_marca.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">Marca:</span></p></body></html>", None))
        self.boton_bajaAutobus.setText(QCoreApplication.translate("Dialog", u"Dar de baja", None))
        self.label_mostrarMatricula.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_mostrarMarca.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_mostrarModelo.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_mostrarTipoAutobus.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><br/></p></body></html>", None))
    # retranslateUi

