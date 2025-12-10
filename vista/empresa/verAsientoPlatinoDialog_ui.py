# -*- coding: utf-8 -*-

from PySide6.QtCore import QMetaObject, QCoreApplication, QRect, Qt
from PySide6.QtWidgets import (QDialog, QFrame, QGridLayout, QVBoxLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy, QWidget)

class VerAsientoPlatino(object):
    """
    VERSIÓN DE SOLO LECTURA - Para visualizar asientos sin selección.
    No permite seleccionar asientos, solo ver cuáles están ocupados/disponibles.
    """
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(650, 820)
        Dialog.setStyleSheet("background-color: #f5f5f5;")
        
        # TÍTULO
        self.label_titulo = QLabel(Dialog)
        self.label_titulo.setGeometry(QRect(20, 10, 640, 70))
        self.label_titulo.setStyleSheet("font-size: 26pt; font-weight: bold; color: #9C27B0;")
        self.label_titulo.setAlignment(Qt.AlignCenter)
        self.label_titulo.setText("Ver Asientos - Platino")
        
        # INFORMACIÓN DE LA CORRIDA
        self.frame_info = QFrame(Dialog)
        self.frame_info.setGeometry(QRect(20, 90, 610, 180))
        self.frame_info.setStyleSheet("""
            QFrame {
                background-color: white;
                border: 2px solid #e0e0e0;
                border-radius: 10px;
                padding: 10px;
            }
        """)
        
        # Labels con más espacio
        self.label_numeroCorrida = QLabel(self.frame_info)
        self.label_numeroCorrida.setGeometry(QRect(20, 20, 320, 40))
        self.label_numeroCorrida.setStyleSheet("font-size: 13pt; color: #333;")  
        
        self.label_ciudadOrigen = QLabel(self.frame_info)
        self.label_ciudadOrigen.setGeometry(QRect(20, 65, 320, 47))  
        self.label_ciudadOrigen.setStyleSheet("font-size: 13pt; color: #333;")  
        
        self.label_ciudadDestino = QLabel(self.frame_info)
        self.label_ciudadDestino.setGeometry(QRect(20, 120, 320, 47))  
        self.label_ciudadDestino.setStyleSheet("font-size: 13pt; color: #333;")  
        
        # Labels columna derecha
        self.label_fechaHoraSalida = QLabel(self.frame_info)
        self.label_fechaHoraSalida.setGeometry(QRect(350, 35, 240, 50))  
        self.label_fechaHoraSalida.setStyleSheet("font-size: 12pt; color: #666;")  
        
        self.label_numeroAutobus = QLabel(self.frame_info)
        self.label_numeroAutobus.setGeometry(QRect(350, 90, 240, 50))  
        self.label_numeroAutobus.setStyleSheet("font-size: 15pt; color: #666;")  
        
        # LEYENDA (sin "Seleccionado" ya que no se puede seleccionar)
        self.frame_leyenda = QFrame(Dialog)
        self.frame_leyenda.setGeometry(QRect(20, 280, 610, 50))
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
        
        # Ocupado
        self.btn_leyenda_ocupado = QPushButton(self.frame_leyenda)
        self.btn_leyenda_ocupado.setText("Ocupado")
        self.btn_leyenda_ocupado.setEnabled(False)
        self.btn_leyenda_ocupado.setStyleSheet("""
            QPushButton {
                background-color: #F44336;
                color: white;
                border: 2px solid #D32F2F;
                border-radius: 5px;
                padding: 5px 15px;
                font-weight: bold;
            }
        """)
        
        layout_leyenda.addWidget(self.btn_leyenda_disponible)
        layout_leyenda.addWidget(self.btn_leyenda_ocupado)
        
        # FRAME DE ASIENTOS
        self.frame_asientos = QFrame(Dialog)
        self.frame_asientos.setGeometry(QRect(120, 340, 410, 450))
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
        
        # CREAR 34 BOTONES DE ASIENTOS (PLATINO) - TODOS DESHABILITADOS PARA SELECCIÓN
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
            btn.setCheckable(False)  # NO CHECKABLE - Solo lectura
            btn.setEnabled(True)  # Habilitado para mostrar colores, pero no clicable
            btn.setMinimumSize(80, 40)
            btn.setMaximumSize(80, 40)
            btn.setCursor(Qt.ArrowCursor)  # Cursor normal, no de mano
            
            # ESTILOS PARA SOLO LECTURA
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #4CAF50;
                    color: white;
                    border: 2px solid #45a049;
                    border-radius: 8px;
                    font-weight: bold;
                    font-size: 16px;
                }
                QPushButton:disabled {
                    background-color: #F44336;
                    color: white;
                    border: 2px solid #D32F2F;
                }
            """)
            
            self.asientos.append(btn)
        
        # LAYOUT 2-2 CON PASILLO EN MEDIO
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
        
        # SOLO BOTÓN CERRAR
        self.frame_botones = QFrame(Dialog)
        self.frame_botones.setGeometry(QRect(225, 800, 200, 60))
        self.layout_botones = QHBoxLayout(self.frame_botones)
        
        self.boton_cerrar = QPushButton(self.frame_botones)
        self.boton_cerrar.setText("Cerrar")
        self.boton_cerrar.setMinimumSize(180, 50)
        self.boton_cerrar.setCursor(Qt.PointingHandCursor)
        self.boton_cerrar.setStyleSheet("""
            QPushButton {
                background-color: #607D8B;
                color: white;
                border: none;
                border-radius: 8px;
                font-size: 16pt;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #546E7A;
            }
            QPushButton:pressed {
                background-color: #455A64;
            }
        """)
        
        self.layout_botones.addWidget(self.boton_cerrar)
        
        QMetaObject.connectSlotsByName(Dialog)