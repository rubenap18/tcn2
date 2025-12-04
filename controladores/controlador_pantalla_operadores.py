# controladores/controlador_pantalla_operadores.py

import re
from datetime import datetime # Importar datetime
from PySide6.QtWidgets import QMessageBox
from dao.operador_dao import OperadorDAO
from objetos.Operador import Operador # Importar la clase Operador

class ControladorPantallaOperadores:
    NOMBRE_REGEX = re.compile(r"^[A-Za-zñÑáéíóúÁÉÍÓÚ]+(?:[ ][A-Za-zñÑáéíóúÁÉÍÓÚ]+)*$")
    
    def __init__(self, operador_dao):
        self.operador_dao = operador_dao

    def _validar_campos_operador(self, parent, nombre, apellPat, apellMat, telefono, fechaNac, fechaContrato):
        errores = []

        if not nombre:
            errores.append("El nombre es un campo obligatorio.")
        elif not self.NOMBRE_REGEX.fullmatch(nombre):
            errores.append("El nombre solo debe contener letras y un espacio entre palabras (sin espacios al inicio o final).")

        if not apellPat:
            errores.append("El apellido paterno es un campo obligatorio.")
        elif not self.NOMBRE_REGEX.fullmatch(apellPat):
            errores.append("El apellido paterno solo debe contener letras y un espacio entre palabras (sin espacios al inicio o final).")
            
        if not apellMat:
            errores.append("El apellido materno es un campo obligatorio.")
        elif not self.NOMBRE_REGEX.fullmatch(apellMat):
            errores.append("El apellido materno solo debe contener letras y un espacio entre palabras (sin espacios al inicio o final).")

        if not telefono:
            errores.append("El teléfono es un campo obligatorio.")
        elif not telefono.isdigit() or len(telefono) != 10:
            errores.append("El número de teléfono debe tener exactamente 10 dígitos y ser solo numérico.")

        if not fechaNac:
            errores.append("La fecha de nacimiento es obligatoria.")
        if not fechaContrato:
            errores.append("La fecha de contrato es obligatoria.")

        if errores:
            mensaje = "Por favor, corrige los siguientes errores:\n\n" + "\n".join(errores)
            QMessageBox.warning(parent, "Errores de Validación", mensaje)
            return False
        return True

    def obtener_todos(self):
        """
        Obtiene todos los operadores de la base de datos a través del DAO.
        """
        try:
            return self.operador_dao.obtener_todos()
        except Exception as e:
            print(f"Error en ControladorPantallaOperadores.obtener_todos: {e}")
            return []

    def insertar_operador(self, parent, nombre, apellPat, apellMat, fechaNac_str, telefono, fechaContrato_str):
        """
        Intenta insertar un nuevo operador.
        """
        if not self._validar_campos_operador(parent, nombre, apellPat, apellMat, telefono, fechaNac_str, fechaContrato_str):
            return False
        try:
            # Convertir las cadenas de fecha a objetos date
            fechaNac_obj = datetime.strptime(fechaNac_str, "%Y-%m-%d").date()
            fechaContrato_obj = datetime.strptime(fechaContrato_str, "%Y-%m-%d").date()

            # Crear el objeto Operador (el numero se asume autoincremental en la BD, por lo que lo pasamos como None)
            operador_obj = Operador(None, nombre, apellPat, apellMat, fechaNac_obj, telefono, fechaContrato_obj)
            
            return self.operador_dao.insertar(operador_obj)
        except Exception as e:
            print(f"Error en ControladorPantallaOperadores.insertar_operador: {e}")
            QMessageBox.critical(parent, "Error", f"Error al insertar operador: {e}")
            return False

    def actualizar_operador(self, parent, numero, nombre, apellPat, apellMat, fechaNac_str, telefono, fechaContrato_str):
        """
        Intenta actualizar un operador existente.
        """
        if not self._validar_campos_operador(parent, nombre, apellPat, apellMat, telefono, fechaNac_str, fechaContrato_str):
            return False
        try:
            # Convertir las cadenas de fecha a objetos date
            fechaNac_obj = datetime.strptime(fechaNac_str, "%Y-%m-%d").date()
            fechaContrato_obj = datetime.strptime(fechaContrato_str, "%Y-%m-%d").date()

            # Crear el objeto Operador con el número existente
            operador_obj = Operador(numero, nombre, apellPat, apellMat, fechaNac_obj, telefono, fechaContrato_obj)
            
            return self.operador_dao.actualizar(operador_obj)
        except Exception as e:
            print(f"Error en ControladorPantallaOperadores.actualizar_operador: {e}")
            QMessageBox.critical(parent, "Error", f"Error al actualizar operador: {e}")
            return False

    def buscar_operadores(self, criterio):
        """
        Busca operadores por un criterio dado a través del DAO.
        """
        try:
            return self.operador_dao.buscar(criterio)
        except Exception as e:
            print(f"Error en ControladorPantallaOperadores.buscar_operadores: {e}")
            return []