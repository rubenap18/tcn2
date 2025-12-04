# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pantalla_rutas.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1916, 1084)
        Form.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.header_widget = QWidget(Form)
        self.header_widget.setObjectName(u"header_widget")
        self.header_widget.setGeometry(QRect(-10, 0, 1951, 111))
        self.header_widget.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-bottom: 1px solid #E3E3E3;")
        self.boton_rutas = QPushButton(self.header_widget)
        self.boton_rutas.setObjectName(u"boton_rutas")
        self.boton_rutas.setGeometry(QRect(1140, 20, 221, 71))
        font = QFont()
        font.setBold(True)
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
        icon = QIcon()
        icon.addFile(u"recursos/recursos_empresa/entrega.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_rutas.setIcon(icon)
        self.boton_rutas.setIconSize(QSize(30, 30))
        self.boton_corridas = QPushButton(self.header_widget)
        self.boton_corridas.setObjectName(u"boton_corridas")
        self.boton_corridas.setGeometry(QRect(640, 20, 221, 71))
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
        icon1 = QIcon()
        icon1.addFile(u"recursos/recursos_empresa/calendario.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_corridas.setIcon(icon1)
        self.boton_corridas.setIconSize(QSize(30, 30))
        self.boton_operadores = QPushButton(self.header_widget)
        self.boton_operadores.setObjectName(u"boton_operadores")
        self.boton_operadores.setGeometry(QRect(1390, 20, 221, 71))
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
        icon2 = QIcon()
        icon2.addFile(u"recursos/recursos_empresa/conductor.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_operadores.setIcon(icon2)
        self.boton_operadores.setIconSize(QSize(30, 30))
        self.boton_autobuses = QPushButton(self.header_widget)
        self.boton_autobuses.setObjectName(u"boton_autobuses")
        self.boton_autobuses.setGeometry(QRect(890, 20, 221, 71))
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
        icon3 = QIcon()
        icon3.addFile(u"recursos/recursos_empresa/autobus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_autobuses.setIcon(icon3)
        self.boton_autobuses.setIconSize(QSize(30, 30))
        self.boton_inicio = QPushButton(self.header_widget)
        self.boton_inicio.setObjectName(u"boton_inicio")
        self.boton_inicio.setGeometry(QRect(270, 20, 91, 71))
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
        icon4 = QIcon()
        icon4.addFile(u"recursos/recursos_empresa/casa-silueta-negra-sin-puerta.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_inicio.setIcon(icon4)
        self.boton_inicio.setIconSize(QSize(30, 30))
        self.boton_reservaciones = QPushButton(self.header_widget)
        self.boton_reservaciones.setObjectName(u"boton_reservaciones")
        self.boton_reservaciones.setGeometry(QRect(390, 20, 221, 71))
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
        icon5 = QIcon()
        icon5.addFile(u"recursos/recursos_empresa/boleto.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_reservaciones.setIcon(icon5)
        self.boton_reservaciones.setIconSize(QSize(30, 30))
        self.label = QLabel(self.header_widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 201, 71))
        self.label.setPixmap(QPixmap(u"recursos/recursos_empresa/logo.png"))
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 120, 1920, 971))
        self.widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.widget_opbotones = QWidget(self.widget)
        self.widget_opbotones.setObjectName(u"widget_opbotones")
        self.widget_opbotones.setGeometry(QRect(20, 20, 221, 881))
        self.widget_opbotones.setStyleSheet(u"\n"
"\n"
"background-color: #1061C4;\n"
"border: 1px solid #dcdfe6;\n"
"border-radius: 15px;\n"
"gridline-color: #e0e0e0;\n"
"outline: none;\n"
"color: #606266;\n"
"\n"
"")
        self.boton_agregaruta = QPushButton(self.widget_opbotones)
        self.boton_agregaruta.setObjectName(u"boton_agregaruta")
        self.boton_agregaruta.setGeometry(QRect(10, 90, 201, 71))
        self.boton_agregaruta.setFont(font)
        self.boton_agregaruta.setStyleSheet(u"QPushButton{\n"
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
        self.boton_agregaruta.setIconSize(QSize(30, 30))
        self.boton_editaruta = QPushButton(self.widget_opbotones)
        self.boton_editaruta.setObjectName(u"boton_editaruta")
        self.boton_editaruta.setGeometry(QRect(10, 180, 201, 71))
        self.boton_editaruta.setFont(font)
        self.boton_editaruta.setStyleSheet(u"QPushButton{\n"
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
        self.boton_editaruta.setIconSize(QSize(30, 30))
        self.boton_ciudades = QPushButton(self.widget_opbotones)
        self.boton_ciudades.setObjectName(u"boton_ciudades")
        self.boton_ciudades.setGeometry(QRect(10, 10, 201, 71))
        self.boton_ciudades.setFont(font)
        self.boton_ciudades.setStyleSheet(u"QPushButton{\n"
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
        self.boton_ciudades.setIconSize(QSize(30, 30))
        self.QtableWidget_rutas = QTableWidget(self.widget)
        if (self.QtableWidget_rutas.columnCount() < 4):
            self.QtableWidget_rutas.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.QtableWidget_rutas.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.QtableWidget_rutas.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.QtableWidget_rutas.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.QtableWidget_rutas.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.QtableWidget_rutas.setObjectName(u"QtableWidget_rutas")
        self.QtableWidget_rutas.setGeometry(QRect(430, 150, 1301, 751))
        self.QtableWidget_rutas.setFont(font)
        self.QtableWidget_rutas.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.QtableWidget_rutas.setStyleSheet(u"QTableView {\n"
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
        self.QtableWidget_rutas.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.QtableWidget_rutas.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.QtableWidget_rutas.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.QtableWidget_rutas.horizontalHeader().setVisible(True)
        self.QtableWidget_rutas.horizontalHeader().setCascadingSectionResizes(False)
        self.QtableWidget_rutas.horizontalHeader().setDefaultSectionSize(325)
        self.QtableWidget_rutas.horizontalHeader().setHighlightSections(False)
        self.QtableWidget_rutas.verticalHeader().setVisible(False)
        self.widget_opfiltro = QWidget(self.widget)
        self.widget_opfiltro.setObjectName(u"widget_opfiltro")
        self.widget_opfiltro.setGeometry(QRect(270, 20, 1621, 101))
        self.widget_opfiltro.setStyleSheet(u"background-color: #ffffff;\n"
"border: 2px solid #dcdfe6;\n"
"border-radius: 15px;\n"
"gridline-color: #e0e0e0;\n"
"outline: none;\n"
"color: #606266;\n"
"border-radius: 15px;\n"
"border-bottom: 1px solid #E3E3E3;\n"
"\n"
"")
        self.label_estatico_rutas = QLabel(self.widget_opfiltro)
        self.label_estatico_rutas.setObjectName(u"label_estatico_rutas")
        self.label_estatico_rutas.setGeometry(QRect(30, 10, 231, 71))
        font1 = QFont()
        font1.setPointSize(59)
        font1.setBold(True)
        font1.setItalic(True)
        self.label_estatico_rutas.setFont(font1)
        self.label_estatico_rutas.setStyleSheet(u"border:none\n"
"\n"
"")
        self.label_estatico_forigen = QLabel(self.widget_opfiltro)
        self.label_estatico_forigen.setObjectName(u"label_estatico_forigen")
        self.label_estatico_forigen.setGeometry(QRect(1220, 10, 179, 40))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.label_estatico_forigen.setFont(font2)
        self.label_estatico_forigen.setStyleSheet(u"border:none;\n"
"\n"
"\n"
"")
        self.label_estatico_forigen.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.comboBox_forigen = QComboBox(self.widget_opfiltro)
        self.comboBox_forigen.addItem("")
        self.comboBox_forigen.addItem("")
        self.comboBox_forigen.addItem("")
        self.comboBox_forigen.addItem("")
        self.comboBox_forigen.addItem("")
        self.comboBox_forigen.addItem("")
        self.comboBox_forigen.addItem("")
        self.comboBox_forigen.setObjectName(u"comboBox_forigen")
        self.comboBox_forigen.setGeometry(QRect(1220, 50, 179, 33))
        self.comboBox_forigen.setStyleSheet(u"\n"
"QComboBox {\n"
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
"}\n"
"")
        self.label_estatico_fdestino = QLabel(self.widget_opfiltro)
        self.label_estatico_fdestino.setObjectName(u"label_estatico_fdestino")
        self.label_estatico_fdestino.setGeometry(QRect(1430, 10, 179, 40))
        self.label_estatico_fdestino.setFont(font2)
        self.label_estatico_fdestino.setStyleSheet(u"border:none;\n"
"\n"
"\n"
"")
        self.label_estatico_fdestino.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.comboBox_fdestino = QComboBox(self.widget_opfiltro)
        self.comboBox_fdestino.addItem("")
        self.comboBox_fdestino.addItem("")
        self.comboBox_fdestino.addItem("")
        self.comboBox_fdestino.addItem("")
        self.comboBox_fdestino.addItem("")
        self.comboBox_fdestino.addItem("")
        self.comboBox_fdestino.addItem("")
        self.comboBox_fdestino.setObjectName(u"comboBox_fdestino")
        self.comboBox_fdestino.setGeometry(QRect(1430, 50, 179, 33))
        self.comboBox_fdestino.setStyleSheet(u"\n"
"QComboBox {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #dcdfe6;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-size: 13px;\n"
"    color: #606266;\n"
"    min-height: 10px;\n"
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

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.boton_rutas.setText(QCoreApplication.translate("Form", u"Rutas", None))
        self.boton_corridas.setText(QCoreApplication.translate("Form", u"Corridas", None))
        self.boton_operadores.setText(QCoreApplication.translate("Form", u"Operadores", None))
        self.boton_autobuses.setText(QCoreApplication.translate("Form", u"Autobuses", None))
        self.boton_inicio.setText("")
        self.boton_reservaciones.setText(QCoreApplication.translate("Form", u"Reservaciones", None))
        self.label.setText("")
        self.boton_agregaruta.setText(QCoreApplication.translate("Form", u"A\u00f1adir", None))
        self.boton_editaruta.setText(QCoreApplication.translate("Form", u"Editar", None))
        self.boton_ciudades.setText(QCoreApplication.translate("Form", u"Ciudades", None))
        ___qtablewidgetitem = self.QtableWidget_rutas.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Codigo", None));
        ___qtablewidgetitem1 = self.QtableWidget_rutas.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Origen", None));
        ___qtablewidgetitem2 = self.QtableWidget_rutas.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Destino", None));
        ___qtablewidgetitem3 = self.QtableWidget_rutas.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Distancia", None));
        self.label_estatico_rutas.setText(QCoreApplication.translate("Form", u"Rutas", None))
        self.label_estatico_forigen.setText(QCoreApplication.translate("Form", u"Filtrar por origen", None))
        self.comboBox_forigen.setItemText(0, QCoreApplication.translate("Form", u"Todos", None))
        self.comboBox_forigen.setItemText(1, QCoreApplication.translate("Form", u"Tijuana", None))
        self.comboBox_forigen.setItemText(2, QCoreApplication.translate("Form", u"Mexicali", None))
        self.comboBox_forigen.setItemText(3, QCoreApplication.translate("Form", u"Ensenada", None))
        self.comboBox_forigen.setItemText(4, QCoreApplication.translate("Form", u"San Felipe", None))
        self.comboBox_forigen.setItemText(5, QCoreApplication.translate("Form", u"Tecate", None))
        self.comboBox_forigen.setItemText(6, QCoreApplication.translate("Form", u"San Quintin", None))

        self.label_estatico_fdestino.setText(QCoreApplication.translate("Form", u"Filtrar por destino", None))
        self.comboBox_fdestino.setItemText(0, QCoreApplication.translate("Form", u"Todos", None))
        self.comboBox_fdestino.setItemText(1, QCoreApplication.translate("Form", u"Tijuana", None))
        self.comboBox_fdestino.setItemText(2, QCoreApplication.translate("Form", u"Mexicali", None))
        self.comboBox_fdestino.setItemText(3, QCoreApplication.translate("Form", u"Ensenada", None))
        self.comboBox_fdestino.setItemText(4, QCoreApplication.translate("Form", u"San Felipe", None))
        self.comboBox_fdestino.setItemText(5, QCoreApplication.translate("Form", u"Tecate", None))
        self.comboBox_fdestino.setItemText(6, QCoreApplication.translate("Form", u"San Quintin", None))

    # retranslateUi

