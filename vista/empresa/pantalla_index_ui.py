# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pantalla_index.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_pagina_inicio(object):
    def setupUi(self, pagina_inicio):
        if not pagina_inicio.objectName():
            pagina_inicio.setObjectName(u"pagina_inicio")
        pagina_inicio.resize(1920, 1102)
        pagina_inicio.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.widget_opfiltro_2 = QWidget(pagina_inicio)
        self.widget_opfiltro_2.setObjectName(u"widget_opfiltro_2")
        self.widget_opfiltro_2.setGeometry(QRect(210, 130, 1491, 101))
        self.widget_opfiltro_2.setStyleSheet(u"background-color: #ffffff;\n"
"border: 2px solid #dcdfe6;\n"
"border-radius: 15px;\n"
"gridline-color: #e0e0e0;\n"
"outline: none;\n"
"color: #606266;\n"
"border-radius: 15px;\n"
"border-bottom: 1px solid #E3E3E3;\n"
"\n"
"")
        self.label_estatico_titulo = QLabel(self.widget_opfiltro_2)
        self.label_estatico_titulo.setObjectName(u"label_estatico_titulo")
        self.label_estatico_titulo.setGeometry(QRect(20, 10, 551, 71))
        font = QFont()
        font.setPointSize(59)
        font.setBold(True)
        font.setItalic(True)
        self.label_estatico_titulo.setFont(font)
        self.label_estatico_titulo.setStyleSheet(u"border:none")
        self.boton_comprarboleto = QPushButton(self.widget_opfiltro_2)
        self.boton_comprarboleto.setObjectName(u"boton_comprarboleto")
        self.boton_comprarboleto.setGeometry(QRect(1240, 10, 241, 81))
        font1 = QFont()
        font1.setBold(True)
        self.boton_comprarboleto.setFont(font1)
        self.boton_comprarboleto.setStyleSheet(u"QPushButton{\n"
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
        icon.addFile(u"recursos/recursos_empresa/boleto.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_comprarboleto.setIcon(icon)
        self.boton_comprarboleto.setIconSize(QSize(30, 30))
        self.label_estatico_operadores = QLabel(pagina_inicio)
        self.label_estatico_operadores.setObjectName(u"label_estatico_operadores")
        self.label_estatico_operadores.setGeometry(QRect(1195, 260, 318, 68))
        font2 = QFont()
        font2.setPointSize(41)
        font2.setBold(True)
        font2.setItalic(True)
        self.label_estatico_operadores.setFont(font2)
        self.QtableWidget_operadores = QTableWidget(pagina_inicio)
        if (self.QtableWidget_operadores.columnCount() < 2):
            self.QtableWidget_operadores.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.QtableWidget_operadores.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.QtableWidget_operadores.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.QtableWidget_operadores.setObjectName(u"QtableWidget_operadores")
        self.QtableWidget_operadores.setGeometry(QRect(1195, 340, 681, 291))
        self.QtableWidget_operadores.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.QtableWidget_operadores.setStyleSheet(u"QTableView {\n"
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
        self.QtableWidget_operadores.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.QtableWidget_operadores.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.QtableWidget_operadores.horizontalHeader().setDefaultSectionSize(338)
        self.QtableWidget_operadores.verticalHeader().setVisible(False)
        self.QtableWidget_corridasact = QTableWidget(pagina_inicio)
        if (self.QtableWidget_corridasact.columnCount() < 5):
            self.QtableWidget_corridasact.setColumnCount(5)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.QtableWidget_corridasact.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.QtableWidget_corridasact.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.QtableWidget_corridasact.setHorizontalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.QtableWidget_corridasact.setHorizontalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.QtableWidget_corridasact.setHorizontalHeaderItem(4, __qtablewidgetitem6)
        self.QtableWidget_corridasact.setObjectName(u"QtableWidget_corridasact")
        self.QtableWidget_corridasact.setGeometry(QRect(52, 340, 1111, 291))
        self.QtableWidget_corridasact.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.QtableWidget_corridasact.setStyleSheet(u"QTableView {\n"
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
        self.QtableWidget_corridasact.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.QtableWidget_corridasact.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.QtableWidget_corridasact.horizontalHeader().setDefaultSectionSize(221)
        self.QtableWidget_corridasact.verticalHeader().setVisible(False)
        self.label_estatico_corridas = QLabel(pagina_inicio)
        self.label_estatico_corridas.setObjectName(u"label_estatico_corridas")
        self.label_estatico_corridas.setGeometry(QRect(50, 260, 448, 68))
        self.label_estatico_corridas.setFont(font2)
        self.comboBox_bfecha = QComboBox(pagina_inicio)
        self.comboBox_bfecha.setObjectName(u"comboBox_bfecha")
        self.comboBox_bfecha.setGeometry(QRect(550, 280, 241, 41))
        font3 = QFont()
        self.comboBox_bfecha.setFont(font3)
        self.comboBox_bfecha.setStyleSheet(u"\n"
"QComboBox {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #dcdfe6;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-size: 18px;\n"
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
"}\n"
"")
        self.QtableWidget_pasajeros = QTableWidget(pagina_inicio)
        if (self.QtableWidget_pasajeros.columnCount() < 4):
            self.QtableWidget_pasajeros.setColumnCount(4)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.QtableWidget_pasajeros.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.QtableWidget_pasajeros.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.QtableWidget_pasajeros.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.QtableWidget_pasajeros.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        self.QtableWidget_pasajeros.setObjectName(u"QtableWidget_pasajeros")
        self.QtableWidget_pasajeros.setGeometry(QRect(50, 730, 1111, 291))
        self.QtableWidget_pasajeros.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.QtableWidget_pasajeros.setStyleSheet(u"QTableView {\n"
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
        self.QtableWidget_pasajeros.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.QtableWidget_pasajeros.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.QtableWidget_pasajeros.horizontalHeader().setDefaultSectionSize(276)
        self.QtableWidget_pasajeros.verticalHeader().setVisible(False)
        self.label_estatico_pasajeros = QLabel(pagina_inicio)
        self.label_estatico_pasajeros.setObjectName(u"label_estatico_pasajeros")
        self.label_estatico_pasajeros.setGeometry(QRect(50, 647, 269, 71))
        self.label_estatico_pasajeros.setFont(font2)
        self.boton_corridasoperadores = QPushButton(pagina_inicio)
        self.boton_corridasoperadores.setObjectName(u"boton_corridasoperadores")
        self.boton_corridasoperadores.setGeometry(QRect(1625, 260, 221, 61))
        self.boton_corridasoperadores.setFont(font1)
        self.boton_corridasoperadores.setStyleSheet(u"QPushButton{\n"
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
        icon1.addFile(u"../../recursos/recursos_empresa/autobus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_corridasoperadores.setIcon(icon1)
        self.boton_corridasoperadores.setIconSize(QSize(30, 30))
        self.label_estatico_operadores_2 = QLabel(pagina_inicio)
        self.label_estatico_operadores_2.setObjectName(u"label_estatico_operadores_2")
        self.label_estatico_operadores_2.setGeometry(QRect(1240, 650, 621, 341))
        self.label_estatico_operadores_2.setFont(font2)
        self.label_estatico_operadores_2.setPixmap(QPixmap(u"recursos/recursos_empresa/irizar i6 blanco.png"))
        self.label_estatico_operadores_2.setScaledContents(True)
        self.header_autobuses = QWidget(pagina_inicio)
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
        self.boton_rutas.setFont(font1)
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
        self.boton_corridas.setFont(font1)
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
        self.boton_operadores.setFont(font1)
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
        self.boton_autobuses.setFont(font1)
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
        self.boton_inicio.setFont(font1)
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
        self.boton_reservaciones.setFont(font1)
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
        self.boton_reservaciones.setIcon(icon)
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

        self.retranslateUi(pagina_inicio)

        QMetaObject.connectSlotsByName(pagina_inicio)
    # setupUi

    def retranslateUi(self, pagina_inicio):
        pagina_inicio.setWindowTitle(QCoreApplication.translate("pagina_inicio", u"TCN", None))
        self.label_estatico_titulo.setText(QCoreApplication.translate("pagina_inicio", u"Inicio", None))
        self.boton_comprarboleto.setText(QCoreApplication.translate("pagina_inicio", u"Comprar boleto", None))
        self.label_estatico_operadores.setText(QCoreApplication.translate("pagina_inicio", u"Operadores", None))
        ___qtablewidgetitem = self.QtableWidget_operadores.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("pagina_inicio", u"N\u00b0 Operador", None));
        ___qtablewidgetitem1 = self.QtableWidget_operadores.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("pagina_inicio", u"Nombre", None));
        ___qtablewidgetitem2 = self.QtableWidget_corridasact.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("pagina_inicio", u"N\u00b0 Corrida", None));
        ___qtablewidgetitem3 = self.QtableWidget_corridasact.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("pagina_inicio", u"Fecha y Hora Salida", None));
        ___qtablewidgetitem4 = self.QtableWidget_corridasact.horizontalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("pagina_inicio", u"Origen", None));
        ___qtablewidgetitem5 = self.QtableWidget_corridasact.horizontalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("pagina_inicio", u"Destino", None));
        ___qtablewidgetitem6 = self.QtableWidget_corridasact.horizontalHeaderItem(4)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("pagina_inicio", u"Autobus", None));
        self.label_estatico_corridas.setText(QCoreApplication.translate("pagina_inicio", u"Corridas activas", None))
        self.comboBox_bfecha.setPlaceholderText(QCoreApplication.translate("pagina_inicio", u"Buscar por fecha", None))
        ___qtablewidgetitem7 = self.QtableWidget_pasajeros.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("pagina_inicio", u"N\u00b0 boleto", None));
        ___qtablewidgetitem8 = self.QtableWidget_pasajeros.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("pagina_inicio", u"N\u00b0 Asiento", None));
        ___qtablewidgetitem9 = self.QtableWidget_pasajeros.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("pagina_inicio", u"Nombre ", None));
        ___qtablewidgetitem10 = self.QtableWidget_pasajeros.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("pagina_inicio", u"Edad", None));
        self.label_estatico_pasajeros.setText(QCoreApplication.translate("pagina_inicio", u"Pasajeros", None))
        self.boton_corridasoperadores.setText(QCoreApplication.translate("pagina_inicio", u" Corridas", None))
        self.label_estatico_operadores_2.setText("")
        self.boton_rutas.setText(QCoreApplication.translate("pagina_inicio", u"Rutas", None))
        self.boton_corridas.setText(QCoreApplication.translate("pagina_inicio", u"Corridas", None))
        self.boton_operadores.setText(QCoreApplication.translate("pagina_inicio", u"Operadores", None))
        self.boton_autobuses.setText(QCoreApplication.translate("pagina_inicio", u"Autobuses", None))
        self.boton_inicio.setText("")
        self.boton_reservaciones.setText(QCoreApplication.translate("pagina_inicio", u"Reservaciones", None))
        self.label.setText("")
    # retranslateUi

