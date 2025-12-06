"""
Controlador para la pantalla de Mis Reservaciones del usuario.
Maneja la carga de reservaciones y visualización de boletos.
"""

from dao.misreservaciones_dao import MisReservacionesDAO
from PySide6.QtWidgets import QMessageBox

class ControladorPantallaMisReservaciones:
    """
    Controlador que maneja las reservaciones del usuario logueado.
    """
    
    def __init__(self):
        self.misreservaciones_dao = MisReservacionesDAO()

    def obtener_reservaciones_cliente(self, user_id):
        """
        Obtiene todas las reservaciones de un cliente específico.
        
        Args:
            user_id: ID del usuario
            
        Returns:
            Lista de tuplas con datos de reservaciones o lista vacía si hay error
        """
        try:
            return self.misreservaciones_dao.obtener_reservaciones_usuario(user_id)
        except Exception as e:
            print(f"Error en ControladorPantallaMisReservaciones.obtener_reservaciones_cliente: {e}")
            return []
    
    def formatear_reservaciones_para_tabla(self, reservaciones):
        """
        Formatea las reservaciones para mostrarlas en la tabla.
        
        Args:
            reservaciones: Lista de tuplas con datos de reservaciones
            
        Returns:
            Lista de listas con datos formateados para la tabla
        """
        datos_formateados = []
        
        for reservacion in reservaciones:
            # reservacion es una tupla con:
            # (numero, fecha, fechaLimPago, cantPasajeros, ciudadOrigen, ciudadDestino, subtotal, IVA, total)
            
            numero = reservacion[0]
            fecha = reservacion[1].strftime('%d/%m/%Y') if hasattr(reservacion[1], 'strftime') else str(reservacion[1])
            fecha_limite = reservacion[2].strftime('%d/%m/%Y') if hasattr(reservacion[2], 'strftime') else str(reservacion[2])
            cant_pasajeros = reservacion[3]
            origen = reservacion[4]  # código de ciudad origen
            destino = reservacion[5]  # código de ciudad destino
            subtotal = f"${reservacion[6]:.2f}"
            iva = f"${reservacion[7]:.2f}"
            total = f"${reservacion[8]:.2f}"
            
            # Obtener nombres de ciudades
            nombre_origen = self._obtener_nombre_ciudad(origen)
            nombre_destino = self._obtener_nombre_ciudad(destino)
            
            fila = [
                str(numero),
                str(cant_pasajeros),
                nombre_origen,
                nombre_destino,
                fecha,
                fecha_limite,
                iva,
                subtotal,
                total
            ]
            
            datos_formateados.append(fila)
        
        return datos_formateados
    
    def _obtener_nombre_ciudad(self, codigo_ciudad):
        """
        Obtiene el nombre de una ciudad por su código.
        
        Args:
            codigo_ciudad: Código de la ciudad
            
        Returns:
            Nombre de la ciudad o el código si no se encuentra
        """
        # Diccionario temporal de ciudades (puedes mejorar esto consultando la BD)
        ciudades = {
            1: "Tijuana",
            2: "Rosarito",
            3: "Ensenada",
            4: "San Quintín",
            5: "San Felipe",
            6: "Mexicali",
            7: "Tecate"
        }
        
        return ciudades.get(codigo_ciudad, str(codigo_ciudad))
    
    def validar_seleccion_tabla(self, tabla_widget):
        """
        Valida que haya una fila seleccionada en la tabla.
        
        Args:
            tabla_widget: Widget de la tabla
            
        Returns:
            Número de reservación seleccionado o None si no hay selección
        """
        filas_seleccionadas = tabla_widget.selectedItems()
        
        if not filas_seleccionadas:
            return None
        
        # Obtener la fila seleccionada
        fila = filas_seleccionadas[0].row()
        
        # El número de reservación está en la primera columna
        item_numero = tabla_widget.item(fila, 0)
        if item_numero:
            try:
                return int(item_numero.text())
            except ValueError:
                return None
        
        return None
    
    def obtener_info_reservacion(self, numero_reservacion):
        """
        Obtiene información detallada de una reservación específica.
        
        Args:
            numero_reservacion: Número de la reservación
            
        Returns:
            Tupla con información de la reservación o None si no existe
        """
        try:
            # Aquí podrías implementar un método específico en el DAO
            # Por ahora retornamos el número para usarlo con el controlador de viajar
            return numero_reservacion
        except Exception as e:
            print(f"Error en obtener_info_reservacion: {e}")
            return None