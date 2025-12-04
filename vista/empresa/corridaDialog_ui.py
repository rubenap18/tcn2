# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'corridaDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTimeEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(442, 543)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(16, 111, 365, 341))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.comboBox_rutaCorrida = QComboBox(self.layoutWidget)
        self.comboBox_rutaCorrida.addItem("")
        self.comboBox_rutaCorrida.addItem("")
        self.comboBox_rutaCorrida.addItem("")
        self.comboBox_rutaCorrida.addItem("")
        self.comboBox_rutaCorrida.addItem("")
        self.comboBox_rutaCorrida.addItem("")
        self.comboBox_rutaCorrida.addItem("")
        self.comboBox_rutaCorrida.addItem("")
        self.comboBox_rutaCorrida.addItem("")
        self.comboBox_rutaCorrida.addItem("")
        self.comboBox_rutaCorrida.addItem("")
        self.comboBox_rutaCorrida.addItem("")
        self.comboBox_rutaCorrida.addItem("")
        self.comboBox_rutaCorrida.addItem("")
        self.comboBox_rutaCorrida.addItem("")
        self.comboBox_rutaCorrida.addItem("")
        self.comboBox_rutaCorrida.addItem("")
        self.comboBox_rutaCorrida.addItem("")
        self.comboBox_rutaCorrida.addItem("")
        self.comboBox_rutaCorrida.addItem("")
        self.comboBox_rutaCorrida.addItem("")
        self.comboBox_rutaCorrida.addItem("")
        self.comboBox_rutaCorrida.addItem("")
        self.comboBox_rutaCorrida.addItem("")
        self.comboBox_rutaCorrida.addItem("")
        self.comboBox_rutaCorrida.addItem("")
        self.comboBox_rutaCorrida.addItem("")
        self.comboBox_rutaCorrida.addItem("")
        self.comboBox_rutaCorrida.addItem("")
        self.comboBox_rutaCorrida.addItem("")
        self.comboBox_rutaCorrida.setObjectName(u"comboBox_rutaCorrida")

        self.verticalLayout.addWidget(self.comboBox_rutaCorrida)


        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_13 = QLabel(self.layoutWidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)

        self.verticalLayout_6.addWidget(self.label_13)

        self.dateEdit_fechaCorrida = QDateEdit(self.layoutWidget)
        self.dateEdit_fechaCorrida.setObjectName(u"dateEdit_fechaCorrida")
        self.dateEdit_fechaCorrida.setMinimumDateTime(QDateTime(QDate(2025, 11, 24), QTime(8, 0, 0)))
        self.dateEdit_fechaCorrida.setMaximumDate(QDate(2030, 11, 23))

        self.verticalLayout_6.addWidget(self.dateEdit_fechaCorrida)


        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_17 = QLabel(self.layoutWidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)

        self.verticalLayout_7.addWidget(self.label_17)

        self.timeEdit_horaSalCorrida = QTimeEdit(self.layoutWidget)
        self.timeEdit_horaSalCorrida.setObjectName(u"timeEdit_horaSalCorrida")

        self.verticalLayout_7.addWidget(self.timeEdit_horaSalCorrida)


        self.horizontalLayout.addLayout(self.verticalLayout_7)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.verticalLayout_10.addWidget(self.label_11)

        self.timeEdit_horaLegCorrida = QTimeEdit(self.layoutWidget)
        self.timeEdit_horaLegCorrida.setObjectName(u"timeEdit_horaLegCorrida")

        self.verticalLayout_10.addWidget(self.timeEdit_horaLegCorrida)


        self.horizontalLayout.addLayout(self.verticalLayout_10)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_14 = QLabel(self.layoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)

        self.verticalLayout_3.addWidget(self.label_14)

        self.lineEdit_precioCorrida = QLineEdit(self.layoutWidget)
        self.lineEdit_precioCorrida.setObjectName(u"lineEdit_precioCorrida")
        self.lineEdit_precioCorrida.setMaxLength(4)

        self.verticalLayout_3.addWidget(self.lineEdit_precioCorrida)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.label_16 = QLabel(self.layoutWidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)

        self.verticalLayout_4.addWidget(self.label_16)

        self.comboBox_autobusCorrida = QComboBox(self.layoutWidget)
        self.comboBox_autobusCorrida.setObjectName(u"comboBox_autobusCorrida")

        self.verticalLayout_4.addWidget(self.comboBox_autobusCorrida)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_15 = QLabel(self.layoutWidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)

        self.verticalLayout_2.addWidget(self.label_15)

        self.comboBox_operadorCorrida = QComboBox(self.layoutWidget)
        self.comboBox_operadorCorrida.setObjectName(u"comboBox_operadorCorrida")

        self.verticalLayout_2.addWidget(self.comboBox_operadorCorrida)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(-10, 80, 741, 20))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 0, 511, 81))
        font1 = QFont()
        font1.setPointSize(27)
        font1.setBold(True)
        self.label.setFont(font1)
        self.boton_cancelar = QPushButton(Form)
        self.boton_cancelar.setObjectName(u"boton_cancelar")
        self.boton_cancelar.setGeometry(QRect(330, 500, 91, 31))
        font2 = QFont()
        font2.setBold(True)
        self.boton_cancelar.setFont(font2)
        self.boton_cancelar.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(237, 51, 59);\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(191, 41, 49);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color: rgb(141, 30, 36);\n"
"}")
        self.boton_crearCorrida = QPushButton(Form)
        self.boton_crearCorrida.setObjectName(u"boton_crearCorrida")
        self.boton_crearCorrida.setGeometry(QRect(220, 500, 101, 31))
        self.boton_crearCorrida.setFont(font2)
        self.boton_crearCorrida.setStyleSheet(u"QPushButton{\n"
"	background: #1061C4;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 6px;\n"
"	font-weight: bold;\n"
"	font-size:15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0D4FAB;    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0A3F8A;     \n"
"}")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Ruta", None))
        self.comboBox_rutaCorrida.setItemText(0, QCoreApplication.translate("Form", u"TIJ-TEC", None))
        self.comboBox_rutaCorrida.setItemText(1, QCoreApplication.translate("Form", u"TIJ-ESE", None))
        self.comboBox_rutaCorrida.setItemText(2, QCoreApplication.translate("Form", u"TIJ-MXL", None))
        self.comboBox_rutaCorrida.setItemText(3, QCoreApplication.translate("Form", u"TIJ-SFL", None))
        self.comboBox_rutaCorrida.setItemText(4, QCoreApplication.translate("Form", u"TIJ-SNQ", None))
        self.comboBox_rutaCorrida.setItemText(5, QCoreApplication.translate("Form", u"TEC-TIJ", None))
        self.comboBox_rutaCorrida.setItemText(6, QCoreApplication.translate("Form", u"TEC-ESE", None))
        self.comboBox_rutaCorrida.setItemText(7, QCoreApplication.translate("Form", u"TEC-MXL", None))
        self.comboBox_rutaCorrida.setItemText(8, QCoreApplication.translate("Form", u"TEC-SFL", None))
        self.comboBox_rutaCorrida.setItemText(9, QCoreApplication.translate("Form", u"TEC-SNQ", None))
        self.comboBox_rutaCorrida.setItemText(10, QCoreApplication.translate("Form", u"ESE-TIJ", None))
        self.comboBox_rutaCorrida.setItemText(11, QCoreApplication.translate("Form", u"ESE-TEC", None))
        self.comboBox_rutaCorrida.setItemText(12, QCoreApplication.translate("Form", u"ESE-MXL", None))
        self.comboBox_rutaCorrida.setItemText(13, QCoreApplication.translate("Form", u"ESE-SFL", None))
        self.comboBox_rutaCorrida.setItemText(14, QCoreApplication.translate("Form", u"ESE-SNQ", None))
        self.comboBox_rutaCorrida.setItemText(15, QCoreApplication.translate("Form", u"MXL-TIJ", None))
        self.comboBox_rutaCorrida.setItemText(16, QCoreApplication.translate("Form", u"MXL-TEC", None))
        self.comboBox_rutaCorrida.setItemText(17, QCoreApplication.translate("Form", u"MXL-ESE", None))
        self.comboBox_rutaCorrida.setItemText(18, QCoreApplication.translate("Form", u"MXL-SFL", None))
        self.comboBox_rutaCorrida.setItemText(19, QCoreApplication.translate("Form", u"MXL-SNQ", None))
        self.comboBox_rutaCorrida.setItemText(20, QCoreApplication.translate("Form", u"SFL-TIJ", None))
        self.comboBox_rutaCorrida.setItemText(21, QCoreApplication.translate("Form", u"SFL-TEC", None))
        self.comboBox_rutaCorrida.setItemText(22, QCoreApplication.translate("Form", u"SFL-ESE", None))
        self.comboBox_rutaCorrida.setItemText(23, QCoreApplication.translate("Form", u"SFL-MXL", None))
        self.comboBox_rutaCorrida.setItemText(24, QCoreApplication.translate("Form", u"SFL-SNQ", None))
        self.comboBox_rutaCorrida.setItemText(25, QCoreApplication.translate("Form", u"SNQ-TIJ", None))
        self.comboBox_rutaCorrida.setItemText(26, QCoreApplication.translate("Form", u"SNQ-TEC", None))
        self.comboBox_rutaCorrida.setItemText(27, QCoreApplication.translate("Form", u"SNQ-MXL", None))
        self.comboBox_rutaCorrida.setItemText(28, QCoreApplication.translate("Form", u"SNQ-SFL", None))
        self.comboBox_rutaCorrida.setItemText(29, QCoreApplication.translate("Form", u"SNQ-ESE", None))

        self.comboBox_rutaCorrida.setPlaceholderText(QCoreApplication.translate("Form", u"Ruta", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Fecha", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Hora de salida", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Hora de llegada", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Precio", None))
        self.lineEdit_precioCorrida.setText("")
        self.lineEdit_precioCorrida.setPlaceholderText(QCoreApplication.translate("Form", u"Precio", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Autob\u00fas", None))
        self.comboBox_autobusCorrida.setPlaceholderText(QCoreApplication.translate("Form", u"Autob\u00fas", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Operador", None))
        self.comboBox_operadorCorrida.setPlaceholderText(QCoreApplication.translate("Form", u"Operador", None))
        self.label.setText(QCoreApplication.translate("Form", u"Agregar nueva corrida", None))
        self.boton_cancelar.setText(QCoreApplication.translate("Form", u"Cancelar", None))
        self.boton_crearCorrida.setText(QCoreApplication.translate("Form", u"Crear corrida", None))
    # retranslateUi

