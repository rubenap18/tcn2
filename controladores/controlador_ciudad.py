from dao.ciudad_dao import CiudadesDAO
from objetos.ciudad import Ciudad

class ControladorCiudad:
    def __init__(self):
        self.ciudades_dao = CiudadesDAO()

    def obtener_todas_las_ciudades(self):
        """
        Obtiene todas las ciudades de la base de datos.
        """
        try:
            return self.ciudades_dao.obtener_todas()
        except Exception as e:
            print(f"Error en controlador al obtener ciudades: {e}")
            return []

    def agregar_nueva_ciudad(self, codigo, nombre):
        """
        Intenta agregar una nueva ciudad.
        Devuelve True, "duplicado", "codigo_invalido", o un string de error.
        """
        if not codigo or not nombre:
            return "El código y el nombre son obligatorios."
        
        try:
            ciudad = Ciudad(codigo=codigo, nombre=nombre)
            resultado = self.ciudades_dao.insertar(ciudad)
            return resultado
        except Exception as e:
            print(f"Error en controlador al agregar ciudad: {e}")
            return "No se pudo agregar la ciudad por un error interno."

    def actualizar_ciudad(self, codigo_actual, nuevo_codigo, nuevo_nombre):
        """
        Intenta actualizar una ciudad existente.
        """
        if not nuevo_codigo or not nuevo_nombre:
            return "El nuevo código y nombre son obligatorios."

        try:
            return self.ciudades_dao.actualizar(codigo_actual, nuevo_codigo, nuevo_nombre)
        except Exception as e:
            print(f"Error en controlador al actualizar ciudad: {e}")
            return False

    def buscar_ciudades_por_nombre(self, nombre):
        """
        Busca ciudades que coincidan con un nombre.
        """
        try:
            return self.ciudades_dao.buscar_por_nombre(nombre)
        except Exception as e:
            print(f"Error en controlador al buscar ciudades: {e}")
            return []
    
    def eliminar_ciudad(self, codigo):
        """
        Intenta eliminar una ciudad.
        """
        try:
            return self.ciudades_dao.eliminar(codigo)
        except Exception as e:
            print(f"Error en controlador al eliminar ciudad: {e}")
            return False

