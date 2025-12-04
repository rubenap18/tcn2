from PySide6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QWidget, QScrollArea
from PySide6.QtCore import Qt
from vista.compartido.boletoWidget_ui import BoletoWidget

class MostrarBoletosDialog(QDialog):
    """
    Diálogo que muestra los boletos uno a la vez con navegación.
    """
    
    def __init__(self, app_manager, numero_reservacion, parent=None):
        super().__init__(parent)
        self.app_manager = app_manager
        self.controlador = app_manager.controlador_viajar
        self.numero_reservacion = numero_reservacion
        
        # Obtener los boletos
        self.boletos = self.controlador.obtener_boletos_reservacion(numero_reservacion)
        self.boleto_actual = 0
        
        # Configurar diálogo con dimensiones ajustadas
        self.setWindowTitle("Boletos - Compra Exitosa")
        self.setModal(True)
        # Aumentar más el tamaño para dar espacio adecuado
        self.resize(650, 1050)
        
        # Crear layout principal
        self.layout_principal = QVBoxLayout()
        self.layout_principal.setContentsMargins(15, 15, 15, 15)
        self.layout_principal.setSpacing(15)
        self.setLayout(self.layout_principal)
        
        # Crear área de scroll para el boleto
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scroll_area.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: #f5f5f5;
            }
        """)
        
        # Widget contenedor para el boleto
        self.contenedor_boleto = QWidget()
        self.contenedor_boleto.setStyleSheet("background-color: #f5f5f5;")
        self.layout_contenedor = QVBoxLayout(self.contenedor_boleto)
        self.layout_contenedor.setContentsMargins(15, 15, 15, 15)
        self.layout_contenedor.setAlignment(Qt.AlignCenter)
        
        # Widget para el boleto (se creará dinámicamente)
        self.widget_boleto = None
        self.crear_widget_boleto()
        
        self.scroll_area.setWidget(self.contenedor_boleto)
        self.layout_principal.addWidget(self.scroll_area, 1)
        
        # Label de contador
        self.label_contador = QLabel()
        self.label_contador.setAlignment(Qt.AlignCenter)
        self.label_contador.setStyleSheet("""
            font-size: 18pt; 
            font-weight: bold; 
            padding: 15px;
            color: #1061C4;
            background-color: white;
            border-radius: 8px;
            margin: 5px;
        """)
        self.layout_principal.addWidget(self.label_contador)
        
        # Layout de botones de navegación
        self.layout_botones = QHBoxLayout()
        self.layout_botones.setSpacing(20)
        self.layout_botones.setContentsMargins(10, 5, 10, 5)
        
        self.boton_anterior = QPushButton("← Anterior")
        self.boton_anterior.setMinimumHeight(55)
        self.boton_anterior.setMinimumWidth(140)
        self.boton_anterior.setStyleSheet("""
            QPushButton {
                background-color: #FF9800;
                color: white;
                border: 2px solid #F57C00;
                border-radius: 10px;
                padding: 15px 30px;
                font-weight: bold;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #F57C00;
            }
            QPushButton:disabled {
                background-color: #CCCCCC;
                color: #666666;
                border: 2px solid #999999;
            }
        """)
        self.boton_anterior.clicked.connect(self.anterior_boleto)
        
        self.boton_siguiente = QPushButton("Siguiente →")
        self.boton_siguiente.setMinimumHeight(55)
        self.boton_siguiente.setMinimumWidth(140)
        self.boton_siguiente.setStyleSheet("""
            QPushButton {
                background-color: #1877F2;
                color: white;
                border: 2px solid #166FE5;
                border-radius: 10px;
                padding: 15px 30px;
                font-weight: bold;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #166FE5;
            }
            QPushButton:disabled {
                background-color: #CCCCCC;
                color: #666666;
                border: 2px solid #999999;
            }
        """)
        self.boton_siguiente.clicked.connect(self.siguiente_boleto)
        
        self.boton_cerrar = QPushButton("✓ Cerrar")
        self.boton_cerrar.setMinimumHeight(55)
        self.boton_cerrar.setMinimumWidth(140)
        self.boton_cerrar.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: 2px solid #45a049;
                border-radius: 10px;
                padding: 15px 30px;
                font-weight: bold;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.boton_cerrar.clicked.connect(self.accept)
        
        self.layout_botones.addWidget(self.boton_anterior)
        self.layout_botones.addStretch()
        self.layout_botones.addWidget(self.boton_cerrar)
        self.layout_botones.addStretch()
        self.layout_botones.addWidget(self.boton_siguiente)
        
        self.layout_principal.addLayout(self.layout_botones)
        
        # Mostrar primer boleto
        self.actualizar_boleto()
    
    def crear_widget_boleto(self):
        """Crea el widget del boleto."""
        if self.widget_boleto:
            self.layout_contenedor.removeWidget(self.widget_boleto)
            self.widget_boleto.deleteLater()
        
        self.widget_boleto = QWidget()
        self.ui_boleto = BoletoWidget()
        self.ui_boleto.setupUi(self.widget_boleto)
        
        # Ajustar tamaño del widget para que se vea completo con más espacio
        self.widget_boleto.setFixedSize(600, 780)
        
        # Ajustar el widget interno para que se vea centrado
        if hasattr(self.ui_boleto, 'widget'):
            # Corregir el offset negativo y centrar
            self.ui_boleto.widget.setGeometry(0, 0, 600, 780)
            # Ajustar elementos con mejor espaciado
            self._reposicionar_elementos()
        
        # Ocultar botones de navegación del widget (usaremos los del diálogo)
        self.ui_boleto.boton_anterior.hide()
        self.ui_boleto.boton_siguiente.hide()
        
        # Agregar sombra y borde al boleto para mejor presentación
        self.widget_boleto.setStyleSheet("""
            QWidget {
                background-color: white;
                border-radius: 12px;
                border: 2px solid #e0e0e0;
            }
        """)
        
        self.layout_contenedor.addWidget(self.widget_boleto, 0, Qt.AlignCenter)
    
    def _reposicionar_elementos(self):
        """Reposiciona todos los elementos con mejor espaciado y alineación."""
        
        margen_izq = 60  # Margen izquierdo general
        
        # Logo - centrado arriba
        self.ui_boleto.label_imagen_logo.setGeometry(170, 40, 261, 71)
        
        # Sección Viaje y No.Boleto - Viaje centrado
        self.ui_boleto.label_estatico_viaje.setGeometry(margen_izq + 80, 130, 100, 34)
        self.ui_boleto.label_dinamico_viaje.setGeometry(margen_izq + 80, 165, 100, 34)
        # Centrar el texto de viaje
        self.ui_boleto.label_estatico_viaje.setAlignment(Qt.AlignCenter)
        self.ui_boleto.label_dinamico_viaje.setAlignment(Qt.AlignCenter)
        
        self.ui_boleto.label_estatico_numboleto.setGeometry(margen_izq + 240, 130, 140, 34)
        self.ui_boleto.label_dinamico_numboleto.setGeometry(margen_izq + 240, 165, 140, 34)
        
        # Sección Salida y Llegada - con más separación
        self.ui_boleto.label_estatico_salida_2.setGeometry(margen_izq + 20, 220, 100, 34)
        self.ui_boleto.label_dinamico_salida.setGeometry(margen_izq + 20, 255, 200, 34)
        # Reducir tamaño de fuente para salida
        self.ui_boleto.label_dinamico_salida.setStyleSheet("border:none; font-size: 14pt;")
        
        self.ui_boleto.label_estatico_llegada.setGeometry(margen_izq + 250, 220, 100, 34)
        self.ui_boleto.label_dinamico_llegada.setGeometry(margen_izq + 250, 255, 200, 34)
        # Reducir tamaño de fuente para llegada
        self.ui_boleto.label_dinamico_llegada.setStyleSheet("border:none; font-size: 14pt;")
        
        # Barra gris Origen-Destino - más grande
        self.ui_boleto.label_2.setGeometry(30, 310, 540, 100)
        
        self.ui_boleto.label_estatico_origen.setGeometry(margen_izq + 80, 325, 100, 34)
        self.ui_boleto.label_dinamico_origen.setGeometry(margen_izq + 40, 360, 180, 34)
        
        self.ui_boleto.label_estatico_destino.setGeometry(margen_izq + 260, 325, 120, 34)
        self.ui_boleto.label_dinamico_destino.setGeometry(margen_izq + 240, 360, 180, 34)
        
        # Pasajero - centrado y con espacio
        self.ui_boleto.label_estatico_pasajero.setGeometry(200, 430, 200, 34)
        self.ui_boleto.label_dinamico_pasajero.setGeometry(100, 465, 400, 34)
        
        # Columna izquierda - No.Asiento y Tipo
        self.ui_boleto.label_estatico_numasientos.setGeometry(margen_izq, 525, 150, 34)
        self.ui_boleto.label_dinamico_numasiento.setGeometry(margen_izq, 560, 150, 34)
        
        self.ui_boleto.label_estatico_tipopasajero.setGeometry(margen_izq, 610, 150, 34)
        self.ui_boleto.label_dinamico_tipopasajero.setGeometry(margen_izq, 645, 150, 34)
        
        # Columna derecha - Precios alineados a la derecha
        col_derecha_label = 270
        col_derecha_valor = 390
        
        self.ui_boleto.label_estatico_precioboleto.setGeometry(col_derecha_label, 525, 100, 34)
        self.ui_boleto.label_dinamico_precioboleto.setGeometry(col_derecha_valor, 525, 150, 34)
        
        self.ui_boleto.label_estatico_descuento.setGeometry(col_derecha_label - 20, 560, 130, 34)
        self.ui_boleto.label_dinamico_pordescuento.setGeometry(col_derecha_valor, 560, 150, 34)
        
        self.ui_boleto.label_dinamico_descuento.setGeometry(col_derecha_valor, 595, 150, 34)
        
        self.ui_boleto.label_estatico_total.setGeometry(col_derecha_label, 640, 100, 34)
        self.ui_boleto.label_dinamico_total.setGeometry(col_derecha_valor, 640, 150, 34)
    
    def actualizar_boleto(self):
        """Actualiza el widget con los datos del boleto actual."""
        if not self.boletos:
            return
        
        boleto = self.boletos[self.boleto_actual]
        
        # Actualizar contador
        self.label_contador.setText(f"Boleto {self.boleto_actual + 1} de {len(self.boletos)}")
        
        # Actualizar información del boleto
        self.ui_boleto.label_dinamico_viaje.setText(str(boleto['numero_corrida']))
        self.ui_boleto.label_dinamico_numboleto.setText(str(boleto['numero_boleto']))
        
        self.ui_boleto.label_dinamico_origen.setText(boleto['ciudad_origen'])
        self.ui_boleto.label_dinamico_destino.setText(boleto['ciudad_destino'])
        
        # Formatear fechas
        fecha_str = boleto['fecha_corrida'].strftime('%d/%m/%Y') if hasattr(boleto['fecha_corrida'], 'strftime') else str(boleto['fecha_corrida'])
        hora_salida = str(boleto['hora_salida'])
        hora_llegada = str(boleto['hora_llegada'])
        
        self.ui_boleto.label_dinamico_salida.setText(f"{fecha_str} {hora_salida}")
        self.ui_boleto.label_dinamico_llegada.setText(f"{fecha_str} {hora_llegada}")
        
        # Información del pasajero
        nombre_completo = f"{boleto['nombre']} {boleto['apellPat']}"
        if boleto['apellMat']:
            nombre_completo += f" {boleto['apellMat']}"
        self.ui_boleto.label_dinamico_pasajero.setText(nombre_completo)
        
        # Asiento
        self.ui_boleto.label_dinamico_numasiento.setText(str(boleto['numero_asiento']))
        
        # Tipo de pasajero
        self.ui_boleto.label_dinamico_tipopasajero.setText(boleto['tipo_pasajero'])
        
        # Cálculos de precio
        if boleto['porcentaje_descuento'] > 0 and boleto['porcentaje_descuento'] < 100:
            precio_base = boleto['precio'] / (1 - boleto['porcentaje_descuento'] / 100)
        else:
            precio_base = boleto['precio']
        
        descuento = precio_base * (boleto['porcentaje_descuento'] / 100)
        
        self.ui_boleto.label_dinamico_precioboleto.setText(f"${precio_base:.2f}")
        self.ui_boleto.label_dinamico_pordescuento.setText(f"{boleto['porcentaje_descuento']}%")
        self.ui_boleto.label_dinamico_descuento.setText(f"-${descuento:.2f}")
        self.ui_boleto.label_dinamico_total.setText(f"${boleto['precio']:.2f}")
        
        # Actualizar estado de botones
        self.boton_anterior.setEnabled(self.boleto_actual > 0)
        self.boton_siguiente.setEnabled(self.boleto_actual < len(self.boletos) - 1)
    
    def anterior_boleto(self):
        """Navega al boleto anterior."""
        if self.boleto_actual > 0:
            self.boleto_actual -= 1
            self.actualizar_boleto()
    
    def siguiente_boleto(self):
        """Navega al siguiente boleto."""
        if self.boleto_actual < len(self.boletos) - 1:
            self.boleto_actual += 1
            self.actualizar_boleto()