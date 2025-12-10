# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pantalla_consulta6.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QDateEdit, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_pantalla_consulta6(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1920, 1080)
        Form.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.QtableWidget_corridas = QTableWidget(Form)
        if (self.QtableWidget_corridas.columnCount() < 7):
            self.QtableWidget_corridas.setColumnCount(7)
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
        __qtablewidgetitem6.setFont(font);
        self.QtableWidget_corridas.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.QtableWidget_corridas.setObjectName(u"QtableWidget_corridas")
        self.QtableWidget_corridas.setGeometry(QRect(180, 360, 1561, 551))
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
        self.widget_opfiltro_2 = QWidget(Form)
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
        self.label_2 = QLabel(self.widget_opfiltro_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(1751, 21, 61, 27))
        font2 = QFont()
        font2.setPointSize(15)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: black;\n"
"border: none;\n"
"")
        self.dateEdit = QDateEdit(self.widget_opfiltro_2)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(1750, 56, 131, 25))
        self.dateEdit.setStyleSheet(u"QDateEdit{\n"
"	border-radius:5px;\n"
"}")
        self.label_fecha = QLabel(self.widget_opfiltro_2)
        self.label_fecha.setObjectName(u"label_fecha")
        self.label_fecha.setGeometry(QRect(30, 160, 150, 40))
        self.label_fecha.setStyleSheet(u"QLabel{\n"
"	border-radius:5px;\n"
"    font-size: 20px;\n"
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
        icon = QIcon()
        icon.addFile(u"../../recursos/recursos_empresa/volver.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_inicio_2.setIcon(icon)
        self.boton_inicio_2.setIconSize(QSize(30, 30))
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
        icon1 = QIcon()
        icon1.addFile(u"../../recursos/recursos_empresa/entrega.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_rutas.setIcon(icon1)
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
        icon2 = QIcon()
        icon2.addFile(u"../../recursos/recursos_empresa/calendario.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_corridas.setIcon(icon2)
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
        icon3 = QIcon()
        icon3.addFile(u"../../recursos/recursos_empresa/conductor.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_operadores.setIcon(icon3)
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
        icon4 = QIcon()
        icon4.addFile(u"../../recursos/recursos_empresa/autobus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_autobuses.setIcon(icon4)
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
        icon5 = QIcon()
        icon5.addFile(u"../../recursos/recursos_empresa/casa-silueta-negra-sin-puerta.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_inicio.setIcon(icon5)
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
        icon6 = QIcon()
        icon6.addFile(u"../../recursos/recursos_empresa/boleto.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_reservaciones.setIcon(icon6)
        self.boton_reservaciones.setIconSize(QSize(30, 30))
        self.label_4 = QLabel(self.header_corridas)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(18, 15, 231, 81))
        self.label_4.setStyleSheet(u"border: none")
        self.label_4.setPixmap(QPixmap(u"../../recursos/recursos_empresa/logo.png"))
        self.label_6 = QLabel(self.header_corridas)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(1790, 10, 70, 70))
        self.label_6.setPixmap(QPixmap(u"recursos/usuario.png"))
        self.label_6.setScaledContents(True)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("pantalla_consulta6", u"Form", None))
        ___qtablewidgetitem = self.QtableWidget_corridas.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("pantalla_consulta6", u"Corrida", None));
        ___qtablewidgetitem1 = self.QtableWidget_corridas.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("pantalla_consulta6", u"Salida", None));
        ___qtablewidgetitem2 = self.QtableWidget_corridas.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("pantalla_consulta6", u"Origen", None));
        ___qtablewidgetitem3 = self.QtableWidget_corridas.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("pantalla_consulta6", u"Destino", None));
        ___qtablewidgetitem4 = self.QtableWidget_corridas.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("pantalla_consulta6", u"Autob\u00fas", None));
        ___qtablewidgetitem5 = self.QtableWidget_corridas.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("pantalla_consulta6", u"Boletos Vendidos", None));
        ___qtablewidgetitem6 = self.QtableWidget_corridas.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("pantalla_consulta6", u"Boletos disponibles", None));
        self.corridas_label.setText(QCoreApplication.translate("pantalla_consulta6", u"Boletos vendidos en un d\u00eda", None))
        self.label_2.setText(QCoreApplication.translate("pantalla_consulta6", u"Fecha", None))
        self.boton_inicio_2.setText("")
        self.boton_rutas.setText(QCoreApplication.translate("pantalla_consulta6", u"Rutas", None))
        self.boton_corridas.setText(QCoreApplication.translate("pantalla_consulta6", u"Corridas", None))
        self.boton_operadores.setText(QCoreApplication.translate("pantalla_consulta6", u"Operadores", None))
        self.boton_autobuses.setText(QCoreApplication.translate("pantalla_consulta6", u"Autobuses", None))
        self.boton_inicio.setText("")
        self.boton_reservaciones.setText(QCoreApplication.translate("pantalla_consulta6", u"Reservaciones", None))
        self.label_4.setText("")
        self.label_6.setText("")
    # retranslateUi

