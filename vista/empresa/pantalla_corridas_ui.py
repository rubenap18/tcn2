# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pantalla_corridas.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1920, 1080)
        Form.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.QtableWidget_corridas = QTableWidget(Form)
        if (self.QtableWidget_corridas.columnCount() < 10):
            self.QtableWidget_corridas.setColumnCount(10)
        font = QFont()
        font.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.QtableWidget_corridas.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.QtableWidget_corridas.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.QtableWidget_corridas.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.QtableWidget_corridas.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font);
        self.QtableWidget_corridas.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font);
        self.QtableWidget_corridas.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.QtableWidget_corridas.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font);
        self.QtableWidget_corridas.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font);
        self.QtableWidget_corridas.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font);
        self.QtableWidget_corridas.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.QtableWidget_corridas.setObjectName(u"QtableWidget_corridas")
        self.QtableWidget_corridas.setGeometry(QRect(240, 250, 1641, 751))
        self.QtableWidget_corridas.setFont(font)
        self.QtableWidget_corridas.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.QtableWidget_corridas.setStyleSheet(u"QTableView {\n"
"    background: #ffffff;\n"
"    border: 2px solid #e6e8ec;\n"
"    border-radius: 8px;\n"
"    gridline-color: #f1f1f3;\n"
"    selection-background-color: #e8f0fe;\n"
"    selection-color: #1a1a1a;\n"
"    font-size: 14px;\n"
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
"    font-size: 17px;\n"
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
        self.QtableWidget_corridas.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.QtableWidget_corridas.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.QtableWidget_corridas.horizontalHeader().setVisible(True)
        self.QtableWidget_corridas.horizontalHeader().setCascadingSectionResizes(True)
        self.QtableWidget_corridas.horizontalHeader().setDefaultSectionSize(164)
        self.QtableWidget_corridas.horizontalHeader().setHighlightSections(False)
        self.QtableWidget_corridas.verticalHeader().setCascadingSectionResizes(True)
        self.widget_corrBotones = QWidget(Form)
        self.widget_corrBotones.setObjectName(u"widget_corrBotones")
        self.widget_corrBotones.setGeometry(QRect(0, 130, 221, 871))
        self.widget_corrBotones.setStyleSheet(u"\n"
"\n"
"background-color: #1061C4;\n"
"border: 1px solid #dcdfe6;\n"
"border-radius: 15px;\n"
"gridline-color: #e0e0e0;\n"
"outline: none;\n"
"color: #606266;\n"
"\n"
"")
        self.boton_anadirCorr = QPushButton(self.widget_corrBotones)
        self.boton_anadirCorr.setObjectName(u"boton_anadirCorr")
        self.boton_anadirCorr.setGeometry(QRect(10, 40, 201, 71))
        self.boton_anadirCorr.setFont(font)
        self.boton_anadirCorr.setStyleSheet(u"QPushButton{\n"
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
        icon.addFile(u"../recursos/recursos empresa/a\u00f1adir.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_anadirCorr.setIcon(icon)
        self.boton_anadirCorr.setIconSize(QSize(30, 30))
        self.boton_actualizarCorr = QPushButton(self.widget_corrBotones)
        self.boton_actualizarCorr.setObjectName(u"boton_actualizarCorr")
        self.boton_actualizarCorr.setGeometry(QRect(10, 130, 201, 71))
        self.boton_actualizarCorr.setFont(font)
        self.boton_actualizarCorr.setStyleSheet(u"QPushButton{\n"
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
        icon1.addFile(u"../recursos/recursos empresa/editar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_actualizarCorr.setIcon(icon1)
        self.boton_actualizarCorr.setIconSize(QSize(30, 30))
        self.boton_estadoCorr = QPushButton(self.widget_corrBotones)
        self.boton_estadoCorr.setObjectName(u"boton_estadoCorr")
        self.boton_estadoCorr.setGeometry(QRect(10, 220, 201, 71))
        self.boton_estadoCorr.setFont(font)
        self.boton_estadoCorr.setStyleSheet(u"QPushButton{\n"
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
        icon2.addFile(u"../recursos/recursos empresa/borrar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_estadoCorr.setIcon(icon2)
        self.boton_estadoCorr.setIconSize(QSize(30, 30))
        self.widget_opfiltro_2 = QWidget(Form)
        self.widget_opfiltro_2.setObjectName(u"widget_opfiltro_2")
        self.widget_opfiltro_2.setGeometry(QRect(240, 130, 1641, 101))
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
        self.corridas_label = QLabel(self.widget_opfiltro_2)
        self.corridas_label.setObjectName(u"corridas_label")
        self.corridas_label.setGeometry(QRect(20, 10, 551, 71))
        font1 = QFont()
        font1.setPointSize(59)
        font1.setBold(True)
        font1.setItalic(True)
        self.corridas_label.setFont(font1)
        self.corridas_label.setStyleSheet(u"border:none\n"
"\n"
"")
        self.label = QLabel(self.widget_opfiltro_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(1061, 21, 58, 27))
        font2 = QFont()
        font2.setPointSize(15)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color: black;\n"
"border:none;")
        self.lineEdit_buscarNumCorr = QLineEdit(self.widget_opfiltro_2)
        self.lineEdit_buscarNumCorr.setObjectName(u"lineEdit_buscarNumCorr")
        self.lineEdit_buscarNumCorr.setGeometry(QRect(1061, 56, 141, 25))
        font3 = QFont()
        font3.setPointSize(12)
        self.lineEdit_buscarNumCorr.setFont(font3)
        self.lineEdit_buscarNumCorr.setStyleSheet(u"border-radius: 5px;")
        self.comboBox_filtroDestinoCorr = QComboBox(self.widget_opfiltro_2)
        self.comboBox_filtroDestinoCorr.addItem("")
        self.comboBox_filtroDestinoCorr.addItem("")
        self.comboBox_filtroDestinoCorr.addItem("")
        self.comboBox_filtroDestinoCorr.addItem("")
        self.comboBox_filtroDestinoCorr.addItem("")
        self.comboBox_filtroDestinoCorr.addItem("")
        self.comboBox_filtroDestinoCorr.addItem("")
        self.comboBox_filtroDestinoCorr.setObjectName(u"comboBox_filtroDestinoCorr")
        self.comboBox_filtroDestinoCorr.setGeometry(QRect(1420, 56, 131, 25))
        self.comboBox_filtroDestinoCorr.setStyleSheet(u"QComboBox {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #dcdfe6;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-size: 12px;\n"
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
"}")
        self.label_2 = QLabel(self.widget_opfiltro_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(1241, 21, 61, 27))
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: black;\n"
"border: none;\n"
"")
        self.label_3 = QLabel(self.widget_opfiltro_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(1421, 21, 71, 27))
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: black;\n"
"border: none;")
        self.comboBox_filtroOrigenCorr = QComboBox(self.widget_opfiltro_2)
        self.comboBox_filtroOrigenCorr.addItem("")
        self.comboBox_filtroOrigenCorr.addItem("")
        self.comboBox_filtroOrigenCorr.addItem("")
        self.comboBox_filtroOrigenCorr.addItem("")
        self.comboBox_filtroOrigenCorr.addItem("")
        self.comboBox_filtroOrigenCorr.addItem("")
        self.comboBox_filtroOrigenCorr.addItem("")
        self.comboBox_filtroOrigenCorr.setObjectName(u"comboBox_filtroOrigenCorr")
        self.comboBox_filtroOrigenCorr.setGeometry(QRect(1240, 56, 131, 25))
        self.comboBox_filtroOrigenCorr.setStyleSheet(u"QComboBox {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #dcdfe6;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-size: 12px;\n"
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
"}")
        self.header_corridas = QWidget(Form)
        self.header_corridas.setObjectName(u"header_corridas")
        self.header_corridas.setGeometry(QRect(0, 10, 1951, 111))
        self.header_corridas.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-bottom: 1px solid #E3E3E3;")
        self.boton_rutas = QPushButton(self.header_corridas)
        self.boton_rutas.setObjectName(u"boton_rutas")
        self.boton_rutas.setGeometry(QRect(1140, 20, 221, 71))
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
        icon3 = QIcon()
        icon3.addFile(u"../recursos/recursos empresa/entrega.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_rutas.setIcon(icon3)
        self.boton_rutas.setIconSize(QSize(30, 30))
        self.boton_corridas = QPushButton(self.header_corridas)
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
        icon4 = QIcon()
        icon4.addFile(u"../recursos/recursos empresa/calendario.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_corridas.setIcon(icon4)
        self.boton_corridas.setIconSize(QSize(30, 30))
        self.boton_operadores = QPushButton(self.header_corridas)
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
        icon5 = QIcon()
        icon5.addFile(u"../recursos/recursos empresa/conductor.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_operadores.setIcon(icon5)
        self.boton_operadores.setIconSize(QSize(30, 30))
        self.boton_autobuses = QPushButton(self.header_corridas)
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
        icon6 = QIcon()
        icon6.addFile(u"../recursos/recursos empresa/autobus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_autobuses.setIcon(icon6)
        self.boton_autobuses.setIconSize(QSize(30, 30))
        self.boton_inicio = QPushButton(self.header_corridas)
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
        icon7 = QIcon()
        icon7.addFile(u"../recursos/recursos empresa/casa-silueta-negra-sin-puerta.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_inicio.setIcon(icon7)
        self.boton_inicio.setIconSize(QSize(30, 30))
        self.boton_reservaciones = QPushButton(self.header_corridas)
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
        icon8 = QIcon()
        icon8.addFile(u"../recursos/recursos empresa/boleto.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_reservaciones.setIcon(icon8)
        self.boton_reservaciones.setIconSize(QSize(30, 30))
        self.boton_salir = QPushButton(self.header_corridas)
        self.boton_salir.setObjectName(u"boton_salir")
        self.boton_salir.setGeometry(QRect(1640, 20, 91, 71))
        self.boton_salir.setFont(font)
        self.boton_salir.setStyleSheet(u"QPushButton{\n"
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
        icon9 = QIcon()
        icon9.addFile(u"../recursos/recursos empresa/cerrar-sesion.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_salir.setIcon(icon9)
        self.boton_salir.setIconSize(QSize(30, 30))
        self.label_4 = QLabel(self.header_corridas)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(18, 15, 231, 81))
        self.label_4.setStyleSheet(u"border: none")
        self.label_4.setPixmap(QPixmap(u"../recursos/recursos empresa/logo.png"))
        self.label_6 = QLabel(self.header_corridas)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(1790, 10, 70, 70))
        self.label_6.setPixmap(QPixmap(u"../recursos/recursos empresa/usuario.png"))
        self.label_6.setScaledContents(True)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        ___qtablewidgetitem = self.QtableWidget_corridas.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Num", None));
        ___qtablewidgetitem1 = self.QtableWidget_corridas.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Origen", None));
        ___qtablewidgetitem2 = self.QtableWidget_corridas.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Destino", None));
        ___qtablewidgetitem3 = self.QtableWidget_corridas.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Distancia", None));
        ___qtablewidgetitem4 = self.QtableWidget_corridas.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Fecha y hora", None));
        ___qtablewidgetitem5 = self.QtableWidget_corridas.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Autobus", None));
        ___qtablewidgetitem6 = self.QtableWidget_corridas.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Operador", None));
        ___qtablewidgetitem7 = self.QtableWidget_corridas.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"Matricula ", None));
        ___qtablewidgetitem8 = self.QtableWidget_corridas.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"Asientos disp.", None));
        ___qtablewidgetitem9 = self.QtableWidget_corridas.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"Pasajeros", None));
        self.boton_anadirCorr.setText(QCoreApplication.translate("Form", u"A\u00f1adir", None))
        self.boton_actualizarCorr.setText(QCoreApplication.translate("Form", u"Actualizar", None))
        self.boton_estadoCorr.setText(QCoreApplication.translate("Form", u"Estado", None))
        self.corridas_label.setText(QCoreApplication.translate("Form", u"Corridas", None))
        self.label.setText(QCoreApplication.translate("Form", u"Buscar", None))
        self.lineEdit_buscarNumCorr.setPlaceholderText(QCoreApplication.translate("Form", u"N\u00famero de corrida", None))
        self.comboBox_filtroDestinoCorr.setItemText(0, QCoreApplication.translate("Form", u"TODOS", None))
        self.comboBox_filtroDestinoCorr.setItemText(1, QCoreApplication.translate("Form", u"Ensenada", None))
        self.comboBox_filtroDestinoCorr.setItemText(2, QCoreApplication.translate("Form", u"Mexicali", None))
        self.comboBox_filtroDestinoCorr.setItemText(3, QCoreApplication.translate("Form", u"San Felipe", None))
        self.comboBox_filtroDestinoCorr.setItemText(4, QCoreApplication.translate("Form", u"San Quint\u00edn", None))
        self.comboBox_filtroDestinoCorr.setItemText(5, QCoreApplication.translate("Form", u"Tecate", None))
        self.comboBox_filtroDestinoCorr.setItemText(6, QCoreApplication.translate("Form", u"Tijuana", None))

        self.label_2.setText(QCoreApplication.translate("Form", u"Origen", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Destino", None))
        self.comboBox_filtroOrigenCorr.setItemText(0, QCoreApplication.translate("Form", u"TODOS", None))
        self.comboBox_filtroOrigenCorr.setItemText(1, QCoreApplication.translate("Form", u"Ensenada", None))
        self.comboBox_filtroOrigenCorr.setItemText(2, QCoreApplication.translate("Form", u"Mexicali", None))
        self.comboBox_filtroOrigenCorr.setItemText(3, QCoreApplication.translate("Form", u"San Felipe", None))
        self.comboBox_filtroOrigenCorr.setItemText(4, QCoreApplication.translate("Form", u"San Quint\u00edn", None))
        self.comboBox_filtroOrigenCorr.setItemText(5, QCoreApplication.translate("Form", u"Tecate", None))
        self.comboBox_filtroOrigenCorr.setItemText(6, QCoreApplication.translate("Form", u"Tijuana", None))

        self.boton_rutas.setText(QCoreApplication.translate("Form", u"Rutas", None))
        self.boton_corridas.setText(QCoreApplication.translate("Form", u"Corridas", None))
        self.boton_operadores.setText(QCoreApplication.translate("Form", u"Operadores", None))
        self.boton_autobuses.setText(QCoreApplication.translate("Form", u"Autobuses", None))
        self.boton_inicio.setText("")
        self.boton_reservaciones.setText(QCoreApplication.translate("Form", u"Reservaciones", None))
        self.boton_salir.setText("")
        self.label_4.setText("")
        self.label_6.setText("")
    # retranslateUi

