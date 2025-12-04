class Ciudad:
    def __init__(self, codigo, nombre):
        self._codigo = codigo
        self._nombre = nombre

    def get_codigo(self):
        return self._codigo

    def get_nombre(self):
        return self._nombre

    def __str__(self):
        return f"Ciudad(codigo='{self._codigo}', nombre='{self._nombre}')"
