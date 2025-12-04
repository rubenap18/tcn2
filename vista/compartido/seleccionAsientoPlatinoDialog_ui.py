# -*- coding: utf-8 -*-

from PySide6.QtCore import QMetaObject, QCoreApplication, QRect, Qt
from PySide6.QtWidgets import (QDialog, QFrame, QGridLayout, QVBoxLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy, QWidget)

class SeleccionAsientoPlatino(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(650, 800)
        Dialog.setStyleSheet("background-color: #f5f5f5;")
        
        # TÍTULO
        self.label_titulo = QLabel(Dialog)
        self.label_titulo.setGeometry(QRect(50, 10, 550, 60))
        self.label_titulo.setStyleSheet("font-size: 32pt; font-weight: bold; color: #9C27B0;")
        self.label_titulo.setAlignment(Qt.AlignCenter)
        self.label_titulo.setText("Selecciona tus Asientos - Platino")
        
        # INFORMACIÓN DE LA CORRIDA
        self.frame_info = QFrame(Dialog)
        self.frame_info.setGeometry(QRect(50, 80, 550, 120))
        self.frame_info.setStyleSheet("""
            QFrame {
                background-color: white;
                border: 2px solid #e0e0e0;
                border-radius: 10px;
                padding: 10px;
            }
        """)
        
        self.label_numeroCorrida = QLabel(self.frame_info)
        self.label_numeroCorrida.setGeometry(QRect(20, 10, 250, 30))
        self.label_numeroCorrida.setStyleSheet("font-size: 14pt; color: #333;")
        
        self.label_ciudadOrigen = QLabel(self.frame_info)
        self.label_ciudadOrigen.setGeometry(QRect(20, 40, 250, 30))
        self.label_ciudadOrigen.setStyleSheet("font-size: 14pt; color: #333;")
        
        self.label_ciudadDestino = QLabel(self.frame_info)
        self.label_ciudadDestino.setGeometry(QRect(20, 70, 250, 30))
        self.label_ciudadDestino.setStyleSheet("font-size: 14pt; color: #333;")
        
        self.label_fechaHoraSalida = QLabel(self.frame_info)
        self.label_fechaHoraSalida.setGeometry(QRect(290, 25, 240, 30))
        self.label_fechaHoraSalida.setStyleSheet("font-size: 13pt; color: #666;")
        
        self.label_numeroAutobus = QLabel(self.frame_info)
        self.label_numeroAutobus.setGeometry(QRect(290, 60, 150, 30))
        self.label_numeroAutobus.setStyleSheet("font-size: 13pt; color: #666;")
        
        # LEYENDA
        self.frame_leyenda = QFrame(Dialog)
        self.frame_leyenda.setGeometry(QRect(50, 210, 550, 50))
        self.frame_leyenda.setStyleSheet("background-color: white; border-radius: 5px;")
        
        layout_leyenda = QHBoxLayout(self.frame_leyenda)
        
        # Disponible
        self.btn_leyenda_disponible = QPushButton(self.frame_leyenda)
        self.btn_leyenda_disponible.setText("Disponible")
        self.btn_leyenda_disponible.setEnabled(False)
        self.btn_leyenda_disponible.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: 2px solid #45a049;
                border-radius: 5px;
                padding: 5px 15px;
                font-weight: bold;
            }
        """)
        
        # Seleccionado
        self.btn_leyenda_seleccionado = QPushButton(self.frame_leyenda)
        self.btn_leyenda_seleccionado.setText("Seleccionado")
        self.btn_leyenda_seleccionado.setEnabled(False)
        self.btn_leyenda_seleccionado.setStyleSheet("""
            QPushButton {
                background-color: #FF9800;
                color: white;
                border: 2px solid #F57C00;
                border-radius: 5px;
                padding: 5px 15px;
                font-weight: bold;
            }
        """)
        
        # Ocupado
        self.btn_leyenda_ocupado = QPushButton(self.frame_leyenda)
        self.btn_leyenda_ocupado.setText("Ocupado")
        self.btn_leyenda_ocupado.setEnabled(False)
        self.btn_leyenda_ocupado.setStyleSheet("""
            QPushButton {
                background-color: #CCCCCC;
                color: #666666;
                border: 2px solid #999999;
                border-radius: 5px;
                padding: 5px 15px;
                font-weight: bold;
            }
        """)
        
        layout_leyenda.addWidget(self.btn_leyenda_disponible)
        layout_leyenda.addWidget(self.btn_leyenda_seleccionado)
        layout_leyenda.addWidget(self.btn_leyenda_ocupado)
        
        # FRAME DE ASIENTOS
        self.frame_asientos = QFrame(Dialog)
        self.frame_asientos.setGeometry(QRect(120, 280, 410, 450))
        self.frame_asientos.setStyleSheet("""
            QFrame {
                background-color: white;
                border: 2px solid #9C27B0;
                border-radius: 10px;
                padding: 10px;
            }
        """)
        
        self.layoutWidget = QWidget(self.frame_asientos)
        self.layoutWidget.setGeometry(QRect(10, 10, 390, 430))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setSpacing(10)
        
        # CREAR 34 BOTONES DE ASIENTOS (PLATINO)
        self.asientos = []
        asiento_ids = [
            '01','02','03','04','05','06','07','08','09','10',
            '11','12','13','14','15','16','17','18','19','20',
            '21','22','23','24','25','26','27','28','29','30',
            '31','32','33','34'
        ]
        
        for asiento_id in asiento_ids:
            btn = QPushButton(self.layoutWidget)
            btn.setObjectName(f"btn_asiento_{asiento_id}")
            btn.setText(asiento_id)
            btn.setCheckable(True)
            btn.setAutoExclusive(False)
            btn.setMinimumSize(80, 40)
            btn.setMaximumSize(80, 40)
            btn.setCursor(Qt.PointingHandCursor)
            
            # ESTILOS COMPLETOS
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #4CAF50;
                    color: white;
                    border: 2px solid #45a049;
                    border-radius: 8px;
                    font-weight: bold;
                    font-size: 16px;
                }
                QPushButton:hover:enabled {
                    background-color: #45a049;
                    border: 3px solid #3d8b40;
                    transform: scale(1.05);
                }
                QPushButton:checked {
                    background-color: #FF9800;
                    border: 3px solid #F57C00;
                    color: white;
                }
                QPushButton:disabled {
                    background-color: #CCCCCC;
                    color: #666666;
                    border: 2px solid #999999;
                    cursor: not-allowed;
                }
            """)
            
            self.asientos.append(btn)
        
        # LAYOUT 2-2 CON PASILLO EN MEDIO (34 asientos = 8.5 filas, redondeamos a 9)
        row = 0
        for i, btn in enumerate(self.asientos):
            asientos_por_fila = 4
            posicion_en_fila = i % asientos_por_fila
            
            if posicion_en_fila == 0:
                col = 0  # Ventana izquierda
            elif posicion_en_fila == 1:
                col = 1  # Pasillo izquierdo
            elif posicion_en_fila == 2:
                col = 3  # Pasillo derecho (saltar col 2)
            else:  # posicion_en_fila == 3
                col = 4  # Ventana derecha
            
            self.gridLayout.addWidget(btn, row, col)
            
            if posicion_en_fila == 3:
                row += 1
        
        # BOTONES DE ACCIÓN
        self.frame_botones = QFrame(Dialog)
        self.frame_botones.setGeometry(QRect(150, 740, 350, 60))
        self.layout_botones = QHBoxLayout(self.frame_botones)
        
        self.boton_cancelar = QPushButton(self.frame_botones)
        self.boton_cancelar.setText("Cancelar")
        self.boton_cancelar.setMinimumSize(150, 50)
        self.boton_cancelar.setCursor(Qt.PointingHandCursor)
        self.boton_cancelar.setStyleSheet("""
            QPushButton {
                background-color: #f44336;
                color: white;
                border: none;
                border-radius: 8px;
                font-size: 16pt;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #da190b;
            }
            QPushButton:pressed {
                background-color: #c1170a;
            }
        """)
        
        self.boton_continuar = QPushButton(self.frame_botones)
        self.boton_continuar.setText("Continuar")
        self.boton_continuar.setMinimumSize(150, 50)
        self.boton_continuar.setCursor(Qt.PointingHandCursor)
        self.boton_continuar.setStyleSheet("""
            QPushButton {
                background-color: #9C27B0;
                color: white;
                border: none;
                border-radius: 8px;
                font-size: 16pt;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #8E24AA;
            }
            QPushButton:pressed {
                background-color: #7B1FA2;
            }
        """)
        
        self.layout_botones.addWidget(self.boton_cancelar)
        self.layout_botones.addWidget(self.boton_continuar)
        
        QMetaObject.connectSlotsByName(Dialog)