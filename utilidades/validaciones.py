import re

class Validaciones:  

    # Validaciones de login
    @classmethod
    def validarNumeroDeTelefono(cls,numero):
        if numero == '':
            return 'Campo obligatorio: Numero de telefono.'
        return numero
    
    @classmethod
    def validarPassword(cls,pwrd):
        if pwrd == '':
            return 'Contrasena no ingresada.'
        return pwrd
    
    # Validaciones del registro
    @classmethod
    def validarPhone(cls,phone):
        if phone == '':
            return 'Campo obligatorio: Numero de telefono.'
        if len(phone) != 10:
            return 'El numero de telefono debe tener 10 digitos.'
        return phone
    
    @classmethod
    def validarContrasena(cls,pwrd):
        if pwrd == '':
            return 'Contrasena no ingresada.'
        if len(pwrd) <= 7:
            return 'La contrasena debe tener al menos 8 caracteres.'
        if len(pwrd) >= 21:
            return 'La contrasena debe tener menos de 21 caracteres.'
        return pwrd
    

    ''' Validaciones para reservaciones '''
    @classmethod
    def validar_id(self,valor):
        valor = str(valor).strip()

        if valor == "":
            return "Numero no ingresado."   # si quieres que un campo vacío signifique "Todo"
        
        if int(valor.isdigit()) == False:
            return "Numero no valido. Solo numeros permitidos."

        return valor

    @classmethod
    def validar_ciudad(self,ciudad):
        ciudad = str(ciudad).strip()

        if ciudad == "":
            return "Ciudad no ingresada."   # si quieres que un campo vacío signifique "Todo"
        
        if int(ciudad.isdigit()):
            return "Ciudad no valida. Solo letras y espacios permitidos."
    
        if len(ciudad) > 20 or len(ciudad) < 1:
            return "Ciudad debe tener entre 1 y 20 caracteres."
        return ciudad
        