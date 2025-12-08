# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pantalla_viajar.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class PantallaViajar(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1920, 1080)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(192)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_estatico_logo = QLabel(Form)
        self.label_estatico_logo.setObjectName(u"label_estatico_logo")
        self.label_estatico_logo.setGeometry(QRect(1560, 20, 331, 91))
        self.label_estatico_logo.setPixmap(QPixmap(u"../../recursos/recursos_empresa/Screenshot from 2025-11-22 14-58-14.png"))
        self.label_estatico_logo.setScaledContents(True)
        self.label_estatico_titulo = QLabel(Form)
        self.label_estatico_titulo.setObjectName(u"label_estatico_titulo")
        self.label_estatico_titulo.setGeometry(QRect(750, 40, 381, 71))
        self.boton_regresar = QPushButton(Form)
        self.boton_regresar.setObjectName(u"boton_regresar")
        self.boton_regresar.setGeometry(QRect(110, 40, 201, 71))
        self.boton_regresar.setStyleSheet(u"QPushButton {\n"
"    /* Sin color de fondo */\n"
"    background-color: transparent;\n"
"    \n"
"    /* Borde naranja */\n"
"    border: 2px solid #FFA500;\n"
"    \n"
"    /* Bordes redondos */\n"
"    border-radius: 15px;\n"
"    \n"
"    /* Texto naranja y en negrita */\n"
"    color: #FFA500;\n"
"    font-weight: bold;\n"
"	font-size: 24px;\n"
"    \n"
"    /* Padding interno */\n"
"    padding: 8px 16px;\n"
"    \n"
"    /* Eliminar outline por defecto */\n"
"    outline: none;\n"
"}\n"
"\n"
"/* Efecto hover */\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 165, 0, 0.1);\n"
"}\n"
"\n"
"/* Efecto pressed */\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 165, 0, 0.2);\n"
"    border: 2px solid #FF8C00;\n"
"    color: #FF8C00;\n"
"}\n"
"\n"
"/* Efecto disabled */\n"
"QPushButton:disabled {\n"
"    border: 2px solid #CCCCCC;\n"
"    color: #CCCCCC;\n"
"    background-color: transparent;\n"
"}")
        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(60, 300, 1781, 521))
        self.tableWidget.setStyleSheet(u"QTableView {\n"
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
"    \n"
"    /* Centrar todo el contenido de las celdas */\n"
"    qproperty-alignment: 'AlignCenter';\n"
"}\n"
"\n"
"QTableView::item {\n"
"    padding: 8px 12px;\n"
"    border: 0px;\n"
"    \n"
"    /* Centrar contenido de cada item */\n"
"    text-align: center;\n"
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
"    \n"
"    /* Cent"
                        "rar texto del encabezado */\n"
"    text-align: center;\n"
"    \n"
"    /* Asegurar que todas las columnas tengan el mismo ancho */\n"
"    qproperty-minimumSectionSize: 150; /* Ancho m\u00ednimo igual para todas */\n"
"    qproperty-defaultAlignment: 'AlignCenter'; /* Centrar texto del header */\n"
"}\n"
"\n"
"QHeaderView::section:hover {\n"
"    background: #f7f9fc;\n"
"}\n"
"\n"
"QHeaderView {\n"
"    background: #ffffff;\n"
"    border: 0;\n"
"    \n"
"    /* IMPORTANTE: Forzar que las secciones se estiren para llenar el espacio */\n"
"    qproperty-stretchLastSection: false;\n"
"    qproperty-resizeMode: 'Stretch'; /* Esto hace que las columnas se ajusten autom\u00e1ticamente */\n"
"}\n"
"\n"
"/* Configuraci\u00f3n adicional para el modelo de datos en Python */\n"
"QTableView QAbstractItemView {\n"
"    /* Asegurar que las columnas se ajusten al contenido */\n"
"    qproperty-horizontalScrollMode: 'ScrollPerPixel';\n"
"    qproperty-verticalScrollMode: 'ScrollPerPixel';\n"
"}\n"
"\n"
"QTableView::indicat"
                        "or {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"    /* Centrar el checkbox si hay */\n"
"    margin-left: auto;\n"
"    margin-right: auto;\n"
"}\n"
"\n"
"QHeaderView::section:first {\n"
"    border-top-left-radius: 8px;\n"
"}\n"
"\n"
"QHeaderView::section:last {\n"
"    border-top-right-radius: 8px;\n"
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
        self.tableWidget.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(223)
        self.label_estatico_titulo_2 = QLabel(Form)
        self.label_estatico_titulo_2.setObjectName(u"label_estatico_titulo_2")
        self.label_estatico_titulo_2.setGeometry(QRect(160, 200, 411, 71))
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, -20, 1931, 1121))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.boton_continuar = QPushButton(self.frame)
        self.boton_continuar.setObjectName(u"boton_continuar")
        self.boton_continuar.setGeometry(QRect(1120, 930, 191, 61))
        self.boton_continuar.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: 4px solid #1877F2;\n"
"    border-radius: 15px;\n"
"    color: #1877F2;\n"
"    font-weight: bold;\n"
"    font-size: 24px;\n"
"    padding: 12px 24px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(24, 119, 242, 0.1);\n"
"    border: 4px solid #166FE5;\n"
"    color: #166FE5;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(24, 119, 242, 0.2);\n"
"    border: 4px solid #1460C4;\n"
"    color: #1460C4;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border: 4px solid #CCCCCC;\n"
"    color: #CCCCCC;\n"
"    background-color: transparent;\n"
"}")
        self.label_estatico_subtitulo_4 = QLabel(self.frame)
        self.label_estatico_subtitulo_4.setObjectName(u"label_estatico_subtitulo_4")
        self.label_estatico_subtitulo_4.setGeometry(QRect(460, 940, 651, 41))
        self.LineEdit_pasajeros = QLineEdit(self.frame)
        self.LineEdit_pasajeros.setObjectName(u"LineEdit_pasajeros")
        self.LineEdit_pasajeros.setGeometry(QRect(600, 230, 221, 61))
        self.LineEdit_pasajeros.setStyleSheet(u"QLineEdit {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #dcdfe6;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-size: 22px;\n"
"    color: #1061C4;\n"
"    min-height: 18px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border-color: #c0c4cc;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: #409eff;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #f5f7fa;\n"
"    color: #c0c4cc;\n"
"    border-color: #e4e7ed;\n"
"}\n"
"\n"
"QLineEdit:read-only {\n"
"    background-color: #f5f7fa;\n"
"    color: #909399;\n"
"}")
        self.comboBox_fecha = QComboBox(self.frame)
        self.comboBox_fecha.setObjectName(u"comboBox_fecha")
        self.comboBox_fecha.setGeometry(QRect(1480, 230, 261, 61))
        self.comboBox_fecha.setStyleSheet(u"QComboBox {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #dcdfe6;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-size: 25px;\n"
"    color: #1061C4;\n"
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
"    /* ELIMINA CUALQUIER cursor: ...; DE AQU\u00cd */\n"
"}")
        self.comboBox_origen = QComboBox(self.frame)
        self.comboBox_origen.setObjectName(u"comboBox_origen")
        self.comboBox_origen.setGeometry(QRect(840, 230, 301, 61))
        self.comboBox_origen.setStyleSheet(u"QComboBox {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #dcdfe6;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-size: 25px;\n"
"    color: #1061C4;\n"
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
"    /* ELIMINA CUALQUIER cursor: ...; DE AQU\u00cd */\n"
"}")
        self.comboBox_destino = QComboBox(self.frame)
        self.comboBox_destino.setObjectName(u"comboBox_destino")
        self.comboBox_destino.setGeometry(QRect(1160, 230, 301, 61))
        self.comboBox_destino.setStyleSheet(u"QComboBox {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #dcdfe6;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-size: 25px;\n"
"    color: #1061C4;\n"
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
"    /* ELIMINA CUALQUIER cursor: ...; DE AQU\u00cd */\n"
"}")
        self.frame.raise_()
        self.label_estatico_logo.raise_()
        self.label_estatico_titulo.raise_()
        self.boton_regresar.raise_()
        self.tableWidget.raise_()
        self.label_estatico_titulo_2.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_estatico_logo.setText("")
        self.label_estatico_titulo.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:700; font-style:italic;\">VIAJAR</span></p></body></html>", None))
        self.boton_regresar.setText(QCoreApplication.translate("Form", u"Regresar", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"No. Corrida", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Ruta", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Autob\u00fas", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Servicio", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Hora de salida", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Hora de llegada", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Lugares disponibles", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"Precio", None));
        self.label_estatico_titulo_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:700;\">Ingrese los datos:</span></p></body></html>", None))
        self.boton_continuar.setText(QCoreApplication.translate("Form", u"Continuar", None))
        self.label_estatico_subtitulo_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:700;\">Selecciona una corrida para continuar</span></p></body></html>", None))
        self.LineEdit_pasajeros.setText("")
        self.LineEdit_pasajeros.setPlaceholderText(QCoreApplication.translate("Form", u"Cantidad pasajeros", None))
        self.comboBox_fecha.setPlaceholderText(QCoreApplication.translate("Form", u"Fecha", None))
        self.comboBox_origen.setPlaceholderText(QCoreApplication.translate("Form", u"Origen", None))
        self.comboBox_destino.setPlaceholderText(QCoreApplication.translate("Form", u"Destino", None))
    # retranslateUi

