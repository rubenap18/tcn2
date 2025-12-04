class Usuario:
    """
    Modelo de datos para un Usuario del sistema.
    """

    def __init__(self, id_usuario: int, phone: str, password: str, es_admin: int):
        # Atributos 
        self.__id = id_usuario
        self.__phone = phone
        self.__password = password
        self.__es_admin = es_admin

    # Getters

    @property
    def id(self):
        return self.__id

    @property
    def phone(self):
        return self.__phone

    @property
    def password(self):
        return self.__password

    @property
    def es_admin(self):
        return self.__es_admin

    # Setters
    @phone.setter
    def phone(self, nuevo_phone: str):
        if isinstance(nuevo_phone, str) and nuevo_phone:
            self.__phone = nuevo_phone
        else:
            raise ValueError("El telefono debe ser una cadena no vacia.")

    @password.setter
    def password(self, nueva_password: str):
        if isinstance(nueva_password, str) and len(nueva_password) >= 11:
            self.__password = nueva_password
        else:
            raise ValueError("La contraseña debe ser una cadena y tener al menos 6 caracteres.")

    @es_admin.setter
    def es_admin(self, valor: int):
        if isinstance(valor, int):
            self.__es_admin = valor
        else:
            raise TypeError("El valor para 'es_admin' debe ser un booleano.")

    # --- Método Especial __str__ ---
    def __str__(self):
        """
        Representacion en cadena del objeto Usuario.
        """
        return (f"Usuario(ID: {self.__id}, Teléfono: {self.__phone}, "
                f"Admin: {self.__es_admin}, Contraseña oculta: *****)")