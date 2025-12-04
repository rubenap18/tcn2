from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import QDate
from vista.compartido.IngresarDatosPasajeroDialog_ui import IngresarDatosPasajeroDialog as IngresarDatosUI
from datetime import datetime

class IngresarDatosPasajeroDialog(QDialog):
    """
    Diálogo para ingresar datos de pasajeros (se repite por cada asiento).
    """
    
    COMPRA_EXITOSA = 100
    
    def __init__(self, app_manager, corrida_info, asientos_seleccionados, parent=None):
        super().__init__(parent)
        self.app_manager = app_manager
        self.controlador = app_manager.controlador_viajar
        self.corrida_info = corrida_info
        self.asientos_seleccionados = asientos_seleccionados
        
        # Lista de pasajeros capturados
        self.pasajeros_data = []
        self.pasajero_actual = 0
        
        # Configurar UI
        self.ui = IngresarDatosUI()
        self.ui.setupUi(self)
        
        # Actualizar título
        self.actualizar_titulo()
        
        # Configurar fecha máxima (hoy)
        self.ui.dateEdit_fechaNacimientoPasajero.setMaximumDate(QDate.currentDate())
        
        # Conectar señales
        self.conectar_senales()
    
    def conectar_senales(self):
        """Conecta las señales de los botones."""
        self.ui.boton_continuar.clicked.connect(self.on_continuar_clicked)
        self.ui.boton_continuar_2.clicked.connect(self.on_regresar_clicked)  # Botón regresar
    
    def actualizar_titulo(self):
        """Actualiza el título mostrando el progreso."""
        asiento_numero = self.asientos_seleccionados[self.pasajero_actual].split('-')[1]
        self.ui.label.setText(
            f"<html><head/><body><p align='center'>"
            f"<span style='font-size:36pt; font-weight:700; font-style:italic;'>"
            f"Pasajero {self.pasajero_actual + 1} de {len(self.asientos_seleccionados)}"
            f"</span></p><p align='center'>"
            f"<span style='font-size:24pt;'>Asiento: {asiento_numero}</span>"
            f"</p></body></html>"
        )
    
    def validar_datos(self):
        """Valida los datos ingresados."""
        nombre = self.ui.lineEdit_ingresarNombre.text().strip()
        apellido_pat = self.ui.lineEdit_ingresarPrimerApellido.text().strip()
        apellido_mat = self.ui.lineEdit_ingresarSegundoApellido.text().strip()
        fecha_nac = self.ui.dateEdit_fechaNacimientoPasajero.date()
        correo = self.ui.lineEdit_ingresarCorreo.text().strip()
        telefono = self.ui.lineEdit_ingresarTelefono.text().strip()
        
        # Validaciones
        if not nombre:
            QMessageBox.warning(self, "Datos incompletos", "Ingresa el nombre del pasajero")
            return None
        
        if not apellido_pat:
            QMessageBox.warning(self, "Datos incompletos", "Ingresa el primer apellido")
            return None
        
        # Segundo apellido es opcional (ya está contemplado en los requerimientos)
        
        if not telefono or len(telefono) != 10:
            QMessageBox.warning(self, "Teléfono inválido", "Ingresa un teléfono válido de 10 dígitos")
            return None
        
        # Validar que la fecha no sea futura
        if fecha_nac >= QDate.currentDate():
            QMessageBox.warning(self, "Fecha inválida", "La fecha de nacimiento no puede ser hoy o en el futuro")
            return None
        
        # Convertir QDate a Python date
        fecha_python = fecha_nac.toPython()
        
        # Calcular edad y tipo de pasajero
        tipo_codigo, tipo_desc, porcentaje_desc, edad = self.controlador.calcular_tipo_pasajero(fecha_python)
        
        return {
            'nombre': nombre,
            'apellido_paterno': apellido_pat,
            'apellido_materno': apellido_mat if apellido_mat else None,
            'fecha_nacimiento': fecha_python,
            'edad': edad,
            'correo': correo if correo else None,
            'telefono': telefono,
            'asiento_clave': self.asientos_seleccionados[self.pasajero_actual],
            'tipo_codigo': tipo_codigo,
            'tipo_descripcion': tipo_desc,
            'porcentaje_descuento': porcentaje_desc
        }
    
    def limpiar_formulario(self):
        """Limpia los campos del formulario."""
        self.ui.lineEdit_ingresarNombre.clear()
        self.ui.lineEdit_ingresarPrimerApellido.clear()
        self.ui.lineEdit_ingresarSegundoApellido.clear()
        self.ui.dateEdit_fechaNacimientoPasajero.setDate(QDate.currentDate().addYears(-18))
        self.ui.lineEdit_ingresarCorreo.clear()
        self.ui.lineEdit_ingresarTelefono.clear()
    
    def on_continuar_clicked(self):
        """Cuando se presiona continuar."""
        # Validar datos
        datos_pasajero = self.validar_datos()
        
        if datos_pasajero is None:
            return
        
        # Guardar datos del pasajero
        self.pasajeros_data.append(datos_pasajero)
        
        # Verificar si hay más pasajeros
        self.pasajero_actual += 1
        
        if self.pasajero_actual < len(self.asientos_seleccionados):
            # Hay más pasajeros, limpiar formulario y continuar
            self.limpiar_formulario()
            self.actualizar_titulo()
        else:
            # Ya se capturaron todos los pasajeros, validar reglas y procesar compra
            self.validar_y_procesar_compra()
    
    def validar_y_procesar_compra(self):
        """Valida las reglas de negocio y procesa la compra."""
        # VALIDACIÓN: Debe haber al menos un adulto
        adultos = [p for p in self.pasajeros_data if p['edad'] > 12]
        
        if not adultos:
            QMessageBox.critical(self, "Error de validación", 
                               "Debe haber al menos un adulto (mayor de 12 años) en la reservación.\n"
                               "Los niños no pueden viajar solos.")
            
            # Reiniciar proceso
            self.pasajeros_data.clear()
            self.pasajero_actual = 0
            self.limpiar_formulario()
            self.actualizar_titulo()
            return
        
        # Preparar datos para la compra
        datos_compra = {
            'numero_corrida': self.corrida_info['numero_corrida'],
            'tarifa_base': self.corrida_info['precio'],
            'fecha_corrida': self.corrida_info['fecha'],
            'pasajeros': self.pasajeros_data
        }
        
        # Obtener usuario logueado (si existe)
        usuario_actual = self.app_manager.get_usuario_actual()
        usuario_id = usuario_actual.id if usuario_actual else None
        
        # Procesar compra
        resultado = self.controlador.procesar_compra(datos_compra, usuario_id)
        
        if resultado['exito']:
            # Mostrar boletos
            from vista.compartido.mostrarBoletosDialog import MostrarBoletosDialog
            
            dialog = MostrarBoletosDialog(
                self.app_manager,
                resultado['numero_reservacion'],
                self
            )
            
            dialog.exec()
            
            # Cerrar todos los diálogos y regresar al index
            self.done(self.COMPRA_EXITOSA)
        else:
            QMessageBox.critical(self, "Error en la compra", resultado['mensaje'])
    
    def on_regresar_clicked(self):
        """Cuando se presiona regresar."""
        if self.pasajero_actual > 0:
            # Retroceder al pasajero anterior
            self.pasajero_actual -= 1
            self.pasajeros_data.pop()  # Eliminar el último pasajero guardado
            
            # Cargar datos del pasajero anterior
            if self.pasajeros_data:
                pasajero_anterior = self.pasajeros_data[-1]
                self.ui.lineEdit_ingresarNombre.setText(pasajero_anterior['nombre'])
                self.ui.lineEdit_ingresarPrimerApellido.setText(pasajero_anterior['apellido_paterno'])
                self.ui.lineEdit_ingresarSegundoApellido.setText(pasajero_anterior['apellido_materno'] or '')
                
                fecha_qdate = QDate(
                    pasajero_anterior['fecha_nacimiento'].year,
                    pasajero_anterior['fecha_nacimiento'].month,
                    pasajero_anterior['fecha_nacimiento'].day
                )
                self.ui.dateEdit_fechaNacimientoPasajero.setDate(fecha_qdate)
                
                self.ui.lineEdit_ingresarCorreo.setText(pasajero_anterior['correo'] or '')
                self.ui.lineEdit_ingresarTelefono.setText(pasajero_anterior['telefono'])
                
                self.pasajeros_data.pop()  # Eliminar para volver a capturar
            
            self.actualizar_titulo()
        else:
            # Regresar al diálogo anterior (selección de asientos)
            self.reject()