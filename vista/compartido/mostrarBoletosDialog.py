from PySide6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QWidget
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
        
        # Configurar diálogo
        self.setWindowTitle("Boletos - Compra Exitosa")
        self.setModal(True)
        self.resize(600, 950)
        
        # Crear layout principal
        self.layout_principal = QVBoxLayout()
        self.setLayout(self.layout_principal)
        
        # Widget para el boleto (se creará dinámicamente)
        self.widget_boleto = None
        self.crear_widget_boleto()
        
        # Label de contador
        self.label_contador = QLabel()
        self.label_contador.setAlignment(Qt.AlignCenter)
        self.label_contador.setStyleSheet("font-size: 18pt; font-weight: bold; padding: 10px;")
        self.layout_principal.addWidget(self.label_contador)
        
        # Layout de botones de navegación
        self.layout_botones = QHBoxLayout()
        
        self.boton_anterior = QPushButton("← Anterior")
        self.boton_anterior.setStyleSheet("""
            QPushButton {
                background-color: #FF9800;
                color: white;
                border: 2px solid #F57C00;
                border-radius: 8px;
                padding: 12px 24px;
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
        self.boton_siguiente.setStyleSheet("""
            QPushButton {
                background-color: #1877F2;
                color: white;
                border: 2px solid #166FE5;
                border-radius: 8px;
                padding: 12px 24px;
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
        
        self.boton_cerrar = QPushButton("Cerrar")
        self.boton_cerrar.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: 2px solid #45a049;
                border-radius: 8px;
                padding: 12px 24px;
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
            self.layout_principal.removeWidget(self.widget_boleto)
            self.widget_boleto.deleteLater()
        
        self.widget_boleto = QWidget()
        self.ui_boleto = BoletoWidget()
        self.ui_boleto.setupUi(self.widget_boleto)
        
        # Ocultar botones de navegación del widget (usaremos los del diálogo)
        self.ui_boleto.boton_anterior.hide()
        self.ui_boleto.boton_siguiente.hide()
        
        self.layout_principal.insertWidget(0, self.widget_boleto)
    
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
        precio_base = boleto['precio'] / (1 - boleto['porcentaje_descuento'] / 100)
        descuento = precio_base * (boleto['porcentaje_descuento'] / 100)
        
        self.ui_boleto.label_dinamico_precioboleto.setText(f"${precio_base:.2f}")
        self.ui_boleto.label_dinamico_pordescuento.setText(f"{boleto['porcentaje_descuento']}%")
        self.ui_boleto.label_dinamico_descuento.setText(f"${descuento:.2f}")
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