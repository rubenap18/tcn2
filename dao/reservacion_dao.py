from objetos.reservacion import Reservacion
from dao.conn import Connection
from mysql.connector import Error

class ReservacionDAO:
    conn = None

    def getNumeroDeReservaciones(self):

        try:
            conn = Connection.getConnection()
            if not conn or not conn.is_connected():
                raise Error('No se puede establecer conexion con la BD.')

            query = 'SELECT COUNT(*) FROM reservacion'
            cursor = conn.cursor()
            cursor.execute(query)
            respuesta = cursor.fetchone()
            cursor.close()
            return respuesta[0] if respuesta else 0
        
        except Error as e:
            print(f'Error en ReservacionDAO (getNumeroDeReservaciones): {e}')
            raise e
        
    def getTodasReservaciones(self):

        try:
            conn = Connection.getConnection() #llamnado a la conexion
            #verificando conexion
            if not conn and not conn.is_connected():
                raise Error('No se puede establecer conexion con la BD.')

            query = 'SELECT * FROM reservacion'
            cursor = conn.cursor()
            cursor.execute(query)
            respuesta = cursor.fetchall()


            #mapeando respuestas a una lista de objetos
            lista_reservaciones = []
            for fila in respuesta:
                lista_reservaciones.append(Reservacion(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8]))
            cursor.close()
            return lista_reservaciones
        
        except Error as e:
            print(f'Error en ReservacionDAO (getTodasReservaciones): {e}')
            raise e



    def _getBaseQuery(self, condicion_where=''):

        query = f"""
            SELECT 
                R.numero,           -- 0. Código de Reservación
                C.fecha,            -- 1. Fecha de la Corrida (para clasificar)
                C.numero,           -- 2. Número de Corrida
                R.fechaLimPago,     -- 3. Límite de Pago
                R.cantPasajeros,    -- 4. Cantidad de Pasajeros
                R.total,            -- 5. Total
                C.estado,           -- 6. Estado de la Corrida
                P.nombre,           -- 7. Nombre del Pasajero
                P.apellPat          -- 8. Apellido Paterno del Pasajero
            FROM reservacion AS R
            JOIN corrida AS C ON R.corrida = C.numero
            JOIN pasajero AS P ON R.pasajero = P.numero
            {condicion_where}
        """
        return query
    

    # --- METODO 2: RESERVACIONES PASADAS ---
    def getTodasReservacionesPasadas(self):
 
        try:
            conn = Connection.getConnection()
            if not conn or not conn.is_connected():
                raise Error('No se puede establecer conexion con la BD.')
            
            query = f"""
                    SELECT reservacion.numero,reservacion.fecha,corrida,co.nombre,cd.nombre,cantPasajeros, 
                    CONCAT(p.nombre,' ', p.apellPat,' ',p.apellMat),fechaLimPago,total
                    FROM reservacion 
                    INNER JOIN corrida AS c ON reservacion.corrida = c.numero
                    INNER JOIN pasajero AS p ON reservacion.pasajero = p.numero
                    INNER JOIN ruta AS rt ON c.ruta = rt.codigo
                    INNER JOIN ciudad AS co ON rt.ciudadOrigen = co.codigo
                    INNER JOIN ciudad AS cd ON rt.ciudadDestino = cd.codigo
                    WHERE reservacion.fecha <= CURDATE()
                    ORDER BY reservacion.numero ASC;
                    """          
            
            cursor = conn.cursor()
            cursor.execute(query)
            respuesta = cursor.fetchall()
            
            #mapeando respuestas a una lista de objetos
            
            cursor.close()
            return respuesta
        except Error as e:
            print(f'Error en ReservacionDAO (getTodasReservacionesPorPasadas): {e}')
            raise e
        
        

    # --- METODO 3: RESERVACIONES POR PASAR---
    def getTodasReservacionesPorPasar(self):

        try:
            conn = Connection.getConnection()
            if not conn or not conn.is_connected():
                raise Error('No se puede establecer conexion con la BD.')
            
            query = f"""
                    SELECT reservacion.numero,reservacion.fecha,corrida,co.nombre,cd.nombre,cantPasajeros, 
                    CONCAT(p.nombre,' ', p.apellPat,' ',p.apellMat),fechaLimPago,total
                    FROM reservacion 
                    INNER JOIN corrida AS c ON reservacion.corrida = c.numero
                    INNER JOIN pasajero AS p ON reservacion.pasajero = p.numero
                    INNER JOIN ruta AS rt ON c.ruta = rt.codigo
                    INNER JOIN ciudad AS co ON rt.ciudadOrigen = co.codigo
                    INNER JOIN ciudad AS cd ON rt.ciudadDestino = cd.codigo
                    WHERE reservacion.fecha >= CURDATE()
                    ORDER BY reservacion.numero ASC;
                    """          
            
            cursor = conn.cursor()
            cursor.execute(query)
            respuesta = cursor.fetchall()
            
            cursor.close()
            return respuesta
        
        except Error as e:
            print(f'Error en ReservacionDAO (getTodasReservacionesPorPasar): {e}')
            raise e
        

    def getTodasReservacionesParaTabla(self):
        """
        CORREGIDO: Ahora incluye reservacion.numero como primera columna
        para poder identificar cada reservación única
        """
        try:
            conn = Connection.getConnection()
            if not conn or not conn.is_connected():
                raise Error('No se puede establecer conexion con la BD.')

            query = f"""
                    SELECT reservacion.numero, reservacion.fecha, corrida, CONCAT(p.nombre,' ', p.apellPat,' ',p.apellMat),
                    co.nombre, cd.nombre, c.hora_salida, c.hora_llegada,
                    cantPasajeros, fechaLimPago
                    FROM reservacion 
                    INNER JOIN corrida AS c ON reservacion.corrida = c.numero
                    INNER JOIN pasajero AS p ON reservacion.pasajero = p.numero
                    INNER JOIN ruta AS rt ON c.ruta = rt.codigo
                    INNER JOIN ciudad AS co ON rt.ciudadOrigen = co.codigo
                    INNER JOIN ciudad AS cd ON rt.ciudadDestino = cd.codigo
                    ORDER BY fecha ASC;
                    """          
            cursor = conn.cursor()
            cursor.execute(query)
            respuesta = cursor.fetchall()
            
            return respuesta
        
        except Error as e:
            print(f'Error en ReservacionDAO (getTodasReservacionesPorParaTabla): {e}')
            raise e
        

    def buscarReservacionPorNumero(self,numero):
 
        try:
            conn = Connection.getConnection()
            if not conn or not conn.is_connected():
                raise Error('No se puede establecer conexion con la BD.')

            query = f"""
                    SELECT reservacion.numero,reservacion.fecha,corrida,co.nombre,cd.nombre,cantPasajeros, 
                    CONCAT(p.nombre,' ', p.apellPat,' ',p.apellMat),fechaLimPago,total
                    FROM reservacion 
                    INNER JOIN corrida AS c ON reservacion.corrida = c.numero
                    INNER JOIN pasajero AS p ON reservacion.pasajero = p.numero
                    INNER JOIN ruta AS rt ON c.ruta = rt.codigo
                    INNER JOIN ciudad AS co ON rt.ciudadOrigen = co.codigo
                    INNER JOIN ciudad AS cd ON rt.ciudadDestino = cd.codigo
                    WHERE reservacion.numero = {numero}
                    ORDER BY reservacion.numero ASC;
                    """          
            cursor = conn.cursor()
            cursor.execute(query)
            respuesta = cursor.fetchall()
            
            return respuesta
        
        except Error as e:
            print(f'Error en ReservacionDAO (buscarReservacionesPorNumero): {e}')
            raise e
        

    def getNumeroDeReservacionesPasadas(self):

        try:
            conn = Connection.getConnection()
            if not conn or not conn.is_connected():
                raise Error('No se puede establecer conexion con la BD.')

            query = query = f"""
                    SELECT COUNT(*)
                    FROM reservacion
                    WHERE reservacion.fecha <= CURDATE()
                    ORDER BY reservacion.numero ASC;
                    """  
            cursor = conn.cursor()
            cursor.execute(query)
            respuesta = cursor.fetchone()
            cursor.close()
            return respuesta[0] if respuesta else 0
        
        except Error as e:
            print(f'Error en ReservacionDAO (getNumeroDeReservacionesPasadas): {e}')
            raise e
        

    def getNumeroDeReservacionesActivas(self):

        try:
            conn = Connection.getConnection()
            if not conn or not conn.is_connected():
                raise Error('No se puede establecer conexion con la BD.')

            query = query = f"""
                    SELECT COUNT(*)
                    FROM reservacion
                    WHERE reservacion.fecha >= CURDATE()
                    ORDER BY reservacion.numero ASC;
                    """  
            cursor = conn.cursor()
            cursor.execute(query)
            respuesta = cursor.fetchone()
            cursor.close()
            return respuesta[0] if respuesta else 0
        
        except Error as e:
            print(f'Error en ReservacionDAO (getNumeroDeReservacionesPasadas): {e}')
            raise e
        
    def buscarReservacionPorCorrida(self,numero):
        """
        CORREGIDO: Ahora incluye reservacion.numero como primera columna
        """
        try:
            conn = Connection.getConnection()
            if not conn or not conn.is_connected():
                raise Error('No se puede establecer conexion con la BD.')

            query = f"""
                    SELECT reservacion.numero, reservacion.fecha, corrida, CONCAT(p.nombre,' ', p.apellPat,' ',p.apellMat),
                    co.nombre, cd.nombre, c.hora_salida, c.hora_llegada,
                    cantPasajeros, fechaLimPago
                    FROM reservacion 
                    INNER JOIN corrida AS c ON reservacion.corrida = c.numero
                    INNER JOIN pasajero AS p ON reservacion.pasajero = p.numero
                    INNER JOIN ruta AS rt ON c.ruta = rt.codigo
                    INNER JOIN ciudad AS co ON rt.ciudadOrigen = co.codigo
                    INNER JOIN ciudad AS cd ON rt.ciudadDestino = cd.codigo
                    WHERE c.numero = {numero}
                    ORDER BY fecha ASC;
                    """          
            cursor = conn.cursor()
            cursor.execute(query)
            respuesta = cursor.fetchall()
            
            return respuesta
        
        except Error as e:
            print(f'Error en ReservacionDAO (buscarReservacionesPorNumero): {e}')
            raise e
        

    def buscarReservacionPorCiudadOrigen(self,ciudad):
  
        try:
            conn = Connection.getConnection()
            if not conn or not conn.is_connected():
                raise Error('No se puede establecer conexion con la BD.')

            query = f"""
                    SELECT reservacion.numero, reservacion.fecha, corrida, CONCAT(p.nombre,' ', p.apellPat,' ',p.apellMat),
                    co.nombre, cd.nombre, c.hora_salida, c.hora_llegada,
                    cantPasajeros, fechaLimPago
                    FROM reservacion 
                    INNER JOIN corrida AS c ON reservacion.corrida = c.numero
                    INNER JOIN pasajero AS p ON reservacion.pasajero = p.numero
                    INNER JOIN ruta AS rt ON c.ruta = rt.codigo
                    INNER JOIN ciudad AS co ON rt.ciudadOrigen = co.codigo
                    INNER JOIN ciudad AS cd ON rt.ciudadDestino = cd.codigo
                    WHERE co.nombre = '{ciudad}'
                    ORDER BY fecha ASC;
                    """          
            cursor = conn.cursor()
            cursor.execute(query)
            respuesta = cursor.fetchall()
            
            return respuesta
        
        except Error as e:
            print(f'Error en ReservacionDAO (buscarReservacionesPorCiudadOrigen): {e}')
            raise e
        
    def buscarReservacionPorCiudadDestino(self,ciudad):
      
        try:
            conn = Connection.getConnection()
            if not conn or not conn.is_connected():
                raise Error('No se puede establecer conexion con la BD.')

            query = f"""
                    SELECT reservacion.numero, reservacion.fecha, corrida, CONCAT(p.nombre,' ', p.apellPat,' ',p.apellMat),
                    co.nombre, cd.nombre, c.hora_salida, c.hora_llegada,
                    cantPasajeros, fechaLimPago
                    FROM reservacion 
                    INNER JOIN corrida AS c ON reservacion.corrida = c.numero
                    INNER JOIN pasajero AS p ON reservacion.pasajero = p.numero
                    INNER JOIN ruta AS rt ON c.ruta = rt.codigo
                    INNER JOIN ciudad AS co ON rt.ciudadOrigen = co.codigo
                    INNER JOIN ciudad AS cd ON rt.ciudadDestino = cd.codigo
                    WHERE cd.nombre = '{ciudad}'
                    ORDER BY fecha ASC;
                    """          
            cursor = conn.cursor()
            cursor.execute(query)
            respuesta = cursor.fetchall()
            
            return respuesta
        
        except Error as e:
            print(f'Error en ReservacionDAO (buscarReservacionesPorCiudadDestino): {e}')
            raise e