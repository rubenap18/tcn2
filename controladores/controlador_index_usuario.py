"""
Controlador para la navegación en la interfaz de usuario.
Maneja el cambio entre las diferentes pantallas del StackedWidget.
"""

from PySide6.QtWidgets import QMessageBox

class ControladorIndexUsuario:
    """
    Controlador que maneja la navegación entre pantallas en la vista de usuario.
    """
    
    # Constantes para los índices del StackedWidget
    PANTALLA_INDEX = 0
    PANTALLA_BLOG = 1
    PANTALLA_CATALOGO_DESTINOS = 2
    PANTALLA_CONTACTANOS = 3
    PANTALLA_MIS_RESERVACIONES = 4
    PANTALLA_NOSOTROS = 5
    PANTALLA_SERVICIOS = 6
    
    def __init__(self):
        """Inicializa el controlador."""
        self.main_window = None
    
    def set_main_window(self, main_window):
        """
        Establece la referencia a la ventana principal.
        
        Args:
            main_window: Instancia de MainUIUsuario
        """
        self.main_window = main_window
    
    def _cambiar_pantalla(self, indice):
        """
        Cambia la pantalla actual del StackedWidget.
        
        Args:
            indice: Índice de la pantalla a mostrar
        """
        if self.main_window and self.main_window.stacked_widget:
            self.main_window.stacked_widget.setCurrentIndex(indice)
            print(f"✓ Navegando a pantalla índice {indice}")
    
    def navegar_a_index(self):
        """Navega a la pantalla de inicio (index)."""
        self._cambiar_pantalla(self.PANTALLA_INDEX)
    
    def navegar_a_blog(self):
        """Navega a la pantalla del blog."""
        self._cambiar_pantalla(self.PANTALLA_BLOG)
    
    def navegar_a_catalogo_destinos(self):
        """Navega a la pantalla de catálogo de destinos."""
        self._cambiar_pantalla(self.PANTALLA_CATALOGO_DESTINOS)
    
    def navegar_a_contactanos(self):
        """Navega a la pantalla de contacto."""
        self._cambiar_pantalla(self.PANTALLA_CONTACTANOS)
    
    def navegar_a_mis_reservaciones(self):
        """
        Navega a la pantalla de Mis Reservaciones.
        Valida que el usuario esté logueado antes de navegar.
        """
        # Verificar si hay un usuario logueado
        if hasattr(self.main_window, 'app_manager'):
            usuario = self.main_window.app_manager.get_usuario_actual()
            
            if not usuario:
                QMessageBox.warning(
                    self.main_window,
                    "Sesión requerida",
                    "Debes iniciar sesión para ver tus reservaciones."
                )
                return
        
        self._cambiar_pantalla(self.PANTALLA_MIS_RESERVACIONES)
    
    def navegar_a_nosotros(self):
        """Navega a la pantalla de Nosotros."""
        self._cambiar_pantalla(self.PANTALLA_NOSOTROS)
    
    def navegar_a_servicios(self):
        """Navega a la pantalla de Servicios."""
        self._cambiar_pantalla(self.PANTALLA_SERVICIOS)
    
    def abrir_pantalla_viajar(self):
        """
        Abre la pantalla de búsqueda de viajes en una ventana separada.
        Este método delega la acción a la ventana principal.
        """
        if self.main_window:
            self.main_window.abrir_pantalla_viajar()
    
    def obtener_nombre_pantalla_actual(self):
        """
        Obtiene el nombre de la pantalla actual.
        
        Returns:
            str: Nombre de la pantalla actual
        """
        if not self.main_window or not self.main_window.stacked_widget:
            return "Desconocida"
        
        indice_actual = self.main_window.stacked_widget.currentIndex()
        
        nombres_pantallas = {
            self.PANTALLA_INDEX: "Index",
            self.PANTALLA_BLOG: "Blog",
            self.PANTALLA_CATALOGO_DESTINOS: "Catálogo de Destinos",
            self.PANTALLA_CONTACTANOS: "Contáctanos",
            self.PANTALLA_MIS_RESERVACIONES: "Mis Reservaciones",
            self.PANTALLA_NOSOTROS: "Nosotros",
            self.PANTALLA_SERVICIOS: "Servicios"
        }
        
        return nombres_pantallas.get(indice_actual, f"Pantalla {indice_actual}")