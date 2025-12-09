from PySide6.QtWidgets import QDialog, QMessageBox, QPushButton
from PySide6.QtCore import Qt
from vista.compartido.seleccionAsientoPlusDialog_ui import SeleccionAsientoPlus
from vista.compartido.seleccionAsientoPlatinoDialog_ui import SeleccionAsientoPlatino

class SeleccionAsientoDialog(QDialog):
    """
    Diálogo unificado para selección de asientos (Plus o Platino).
    Determina automáticamente qué UI usar según el número de autobús.
    """
    
    COMPRA_EXITOSA = 100
    
    def __init__(self, app_manager, corrida_info, num_pasajeros, parent=None):
        super().__init__(parent)
        self.app_manager = app_manager
        self.controlador = app_manager.controlador_viajar
        self.corrida_info = corrida_info
        self.num_pasajeros = num_pasajeros
        
        # Lista de asientos seleccionados
        self.asientos_seleccionados = []
        
        # Determinar qué UI usar según el número de autobús
        numero_autobus = corrida_info['numero_autobus']
        
        if 100 <= numero_autobus < 200:
            # Autobús Plus (44 asientos)
            self.ui = SeleccionAsientoPlus()
            self.tipo_servicio = 'PLUS'
        elif 500 <= numero_autobus < 600:
            # Autobús Platino (34 asientos)
            self.ui = SeleccionAsientoPlatino()
            self.tipo_servicio = 'PLATINO'
        else:
            QMessageBox.critical(self, "Error", "Tipo de autobús no válido")
            self.reject()
            return
        
        self.ui.setupUi(self)
        
        # Cargar información de la corrida
        self.cargar_info_corrida()
        
        # Cargar estado de asientos
        self.cargar_asientos()
        
        # Conectar señales
        self.conectar_senales()
    
    def cargar_info_corrida(self):
        """Carga la información de la corrida en los labels."""
        self.ui.label_numeroCorrida.setText(f"Corrida: {self.corrida_info['numero_corrida']}")
        self.ui.label_ciudadOrigen.setText(f"Origen: {self.corrida_info['ciudad_origen']}")
        self.ui.label_ciudadDestino.setText(f"Destino: {self.corrida_info['ciudad_destino']}")
        
        fecha_hora = f"{self.corrida_info['fecha']} {self.corrida_info['hora_salida']}"
        self.ui.label_fechaHoraSalida.setText(f"Salida: {fecha_hora}")
        
        self.ui.label_numeroAutobus.setText(f"Autobús: {self.corrida_info['numero_autobus']}")
    
    def cargar_asientos(self):
        """Carga el estado de los asientos desde la base de datos."""
        asientos = self.controlador.obtener_asientos_disponibles(self.corrida_info['numero_corrida'])
        
        # Si no hay asientos en corrida_asiento, todos están disponibles por defecto
        if not asientos:
            print(f"ADVERTENCIA: No hay registros en corrida_asiento para la corrida {self.corrida_info['numero_corrida']}")
            print("Todos los asientos se marcarán como DISPONIBLES")
            # Dejar todos los botones habilitados con el estilo por defecto de la UI
            return
        
        # Crear un diccionario para acceso rápido
        estado_asientos = {asiento['clave']: asiento['estado'] for asiento in asientos}
        
        # Actualizar los botones de asiento
        for btn in self.ui.asientos:
            asiento_numero = btn.text()
            asiento_clave = f"{self.corrida_info['numero_autobus']}-{asiento_numero.zfill(2)}"
            
            # Si el asiento está en la BD, usar su estado; si no, disponible
            estado = estado_asientos.get(asiento_clave, 'DISPONIBLE')
            
            
            if estado == 'NO DISPONIBLE':
                btn.setEnabled(False)
                btn.setCheckable(False)
                btn.setStyleSheet("""
                    QPushButton {
                        background-color: #CCCCCC !important;
                        color: #666666 !important;
                        border: 2px solid #999999 !important;
                        border-radius: 8px;
                        padding: 8px;
                        font-weight: bold;
                        font-size: 16px;
                    }
                    QPushButton:disabled {
                        background-color: #CCCCCC !important;
                        color: #666666 !important;
                        border: 2px solid #999999 !important;
                    }
                """)
            else:
                # Asiento disponible: asegurar que esté habilitado para seleccionar
                btn.setEnabled(True)
                btn.setCheckable(True)
                # El estilo ya viene de la UI, pero lo reforzamos
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
                    }
                    QPushButton:checked {
                        background-color: #FF9800 !important;
                        border: 3px solid #F57C00 !important;
                        color: white;
                    }
                """)
    
    def conectar_senales(self):
        """Conecta las señales de los botones."""
        # Conectar todos los botones de asiento
        for btn in self.ui.asientos:
            btn.clicked.connect(lambda checked, b=btn: self.on_asiento_clicked(b, checked))
        
        # Conectar botones de acción
        self.ui.boton_continuar.clicked.connect(self.on_continuar_clicked)
        self.ui.boton_cancelar.clicked.connect(self.reject)
    
    def on_asiento_clicked(self, boton, checked):
        """Cuando se selecciona/deselecciona un asiento."""
        asiento_numero = boton.text()
        asiento_clave = f"{self.corrida_info['numero_autobus']}-{asiento_numero.zfill(2)}"
        
        if checked:
            # Validar que no se excedan los pasajeros
            if len(self.asientos_seleccionados) >= self.num_pasajeros:
                QMessageBox.warning(self, "Límite alcanzado", 
                                  f"Solo puedes seleccionar {self.num_pasajeros} asiento(s)")
                boton.setChecked(False)
                return
            
            self.asientos_seleccionados.append(asiento_clave)
        else:
            if asiento_clave in self.asientos_seleccionados:
                self.asientos_seleccionados.remove(asiento_clave)
    
    def on_continuar_clicked(self):
        """Cuando se presiona continuar."""
        # Validar que se hayan seleccionado todos los asientos necesarios
        if len(self.asientos_seleccionados) != self.num_pasajeros:
            QMessageBox.warning(self, "Selección incompleta", 
                              f"Debes seleccionar exactamente {self.num_pasajeros} asiento(s).\n"
                              f"Actualmente tienes {len(self.asientos_seleccionados)} seleccionado(s).")
            return
        
        # Validar disponibilidad en BD (por si acaso)
        if not self.controlador.validar_asientos_disponibles(
            self.corrida_info['numero_corrida'], 
            self.asientos_seleccionados
        ):
            QMessageBox.critical(self, "Error", 
                               "Uno o más asientos ya no están disponibles. Por favor selecciona otros.")
            # Recargar asientos
            self.asientos_seleccionados.clear()
            for btn in self.ui.asientos:
                btn.setChecked(False)
            self.cargar_asientos()
            return
        
        # Abrir diálogo de datos de pasajeros
        from vista.compartido.IngresarPasajeroDialog import IngresarDatosPasajeroDialog
        
        dialog = IngresarDatosPasajeroDialog(
            self.app_manager,
            self.corrida_info,
            self.asientos_seleccionados,
            self
        )
        
        resultado = dialog.exec()
        
        if resultado == dialog.COMPRA_EXITOSA:
            # Propagar el éxito hacia arriba
            self.done(self.COMPRA_EXITOSA)