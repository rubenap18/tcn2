#Este modulo contiene todas las referencias a los controladores del programa.
class AppManager:
    
    def __init__(self, controlador_index,controlador_isd, controlador_rd, controlador_pr, 
                controlador_pc,controlador_pa,controlador_prutas, controlador_po,controlador_pp, controlador_pcidad, controlador_index_usuario=None):
        # Almacena los controladores como atributos
        self.controlador_index = controlador_index #controlador index
        self.controlador_isd = controlador_isd #controlador inicio sesion dialog
        self.controlador_rd = controlador_rd #controlador registro dialog
        self.controlador_pr = controlador_pr #controlador pantalla reservaciones
        self.controlador_pc = controlador_pc #controlador pantalla corridas
        self.controlador_pa = controlador_pa #controlador pantalla autobuses
        self.controlador_prutas = controlador_prutas #controlador pantalla rutas 
        self.controlador_po = controlador_po #controlador pantalla operadores
        self.controlador_pp = controlador_pp #controlador pantalla pasajeros
        self.controlador_pcidad = controlador_pcidad #controlador pantalla ciudad
        self.controlador_index_usuario = controlador_index_usuario #controlador pantalla index usuario
        
        # Usuario logueado y controlador de compra
        self.usuario_actual = None
        self.controlador_viajar = None  # Se inicializará después
        
    def set_usuario_actual(self, usuario):
        """Guarda el usuario que acaba de iniciar sesión"""
        self.usuario_actual = usuario

    def get_usuario_actual(self):
        """Obtiene el usuario logueado"""
        return self.usuario_actual

    def cerrar_sesion(self):
        """Limpia la sesión del usuario"""
        self.usuario_actual = None
