from dao.marca_modelo_dao import MarcaModeloDAO
import mysql.connector
from mysql.connector import Error
from dao.conn import Connection
from objetos.autobus import Autobus
class AutobusDAO:
    def __init__(self):
        self._conexion = Connection.getConnection()
        self._marca_modelo_dao = MarcaModeloDAO()
    
    def obtener_autobuses_activos(self, filtro_servicio="TODOS"):
        """
        Obtiene autobuses activos, filtrados por servicio si es necesario
        Retorna: Lista de objetos Autobus
        """
        cursor = self._conexion.cursor(dictionary=True)
        try:
            query = """
            SELECT a.numero, a.matricula, a.claveWIFI, a.cantAsientos, 
                   ta.descripcion as tipoAutobus, ma.nombre as marca, 
                   mo.nombre as modelo, ea.descripcion as estado
            FROM autobus a
            JOIN tipo_autobus ta ON a.tipoAutobus = ta.codigo
            JOIN marca ma ON a.marca = ma.clave
            JOIN modelo mo ON a.modelo = mo.clave
            JOIN edo_autobus ea ON a.estado = ea.codigo
            WHERE ea.descripcion = 'ACTIVO'
            """
            
            params = []
            if filtro_servicio != "TODOS":
                query += " AND ta.descripcion = %s"
                params.append(filtro_servicio)
            
            query += " ORDER BY a.numero"
            
            cursor.execute(query, params)
            resultados = cursor.fetchall()
            
            autobuses = []
            for row in resultados:
                autobus = Autobus()
                autobus.set_numero(row['numero'])
                autobus.set_matricula(row['matricula'])
                autobus.set_claveWIFI(row['claveWIFI'])
                autobus.set_cantAsientos(row['cantAsientos'])
                autobus.set_tipoAutobus(row['tipoAutobus'])
                autobus.set_marca(row['marca'])
                autobus.set_modelo(row['modelo'])
                autobus.set_estado(row['estado'])
                autobuses.append(autobus)
            
            return autobuses
            
        finally:
            cursor.close()
    
    def obtener_autobuses_activos_para_baja(self):
        """Obtiene solo número y matrícula de autobuses activos para combobox"""
        cursor = self._conexion.cursor(dictionary=True)
        try:
            query = """
            SELECT a.numero, a.matricula
            FROM autobus a
            JOIN edo_autobus ea ON a.estado = ea.codigo
            WHERE ea.descripcion = 'ACTIVO'
            ORDER BY a.numero
            """
            cursor.execute(query)
            return cursor.fetchall()
        finally:
            cursor.close()
    
    def obtener_datos_autobus(self, numero_autobus):
        """Obtiene todos los datos de un autobús específico"""
        cursor = self._conexion.cursor(dictionary=True)
        try:
            query = """
            SELECT a.numero, a.matricula, a.claveWIFI, a.cantAsientos, 
                   ta.descripcion as tipoAutobus, ma.nombre as marca, 
                   mo.nombre as modelo, ea.descripcion as estado
            FROM autobus a
            JOIN tipo_autobus ta ON a.tipoAutobus = ta.codigo
            JOIN marca ma ON a.marca = ma.clave
            JOIN modelo mo ON a.modelo = mo.clave
            JOIN edo_autobus ea ON a.estado = ea.codigo
            WHERE a.numero = %s
            """
            cursor.execute(query, (numero_autobus,))
            resultado = cursor.fetchone()
            
            if resultado:
                autobus = Autobus()
                autobus.set_numero(resultado['numero'])
                autobus.set_matricula(resultado['matricula'])
                autobus.set_claveWIFI(resultado['claveWIFI'])
                autobus.set_cantAsientos(resultado['cantAsientos'])
                autobus.set_tipoAutobus(resultado['tipoAutobus'])
                autobus.set_marca(resultado['marca'])
                autobus.set_modelo(resultado['modelo'])
                autobus.set_estado(resultado['estado'])
                return autobus
            return None
            
        finally:
            cursor.close()
    
    def existe_matricula(self, matricula):
        """Verifica si una matrícula ya existe en la BD"""
        cursor = self._conexion.cursor()
        try:
            query = "SELECT COUNT(*) FROM autobus WHERE matricula = %s"
            cursor.execute(query, (matricula,))
            count = cursor.fetchone()[0]
            return count > 0
        finally:
            cursor.close()
    
    def existe_numero(self, numero):
        """Verifica si un número de autobús ya existe"""
        cursor = self._conexion.cursor()
        try:
            query = "SELECT COUNT(*) FROM autobus WHERE numero = %s"
            cursor.execute(query, (numero,))
            count = cursor.fetchone()[0]
            return count > 0
        finally:
            cursor.close()
    
    def registrar_autobus(self, autobus):
        """
        Registra un nuevo autobús en la BD
        Retorna: True si se registró correctamente
        """
        cursor = self._conexion.cursor()
        try:
            # Obtener códigos necesarios
            tipo_codigo = self._obtener_codigo_tipo(autobus.get_tipoAutobus())
            estado_codigo = "ACTI"  
            marca_codigo = self._marca_modelo_dao.obtener_codigo_marca_por_nombre(autobus.get_marca())
            modelo_codigo = self._marca_modelo_dao.obtener_codigo_modelo_por_nombre(
                autobus.get_modelo(), marca_codigo
            )
            
            if not all([tipo_codigo, estado_codigo, marca_codigo, modelo_codigo]):
                raise ValueError("No se pudieron obtener todos los códigos necesarios")
            
            # Determinar cantidad de asientos según tipo
            if autobus.get_tipoAutobus() == "PLUS":
                cant_asientos = 44
            elif autobus.get_tipoAutobus() == "PLATINO":
                cant_asientos = 34
            else:
                raise ValueError(f"Tipo de autobús no válido: {autobus.get_tipoAutobus()}")
            
            query = """
            INSERT INTO autobus (numero, matricula, claveWIFI, cantAsientos, 
                                tipoAutobus, estado, marca, modelo)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            
            cursor.execute(query, (
                autobus.get_numero(),
                autobus.get_matricula(),
                autobus.get_claveWIFI(),
                cant_asientos,
                tipo_codigo,
                estado_codigo,
                marca_codigo,
                modelo_codigo
            ))
            
            self._conexion.commit()
            return True
            
        except Exception as e:
            self._conexion.rollback()
            raise e
        finally:
            cursor.close()
    
    def dar_baja_autobus(self, numero_autobus):
        """
        Cambia el estado del autobús a INACTIVO
        Retorna: True si se actualizó correctamente
        """
        cursor = self._conexion.cursor()
        try:
            # Asumiendo que 'INA' es el código para INACTIVO
            query = "UPDATE autobus SET estado = 'INAC' WHERE numero = %s"
            cursor.execute(query, (numero_autobus,))
            self._conexion.commit()
            return cursor.rowcount > 0
        except Exception as e:
            self._conexion.rollback()
            raise e
        finally:
            cursor.close()
    
    def _obtener_codigo_tipo(self, tipo_descripcion):
        """Obtiene el código del tipo de autobús"""
        cursor = self._conexion.cursor()
        try:
            query = "SELECT codigo FROM tipo_autobus WHERE descripcion = %s"
            cursor.execute(query, (tipo_descripcion,))
            result = cursor.fetchone()
            return result[0] if result else None
        finally:
            cursor.close()

    def tiene_corridas_futuras(self, numero_autobus):
        """
        Verifica si el autobús tiene corridas asignadas para hoy o fechas futuras
        con estado ACTIVO.
        Retorna: True si tiene corridas, False si no
        """
        cursor = self._conexion.cursor()
        try:
            query = """
            SELECT COUNT(*) 
            FROM corrida c
            JOIN edo_corrida ec ON c.estado = ec.codigo
            WHERE c.autobus = %s 
            AND c.fecha >= CURDATE()  -- Fechas de hoy en adelante
            AND ec.descripcion = 'ACTIVO'  -- Solo corridas ACTIVAS
            """
            cursor.execute(query, (numero_autobus,))
            count = cursor.fetchone()[0]
            return count > 0
        finally:
            cursor.close()

    def obtener_corridas_futuras(self, numero_autobus):
        """
        Obtiene las corridas futuras asignadas al autobús
        Retorna: Lista de diccionarios con información básica
        """
        cursor = self._conexion.cursor(dictionary=True)
        try:
            query = """
            SELECT c.numero, c.fecha, c.hora_salida, c.hora_llegada, r.codigo as ruta
            FROM corrida c
            JOIN ruta r ON c.ruta = r.codigo
            JOIN edo_corrida ec ON c.estado = ec.codigo
            WHERE c.autobus = %s 
            AND c.fecha >= CURDATE()
            AND ec.descripcion = 'ACTIVO'
            ORDER BY c.fecha, c.hora_salida
            LIMIT 5  -- Limitar a 5 corridas para no saturar el mensaje
            """
            cursor.execute(query, (numero_autobus,))
            return cursor.fetchall()
        finally:
            cursor.close()

    # REEMPLAZA el método dar_baja_autobus existente con este:
    def dar_baja_autobus(self, numero_autobus):
        """
        Cambia el estado del autobús a INACTIVO
        Retorna: (exito, mensaje_error)
        """
        cursor = self._conexion.cursor()
        try:
            # 1. Verificar si tiene corridas futuras
            if self.tiene_corridas_futuras(numero_autobus):
                return (False, "Tiene corridas asignadas.")
            
            # 2. Dar de baja
            query = "UPDATE autobus SET estado = 'INAC' WHERE numero = %s"
            cursor.execute(query, (numero_autobus,))
            self._conexion.commit()
            
            return (True, None)
            
        except Exception as e:
            self._conexion.rollback()
            return (False, f"Error al dar de baja autobús: {str(e)}")
        finally:
            cursor.close()
    
    
    
    
    
    
    def listar_autobuses(self):
        autobuses = []
        conexion = None
        cursor = None
        try:
            conexion = Connection.getConnection()
            cursor = conexion.cursor()
            query = """
                SELECT
                    a.numero,
                    a.matricula,
                    a.claveWIFI,
                    a.cantAsientos,
                    a.tipoAutobus,
                    m.clave,
                    mo.clave,
                    a.estado
                FROM
                    autobus as a
                INNER JOIN marca AS m ON a.marca = m.clave
                INNER JOIN modelo AS mo ON a.modelo = mo.clave
            """
            # a.marca AS marca_clave,
                    # a.modelo AS modelo_clave,
                    # m.nombre AS marca_nombre,
                    # mo.nombre AS modelo_nombre
            cursor.execute(query)
            resultados = cursor.fetchall()

            for fila in resultados:
                autobus = Autobus(
                    fila[0], fila[1], fila[2], fila[3], fila[4], # numero, matricula, cantAsientos, tipoAutobus, estado
                    fila[5], fila[6], # marca_clave, modelo_clave
                    fila[7]  # marca_nombre, modelo_nombre
                )
                autobuses.append(autobus)
                print(f"DEBUG DAO: Autobús cargado: {autobus}") # Re-added Debug print

        except Error as e:
            print(f"Error al listar autobuses: {e}")
        finally:
            if cursor:
                cursor.close()
            # Not closing the connection here because it's a Singleton
            # and should be managed by the main application flow.
            # Connection.closeConnection()
        return autobuses
