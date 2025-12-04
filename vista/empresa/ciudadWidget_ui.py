# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ciudadWidget.ui'
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
    QVBoxLayout, QWidget)

class Ui_pagina_ciudad(object):
    def setupUi(self, pagina_ciudad):
        if not pagina_ciudad.objectName():
            pagina_ciudad.setObjectName(u"pagina_ciudad")
        pagina_ciudad.resize(424, 452)
        pagina_ciudad.setMinimumSize(QSize(424, 452))
        pagina_ciudad.setMaximumSize(QSize(424, 452))
        pagina_ciudad.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.boton_editar = QPushButton(pagina_ciudad)
        self.boton_editar.setObjectName(u"boton_editar")
        self.boton_editar.setGeometry(QRect(170, 410, 81, 24))
        font = QFont()
        font.setBold(True)
        self.boton_editar.setFont(font)
        self.boton_editar.setStyleSheet(u"QPushButton{\n"
"	background: #FF6A36;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"}")
        self.label_estatico_titulo = QLabel(pagina_ciudad)
        self.label_estatico_titulo.setObjectName(u"label_estatico_titulo")
        self.label_estatico_titulo.setGeometry(QRect(70, 20, 281, 31))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setItalic(True)
        self.label_estatico_titulo.setFont(font1)
        self.layoutWidget_2 = QWidget(pagina_ciudad)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(220, 290, 171, 66))
        self.Layout_ciudad = QVBoxLayout(self.layoutWidget_2)
        self.Layout_ciudad.setObjectName(u"Layout_ciudad")
        self.Layout_ciudad.setContentsMargins(0, 0, 0, 0)
        self.label_estatico_ciudad = QLabel(self.layoutWidget_2)
        self.label_estatico_ciudad.setObjectName(u"label_estatico_ciudad")
        font2 = QFont()
        font2.setPointSize(12)
        self.label_estatico_ciudad.setFont(font2)

        self.Layout_ciudad.addWidget(self.label_estatico_ciudad)

        self.lineEdit_ciudad = QLineEdit(self.layoutWidget_2)
        self.lineEdit_ciudad.setObjectName(u"lineEdit_ciudad")
        self.lineEdit_ciudad.setStyleSheet(u"QLineEdit {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #dcdfe6;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-size: 13px;\n"
"    color: #606266;\n"
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

        self.Layout_ciudad.addWidget(self.lineEdit_ciudad)

        self.boton_agregar = QPushButton(pagina_ciudad)
        self.boton_agregar.setObjectName(u"boton_agregar")
        self.boton_agregar.setGeometry(QRect(260, 410, 141, 24))
        self.boton_agregar.setFont(font)
        self.boton_agregar.setStyleSheet(u"QPushButton{\n"
"	background: #1061C4;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"}")
        self.layoutWidget = QWidget(pagina_ciudad)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 290, 171, 66))
        self.Layout_codigo = QVBoxLayout(self.layoutWidget)
        self.Layout_codigo.setObjectName(u"Layout_codigo")
        self.Layout_codigo.setContentsMargins(0, 0, 0, 0)
        self.label_estatico_codigo = QLabel(self.layoutWidget)
        self.label_estatico_codigo.setObjectName(u"label_estatico_codigo")
        self.label_estatico_codigo.setFont(font2)

        self.Layout_codigo.addWidget(self.label_estatico_codigo)

        self.lineEdit_codigo = QLineEdit(self.layoutWidget)
        self.lineEdit_codigo.setObjectName(u"lineEdit_codigo")
        self.lineEdit_codigo.setStyleSheet(u"QLineEdit {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #dcdfe6;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-size: 13px;\n"
"    color: #606266;\n"
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

        self.Layout_codigo.addWidget(self.lineEdit_codigo)

        self.boton_cancelar = QPushButton(pagina_ciudad)
        self.boton_cancelar.setObjectName(u"boton_cancelar")
        self.boton_cancelar.setGeometry(QRect(80, 410, 81, 24))
        self.boton_cancelar.setFont(font)
        self.boton_cancelar.setStyleSheet(u"QPushButton{\n"
"	background: #FF6A36;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"}")
        self.tableWidget_ciudad = QTableWidget(pagina_ciudad)
        if (self.tableWidget_ciudad.columnCount() < 2):
            self.tableWidget_ciudad.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_ciudad.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_ciudad.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget_ciudad.setObjectName(u"tableWidget_ciudad")
        self.tableWidget_ciudad.setGeometry(QRect(30, 80, 361, 181))
        self.tableWidget_ciudad.setStyleSheet(u"QTableView {\n"
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
        self.tableWidget_ciudad.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_ciudad.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_ciudad.horizontalHeader().setVisible(True)
        self.tableWidget_ciudad.horizontalHeader().setDefaultSectionSize(179)
        self.tableWidget_ciudad.verticalHeader().setVisible(False)

        self.retranslateUi(pagina_ciudad)

        QMetaObject.connectSlotsByName(pagina_ciudad)
    # setupUi

    def retranslateUi(self, pagina_ciudad):
        pagina_ciudad.setWindowTitle(QCoreApplication.translate("pagina_ciudad", u"Form", None))
        self.boton_editar.setText(QCoreApplication.translate("pagina_ciudad", u"editar", None))
        self.label_estatico_titulo.setText(QCoreApplication.translate("pagina_ciudad", u"A\u00f1adir nueva ciudad", None))
        self.label_estatico_ciudad.setText(QCoreApplication.translate("pagina_ciudad", u"Ciudad", None))
        self.lineEdit_ciudad.setInputMask(QCoreApplication.translate("pagina_ciudad", u"aaaaaaaaaaaaaaaaaaaa", None))
        self.boton_agregar.setText(QCoreApplication.translate("pagina_ciudad", u"A\u00f1adir ciudad", None))
        self.label_estatico_codigo.setText(QCoreApplication.translate("pagina_ciudad", u"Codigo ", None))
        self.lineEdit_codigo.setInputMask(QCoreApplication.translate("pagina_ciudad", u">AAA", None))
        self.boton_cancelar.setText(QCoreApplication.translate("pagina_ciudad", u"Cancelar", None))
        ___qtablewidgetitem = self.tableWidget_ciudad.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("pagina_ciudad", u"Codigo", None));
        ___qtablewidgetitem1 = self.tableWidget_ciudad.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("pagina_ciudad", u"Nombre", None));
    # retranslateUi

