# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registrarAutobusDialog.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(429, 532)
        Dialog.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_estatico_titulo = QLabel(Dialog)
        self.label_estatico_titulo.setObjectName(u"label_estatico_titulo")
        self.label_estatico_titulo.setGeometry(QRect(50, 10, 331, 51))
        self.label_estatico_numerodeautobus = QLabel(Dialog)
        self.label_estatico_numerodeautobus.setObjectName(u"label_estatico_numerodeautobus")
        self.label_estatico_numerodeautobus.setGeometry(QRect(90, 150, 121, 61))
        self.label_estatico_marca = QLabel(Dialog)
        self.label_estatico_marca.setObjectName(u"label_estatico_marca")
        self.label_estatico_marca.setGeometry(QRect(110, 270, 91, 61))
        self.label_estatico_titulo_4 = QLabel(Dialog)
        self.label_estatico_titulo_4.setObjectName(u"label_estatico_titulo_4")
        self.label_estatico_titulo_4.setGeometry(QRect(90, 330, 101, 61))
        self.label_estatico_matricula = QLabel(Dialog)
        self.label_estatico_matricula.setObjectName(u"label_estatico_matricula")
        self.label_estatico_matricula.setGeometry(QRect(70, 210, 121, 51))
        self.label_estatico_tipoAutobus = QLabel(Dialog)
        self.label_estatico_tipoAutobus.setObjectName(u"label_estatico_tipoAutobus")
        self.label_estatico_tipoAutobus.setGeometry(QRect(10, 100, 201, 51))
        self.label_estatico_titulo_7 = QLabel(Dialog)
        self.label_estatico_titulo_7.setObjectName(u"label_estatico_titulo_7")
        self.label_estatico_titulo_7.setGeometry(QRect(60, 390, 131, 61))
        self.boton_registrarAutobus = QPushButton(Dialog)
        self.boton_registrarAutobus.setObjectName(u"boton_registrarAutobus")
        self.boton_registrarAutobus.setGeometry(QRect(140, 460, 151, 51))
        self.boton_registrarAutobus.setStyleSheet(u"QPushButton {\n"
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
        self.comboBox_tiposdeautobus = QComboBox(Dialog)
        self.comboBox_tiposdeautobus.addItem("")
        self.comboBox_tiposdeautobus.addItem("")
        self.comboBox_tiposdeautobus.addItem("")
        self.comboBox_tiposdeautobus.setObjectName(u"comboBox_tiposdeautobus")
        self.comboBox_tiposdeautobus.setGeometry(QRect(210, 100, 151, 41))
        self.comboBox_tiposdeautobus.setStyleSheet(u"QComboBox {\n"
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
        self.lineEdit_numeroAutobus = QLineEdit(Dialog)
        self.lineEdit_numeroAutobus.setObjectName(u"lineEdit_numeroAutobus")
        self.lineEdit_numeroAutobus.setGeometry(QRect(210, 160, 151, 41))
        self.lineEdit_numeroAutobus.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #1877f2;  /* Borde azul de Facebook */\n"
"    border-radius: 6px;\n"
"    padding: 8px 12px;\n"
"    font-size: 14px;\n"
"    background-color: white;\n"
"    color: #333333;\n"
"    selection-background-color: #1877f2;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #1877f2;  /* Mantener el mismo color al enfocar */\n"
"    background-color: #f8f9fa;  /* Fondo ligeramente m\u00e1s claro al enfocar */\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #166fe5;  /* Azul m\u00e1s oscuro al hacer hover */\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    border: 2px solid #cccccc;\n"
"    background-color: #f5f5f5;\n"
"    color: #999999;\n"
"}")
        self.lineEdit_matriculaAutobus = QLineEdit(Dialog)
        self.lineEdit_matriculaAutobus.setObjectName(u"lineEdit_matriculaAutobus")
        self.lineEdit_matriculaAutobus.setGeometry(QRect(210, 220, 201, 41))
        self.lineEdit_matriculaAutobus.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #1877f2;  /* Borde azul de Facebook */\n"
"    border-radius: 6px;\n"
"    padding: 8px 12px;\n"
"    font-size: 14px;\n"
"    background-color: white;\n"
"    color: #333333;\n"
"    selection-background-color: #1877f2;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #1877f2;  /* Mantener el mismo color al enfocar */\n"
"    background-color: #f8f9fa;  /* Fondo ligeramente m\u00e1s claro al enfocar */\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #166fe5;  /* Azul m\u00e1s oscuro al hacer hover */\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    border: 2px solid #cccccc;\n"
"    background-color: #f5f5f5;\n"
"    color: #999999;\n"
"}")
        self.comboBox_marcaAutobus = QComboBox(Dialog)
        self.comboBox_marcaAutobus.setObjectName(u"comboBox_marcaAutobus")
        self.comboBox_marcaAutobus.setGeometry(QRect(210, 280, 161, 41))
        self.comboBox_marcaAutobus.setStyleSheet(u"QComboBox {\n"
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
        self.comboBox_modeloAutobus = QComboBox(Dialog)
        self.comboBox_modeloAutobus.setObjectName(u"comboBox_modeloAutobus")
        self.comboBox_modeloAutobus.setGeometry(QRect(210, 340, 161, 41))
        self.comboBox_modeloAutobus.setStyleSheet(u"QComboBox {\n"
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
        self.lineEdit_claveWIFIAutobus = QLineEdit(Dialog)
        self.lineEdit_claveWIFIAutobus.setObjectName(u"lineEdit_claveWIFIAutobus")
        self.lineEdit_claveWIFIAutobus.setGeometry(QRect(210, 400, 201, 41))
        self.lineEdit_claveWIFIAutobus.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #1877f2;  /* Borde azul de Facebook */\n"
"    border-radius: 6px;\n"
"    padding: 8px 12px;\n"
"    font-size: 14px;\n"
"    background-color: white;\n"
"    color: #333333;\n"
"    selection-background-color: #1877f2;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #1877f2;  /* Mantener el mismo color al enfocar */\n"
"    background-color: #f8f9fa;  /* Fondo ligeramente m\u00e1s claro al enfocar */\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #166fe5;  /* Azul m\u00e1s oscuro al hacer hover */\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    border: 2px solid #cccccc;\n"
"    background-color: #f5f5f5;\n"
"    color: #999999;\n"
"}")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_estatico_titulo.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:700; font-style:italic;\">Registrar autob\u00fas</span></p></body></html>", None))
        self.label_estatico_numerodeautobus.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">N\u00famero:</span></p></body></html>", None))
        self.label_estatico_marca.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">Marca:</span></p></body></html>", None))
        self.label_estatico_titulo_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">Modelo:</span></p></body></html>", None))
        self.label_estatico_matricula.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">Matr\u00edcula:</span></p></body></html>", None))
        self.label_estatico_tipoAutobus.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">Tipo de servicio:</span></p></body></html>", None))
        self.label_estatico_titulo_7.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">Clave WIFI:</span></p></body></html>", None))
        self.boton_registrarAutobus.setText(QCoreApplication.translate("Dialog", u"Registrar", None))
        self.comboBox_tiposdeautobus.setItemText(0, QCoreApplication.translate("Dialog", u"TODOS", None))
        self.comboBox_tiposdeautobus.setItemText(1, QCoreApplication.translate("Dialog", u"PLUS", None))
        self.comboBox_tiposdeautobus.setItemText(2, QCoreApplication.translate("Dialog", u"PLATINO", None))

    # retranslateUi

