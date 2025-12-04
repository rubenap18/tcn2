import os
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QMessageBox, QTableWidgetItem)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, Qt # Import Qt for alignment

class PantallaMisReservaciones(QWidget):
    def __init__(self, controlador, user_id, parent=None):
        super().__init__(parent)
        self.controlador = controlador
        self.user_id = user_id # Store the user_id
        
        # Crear una instancia del loader
        loader = QUiLoader()

        # Esto construye la ruta correcta sin importar desde donde se ejecute el script
        path = os.path.join(os.path.dirname(__file__),"pantalla_misreservaciones.ui")
        ui_file = QFile(path)

        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Error: No se puede abrir el archivo UI en: {path}")
            return
        
        # Cargar el UI en self.ui
        self.ui = loader.load(ui_file, self)
        ui_file.close()

        # Integrar el widget cargado en este QWidget usando un layout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.ui)
        self.setLayout(layout)

        # Assuming tableWidget_tusReservaciones exists in the UI
        self.ui.tableWidget_tusReservaciones.setColumnCount(9) # 9 columns based on the provided logic
        self.ui.tableWidget_tusReservaciones.setHorizontalHeaderLabels([
            "N° Reserva", "Fecha", "Límite Pago", "Pasajeros", "Origen", "Destino", "Subtotal", "IVA", "Total"
        ])
        
        self.cargar_reservaciones_usuario()

    def cargar_reservaciones_usuario(self):
        """Cargar reservaciones con origen y destino"""
        if not self.user_id:
            QMessageBox.warning(self, "Advertencia", "No se ha proporcionado un ID de usuario.")
            return
        
        try:
            # The controller method for user reservations
            reservaciones = self.controlador.obtener_reservaciones_cliente(self.user_id)
            
            tabla = self.ui.tableWidget_tusReservaciones
            tabla.setRowCount(len(reservaciones))
            
            if reservaciones:
                for fila, reserva in enumerate(reservaciones):
                    # The provided 'reserva' tuple has 9 elements:
                    # 0: r.numero, 1: r.fecha, 2: r.fechaLimPago, 3: r.cantPasajeros,
                    # 4: rt.ciudadOrigen, 5: rt.ciudadDestino, 6: r.subtotal, 7: r.IVA, 8: r.total

                    # Original order in the provided logic:
                    # 0: N° Reserva, 1: Fecha, 2: Límite Pago, 3: Pasajeros, 
                    # 4: Origen, 5: Destino, 6: Subtotal, 7: IVA, 8: Total

                    tabla.setItem(fila, 0, QTableWidgetItem(str(reserva[0])))  # N° Reserva (r.numero)
                    tabla.setItem(fila, 1, QTableWidgetItem(str(reserva[1])))  # Fecha (r.fecha)
                    tabla.setItem(fila, 2, QTableWidgetItem(str(reserva[2])))  # Límite Pago (r.fechaLimPago)
                    tabla.setItem(fila, 3, QTableWidgetItem(str(reserva[3])))  # Pasajeros (r.cantPasajeros)
                    tabla.setItem(fila, 4, QTableWidgetItem(str(reserva[4])))  # Origen (rt.ciudadOrigen)
                    tabla.setItem(fila, 5, QTableWidgetItem(str(reserva[5])))  # Destino (rt.ciudadDestino)
                    tabla.setItem(fila, 6, QTableWidgetItem(str(reserva[6])))  # Subtotal (r.subtotal)
                    tabla.setItem(fila, 7, QTableWidgetItem(str(reserva[7])))  # IVA (r.IVA)
                    tabla.setItem(fila, 8, QTableWidgetItem(str(reserva[8])))  # Total (r.total)
            else:
                QMessageBox.information(self, "Reservaciones", "No tienes reservaciones registradas.")
                
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al cargar reservaciones: {str(e)}")
        # finally: # Removed this block as self.consultas.cerrar_conexion() is not needed here
            # self.consultas.cerrar_conexion() # This should be handled by the DAO's connection management
