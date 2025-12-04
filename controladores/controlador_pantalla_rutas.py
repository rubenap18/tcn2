import re 
from PySide6.QtWidgets import QMessageBox 
from dao.ruta_dao import RutaDAO
from dao.ciudad_dao import CiudadesDAO
from objetos.Ruta import Ruta 

class ControladorPantallaRutas:
    def __init__(self, ruta_dao, ciudad_dao):
        self.ruta_dao = ruta_dao
        self.ciudad_dao = ciudad_dao

    def obtener_todas_las_rutas(self):
        try:
            return self.ruta_dao.obtener_todas()
        except Exception as e:
            print(f"Error en controlador al obtener rutas: {e}")
            return [] 

    def obtener_ciudades_map(self):
        try:
            ciudades = self.ciudad_dao.obtener_todas()
            ciudades_map = {ciudad.get_nombre(): ciudad.get_codigo() for ciudad in ciudades}
            return ciudades_map
        except Exception as e:
            print(f"Error en controlador al obtener ciudades: {e}")
            return {} 

    def agregar_nueva_ruta(self, parent, codigo_origen, codigo_destino, distancia_str):
        errores = []

        if not codigo_origen:
            errores.append("El origen es un campo obligatorio.")
        if not codigo_destino:
            errores.append("El destino es un campo obligatorio.")
        if not distancia_str:
            errores.append("La distancia es un campo obligatorio.")

        if codigo_origen and codigo_destino and codigo_origen == codigo_destino:
            errores.append("El origen y el destino no pueden ser la misma ciudad.")

        distancia_float = 0.0
        if distancia_str:
            try:
                distancia_float = float(distancia_str)
                if distancia_float <= 0:
                    errores.append("La distancia debe ser mayor a 0.")
                if distancia_float > 1500: # Removed direct return, added to errores
                    errores.append("La distancia no puede ser mayor a 1500.")
            except ValueError:
                errores.append("La distancia debe ser un número válido.")
        
        if errores:
            mensaje = "Por favor, corrige los siguientes errores:\n\n" + "\n".join(errores)
            QMessageBox.warning(parent, "Errores de Validación", mensaje)
            return False
        
        try:
            resultado = self.ruta_dao.insertar(codigo_origen, codigo_destino, distancia_float)
            
            if resultado == "duplicado":
                QMessageBox.warning(parent, "Error de Inserción", "Ya existe una ruta con el mismo origen y destino.")
                return False
            elif resultado is False: 
                QMessageBox.critical(parent, "Error", "No se pudo agregar la ruta. Verifique los datos.")
                return False
            return True 
        except Exception as e:
            print(f"Error en controlador al agregar ruta: {e}")
            QMessageBox.critical(parent, "Error", f"Error interno al agregar la ruta: {e}")
            return False

    def actualizar_distancia_ruta(self, parent, codigo_ruta, distancia_str):
        errores = []

        if not codigo_ruta:
            errores.append("El código de la ruta es obligatorio para actualizar.")
        if not distancia_str:
            errores.append("La distancia es un campo obligatorio.")
        
        distancia_float = 0.0
        if distancia_str:
            try:
                distancia_float = float(distancia_str)
                if distancia_float <= 0:
                    errores.append("La distancia debe ser mayor a 0.")
                if distancia_float > 1500: # Removed direct return, added to errores
                    errores.append("La distancia no puede ser mayor a 1500.")
            except ValueError:
                errores.append("La distancia debe ser un número válido.")

        if errores:
            mensaje = "Por favor, corrige los siguientes errores:\n\n" + "\n".join(errores)
            QMessageBox.warning(parent, "Errores de Validación", mensaje)
            return False

        try:
            resultado = self.ruta_dao.actualizar_distancia(codigo_ruta, distancia_float)
            if resultado is False: 
                QMessageBox.warning(parent, "Error de Actualización", "No se pudo actualizar la ruta. Verifique el código.")
                return False
            return True 
        except Exception as e:
            print(f"Error en controlador al actualizar distancia: {e}")
            QMessageBox.critical(parent, "Error", f"Error interno al actualizar la ruta: {e}")
            return False


