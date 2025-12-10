# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pantalla_operadores.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_pantalla_operadores(object):
    def setupUi(self, pantalla_operadores):
        if not pantalla_operadores.objectName():
            pantalla_operadores.setObjectName(u"pantalla_operadores")
        pantalla_operadores.resize(1916, 1074)
        pantalla_operadores.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.widget_opbotones_6 = QWidget(pantalla_operadores)
        self.widget_opbotones_6.setObjectName(u"widget_opbotones_6")
        self.widget_opbotones_6.setGeometry(QRect(20, 140, 221, 881))
        self.widget_opbotones_6.setStyleSheet(u"\n"
"\n"
"background-color: #1061C4;\n"
"border: 1px solid #dcdfe6;\n"
"border-radius: 15px;\n"
"gridline-color: #e0e0e0;\n"
"outline: none;\n"
"color: #606266;\n"
"\n"
"")
        self.boton_editaroperadores = QPushButton(self.widget_opbotones_6)
        self.boton_editaroperadores.setObjectName(u"boton_editaroperadores")
        self.boton_editaroperadores.setGeometry(QRect(10, 90, 201, 71))
        font = QFont()
        font.setBold(True)
        self.boton_editaroperadores.setFont(font)
        self.boton_editaroperadores.setStyleSheet(u"QPushButton{\n"
"	background: #1061C4;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0D4FAB;    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0A3F8A;     \n"
"}")
        icon = QIcon()
        icon.addFile(u"recursos/recursos_empresa/editar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_editaroperadores.setIcon(icon)
        self.boton_editaroperadores.setIconSize(QSize(30, 30))
        self.boton_agregaroperadores = QPushButton(self.widget_opbotones_6)
        self.boton_agregaroperadores.setObjectName(u"boton_agregaroperadores")
        self.boton_agregaroperadores.setGeometry(QRect(10, 10, 201, 71))
        self.boton_agregaroperadores.setFont(font)
        self.boton_agregaroperadores.setStyleSheet(u"QPushButton{\n"
"	background: #1061C4;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0D4FAB;    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0A3F8A;     \n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"recursos/recursos_empresa/agregar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_agregaroperadores.setIcon(icon1)
        self.boton_agregaroperadores.setIconSize(QSize(30, 30))
        self.widget_titulo = QWidget(pantalla_operadores)
        self.widget_titulo.setObjectName(u"widget_titulo")
        self.widget_titulo.setGeometry(QRect(270, 140, 1621, 101))
        self.widget_titulo.setStyleSheet(u"background-color: #ffffff;\n"
"border: 2px solid #dcdfe6;\n"
"border-radius: 15px;\n"
"gridline-color: #e0e0e0;\n"
"outline: none;\n"
"color: #606266;\n"
"border-radius: 15px;\n"
"border-bottom: 1px solid #E3E3E3;\n"
"\n"
"")
        self.label_estatico_operadores = QLabel(self.widget_titulo)
        self.label_estatico_operadores.setObjectName(u"label_estatico_operadores")
        self.label_estatico_operadores.setGeometry(QRect(30, 10, 461, 81))
        font1 = QFont()
        font1.setPointSize(59)
        font1.setBold(True)
        font1.setItalic(True)
        self.label_estatico_operadores.setFont(font1)
        self.label_estatico_operadores.setStyleSheet(u"border:none\n"
"\n"
"")
        self.lineEdit_boperadores = QLineEdit(self.widget_titulo)
        self.lineEdit_boperadores.setObjectName(u"lineEdit_boperadores")
        self.lineEdit_boperadores.setGeometry(QRect(1260, 30, 311, 41))
        font2 = QFont()
        font2.setPointSize(20)
        self.lineEdit_boperadores.setFont(font2)
        self.QTableWidget_operadores = QTableWidget(pantalla_operadores)
        if (self.QTableWidget_operadores.columnCount() < 5):
            self.QTableWidget_operadores.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.QTableWidget_operadores.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.QTableWidget_operadores.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.QTableWidget_operadores.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.QTableWidget_operadores.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font);
        self.QTableWidget_operadores.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.QTableWidget_operadores.setObjectName(u"QTableWidget_operadores")
        self.QTableWidget_operadores.setGeometry(QRect(360, 280, 1421, 661))
        self.QTableWidget_operadores.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.QTableWidget_operadores.setStyleSheet(u"QTableView {\n"
"    background: #ffffff;\n"
"    border: 2px solid #e6e8ec;\n"
"    border-radius: 8px;\n"
"    gridline-color: #f1f1f3;\n"
"    selection-background-color: #e8f0fe;\n"
"    selection-color: #1a1a1a;\n"
"    font-size: 18px;\n"
"    color: #333;\n"
"    alternate-background-color: #fafbff;\n"
"    show-grid: false;\n"
"}\n"
"\n"
"QTableView::item {\n"
"    padding: 8px 12px;\n"
"    border: 0px;\n"
"}\n"
"\n"
"QTableView::item:hover {\n"
"    background: #f5f8ff;\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"    background: #e2edff;\n"
"    color: #1a1a1a;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background: #ffffff;\n"
"    color: #6b7280;\n"
"    padding: 10px 12px;\n"
"    border: 0;\n"
"    border-bottom: 2px solid #e6e8ec;\n"
"    font-size: 20px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QHeaderView::section:hover {\n"
"    background: #f7f9fc;\n"
"}\n"
"\n"
"QHeaderView {\n"
"    background: #ffffff;\n"
"    border: 0;\n"
"}\n"
"\n"
"QTableView::indicator {\n"
"    width: 18px;\n"
""
                        "    height: 18px;\n"
"}\n"
"\n"
"QHeaderView::section:first {\n"
"    border-top-left-radius: 15px;\n"
"}\n"
"\n"
"QHeaderView::section:last {\n"
"    border-top-right-radius: 15px;\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical {\n"
"    background: transparent;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #cfd3da;\n"
"    min-height: 25px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #b5bac4;\n"
"}\n"
"\n"
"QScrollBar::add-line,\n"
"QScrollBar::sub-line {\n"
"    background: none;\n"
"    height: 0px;\n"
"}\n"
"")
        self.QTableWidget_operadores.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.QTableWidget_operadores.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.QTableWidget_operadores.horizontalHeader().setDefaultSectionSize(284)
        self.QTableWidget_operadores.verticalHeader().setVisible(False)
        self.QTableWidget_operadores.verticalHeader().setHighlightSections(False)
        self.header_autobuses = QWidget(pantalla_operadores)
        self.header_autobuses.setObjectName(u"header_autobuses")
        self.header_autobuses.setGeometry(QRect(0, 0, 1921, 111))
        self.header_autobuses.setStyleSheet(u"QWidget {\n"
"    background: transparent;\n"
"    border: none;\n"
"    border-radius: 0px;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"}")
        self.boton_rutas = QPushButton(self.header_autobuses)
        self.boton_rutas.setObjectName(u"boton_rutas")
        self.boton_rutas.setGeometry(QRect(1190, 20, 221, 71))
        self.boton_rutas.setFont(font)
        self.boton_rutas.setStyleSheet(u"QPushButton{\n"
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
        icon2 = QIcon()
        icon2.addFile(u"recursos/recursos_empresa/entrega.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_rutas.setIcon(icon2)
        self.boton_rutas.setIconSize(QSize(30, 30))
        self.boton_corridas = QPushButton(self.header_autobuses)
        self.boton_corridas.setObjectName(u"boton_corridas")
        self.boton_corridas.setGeometry(QRect(690, 20, 221, 71))
        self.boton_corridas.setFont(font)
        self.boton_corridas.setStyleSheet(u"QPushButton{\n"
"	background: #1061C4;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0D4FAB;    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0A3F8A;     \n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"recursos/recursos_empresa/calendario.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_corridas.setIcon(icon3)
        self.boton_corridas.setIconSize(QSize(30, 30))
        self.boton_operadores = QPushButton(self.header_autobuses)
        self.boton_operadores.setObjectName(u"boton_operadores")
        self.boton_operadores.setGeometry(QRect(1440, 20, 221, 71))
        self.boton_operadores.setFont(font)
        self.boton_operadores.setStyleSheet(u"QPushButton{\n"
"	background: #1061C4;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0D4FAB;    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0A3F8A;     \n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"recursos/recursos_empresa/conductor.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_operadores.setIcon(icon4)
        self.boton_operadores.setIconSize(QSize(30, 30))
        self.boton_autobuses = QPushButton(self.header_autobuses)
        self.boton_autobuses.setObjectName(u"boton_autobuses")
        self.boton_autobuses.setGeometry(QRect(940, 20, 221, 71))
        self.boton_autobuses.setFont(font)
        self.boton_autobuses.setStyleSheet(u"QPushButton{\n"
"	background: #1061C4;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0D4FAB;    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0A3F8A;     \n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"recursos/recursos_empresa/autobus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_autobuses.setIcon(icon5)
        self.boton_autobuses.setIconSize(QSize(30, 30))
        self.boton_inicio = QPushButton(self.header_autobuses)
        self.boton_inicio.setObjectName(u"boton_inicio")
        self.boton_inicio.setGeometry(QRect(320, 20, 91, 71))
        self.boton_inicio.setFont(font)
        self.boton_inicio.setStyleSheet(u"QPushButton{\n"
"	background: #1061C4;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0D4FAB;    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0A3F8A;     \n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"recursos/recursos_empresa/casa-silueta-negra-sin-puerta.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_inicio.setIcon(icon6)
        self.boton_inicio.setIconSize(QSize(30, 30))
        self.boton_reservaciones = QPushButton(self.header_autobuses)
        self.boton_reservaciones.setObjectName(u"boton_reservaciones")
        self.boton_reservaciones.setGeometry(QRect(440, 20, 221, 71))
        self.boton_reservaciones.setFont(font)
        self.boton_reservaciones.setStyleSheet(u"QPushButton{\n"
"	background: #1061C4;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0D4FAB;    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0A3F8A;     \n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"recursos/recursos_empresa/boleto.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_reservaciones.setIcon(icon7)
        self.boton_reservaciones.setIconSize(QSize(30, 30))
        self.label = QLabel(self.header_autobuses)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 211, 81))
        self.label.setStyleSheet(u"QLabel {\n"
"    background: transparent;\n"
"    border: none;\n"
"    border-radius: 0px;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"}")
        self.label.setPixmap(QPixmap(u"recursos/recursos_empresa/logo.png"))
        self.label.setScaledContents(True)

        self.retranslateUi(pantalla_operadores)

        QMetaObject.connectSlotsByName(pantalla_operadores)
    # setupUi

    def retranslateUi(self, pantalla_operadores):
        pantalla_operadores.setWindowTitle(QCoreApplication.translate("pantalla_operadores", u"Form", None))
        self.boton_editaroperadores.setText(QCoreApplication.translate("pantalla_operadores", u" Editar", None))
        self.boton_agregaroperadores.setText(QCoreApplication.translate("pantalla_operadores", u" A\u00f1adir", None))
        self.label_estatico_operadores.setText(QCoreApplication.translate("pantalla_operadores", u"<html><head/><body><p><span style=\" font-size:48pt;\">Operadores</span></p></body></html>", None))
        self.lineEdit_boperadores.setPlaceholderText(QCoreApplication.translate("pantalla_operadores", u"Buscar operador..", None))
        ___qtablewidgetitem = self.QTableWidget_operadores.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("pantalla_operadores", u"Num", None));
        ___qtablewidgetitem1 = self.QTableWidget_operadores.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("pantalla_operadores", u"Nombre", None));
        ___qtablewidgetitem2 = self.QTableWidget_operadores.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("pantalla_operadores", u"Fecha de nacimiento", None));
        ___qtablewidgetitem3 = self.QTableWidget_operadores.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("pantalla_operadores", u"Tel\u00e9fono", None));
        ___qtablewidgetitem4 = self.QTableWidget_operadores.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("pantalla_operadores", u"Fecha de contrato", None));
        self.boton_rutas.setText(QCoreApplication.translate("pantalla_operadores", u"Rutas", None))
        self.boton_corridas.setText(QCoreApplication.translate("pantalla_operadores", u"Corridas", None))
        self.boton_operadores.setText(QCoreApplication.translate("pantalla_operadores", u"Operadores", None))
        self.boton_autobuses.setText(QCoreApplication.translate("pantalla_operadores", u"Autobuses", None))
        self.boton_inicio.setText("")
        self.boton_reservaciones.setText(QCoreApplication.translate("pantalla_operadores", u"Reservaciones", None))
        self.label.setText("")
    # retranslateUi

