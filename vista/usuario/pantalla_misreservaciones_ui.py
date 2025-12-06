# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pantalla_misreservaciones.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_pagina_misreservaciones(object):
    def setupUi(self, pagina_misreservaciones):
        if not pagina_misreservaciones.objectName():
            pagina_misreservaciones.setObjectName(u"pagina_misreservaciones")
        pagina_misreservaciones.resize(1920, 1080)
        pagina_misreservaciones.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_estatico_logo = QLabel(pagina_misreservaciones)
        self.label_estatico_logo.setObjectName(u"label_estatico_logo")
        self.label_estatico_logo.setGeometry(QRect(70, 70, 461, 131))
        self.label_estatico_logo.setStyleSheet(u"border:none")
        self.label_estatico_logo.setPixmap(QPixmap(u"recursos/recursos_empresa/loguito1.png"))
        self.label_estatico_logo.setScaledContents(True)
        self.label_estatico_logo.setWordWrap(False)
        self.tableWidget_tusReservaciones = QTableWidget(pagina_misreservaciones)
        if (self.tableWidget_tusReservaciones.columnCount() < 9):
            self.tableWidget_tusReservaciones.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_tusReservaciones.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_tusReservaciones.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_tusReservaciones.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_tusReservaciones.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_tusReservaciones.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_tusReservaciones.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_tusReservaciones.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_tusReservaciones.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_tusReservaciones.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tableWidget_tusReservaciones.setObjectName(u"tableWidget_tusReservaciones")
        self.tableWidget_tusReservaciones.setGeometry(QRect(60, 330, 1801, 771))
        self.tableWidget_tusReservaciones.setStyleSheet(u"QTableView {\n"
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
"    font-size: 22px;\n"
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
"\n"
"")
        self.tableWidget_tusReservaciones.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.tableWidget_tusReservaciones.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.tableWidget_tusReservaciones.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_tusReservaciones.verticalHeader().setVisible(False)
        self.boton_regresar = QPushButton(pagina_misreservaciones)
        self.boton_regresar.setObjectName(u"boton_regresar")
        self.boton_regresar.setGeometry(QRect(1540, 240, 91, 71))
        font = QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.boton_regresar.setFont(font)
        self.boton_regresar.setStyleSheet(u"QPushButton{\n"
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
        icon.addFile(u"recursos/recursos_usuario/volver.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_regresar.setIcon(icon)
        self.boton_regresar.setIconSize(QSize(35, 35))
        self.label_estatico_reservaciones = QLabel(pagina_misreservaciones)
        self.label_estatico_reservaciones.setObjectName(u"label_estatico_reservaciones")
        self.label_estatico_reservaciones.setGeometry(QRect(60, 230, 741, 71))
        font1 = QFont()
        font1.setPointSize(59)
        font1.setBold(True)
        font1.setItalic(True)
        self.label_estatico_reservaciones.setFont(font1)
        self.boton_verBoleto = QPushButton(pagina_misreservaciones)
        self.boton_verBoleto.setObjectName(u"boton_verBoleto")
        self.boton_verBoleto.setGeometry(QRect(1670, 240, 191, 71))
        self.boton_verBoleto.setStyleSheet(u"QPushButton{\n"
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

        self.retranslateUi(pagina_misreservaciones)

        QMetaObject.connectSlotsByName(pagina_misreservaciones)
    # setupUi

    def retranslateUi(self, pagina_misreservaciones):
        pagina_misreservaciones.setWindowTitle(QCoreApplication.translate("pagina_misreservaciones", u"Form", None))
        self.label_estatico_logo.setText("")
        ___qtablewidgetitem = self.tableWidget_tusReservaciones.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("pagina_misreservaciones", u"Reservacion", None));
        ___qtablewidgetitem1 = self.tableWidget_tusReservaciones.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("pagina_misreservaciones", u"Pasajeros", None));
        ___qtablewidgetitem2 = self.tableWidget_tusReservaciones.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("pagina_misreservaciones", u"Origen", None));
        ___qtablewidgetitem3 = self.tableWidget_tusReservaciones.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("pagina_misreservaciones", u"Destino", None));
        ___qtablewidgetitem4 = self.tableWidget_tusReservaciones.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("pagina_misreservaciones", u"Fecha de viaje", None));
        ___qtablewidgetitem5 = self.tableWidget_tusReservaciones.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("pagina_misreservaciones", u"Límite de pago", None));
        ___qtablewidgetitem6 = self.tableWidget_tusReservaciones.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("pagina_misreservaciones", u"IVA aplicado", None));
        ___qtablewidgetitem7 = self.tableWidget_tusReservaciones.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("pagina_misreservaciones", u"Subtotal", None));
        ___qtablewidgetitem8 = self.tableWidget_tusReservaciones.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("pagina_misreservaciones", u"Total", None));
        self.boton_regresar.setText("")
        self.label_estatico_reservaciones.setText(QCoreApplication.translate("pagina_misreservaciones", u"Tus Reservaciones", None))
        self.boton_verBoleto.setText(QCoreApplication.translate("pagina_misreservaciones", u"Ver boletos", None))
    # retranslateUi