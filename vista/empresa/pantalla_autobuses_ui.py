# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pantalla_autobuses.ui'
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
import recursos.resources_rc

class Ui_pantalla_autobuses(object):
    def setupUi(self, pantalla_autobuses):
        if not pantalla_autobuses.objectName():
            pantalla_autobuses.setObjectName(u"pantalla_autobuses")
        pantalla_autobuses.resize(1920, 1080)
        pantalla_autobuses.setStyleSheet(u"background-color: #F5F3F1;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-bottom: 1px solid #E3E3E3;")
        self.sidebar_autobuses = QWidget(pantalla_autobuses)
        self.sidebar_autobuses.setObjectName(u"sidebar_autobuses")
        self.sidebar_autobuses.setGeometry(QRect(20, 130, 221, 931))
        self.sidebar_autobuses.setStyleSheet(u"\n"
"background-color: #1061C4;\n"
"border: 1px solid #dcdfe6;\n"
"border-radius: 15px;\n"
"gridline-color: #e0e0e0;\n"
"outline: none;\n"
"color: #606266;\n"
"")
        self.boton_registrarAutobus = QPushButton(self.sidebar_autobuses)
        self.boton_registrarAutobus.setObjectName(u"boton_registrarAutobus")
        self.boton_registrarAutobus.setGeometry(QRect(10, 40, 201, 71))
        font = QFont()
        font.setBold(True)
        self.boton_registrarAutobus.setFont(font)
        self.boton_registrarAutobus.setStyleSheet(u"QPushButton{\n"
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
        icon.addFile(u"recursos/recursos_empresa/agregar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_registrarAutobus.setIcon(icon)
        self.boton_registrarAutobus.setIconSize(QSize(30, 30))
        self.boton_bajaAutobus = QPushButton(self.sidebar_autobuses)
        self.boton_bajaAutobus.setObjectName(u"boton_bajaAutobus")
        self.boton_bajaAutobus.setGeometry(QRect(10, 110, 201, 71))
        self.boton_bajaAutobus.setFont(font)
        self.boton_bajaAutobus.setStyleSheet(u"QPushButton{\n"
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
        icon1.addFile(u"recursos/recursos_empresa/eliminar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_bajaAutobus.setIcon(icon1)
        self.boton_bajaAutobus.setIconSize(QSize(30, 30))
        self.widget_opfiltro_autobus = QWidget(pantalla_autobuses)
        self.widget_opfiltro_autobus.setObjectName(u"widget_opfiltro_autobus")
        self.widget_opfiltro_autobus.setGeometry(QRect(260, 130, 1651, 111))
        self.widget_opfiltro_autobus.setStyleSheet(u"QWidget {\n"
"    background: transparent;\n"
"    border: none;\n"
"    border-radius: 0px;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"}")
        self.label_estatico_tituloAutobuses = QLabel(self.widget_opfiltro_autobus)
        self.label_estatico_tituloAutobuses.setObjectName(u"label_estatico_tituloAutobuses")
        self.label_estatico_tituloAutobuses.setGeometry(QRect(50, 0, 481, 101))
        font1 = QFont()
        font1.setPointSize(59)
        font1.setBold(True)
        font1.setItalic(True)
        self.label_estatico_tituloAutobuses.setFont(font1)
        self.label_estatico_tituloAutobuses.setStyleSheet(u"border:none\n"
"")
        self.label_estatico_servicio = QLabel(self.widget_opfiltro_autobus)
        self.label_estatico_servicio.setObjectName(u"label_estatico_servicio")
        self.label_estatico_servicio.setGeometry(QRect(1050, 30, 221, 51))
        self.label_estatico_servicio.setStyleSheet(u"QLabel {\n"
"    background: transparent;\n"
"    border: none;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"    color: #000000;\n"
"}")
        self.comboBox_tiposAutobus = QComboBox(self.widget_opfiltro_autobus)
        self.comboBox_tiposAutobus.setObjectName(u"comboBox_tiposAutobus")
        self.comboBox_tiposAutobus.setGeometry(QRect(1270, 40, 221, 41))
        self.comboBox_tiposAutobus.setStyleSheet(u"QComboBox {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #dcdfe6;\n"
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
"}")
        self.QtableWidget_autobuses = QTableWidget(pantalla_autobuses)
        if (self.QtableWidget_autobuses.columnCount() < 6):
            self.QtableWidget_autobuses.setColumnCount(6)
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2);
        self.QtableWidget_autobuses.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font2);
        self.QtableWidget_autobuses.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font2);
        self.QtableWidget_autobuses.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font2);
        self.QtableWidget_autobuses.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font2);
        self.QtableWidget_autobuses.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font3);
        self.QtableWidget_autobuses.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.QtableWidget_autobuses.setObjectName(u"QtableWidget_autobuses")
        self.QtableWidget_autobuses.setGeometry(QRect(300, 240, 1491, 801))
        self.QtableWidget_autobuses.setFont(font)
        self.QtableWidget_autobuses.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.QtableWidget_autobuses.setStyleSheet(u"QTableView {\n"
"    background: #ffffff;\n"
"    border: 1px solid #e6e8ec;\n"
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
"}")
        self.QtableWidget_autobuses.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.QtableWidget_autobuses.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.QtableWidget_autobuses.horizontalHeader().setVisible(True)
        self.QtableWidget_autobuses.horizontalHeader().setCascadingSectionResizes(True)
        self.QtableWidget_autobuses.horizontalHeader().setDefaultSectionSize(248)
        self.QtableWidget_autobuses.horizontalHeader().setHighlightSections(False)
        self.QtableWidget_autobuses.verticalHeader().setCascadingSectionResizes(True)
        self.header_autobuses = QWidget(pantalla_autobuses)
        self.header_autobuses.setObjectName(u"header_autobuses")
        self.header_autobuses.setGeometry(QRect(-30, 0, 1961, 111))
        self.header_autobuses.setStyleSheet(u"QWidget {\n"
"    background: transparent;\n"
"    border: none;\n"
"    border-radius: 0px;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"}")
        self.boton_rutas = QPushButton(self.header_autobuses)
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
        icon2 = QIcon()
        icon2.addFile(u"recursos/recursos_empresa/entrega.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_rutas.setIcon(icon2)
        self.boton_rutas.setIconSize(QSize(30, 30))
        self.boton_corridas = QPushButton(self.header_autobuses)
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
        icon3 = QIcon()
        icon3.addFile(u"recursos/recursos_empresa/calendario.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_corridas.setIcon(icon3)
        self.boton_corridas.setIconSize(QSize(30, 30))
        self.boton_operadores = QPushButton(self.header_autobuses)
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
        icon4 = QIcon()
        icon4.addFile(u"recursos/recursos_empresa/conductor.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_operadores.setIcon(icon4)
        self.boton_operadores.setIconSize(QSize(30, 30))
        self.boton_autobuses = QPushButton(self.header_autobuses)
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
        icon5 = QIcon()
        icon5.addFile(u"recursos/recursos_empresa/autobus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_autobuses.setIcon(icon5)
        self.boton_autobuses.setIconSize(QSize(30, 30))
        self.boton_inicio = QPushButton(self.header_autobuses)
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
        icon6 = QIcon()
        icon6.addFile(u"recursos/recursos_empresa/casa-silueta-negra-sin-puerta.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_inicio.setIcon(icon6)
        self.boton_inicio.setIconSize(QSize(30, 30))
        self.boton_reservaciones = QPushButton(self.header_autobuses)
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
        icon7 = QIcon()
        icon7.addFile(u"recursos/recursos_empresa/boleto.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_reservaciones.setIcon(icon7)
        self.boton_reservaciones.setIconSize(QSize(30, 30))
        self.label = QLabel(self.header_autobuses)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 20, 211, 81))
        self.label.setStyleSheet(u"QLabel {\n"
"    background: transparent;\n"
"    border: none;\n"
"    border-radius: 0px;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"}")
        self.label.setPixmap(QPixmap(u"recursos/recursos_empresa/logo.png"))
        self.label.setScaledContents(True)

        self.retranslateUi(pantalla_autobuses)

        QMetaObject.connectSlotsByName(pantalla_autobuses)
    # setupUi

    def retranslateUi(self, pantalla_autobuses):
        self.boton_registrarAutobus.setText(QCoreApplication.translate("pantalla_autobuses", u" Registrar", None))
        self.boton_bajaAutobus.setText(QCoreApplication.translate("pantalla_autobuses", u"Dar de baja", None))
        self.label_estatico_tituloAutobuses.setText(QCoreApplication.translate("pantalla_autobuses", u"<html><head/><body><p><span style=\" color:#636363;\">Autobuses</span></p></body></html>", None))
        self.label_estatico_servicio.setText(QCoreApplication.translate("pantalla_autobuses", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:700;\">Tipo de servicio:</span></p></body></html>", None))
        ___qtablewidgetitem = self.QtableWidget_autobuses.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("pantalla_autobuses", u"N\u00famero", None));
        ___qtablewidgetitem1 = self.QtableWidget_autobuses.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("pantalla_autobuses", u"Matr\u00edcula", None));
        ___qtablewidgetitem2 = self.QtableWidget_autobuses.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("pantalla_autobuses", u"Marca", None));
        ___qtablewidgetitem3 = self.QtableWidget_autobuses.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("pantalla_autobuses", u"Modelo", None));
        ___qtablewidgetitem4 = self.QtableWidget_autobuses.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("pantalla_autobuses", u"Asientos", None));
        ___qtablewidgetitem5 = self.QtableWidget_autobuses.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("pantalla_autobuses", u"Estado", None));
        self.boton_rutas.setText(QCoreApplication.translate("pantalla_autobuses", u"Rutas", None))
        self.boton_corridas.setText(QCoreApplication.translate("pantalla_autobuses", u"Corridas", None))
        self.boton_operadores.setText(QCoreApplication.translate("pantalla_autobuses", u"Operadores", None))
        self.boton_autobuses.setText(QCoreApplication.translate("pantalla_autobuses", u"Autobuses", None))
        self.boton_inicio.setText("")
        self.boton_reservaciones.setText(QCoreApplication.translate("pantalla_autobuses", u"Reservaciones", None))
        self.label.setText("")
        pass
    # retranslateUi

