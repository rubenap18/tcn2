import re
from PySide6.QtWidgets import QMessageBox # Importar QMessageBox
from dao.ciudad_dao import CiudadesDAO
from objetos.ciudad import Ciudad

class ControladorPantallaCiudad:
    NOMBRE_REGEX = re.compile(r"^[A-Za-zñÑáéíóúÁÉÍÓÚ]+(?:[ ][A-Za-zñÑáéíóúÁÉÍÓÚ]+)*$")
    
    def __init__(self, ciudad_dao):
        self.ciudad_dao = ciudad_dao

    def obtener_todas_las_ciudades(self):
        """
        Obtiene todas las ciudades de la base de datos.
        Devuelve una lista de objetos Ciudad.
        """
        try:
            return self.ciudad_dao.obtener_todas()
        except Exception as e:
            print(f"Error en controlador al obtener ciudades: {e}")
            return [] # Devolver lista vacía en lugar de False

    def insertar_ciudad(self, parent, codigo, nombre):
        """
        Inserta una nueva ciudad en la base de datos.
        Devuelve True si tiene éxito, o False si hay errores de validación o inserción.
        """
        errores = []

        if not codigo:
            errores.append("El código es un campo obligatorio.")
        elif len(codigo) != 3:
            errores.append("El código de la ciudad debe tener 3 caracteres.")
        
        if not nombre:
            errores.append("El nombre es un campo obligatorio.")
        elif not self.NOMBRE_REGEX.fullmatch(nombre):
            errores.append("El nombre de la ciudad solo debe contener letras y un espacio entre palabras (sin espacios al inicio o final).")

        if errores:
            mensaje = "Por favor, corrige los siguientes errores:\n\n" + "\n".join(errores)
            QMessageBox.warning(parent, "Errores de Validación", mensaje)
            return False

        ciudad = Ciudad(codigo.upper(), nombre.capitalize())
        try:
            resultado = self.ciudad_dao.insertar(ciudad)
            if resultado == "duplicado":
                QMessageBox.warning(parent, "Error de Inserción", "Ya existe una ciudad con ese código o nombre.")
                return False
            return True # Si la inserción fue exitosa
        except Exception as e:
            print(f"Error en controlador al insertar ciudad: {e}")
            QMessageBox.critical(parent, "Error", f"Error interno al insertar la ciudad: {e}")
            return False

    def actualizar_ciudad(self, parent, codigo_actual, nuevo_codigo, nuevo_nombre):
        """
        Actualiza una ciudad existente.
        Devuelve True si tiene éxito, o False si hay errores de validación o actualización.
        """
        errores = []

        if not codigo_actual:
            errores.append("El código actual de la ciudad es obligatorio para actualizar.")
        
        if not nuevo_codigo:
            errores.append("El nuevo código es un campo obligatorio.")
        elif len(nuevo_codigo) != 3:
            errores.append("El nuevo código de la ciudad debe tener 3 caracteres.")

        if not nuevo_nombre:
            errores.append("El nuevo nombre es un campo obligatorio.")
        elif not self.NOMBRE_REGEX.fullmatch(nuevo_nombre):
            errores.append("El nuevo nombre de la ciudad solo debe contener letras y un espacio entre palabras (sin espacios al inicio o final).")

        if errores:
            mensaje = "Por favor, corrige los siguientes errores:\n\n" + "\n".join(errores)
            QMessageBox.warning(parent, "Errores de Validación", mensaje)
            return False

        try:
            resultado = self.ciudad_dao.actualizar(codigo_actual, nuevo_codigo.upper(), nuevo_nombre.capitalize())
            if resultado == "duplicado":
                QMessageBox.warning(parent, "Error de Actualización", "Ya existe una ciudad con el nuevo código.")
                return False
            elif resultado is False: # Asumiendo que False significa que no se encontró la ciudad a actualizar
                QMessageBox.warning(parent, "Error de Actualización", "No se pudo actualizar la ciudad. Verifique el código actual.")
                return False
            return True # Si la actualización fue exitosa
        except Exception as e:
            print(f"Error en controlador al actualizar ciudad: {e}")
            QMessageBox.critical(parent, "Error", f"Error interno al actualizar la ciudad: {e}")
            return False

    def eliminar_ciudad(self, codigo):
        """
        Elimina una ciudad de la base de datos.
        Devuelve True si tiene éxito, o un mensaje de error.
        """
        if not codigo:
            QMessageBox.warning(None, "Advertencia", "El código de la ciudad es obligatorio para eliminar.") # Asumiendo None como parent si no hay contexto
            return False
        try:
            resultado = self.ciudad_dao.eliminar(codigo)
            if resultado is False:
                QMessageBox.warning(None, "Advertencia", "No se pudo eliminar la ciudad. Verifique el código.") # Asumiendo None como parent
                return False
            return True
        except Exception as e:
            print(f"Error en controlador al eliminar ciudad: {e}")
            QMessageBox.critical(None, "Error", f"Error interno al eliminar la ciudad: {e}") # Asumiendo None como parent
            return False

    def buscar_ciudades(self, nombre):
        """
        Busca ciudades por nombre.
        Devuelve una lista de objetos Ciudad.
        """
        try:
            return self.ciudad_dao.buscar_por_nombre(nombre)
        except Exception as e:
            print(f"Error en controlador al buscar ciudades: {e}")
            return []