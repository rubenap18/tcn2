"""
Wrapper para la pantalla de Mis Reservaciones.
Maneja la interfaz de usuario y la interacción con el controlador.
"""

from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QPushButton, QAbstractItemView
from PySide6.QtCore import Qt
from vista.usuario.pantalla_misreservaciones_ui import Ui_pagina_misreservaciones
from controladores.controlador_pantalla_misreservaciones import ControladorPantallaMisReservaciones

class PantallaMisReservacionesWidget(QWidget):
    """
    Widget que muestra las reservaciones del usuario logueado.
    """
    
    def __init__(self, app_manager, parent=None):
        super().__init__(parent)
        self.app_manager = app_manager
        
        # Configurar la UI
        self.ui = Ui_pagina_misreservaciones()
        self.ui.setupUi(self)
        
        # Obtener el controlador
        if not hasattr(self.app_manager, 'controlador_misreservaciones'):
            self.app_manager.controlador_misreservaciones = ControladorPantallaMisReservaciones()
        
        self.controlador = self.app_manager.controlador_misreservaciones
        
        # Configurar la tabla
        self.configurar_tabla()
        
        # Conectar botones
        self.conectar_senales()
        
        # Cargar las reservaciones del usuario
        self.cargar_reservaciones()
    
    def configurar_tabla(self):
        """Configura las propiedades de la tabla de reservaciones."""
        tabla = self.ui.tableWidget_tusReservaciones
        
        # Configurar encabezados
        headers = [
            "Reservación",
            "Pasajeros",
            "Origen",
            "Destino",
            "Fecha de viaje",
            "Límite de pago",
            "IVA aplicado",
            "Subtotal",
            "Total"
        ]
        tabla.setColumnCount(len(headers))
        tabla.setHorizontalHeaderLabels(headers)
        
        # Configurar selección
        tabla.setSelectionBehavior(QAbstractItemView.SelectRows)  # Seleccionar fila completa
        tabla.setSelectionMode(QAbstractItemView.SingleSelection)  # Solo una fila a la vez
        
        # Ajustar ancho de columnas (más parejas y balanceadas)
        tabla.setColumnWidth(0, 140)  # Reservación
        tabla.setColumnWidth(1, 120)  # Pasajeros
        tabla.setColumnWidth(2, 180)  # Origen
        tabla.setColumnWidth(3, 180)  # Destino
        tabla.setColumnWidth(4, 180)  # Fecha de viaje
        tabla.setColumnWidth(5, 180)  # Límite de pago
        tabla.setColumnWidth(6, 140)  # IVA
        tabla.setColumnWidth(7, 140)  # Subtotal
        tabla.setColumnWidth(8, 140)  # Total
        
        # Hacer que la tabla no sea editable
        tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
    
    def conectar_senales(self):
        """Conecta las señales de los botones."""
        # Botón para regresar al index
        self.ui.boton_regresar.clicked.connect(self.regresar_a_index)
        
        # Botón para ver boletos
        self.ui.boton_verBoleto.clicked.connect(self.ver_boletos_reservacion)
    
    def cargar_reservaciones(self):
        """Carga las reservaciones del usuario logueado en la tabla."""
        # Obtener el usuario actual
        usuario = self.app_manager.get_usuario_actual()
        
        if not usuario:
            QMessageBox.warning(
                self,
                "Sin sesión",
                "No hay un usuario logueado. Por favor, inicie sesión."
            )
            return
        
        # Obtener reservaciones del usuario
        reservaciones = self.controlador.obtener_reservaciones_cliente(usuario.id)
        
        if not reservaciones:
            # Solo limpiar la tabla sin mostrar mensaje
            self.ui.tableWidget_tusReservaciones.setRowCount(0)
            print(f"ℹ Usuario ID {usuario.id} no tiene reservaciones")
            return
        
        # Formatear datos para la tabla
        datos_tabla = self.controlador.formatear_reservaciones_para_tabla(reservaciones)
        
        # Llenar la tabla
        self.llenar_tabla(datos_tabla)
        
        print(f"✓ Cargadas {len(reservaciones)} reservaciones para el usuario ID: {usuario.id}")
    
    def llenar_tabla(self, datos):
        """
        Llena la tabla con los datos de reservaciones.
        
        Args:
            datos: Lista de listas con los datos a mostrar
        """
        tabla = self.ui.tableWidget_tusReservaciones
        tabla.setRowCount(0)  # Limpiar tabla
        
        # Agregar filas
        for fila_datos in datos:
            fila = tabla.rowCount()
            tabla.insertRow(fila)
            
            for columna, valor in enumerate(fila_datos):
                item = QTableWidgetItem(str(valor))
                item.setTextAlignment(Qt.AlignCenter)
                tabla.setItem(fila, columna, item)
        
        # Ajustar altura de filas
        for i in range(tabla.rowCount()):
            tabla.setRowHeight(i, 50)
    
    def ver_boletos_reservacion(self):
        """Muestra los boletos de la reservación seleccionada."""
        # Validar que haya una selección
        numero_reservacion = self.controlador.validar_seleccion_tabla(
            self.ui.tableWidget_tusReservaciones
        )
        
        if numero_reservacion is None:
            QMessageBox.warning(
                self,
                "Sin selección",
                "Por favor, selecciona una reservación de la tabla para ver sus boletos."
            )
            return
        
        # Abrir el diálogo de boletos
        try:
            from vista.compartido.mostrarBoletosDialog import MostrarBoletosDialog
            
            dialog = MostrarBoletosDialog(
                self.app_manager,
                numero_reservacion,
                self
            )
            dialog.exec()
            
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"No se pudieron cargar los boletos:\n{str(e)}"
            )
            print(f"Error al abrir diálogo de boletos: {e}")
    
    def regresar_a_index(self):
        """Regresa a la pantalla principal (index)."""
        if hasattr(self.app_manager, 'controlador_index_usuario'):
            self.app_manager.controlador_index_usuario.navegar_a_index()
    
    def actualizar_tabla(self):
        """Actualiza los datos de la tabla (útil después de cambios)."""
        self.cargar_reservaciones()