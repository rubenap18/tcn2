#Esta es la clase Reservacion creada por Ruben Aguilar


class Reservacion:
    def __init__(self, fechaReservacion, fechaLimitePago, subtotal, total, iva, cantidad_pasajeros):
        self.__numeroReservacion = 0
        self.__fecha_reservacion =  fechaReservacion
        self.__fecha_limite_pago = fechaLimitePago
        self.__cantidad_pasajeros = cantidad_pasajeros
        self.__subtotal = subtotal
        self.__iva = iva
        self.__total = total
        #self.__pasajero = pasajero FK
        #self.__corrida = corrida FK
        
    #getters
    def getID(self):
        return self.__idReservacion
    
    def getFechaReservacion(self):
        return self.__fecha_reservacion

    def getFechaLimitePago(self):
        return self.__fecha_limite_pago
    
    def getSubtotal(self):
        return self.__subtotal
    
    def getTotal(self):
        return self.__total
    
    def getIVA(self):
        return self.__iva
    
    def getCantPasajeros(self):
        return self.__cantidad_pasajeros

    #setters

    #def setFechaLimitePago(self,fecha):
    #    self.__fecha_limite_pago = fecha

    def setSubtotal(self, monto):
        self.__subtotal = monto

    def setTotal(self, montoTotal):
        self.__total = montoTotal

    def setIVA(self, iva):
        self.__iva = iva

    def setCantPasajeros(self, cantidad):
        self.__cantidad_pasajeros = cantidad


    def __str__(self):
        return (
            f"ID Reservación: {self.__numeroReservacion}\n"
            f"Fecha de Reservación: {self.__fecha_reservacion}\n"
            f"Fecha Límite de Pago: {self.__fecha_limite_pago}\n"
            f"Subtotal: ${self.__subtotal:.2f}\n"
            f"IVA: ${self.__iva:.2f}\n"
            f"Total: ${self.__total:.2f}\n"
            f"Cantidad de Pasajeros: {self.__cantidad_pasajeros}"
        )