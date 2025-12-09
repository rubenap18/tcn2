# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pantalla_consulta9.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QDateEdit,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_pantalla_consulta9(object):
    def setupUi(self, pantalla_consulta9):
        if not pantalla_consulta9.objectName():
            pantalla_consulta9.setObjectName(u"pantalla_consulta9")
        pantalla_consulta9.resize(1920, 1080)
        pantalla_consulta9.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.header_corridas = QWidget(pantalla_consulta9)
        self.header_corridas.setObjectName(u"header_corridas")
        self.header_corridas.setGeometry(QRect(0, 10, 1951, 111))
        self.header_corridas.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-bottom: 1px solid #E3E3E3;")
        self.boton_rutas = QPushButton(self.header_corridas)
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
        icon.addFile(u"tcn2/tcn2/recursos/recursos_empresa/entrega.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_rutas.setIcon(icon)
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
        icon1 = QIcon()
        icon1.addFile(u"tcn2/tcn2/recursos/recursos_empresa/calendario.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_corridas.setIcon(icon1)
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
        icon2 = QIcon()
        icon2.addFile(u"tcn2/tcn2/recursos/recursos_empresa/conductor.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_operadores.setIcon(icon2)
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
        icon3 = QIcon()
        icon3.addFile(u"tcn2/tcn2/recursos/recursos_empresa/autobus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_autobuses.setIcon(icon3)
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
        icon4 = QIcon()
        icon4.addFile(u"tcn2/tcn2/recursos/recursos_empresa/casa-silueta-negra-sin-puerta.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_inicio.setIcon(icon4)
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
        icon5 = QIcon()
        icon5.addFile(u"tcn2/tcn2/recursos/recursos_empresa/boleto.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_reservaciones.setIcon(icon5)
        self.boton_reservaciones.setIconSize(QSize(30, 30))
        self.label_4 = QLabel(self.header_corridas)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(18, 15, 231, 81))
        self.label_4.setStyleSheet(u"border: none")
        self.label_4.setPixmap(QPixmap(u"tcn2/tcn2/recursos/recursos_empresa/logo.png"))
        self.label_6 = QLabel(self.header_corridas)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(1790, 10, 70, 70))
        self.label_6.setPixmap(QPixmap(u"tcn2/tcn2/vista/empresa/recursos/usuario.png"))
        self.label_6.setScaledContents(True)
        self.widget_opfiltro_2 = QWidget(pantalla_consulta9)
        self.widget_opfiltro_2.setObjectName(u"widget_opfiltro_2")
        self.widget_opfiltro_2.setGeometry(QRect(0, 130, 1911, 221))
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
        self.corridas_label.setGeometry(QRect(20, 10, 1031, 91))
        font1 = QFont()
        font1.setPointSize(59)
        font1.setBold(True)
        font1.setItalic(True)
        self.corridas_label.setFont(font1)
        self.corridas_label.setStyleSheet(u"border:none\n"
"\n"
"")
        self.corridas_label.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.comboBox_filtroDestinoCorr = QComboBox(self.widget_opfiltro_2)
        self.comboBox_filtroDestinoCorr.addItem("")
        self.comboBox_filtroDestinoCorr.addItem("")
        self.comboBox_filtroDestinoCorr.addItem("")
        self.comboBox_filtroDestinoCorr.addItem("")
        self.comboBox_filtroDestinoCorr.addItem("")
        self.comboBox_filtroDestinoCorr.addItem("")
        self.comboBox_filtroDestinoCorr.addItem("")
        self.comboBox_filtroDestinoCorr.setObjectName(u"comboBox_filtroDestinoCorr")
        self.comboBox_filtroDestinoCorr.setGeometry(QRect(1750, 56, 131, 25))
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
        self.label_2.setGeometry(QRect(1571, 21, 61, 27))
        font2 = QFont()
        font2.setPointSize(15)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: black;\n"
"border: none;\n"
"")
        self.label_3 = QLabel(self.widget_opfiltro_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(1751, 21, 71, 27))
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: black;\n"
"border: none;")
        self.dateEdit = QDateEdit(self.widget_opfiltro_2)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(1570, 56, 131, 25))
        self.dateEdit.setStyleSheet(u"QDateEdit{\n"
"	border-radius:5px;\n"
"}")
        self.label_5 = QLabel(self.widget_opfiltro_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 130, 71, 27))
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: black;\n"
"border: none;")
        self.lineEdit_origen = QLineEdit(self.widget_opfiltro_2)
        self.lineEdit_origen.setObjectName(u"lineEdit_origen")
        self.lineEdit_origen.setGeometry(QRect(30, 160, 113, 22))
        self.lineEdit_origen.setStyleSheet(u"QLineEdit{\n"
"	border-radius:5px;\n"
"}")
        self.boton_inicio_2 = QPushButton(self.widget_opfiltro_2)
        self.boton_inicio_2.setObjectName(u"boton_inicio_2")
        self.boton_inicio_2.setGeometry(QRect(1790, 120, 91, 71))
        self.boton_inicio_2.setFont(font)
        self.boton_inicio_2.setStyleSheet(u"QPushButton{\n"
"	background: #FF6A36;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #E85F30;   /* Naranja m\u00e1s oscuro */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #CC532A;   /* M\u00e1s oscuro para click */\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"tcn2/tcn2/recursos/recursos_empresa/volver.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_inicio_2.setIcon(icon6)
        self.boton_inicio_2.setIconSize(QSize(30, 30))
        self.QtableWidget_corridas = QTableWidget(pantalla_consulta9)
        if (self.QtableWidget_corridas.columnCount() < 6):
            self.QtableWidget_corridas.setColumnCount(6)
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
        if (self.QtableWidget_corridas.rowCount() < 3):
            self.QtableWidget_corridas.setRowCount(3)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.QtableWidget_corridas.setVerticalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.QtableWidget_corridas.setVerticalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.QtableWidget_corridas.setVerticalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.QtableWidget_corridas.setItem(0, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.QtableWidget_corridas.setItem(0, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.QtableWidget_corridas.setItem(0, 2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.QtableWidget_corridas.setItem(0, 3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.QtableWidget_corridas.setItem(0, 4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.QtableWidget_corridas.setItem(0, 5, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.QtableWidget_corridas.setItem(1, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.QtableWidget_corridas.setItem(1, 1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.QtableWidget_corridas.setItem(1, 2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.QtableWidget_corridas.setItem(1, 3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.QtableWidget_corridas.setItem(1, 4, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.QtableWidget_corridas.setItem(1, 5, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.QtableWidget_corridas.setItem(2, 0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.QtableWidget_corridas.setItem(2, 1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.QtableWidget_corridas.setItem(2, 2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.QtableWidget_corridas.setItem(2, 3, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.QtableWidget_corridas.setItem(2, 4, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.QtableWidget_corridas.setItem(2, 5, __qtablewidgetitem26)
        self.QtableWidget_corridas.setObjectName(u"QtableWidget_corridas")
        self.QtableWidget_corridas.setGeometry(QRect(0, 360, 1641, 551))
        self.QtableWidget_corridas.setFont(font)
        self.QtableWidget_corridas.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.QtableWidget_corridas.setStyleSheet(u"QTableView {\n"
"    background: #ffffff;\n"
"    border: 2px solid #e6e8ec;\n"
"    border-radius: 8px;\n"
"    gridline-color: #f1f1f3;\n"
"    selection-background-color: #e8f0fe;\n"
"    selection-color: #1a1a1a;\n"
"    font-size: 15px;\n"
"    color: #333;\n"
"    alternate-background-color: #fafbff;\n"
"    show-grid: false;\n"
"	\n"
"}\n"
"\n"
"QTableView::item {\n"
"    padding: 8px 12px;\n"
"    border: 0px;\n"
"	text-align: center;\n"
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
"QTableView::indic"
                        "ator {\n"
"    width: 18px;\n"
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
        self.QtableWidget_corridas.horizontalHeader().setDefaultSectionSize(218)
        self.QtableWidget_corridas.horizontalHeader().setHighlightSections(False)
        self.QtableWidget_corridas.verticalHeader().setCascadingSectionResizes(True)

        self.retranslateUi(pantalla_consulta9)

        QMetaObject.connectSlotsByName(pantalla_consulta9)
    # setupUi

    def retranslateUi(self, pantalla_consulta9):
        pantalla_consulta9.setWindowTitle(QCoreApplication.translate("pantalla_consulta9", u"Form", None))
        self.boton_rutas.setText(QCoreApplication.translate("pantalla_consulta9", u"Rutas", None))
        self.boton_corridas.setText(QCoreApplication.translate("pantalla_consulta9", u"Corridas", None))
        self.boton_operadores.setText(QCoreApplication.translate("pantalla_consulta9", u"Operadores", None))
        self.boton_autobuses.setText(QCoreApplication.translate("pantalla_consulta9", u"Autobuses", None))
        self.boton_inicio.setText("")
        self.boton_reservaciones.setText(QCoreApplication.translate("pantalla_consulta9", u"Reservaciones", None))
        self.label_4.setText("")
        self.label_6.setText("")
        self.corridas_label.setText(QCoreApplication.translate("pantalla_consulta9", u"Corridas por fecha y ciudad", None))
        self.comboBox_filtroDestinoCorr.setItemText(0, QCoreApplication.translate("pantalla_consulta9", u"TODOS", None))
        self.comboBox_filtroDestinoCorr.setItemText(1, QCoreApplication.translate("pantalla_consulta9", u"Ensenada", None))
        self.comboBox_filtroDestinoCorr.setItemText(2, QCoreApplication.translate("pantalla_consulta9", u"Mexicali", None))
        self.comboBox_filtroDestinoCorr.setItemText(3, QCoreApplication.translate("pantalla_consulta9", u"San Felipe", None))
        self.comboBox_filtroDestinoCorr.setItemText(4, QCoreApplication.translate("pantalla_consulta9", u"San Quint\u00edn", None))
        self.comboBox_filtroDestinoCorr.setItemText(5, QCoreApplication.translate("pantalla_consulta9", u"Tecate", None))
        self.comboBox_filtroDestinoCorr.setItemText(6, QCoreApplication.translate("pantalla_consulta9", u"Tijuana", None))

        self.label_2.setText(QCoreApplication.translate("pantalla_consulta9", u"Fecha", None))
        self.label_3.setText(QCoreApplication.translate("pantalla_consulta9", u"Origen", None))
        self.label_5.setText(QCoreApplication.translate("pantalla_consulta9", u"Origen", None))
        self.lineEdit_origen.setText(QCoreApplication.translate("pantalla_consulta9", u"Mexicali", None))
        self.boton_inicio_2.setText("")
        ___qtablewidgetitem = self.QtableWidget_corridas.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("pantalla_consulta9", u"Salida", None));
        ___qtablewidgetitem1 = self.QtableWidget_corridas.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("pantalla_consulta9", u"Corrida", None));
        ___qtablewidgetitem2 = self.QtableWidget_corridas.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("pantalla_consulta9", u"Destino", None));
        ___qtablewidgetitem3 = self.QtableWidget_corridas.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("pantalla_consulta9", u"Autob\u00fas", None));
        ___qtablewidgetitem4 = self.QtableWidget_corridas.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("pantalla_consulta9", u"Matr\u00edcula", None));
        ___qtablewidgetitem5 = self.QtableWidget_corridas.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("pantalla_consulta9", u"Operador", None));

        __sortingEnabled = self.QtableWidget_corridas.isSortingEnabled()
        self.QtableWidget_corridas.setSortingEnabled(False)
        ___qtablewidgetitem6 = self.QtableWidget_corridas.item(0, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("pantalla_consulta9", u"2025-12-06 9:00:00", None));
        ___qtablewidgetitem7 = self.QtableWidget_corridas.item(0, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("pantalla_consulta9", u"5", None));
        ___qtablewidgetitem8 = self.QtableWidget_corridas.item(0, 2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("pantalla_consulta9", u"Tijuana", None));
        ___qtablewidgetitem9 = self.QtableWidget_corridas.item(0, 3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("pantalla_consulta9", u"502", None));
        ___qtablewidgetitem10 = self.QtableWidget_corridas.item(0, 4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("pantalla_consulta9", u"OSF87U", None));
        ___qtablewidgetitem11 = self.QtableWidget_corridas.item(0, 5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("pantalla_consulta9", u"Carlos Rodr\u00edguez Mart\u00ednez", None));
        ___qtablewidgetitem12 = self.QtableWidget_corridas.item(1, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("pantalla_consulta9", u"2025-12-06 12:00:00", None));
        ___qtablewidgetitem13 = self.QtableWidget_corridas.item(1, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("pantalla_consulta9", u"6", None));
        ___qtablewidgetitem14 = self.QtableWidget_corridas.item(1, 2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("pantalla_consulta9", u"Tijuana", None));
        ___qtablewidgetitem15 = self.QtableWidget_corridas.item(1, 3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("pantalla_consulta9", u"100", None));
        ___qtablewidgetitem16 = self.QtableWidget_corridas.item(1, 4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("pantalla_consulta9", u"TU87Y6", None));
        ___qtablewidgetitem17 = self.QtableWidget_corridas.item(1, 5)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("pantalla_consulta9", u"Mar\u00eda L\u00f3pez Garc\u00eda", None));
        ___qtablewidgetitem18 = self.QtableWidget_corridas.item(2, 0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("pantalla_consulta9", u"2025-12-07 14:00:00", None));
        ___qtablewidgetitem19 = self.QtableWidget_corridas.item(2, 1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("pantalla_consulta9", u"37", None));
        ___qtablewidgetitem20 = self.QtableWidget_corridas.item(2, 2)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("pantalla_consulta9", u"TIjuana", None));
        ___qtablewidgetitem21 = self.QtableWidget_corridas.item(2, 3)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("pantalla_consulta9", u"104", None));
        ___qtablewidgetitem22 = self.QtableWidget_corridas.item(2, 4)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("pantalla_consulta9", u"UY767Y", None));
        ___qtablewidgetitem23 = self.QtableWidget_corridas.item(2, 5)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("pantalla_consulta9", u"Miguel P\u00e9rez Gonz\u00e1lez", None));
        self.QtableWidget_corridas.setSortingEnabled(__sortingEnabled)

    # retranslateUi

