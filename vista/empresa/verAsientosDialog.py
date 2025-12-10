"""
Diálogo de Solo Lectura para Visualizar Asientos
Muestra los asientos ocupados/disponibles sin permitir selección.
"""

from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import Qt
from vista.empresa.verAsientoPlusDialog_ui import VerAsientoPlus
from vista.empresa.verAsientoPlatinoDialog_ui import VerAsientoPlatino

class VerAsientosDialog(QDialog):
    """
    Diálogo de solo lectura para visualizar asientos de una corrida.
    Determina automáticamente qué UI usar según el número de autobús.
    NO permite seleccionar asientos, solo visualizarlos.
    """
    
    def __init__(self, app_manager, numero_corrida, parent=None):
        super().__init__(parent)
        self.app_manager = app_manager
        self.controlador_corridas = app_manager.controlador_pc  # Controlador de corridas
        self.numero_corrida = numero_corrida
        
        # Obtener información de la corrida
        if not self.cargar_informacion_corrida():
            self.reject()
            return
        
        # Determinar qué UI usar según el número de autobús
        numero_autobus = self.corrida_info['numero_autobus']
        
        if 100 <= numero_autobus < 200:
            # Autobús Plus (44 asientos)
            self.ui = VerAsientoPlus()
            self.tipo_servicio = 'PLUS'
        elif 500 <= numero_autobus < 600:
            # Autobús Platino (34 asientos)
            self.ui = VerAsientoPlatino()
            self.tipo_servicio = 'PLATINO'
        else:
            QMessageBox.critical(self, "Error", "Tipo de autobús no válido")
            self.reject()
            return
        
        self.ui.setupUi(self)
        
        # Cargar información de la corrida en los labels
        self.mostrar_info_corrida()
        
        # Cargar estado de asientos (solo visualización)
        self.cargar_estado_asientos()
        
        # Conectar botón cerrar
        self.ui.boton_cerrar.clicked.connect(self.close)
    
    def cargar_informacion_corrida(self):
        """
        Carga la información completa de la corrida desde la base de datos.
        Retorna True si se cargó correctamente, False en caso contrario.
        """
        try:
            # Obtener información de la corrida usando el controlador de corridas
            corrida_data = self.controlador_corridas.obtener_informacion_corrida_para_asientos(self.numero_corrida)
            
            if not corrida_data:
                QMessageBox.warning(
                    self,
                    "Error",
                    f"No se encontró información para la corrida #{self.numero_corrida}"
                )
                return False
            
            self.corrida_info = corrida_data
            return True
            
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Error al cargar información de la corrida:\n{str(e)}"
            )
            print(f"Error en cargar_informacion_corrida: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def mostrar_info_corrida(self):
        """Muestra la información de la corrida en los labels del diálogo."""
        try:
            self.ui.label_numeroCorrida.setText(f"Corrida: {self.corrida_info['numero_corrida']}")
            self.ui.label_ciudadOrigen.setText(f"Origen: {self.corrida_info['ciudad_origen']}")
            self.ui.label_ciudadDestino.setText(f"Destino: {self.corrida_info['ciudad_destino']}")
            
            fecha_hora = f"{self.corrida_info['fecha']} {self.corrida_info['hora_salida']}"
            self.ui.label_fechaHoraSalida.setText(f"Salida: {fecha_hora}")
            
            self.ui.label_numeroAutobus.setText(f"Autobús: {self.corrida_info['numero_autobus']}")
        except Exception as e:
            print(f"Error al mostrar información de corrida: {e}")
    
    def cargar_estado_asientos(self):
        """
        Carga el estado de los asientos desde la base de datos.
        SOLO VISUALIZACIÓN - No permite seleccionar asientos.
        Verde = Disponible, Rojo = Ocupado.
        """
        try:
            # Usar el controlador_viajar para obtener asientos
            if not hasattr(self.app_manager, 'controlador_viajar') or not self.app_manager.controlador_viajar:
                print("ADVERTENCIA: controlador_viajar no disponible")
                # Marcar todos como disponibles si no hay controlador
                for btn in self.ui.asientos:
                    btn.setEnabled(True)
                    self.hacer_boton_no_clicable(btn)
                return
            
            asientos = self.app_manager.controlador_viajar.obtener_asientos_disponibles(self.numero_corrida)
            
            # Si no hay asientos en corrida_asiento, todos están disponibles por defecto
            if not asientos:
                print(f"INFO: No hay registros en corrida_asiento para la corrida {self.numero_corrida}")
                print("Todos los asientos se mostrarán como DISPONIBLES")
                # Todos los botones quedan habilitados (verdes) pero no clicables
                for btn in self.ui.asientos:
                    btn.setEnabled(True)  # Verde (disponible)
                    self.hacer_boton_no_clicable(btn)
                return
            
            # Crear un diccionario para acceso rápido
            estado_asientos = {asiento['clave']: asiento['estado'] for asiento in asientos}
            
            # Actualizar los botones de asiento (SOLO VISUALIZACIÓN)
            for btn in self.ui.asientos:
                asiento_numero = btn.text()
                asiento_clave = f"{self.corrida_info['numero_autobus']}-{asiento_numero.zfill(2)}"
                
                # Si el asiento está en la BD, usar su estado; si no, disponible
                estado = estado_asientos.get(asiento_clave, 'DISPONIBLE')
                
                if estado == 'NO DISPONIBLE':
                    # Mostrar como ocupado (ROJO) - deshabilitado
                    btn.setEnabled(False)
                    btn.setStyleSheet("""
                        QPushButton {
                            background-color: #F44336 !important;
                            color: white !important;
                            border: 2px solid #D32F2F !important;
                            border-radius: 8px;
                            font-weight: bold;
                            font-size: 16px;
                        }
                        QPushButton:disabled {
                            background-color: #F44336 !important;
                            color: white !important;
                            border: 2px solid #D32F2F !important;
                        }
                    """)
                else:
                    # Mostrar como disponible (VERDE) - habilitado visualmente pero no clicable
                    btn.setEnabled(True)
                    btn.setStyleSheet("""
                        QPushButton {
                            background-color: #4CAF50 !important;
                            color: white !important;
                            border: 2px solid #45a049 !important;
                            border-radius: 8px;
                            font-weight: bold;
                            font-size: 16px;
                        }
                    """)
                
                # CRÍTICO: Prevenir cualquier interacción de selección
                self.hacer_boton_no_clicable(btn)
                
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Error al cargar el estado de los asientos:\n{str(e)}"
            )
            print(f"Error en cargar_estado_asientos: {e}")
            import traceback
            traceback.print_exc()
    
    def hacer_boton_no_clicable(self, btn):
        """Hace que un botón no sea clicable pero mantenga su apariencia."""
        btn.setCheckable(False)
        btn.setAutoExclusive(False)
        # Desconectar cualquier señal existente y conectar a función vacía
        try:
            btn.clicked.disconnect()
        except:
            pass
        btn.clicked.connect(lambda: None)