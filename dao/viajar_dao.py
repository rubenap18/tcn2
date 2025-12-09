from dao.conn import Connection
from mysql.connector import Error
from datetime import datetime, date

class ViajarDAO:
   
    
    def __init__(self):
        pass
    
    #BÚSQUEDA DE CORRIDAS
    def obtener_corridas_disponibles(self, ciudad_origen, ciudad_destino, fecha, num_pasajeros):
        
        
        corridas = []
        conn = None
        cursor = None
        
        try:
            conn = Connection.getConnection()
            if not conn or not conn.is_connected():
                raise Error('No se puede establecer conexión con la BD')
            
            cursor = conn.cursor(dictionary=True)
            
            query = """
                SELECT 
                    c.numero AS numero_corrida,
                    c.fecha,
                    c.hora_salida,
                    c.hora_llegada,
                    c.tarifaBase AS precio,
                    c.lugaresDisp AS lugares_disponibles,
                    c.autobus AS numero_autobus,
                    c.ruta AS codigo_ruta,
                    origen.nombre AS ciudad_origen,
                    destino.nombre AS ciudad_destino,
                    a.tipoAutobus AS tipo_servicio,
                    ta.descripcion AS descripcion_servicio
                FROM corrida c
                INNER JOIN ruta r ON c.ruta = r.codigo
                INNER JOIN ciudad origen ON r.ciudadOrigen = origen.codigo
                INNER JOIN ciudad destino ON r.ciudadDestino = destino.codigo
                INNER JOIN autobus a ON c.autobus = a.numero
                INNER JOIN tipo_autobus ta ON a.tipoAutobus = ta.codigo
                WHERE origen.nombre = %s
                    AND destino.nombre = %s
                    AND c.fecha = %s
                    AND c.lugaresDisp >= %s
                    AND c.estado = 'ACT'
                ORDER BY c.hora_salida
            """
            
            cursor.execute(query, (ciudad_origen, ciudad_destino, fecha, num_pasajeros))
            corridas = cursor.fetchall()
            
        except Error as e:
            print(f'Error en ViajarDAO.obtener_corridas_disponibles: {e}')
            raise e
        finally:
            if cursor:
                cursor.close()
        
        return corridas
    
    def obtener_ciudades_origen(self):
        
        ciudades = []
        conn = None
        cursor = None
        
        try:
            conn = Connection.getConnection()
            cursor = conn.cursor(dictionary=True)
            
            query = """
                SELECT DISTINCT c.codigo, c.nombre
                FROM ciudad c
                INNER JOIN ruta r ON c.codigo = r.ciudadOrigen
                ORDER BY c.nombre
            """
            
            cursor.execute(query)
            ciudades = cursor.fetchall()
            
        except Error as e:
            print(f'Error en ViajarDAO.obtener_ciudades_origen: {e}')
            raise e
        finally:
            if cursor:
                cursor.close()
        
        return ciudades
    
    def obtener_ciudades_destino(self, ciudad_origen):
        
        ciudades = []
        conn = None
        cursor = None
        
        try:
            conn = Connection.getConnection()
            cursor = conn.cursor(dictionary=True)
            
            query = """
                SELECT DISTINCT c.codigo, c.nombre
                FROM ciudad c
                INNER JOIN ruta r ON c.codigo = r.ciudadDestino
                WHERE r.ciudadOrigen = (SELECT codigo FROM ciudad WHERE nombre = %s)
                ORDER BY c.nombre
            """
            
            cursor.execute(query, (ciudad_origen,))
            ciudades = cursor.fetchall()
            
        except Error as e:
            print(f'Error en ViajarDAO.obtener_ciudades_destino: {e}')
            raise e
        finally:
            if cursor:
                cursor.close()
        
        return ciudades
    
    def obtener_fechas_disponibles(self, ciudad_origen, ciudad_destino):
        
        fechas = []
        conn = None
        cursor = None
        
        try:
            conn = Connection.getConnection()
            cursor = conn.cursor()
            
            query = """
                SELECT DISTINCT c.fecha
                FROM corrida c
                INNER JOIN ruta r ON c.ruta = r.codigo
                INNER JOIN ciudad origen ON r.ciudadOrigen = origen.codigo
                INNER JOIN ciudad destino ON r.ciudadDestino = destino.codigo
                WHERE origen.nombre = %s
                    AND destino.nombre = %s
                    AND c.fecha >= CURDATE()
                    AND c.estado = 'ACT'
                ORDER BY c.fecha
            """
            
            cursor.execute(query, (ciudad_origen, ciudad_destino))
            resultados = cursor.fetchall()
            fechas = [row[0] for row in resultados]
            
        except Error as e:
            print(f'Error en ViajarDAO.obtener_fechas_disponibles: {e}')
            raise e
        finally:
            if cursor:
                cursor.close()
        
        return fechas
    
    # ASIENTOS 
    
    def obtener_asientos_disponibles(self, numero_corrida):
        
        asientos = []
        conn = None
        cursor = None
        
        try:
            conn = Connection.getConnection()
            cursor = conn.cursor(dictionary=True)
            
            query = """
                SELECT 
                    a.clave,
                    a.numero,
                    a.ubicacion,
                    ca.estado
                FROM asiento a
                INNER JOIN corrida_asiento ca ON a.clave = ca.asiento
                WHERE ca.corrida = %s
                ORDER BY a.numero
            """
            
            cursor.execute(query, (numero_corrida,))
            asientos = cursor.fetchall()
            
        except Error as e:
            print(f'Error en ViajarDAO.obtener_asientos_disponibles: {e}')
            raise e
        finally:
            if cursor:
                cursor.close()
        
        return asientos
    
    def validar_asientos_disponibles(self, numero_corrida, asientos_seleccionados):
        
        conn = None
        cursor = None
        
        try:
            conn = Connection.getConnection()
            cursor = conn.cursor()
            
            placeholders = ','.join(['%s'] * len(asientos_seleccionados))
            query = f"""
                SELECT COUNT(*) 
                FROM corrida_asiento
                WHERE corrida = %s 
                    AND asiento IN ({placeholders})
                    AND estado = 'DISPONIBLE'
            """
            
            params = [numero_corrida] + asientos_seleccionados
            cursor.execute(query, tuple(params))
            count = cursor.fetchone()[0]
            
            return count == len(asientos_seleccionados)
            
        except Error as e:
            print(f'Error en ViajarDAO.validar_asientos_disponibles: {e}')
            return False
        finally:
            if cursor:
                cursor.close()
    
    #  CÁLCULO DE PRECIOS 
    
    def calcular_tipo_pasajero(self, fecha_nacimiento):
        
        try:
            # Convertir string a date si es necesario
            if isinstance(fecha_nacimiento, str):
                fecha_nac = datetime.strptime(fecha_nacimiento, '%Y-%m-%d').date()
            else:
                fecha_nac = fecha_nacimiento
            
            # Calcular edad
            hoy = date.today()
            edad = hoy.year - fecha_nac.year - ((hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day))
            
            # Determinar tipo según edad
            if edad <= 12:
                return ('NINO', 'Niño', 50, edad)
            elif edad >= 62:
                return ('ADUL', '3ra Edad', 50, edad)
            else:
                return ('REGU', 'Regular', 0, edad)
                
        except Exception as e:
            print(f'Error en calcular_tipo_pasajero: {e}')
            return ('REGU', 'Regular', 0, 0)
    
    def calcular_precio_boleto(self, tarifa_base, porcentaje_descuento):
       
        descuento = (tarifa_base * porcentaje_descuento) / 100
        precio_final = tarifa_base - descuento
        return (precio_final, descuento)
    
    #  PROCESO DE COMPRA COMPLETO 
    
    def procesar_compra_boletos(self, datos_compra, usuario_id=None):
       
        conn = None
        cursor = None
        
        try:
            conn = Connection.getConnection()
            if not conn or not conn.is_connected():
                return {'exito': False, 'mensaje': 'No se puede conectar con la BD'}
            
            cursor = conn.cursor()
            
            # Asegurar que autocommit esté desactivado para transacciones manuales
            conn.autocommit = False
            
            # 1. VALIDAR QUE HAY AL MENOS UN ADULTO
            adultos = [p for p in datos_compra['pasajeros'] 
                      if self.calcular_tipo_pasajero(p['fecha_nacimiento'])[3] > 12]
            
            if not adultos:
                conn.rollback()
                return {'Exito': False, 'Error': 'Debe haber al menos un adulto en la reservación'}
            
            # 2. VALIDAR DISPONIBILIDAD DE ASIENTOS
            asientos_seleccionados = [p['asiento_clave'] for p in datos_compra['pasajeros']]
            if not self.validar_asientos_disponibles(datos_compra['numero_corrida'], asientos_seleccionados):
                conn.rollback()
                return {'Exito': False, 'Error': 'Uno o más asientos ya no están disponibles'}
            
            # 3. CREAR/OBTENER PASAJEROS Y CALCULAR TOTALES
            pasajeros_ids = []
            subtotal = 0
            
            for pasajero_data in datos_compra['pasajeros']:
                # Calcular tipo y edad
                tipo_codigo, tipo_desc, porcentaje_desc, edad = self.calcular_tipo_pasajero(
                    pasajero_data['fecha_nacimiento']
                )
                
                # Crear pasajero
                query_pasajero = """
                    INSERT INTO pasajero (nombre, apellPat, apellMat, fechaNac, edad, correoElect, telefono)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                
                cursor.execute(query_pasajero, (
                    pasajero_data['nombre'],
                    pasajero_data['apellido_paterno'],
                    pasajero_data.get('apellido_materno'),
                    pasajero_data['fecha_nacimiento'],
                    edad,
                    pasajero_data.get('correo'),
                    pasajero_data['telefono']
                ))
                
                pasajero_id = cursor.lastrowid
                pasajeros_ids.append({
                    'id': pasajero_id,
                    'tipo_codigo': tipo_codigo,
                    'asiento': pasajero_data['asiento_clave'],
                    'porcentaje_desc': porcentaje_desc
                })
                
                # Calcular precio
                precio_final, _ = self.calcular_precio_boleto(datos_compra['tarifa_base'], porcentaje_desc)
                subtotal += precio_final
            
            # 4. CALCULAR IVA Y TOTAL
            iva = subtotal * 0.16
            total = subtotal + iva
            
            # 5. CREAR RESERVACIÓN (a nombre del primer adulto)
            primer_adulto_id = next(
                p['id'] for p in pasajeros_ids 
                if any(pa['id'] == p['id'] for pa in 
                       [{'id': pid['id']} for pid in pasajeros_ids 
                        if self.calcular_tipo_pasajero(
                            datos_compra['pasajeros'][pasajeros_ids.index(pid)]['fecha_nacimiento']
                        )[3] > 12])
            )
            
            query_reservacion = """
                INSERT INTO reservacion 
                (fecha, fechaLimPago, cantPasajeros, subtotal, IVA, total, pasajero, corrida, usuario)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            
            cursor.execute(query_reservacion, (
                date.today(),
                datos_compra['fecha_corrida'],  # Fecha límite = día de la corrida
                len(datos_compra['pasajeros']),
                subtotal,
                iva,
                total,
                primer_adulto_id,
                datos_compra['numero_corrida'],
                usuario_id
            ))
            
            numero_reservacion = cursor.lastrowid
            
            # 6. CREAR BOLETOS
            boletos_numeros = []
            
            for i, pasajero_info in enumerate(pasajeros_ids):
                precio_final, _ = self.calcular_precio_boleto(
                    datos_compra['tarifa_base'], 
                    pasajero_info['porcentaje_desc']
                )
                
                query_boleto = """
                    INSERT INTO boleto (precio, asiento, pasajero, tipoPasajero, corrida)
                    VALUES (%s, %s, %s, %s, %s)
                """
                
                cursor.execute(query_boleto, (
                    precio_final,
                    pasajero_info['asiento'],
                    pasajero_info['id'],
                    pasajero_info['tipo_codigo'],
                    datos_compra['numero_corrida']
                ))
                
                boletos_numeros.append(cursor.lastrowid)
                
                # 7. RELACIONAR ASIENTO CON RESERVACIÓN
                query_asiento_reservacion = """
                    INSERT INTO asiento_reservacion (asiento, reservacion)
                    VALUES (%s, %s)
                """
                
                cursor.execute(query_asiento_reservacion, (
                    pasajero_info['asiento'],
                    numero_reservacion
                ))
            
            # 8. ACTUALIZAR ESTADO DE ASIENTOS
            for asiento_clave in asientos_seleccionados:
                query_update_asiento = """
                    UPDATE corrida_asiento
                    SET estado = 'NO DISPONIBLE'
                    WHERE corrida = %s AND asiento = %s
                """
                cursor.execute(query_update_asiento, (datos_compra['numero_corrida'], asiento_clave))
            
            # 9. ACTUALIZAR LUGARES DISPONIBLES EN CORRIDA
            query_update_corrida = """
                UPDATE corrida
                SET lugaresDisp = lugaresDisp - %s
                WHERE numero = %s
            """
            
            cursor.execute(query_update_corrida, (len(asientos_seleccionados), datos_compra['numero_corrida']))
            
            # CONFIRMAR TRANSACCIÓN
            conn.commit()
            
            # Restaurar autocommit
            conn.autocommit = True
            
            return {
                'exito': True,
                'mensaje': 'Compra realizada exitosamente',
                'numero_reservacion': numero_reservacion,
                'boletos': boletos_numeros,
                'subtotal': subtotal,
                'iva': iva,
                'total': total
            }
            
        except Error as e:
            if conn:
                conn.rollback()
                # Restaurar autocommit
                try:
                    conn.autocommit = True
                except:
                    pass
            print(f'Error en ViajarDAO.procesar_compra_boletos: {e}')
            return {
                'exito': False,
                'mensaje': f'Error al procesar la compra: {str(e)}'
            }
        finally:
            if cursor:
                cursor.close()
    
    #  CONSULTAS DE RESERVACIONES 
    
    def obtener_boletos_reservacion(self, numero_reservacion):
        """
        Obtiene todos los boletos de una reservación específica.
        CORREGIDO: Ahora filtra correctamente por reservación Y corrida.
        """
        boletos = []
        conn = None
        cursor = None
        
        try:
            conn = Connection.getConnection()
            cursor = conn.cursor(dictionary=True)
            
            query = """
                SELECT 
                    b.numero AS numero_boleto,
                    b.precio,
                    b.asiento AS clave_asiento,
                    a.numero AS numero_asiento,
                    p.nombre,
                    p.apellPat,
                    p.apellMat,
                    p.edad,
                    tp.descripcion AS tipo_pasajero,
                    tp.porcentajeDesc AS porcentaje_descuento,
                    c.numero AS numero_corrida,
                    c.fecha AS fecha_corrida,
                    c.hora_salida,
                    c.hora_llegada,
                    origen.nombre AS ciudad_origen,
                    destino.nombre AS ciudad_destino
                FROM boleto b
                INNER JOIN asiento a ON b.asiento = a.clave
                INNER JOIN pasajero p ON b.pasajero = p.numero
                INNER JOIN tipo_pasajero tp ON b.tipoPasajero = tp.codigo
                INNER JOIN corrida c ON b.corrida = c.numero
                INNER JOIN ruta r ON c.ruta = r.codigo
                INNER JOIN ciudad origen ON r.ciudadOrigen = origen.codigo
                INNER JOIN ciudad destino ON r.ciudadDestino = destino.codigo
                INNER JOIN asiento_reservacion ar ON b.asiento = ar.asiento AND ar.reservacion = %s
                INNER JOIN reservacion res ON ar.reservacion = res.numero AND res.corrida = c.numero
                WHERE ar.reservacion = %s AND b.corrida = res.corrida
                ORDER BY b.numero
            """
            
            cursor.execute(query, (numero_reservacion, numero_reservacion))
            boletos = cursor.fetchall()
            
            print(f"Encontrados {len(boletos)} boletos para reservación {numero_reservacion}")
            
        except Error as e:
            print(f'Error en ViajarDAO.obtener_boletos_reservacion: {e}')
            raise e
        finally:
            if cursor:
                cursor.close()
        
        return boletos
    
    def obtener_reservaciones_usuario(self, usuario_id):
        
        reservaciones = []
        conn = None
        cursor = None
        
        try:
            conn = Connection.getConnection()
            cursor = conn.cursor(dictionary=True)
            
            query = """
                SELECT 
                    r.numero AS numero_reservacion,
                    r.fecha AS fecha_reservacion,
                    r.fechaLimPago AS fecha_limite_pago,
                    r.cantPasajeros,
                    r.total,
                    c.numero AS numero_corrida,
                    c.fecha AS fecha_corrida,
                    c.hora_salida,
                    origen.nombre AS ciudad_origen,
                    destino.nombre AS ciudad_destino,
                    CONCAT(p.nombre, ' ', p.apellPat, ' ', COALESCE(p.apellMat, '')) AS nombre_pasajero
                FROM reservacion r
                INNER JOIN corrida c ON r.corrida = c.numero
                INNER JOIN ruta rt ON c.ruta = rt.codigo
                INNER JOIN ciudad origen ON rt.ciudadOrigen = origen.codigo
                INNER JOIN ciudad destino ON rt.ciudadDestino = destino.codigo
                INNER JOIN pasajero p ON r.pasajero = p.numero
                WHERE r.usuario = %s
                ORDER BY r.fecha DESC, c.fecha DESC
            """
            
            cursor.execute(query, (usuario_id,))
            reservaciones = cursor.fetchall()
            
        except Error as e:
            print(f'Error en ViajarDAO.obtener_reservaciones_usuario: {e}')
            raise e
        finally:
            if cursor:
                cursor.close()
        
        return reservaciones