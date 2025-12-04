# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pantalla_reservaciones.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QStackedWidget,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_pantalla_reservaciones(object):
    def setupUi(self, pantalla_reservaciones):
        if not pantalla_reservaciones.objectName():
            pantalla_reservaciones.setObjectName(u"pantalla_reservaciones")
        pantalla_reservaciones.resize(1920, 1080)
        self.header_widget = QWidget(pantalla_reservaciones)
        self.header_widget.setObjectName(u"header_widget")
        self.header_widget.setGeometry(QRect(-10, 10, 1951, 111))
        self.header_widget.setStyleSheet(u"background-color: #FFF;\n"
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
        self.label_logo = QLabel(self.header_widget)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setGeometry(QRect(30, 10, 211, 81))
        self.label_logo.setPixmap(QPixmap(u"recursos/recursos_empresa/logo.png"))
        self.main_stackedWidget = QStackedWidget(pantalla_reservaciones)
        self.main_stackedWidget.setObjectName(u"main_stackedWidget")
        self.main_stackedWidget.setGeometry(QRect(0, 130, 1920, 971))
        self.main_stackedWidget.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 15px;\n"
"border-bottom: 1px solid #FFF;")
        self.pantalla_reservaciones_content = QWidget()
        self.pantalla_reservaciones_content.setObjectName(u"pantalla_reservaciones_content")
        self.widget_opbotones_6 = QWidget(self.pantalla_reservaciones_content)
        self.widget_opbotones_6.setObjectName(u"widget_opbotones_6")
        self.widget_opbotones_6.setGeometry(QRect(30, 20, 221, 871))
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
        self.boton_mostrarboleto = QPushButton(self.widget_opbotones_6)
        self.boton_mostrarboleto.setObjectName(u"boton_mostrarboleto")
        self.boton_mostrarboleto.setGeometry(QRect(9, 30, 201, 71))
        self.boton_mostrarboleto.setFont(font)
        self.boton_mostrarboleto.setStyleSheet(u"QPushButton{\n"
"	background: #1061C4;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0D4FAB;    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-c\n"
"\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"recursos/recursos_empresa/editar-reservacion.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_mostrarboleto.setIcon(icon6)
        self.boton_mostrarboleto.setIconSize(QSize(30, 30))
        self.widget_opfiltro_6 = QWidget(self.pantalla_reservaciones_content)
        self.widget_opfiltro_6.setObjectName(u"widget_opfiltro_6")
        self.widget_opfiltro_6.setGeometry(QRect(270, 20, 1641, 101))
        self.widget_opfiltro_6.setStyleSheet(u"background-color: #ffffff;\n"
"border: 1px solid #dcdfe6;\n"
"border-radius: 15px;\n"
"gridline-color: #e0e0e0;\n"
"outline: none;\n"
"color: #606266;\n"
"border-radius: 15px;\n"
"border-bottom: 1px solid #E3E3E3;\n"
"\n"
"")
        self.label_estatico_reservaciones = QLabel(self.widget_opfiltro_6)
        self.label_estatico_reservaciones.setObjectName(u"label_estatico_reservaciones")
        self.label_estatico_reservaciones.setGeometry(QRect(20, 10, 881, 71))
        font1 = QFont()
        font1.setPointSize(59)
        font1.setBold(True)
        font1.setItalic(False)
        self.label_estatico_reservaciones.setFont(font1)
        self.label_estatico_reservaciones.setStyleSheet(u"border:none\n"
"\n"
"")
        self.lineEdit_buscar = QLineEdit(self.widget_opfiltro_6)
        self.lineEdit_buscar.setObjectName(u"lineEdit_buscar")
        self.lineEdit_buscar.setGeometry(QRect(720, 30, 431, 41))
        self.lineEdit_buscar.setStyleSheet(u"QLineEdit { padding: 0 10px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"border: 1px solid #FF6A36\n"
"}")
        self.lineEdit_buscar.setMaxLength(20)
        self.boton_buscar = QPushButton(self.widget_opfiltro_6)
        self.boton_buscar.setObjectName(u"boton_buscar")
        self.boton_buscar.setGeometry(QRect(1130, 30, 41, 41))
        self.boton_buscar.setFont(font)
        self.boton_buscar.setStyleSheet(u"QPushButton{\n"
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
        icon7 = QIcon()
        icon7.addFile(u"recursos/recursos_empresa/boton_buscar_reservaciones.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_buscar.setIcon(icon7)
        self.boton_buscar.setIconSize(QSize(30, 30))
        self.tabla_reservaciones = QTableWidget(self.pantalla_reservaciones_content)
        if (self.tabla_reservaciones.columnCount() < 10):
            self.tabla_reservaciones.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem.setFont(font);
        self.tabla_reservaciones.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem1.setFont(font);
        self.tabla_reservaciones.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem2.setFont(font);
        self.tabla_reservaciones.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem3.setFont(font);
        self.tabla_reservaciones.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem4.setFont(font);
        self.tabla_reservaciones.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem5.setFont(font);
        self.tabla_reservaciones.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem6.setFont(font);
        self.tabla_reservaciones.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tabla_reservaciones.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem8.setFont(font);
        self.tabla_reservaciones.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem9.setFont(font);
        self.tabla_reservaciones.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.tabla_reservaciones.setObjectName(u"tabla_reservaciones")
        self.tabla_reservaciones.setGeometry(QRect(270, 140, 1641, 751))
        self.tabla_reservaciones.setFont(font)
        self.tabla_reservaciones.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tabla_reservaciones.setStyleSheet(u"QTableView {\n"
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
"}\n"
"")
        self.tabla_reservaciones.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tabla_reservaciones.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.tabla_reservaciones.setShowGrid(False)
        self.tabla_reservaciones.horizontalHeader().setVisible(True)
        self.tabla_reservaciones.horizontalHeader().setCascadingSectionResizes(True)
        self.tabla_reservaciones.horizontalHeader().setDefaultSectionSize(164)
        self.tabla_reservaciones.horizontalHeader().setHighlightSections(False)
        self.tabla_reservaciones.verticalHeader().setVisible(False)
        self.tabla_reservaciones.verticalHeader().setCascadingSectionResizes(True)
        self.main_stackedWidget.addWidget(self.pantalla_reservaciones_content)

        self.retranslateUi(pantalla_reservaciones)

        self.main_stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(pantalla_reservaciones)
    # setupUi

    def retranslateUi(self, pantalla_reservaciones):
        pantalla_reservaciones.setWindowTitle(QCoreApplication.translate("pantalla_reservaciones", u"Form", None))
        self.boton_rutas.setText(QCoreApplication.translate("pantalla_reservaciones", u"Rutas", None))
        self.boton_corridas.setText(QCoreApplication.translate("pantalla_reservaciones", u"Corridas", None))
        self.boton_operadores.setText(QCoreApplication.translate("pantalla_reservaciones", u"Operadores", None))
        self.boton_autobuses.setText(QCoreApplication.translate("pantalla_reservaciones", u"Autobuses", None))
        self.boton_inicio.setText("")
        self.boton_reservaciones.setText(QCoreApplication.translate("pantalla_reservaciones", u"Reservaciones", None))
        self.label_logo.setText("")
        self.boton_mostrarboleto.setText(QCoreApplication.translate("pantalla_reservaciones", u"Mostrar boleto", None))
        self.label_estatico_reservaciones.setText(QCoreApplication.translate("pantalla_reservaciones", u"Reservaciones", None))
        self.lineEdit_buscar.setPlaceholderText(QCoreApplication.translate("pantalla_reservaciones", u"Buscar por numero de corrida...", None))
        self.boton_buscar.setText("")
        ___qtablewidgetitem = self.tabla_reservaciones.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("pantalla_reservaciones", u"Fecha", None));
        ___qtablewidgetitem1 = self.tabla_reservaciones.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("pantalla_reservaciones", u"Corrida", None));
        ___qtablewidgetitem2 = self.tabla_reservaciones.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("pantalla_reservaciones", u"Cliente", None));
        ___qtablewidgetitem3 = self.tabla_reservaciones.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("pantalla_reservaciones", u"Origen", None));
        ___qtablewidgetitem4 = self.tabla_reservaciones.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("pantalla_reservaciones", u"Destino", None));
        ___qtablewidgetitem5 = self.tabla_reservaciones.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("pantalla_reservaciones", u"Salida", None));
        ___qtablewidgetitem6 = self.tabla_reservaciones.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("pantalla_reservaciones", u"Llegada", None));
        ___qtablewidgetitem7 = self.tabla_reservaciones.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("pantalla_reservaciones", u"Pasajeros", None));
        ___qtablewidgetitem8 = self.tabla_reservaciones.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("pantalla_reservaciones", u"Limite de Pago", None));
        ___qtablewidgetitem9 = self.tabla_reservaciones.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("pantalla_reservaciones", u"Acciones", None));
    # retranslateUi

