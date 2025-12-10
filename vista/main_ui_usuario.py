import os
from PySide6.QtWidgets import (QApplication, QMainWindow, QStackedWidget, QWidget,
                            QVBoxLayout, QDialog, QPushButton, QLineEdit, QLabel)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, QCoreApplication, Qt
from PySide6.QtGui import QCloseEvent


class MainUIUsuario(QMainWindow):
    def __init__(self, app_manager):
        super().__init__()
        self.app_manager = app_manager
        
        # Configurar stacked widget
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Variables para que el recolector de basura no elimine las UIs
        self.index_ui = None
        self.blog_ui = None
        self.catalogo_destinos_ui = None
        self.contactanos_ui = None
        self.mis_reservaciones_ui = None
        self.nosotros_ui = None
        self.servicios_ui = None
        
        # Cargar todas las interfaces
        self.cargar_interfaces()
        
        # Configurar el controlador de navegación
        self.configurar_controlador_navegacion()
        
        # Configurar las conexiones de botones
        self.setup_connections()  

        # Mostrar pantalla de inicio por defecto (índice 0)
        self.stacked_widget.setCurrentIndex(0)
        self.setWindowTitle('Transportes Cuervo Negro - Usuario')
        self.showMaximized()

    def cargar_interfaces(self):
        """Carga todas las interfaces de usuario desde los archivos .ui"""
        base_path = os.path.dirname(__file__)  # Ruta del directorio de main_ui_usuario.py
        
        # Cargar todas las interfaces con rutas absolutas
        self.index_ui = self.load_ui(os.path.join(base_path, 'usuario', 'index.ui'))
        self.blog_ui = self.load_ui(os.path.join(base_path, 'usuario', 'pantalla_blog.ui'))
        self.catalogo_destinos_ui = self.load_ui(os.path.join(base_path, 'usuario', 'pantalla_catalogodestinos.ui'))
        self.contactanos_ui = self.load_ui(os.path.join(base_path, 'usuario', 'pantalla_contactanos.ui'))
        
        # Mis Reservaciones usa un wrapper personalizado en lugar de solo el .ui
        from vista.usuario.pantalla_misreservaciones import PantallaMisReservacionesWidget
        self.mis_reservaciones_ui = PantallaMisReservacionesWidget(self.app_manager, self)
        
        self.nosotros_ui = self.load_ui(os.path.join(base_path, 'usuario', 'pantalla_nosotros.ui'))
        self.servicios_ui = self.load_ui(os.path.join(base_path, 'usuario', 'pantalla_servicios.ui'))
        
        # Agregar al stacked widget en el orden correcto
        # IMPORTANTE: El orden debe coincidir con las constantes en ControladorIndexUsuario
        if self.index_ui: 
            self.stacked_widget.addWidget(self.index_ui)  # Index 0
        if self.blog_ui: 
            self.stacked_widget.addWidget(self.blog_ui)  # Index 1
        if self.catalogo_destinos_ui: 
            self.stacked_widget.addWidget(self.catalogo_destinos_ui)  # Index 2
        if self.contactanos_ui: 
            self.stacked_widget.addWidget(self.contactanos_ui)  # Index 3
        if self.mis_reservaciones_ui: 
            self.stacked_widget.addWidget(self.mis_reservaciones_ui)  # Index 4
        if self.nosotros_ui: 
            self.stacked_widget.addWidget(self.nosotros_ui)  # Index 5
        if self.servicios_ui: 
            self.stacked_widget.addWidget(self.servicios_ui)  # Index 6
    
    def load_ui(self, ui_path):
        """
        Carga un archivo .ui y retorna el widget.
        
        Args:
            ui_path: Ruta al archivo .ui
            
        Returns:
            QWidget o None si hay error
        """
        file = QFile(ui_path)
        if not file.open(QFile.ReadOnly):
            print(f"ERROR: No se pudo abrir el archivo UI: {ui_path}")
            return None
        
        loader = QUiLoader()
        ui = loader.load(file)
        file.close()
        return ui
    
    def configurar_controlador_navegacion(self):
        """Configura el controlador de navegación y establece la referencia a esta ventana."""
        if hasattr(self.app_manager, 'controlador_index_usuario'):
            self.app_manager.controlador_index_usuario.set_main_window(self)
    
    def abrir_pantalla_viajar(self):
        """Abre la pantalla de búsqueda de viajes en una ventana separada."""
        from vista.compartido.pantalla_viajar import PantallaViajarWidget
        
        pantalla = PantallaViajarWidget(self.app_manager, self)
        pantalla.show()

    def setup_connections(self):
        """Configura las conexiones de todos los botones de navegación."""
        
        # ============ CONEXIONES DE LA PANTALLA INDEX ============
        if self.index_ui:
            # Botón Viajar - Abre ventana separada
            boton_viajar = self.index_ui.findChild(QPushButton, "boton_viajar")
            if boton_viajar:
                boton_viajar.clicked.connect(self.abrir_pantalla_viajar)
            
            # Botón Reservaciones - Navega a Mis Reservaciones
            boton_reservaciones = self.index_ui.findChild(QPushButton, "boton_reservaciones")
            if boton_reservaciones:
                boton_reservaciones.clicked.connect(
                    self.app_manager.controlador_index_usuario.navegar_a_mis_reservaciones
                )
            
            # Botón Destinos - Navega a Catálogo de Destinos
            boton_destinos = self.index_ui.findChild(QPushButton, "boton_destinos")
            if boton_destinos:
                boton_destinos.clicked.connect(
                    self.app_manager.controlador_index_usuario.navegar_a_catalogo_destinos
                )
            
            # Botón Nosotros
            boton_nosotros = self.index_ui.findChild(QPushButton, "boton_nosotros")
            if boton_nosotros:
                boton_nosotros.clicked.connect(
                    self.app_manager.controlador_index_usuario.navegar_a_nosotros
                )
            
            # Botón Contáctanos
            boton_contactanos = self.index_ui.findChild(QPushButton, "boton_contactanos")
            if boton_contactanos:
                boton_contactanos.clicked.connect(
                    self.app_manager.controlador_index_usuario.navegar_a_contactanos
                )
            
            # Botón Blog
            boton_blog = self.index_ui.findChild(QPushButton, "boton_blog")
            if boton_blog:
                boton_blog.clicked.connect(
                    self.app_manager.controlador_index_usuario.navegar_a_blog
                )
            
            # Botón/Label "Conoce nuestros servicios"
            boton_servicios = self.index_ui.findChild(QPushButton, "label_estatico_nuestroservicios")
            if boton_servicios:
                boton_servicios.clicked.connect(
                    self.app_manager.controlador_index_usuario.navegar_a_servicios
                )
        
        # ============ CONEXIONES PARA OTRAS PANTALLAS ============
        # Aquí puedes agregar botones de "Volver" o navegación adicional en cada pantalla
        
        # Conectar botón específico de la pantalla Catálogo de Destinos
        if self.catalogo_destinos_ui:
            boton_regresas = self.catalogo_destinos_ui.findChild(QPushButton, "boton_regresas")
            if boton_regresas:
                boton_regresas.clicked.connect(
                    self.app_manager.controlador_index_usuario.navegar_a_index
                )
                print("Conectado botón 'boton_regresas' en pantalla Catálogo de Destinos")
            else:
                print("No se encontró 'boton_regresas' en pantalla Catálogo de Destinos")
        
        # Conectar botón específico de la pantalla Contáctanos
        if self.contactanos_ui:
            boton_salir = self.contactanos_ui.findChild(QPushButton, "boton_salir")
            if boton_salir:
                boton_salir.clicked.connect(
                    self.app_manager.controlador_index_usuario.navegar_a_index
                )
                print("Conectado botón boton_salir en pantalla Contáctanos")
            else:
                print("No se encontró boton_salir en pantalla Contáctanos")
        
        # Buscar automáticamente botones de "Volver" en otras pantallas
        self._conectar_boton_volver(self.blog_ui)
        self._conectar_boton_volver(self.mis_reservaciones_ui)
        self._conectar_boton_volver(self.nosotros_ui)
        self._conectar_boton_volver(self.servicios_ui)
    
    def _conectar_boton_volver(self, ui_widget):
        """
        Busca y conecta un botón de "Volver" al inicio si existe en la UI.
        
        Args:
            ui_widget: Widget de la UI donde buscar el botón
        """
        if ui_widget:
            # Buscar botones comunes de navegación
            nombres_botones = ["boton_volver", "boton_inicio", "boton_regresar", "boton_home"]
            
            for nombre in nombres_botones:
                boton = ui_widget.findChild(QPushButton, nombre)
                if boton:
                    boton.clicked.connect(
                        self.app_manager.controlador_index_usuario.navegar_a_index
                    )
                    print(f"Conectado botón '{nombre}' para volver al inicio")
                    break

    def closeEvent(self, event: QCloseEvent):
        """
        Este método se llama cuando se presiona la X en esta ventana.
        """
        print("Cerrando ventana de usuario...")
        
        # Aquí podrías agregar lógica adicional antes de cerrar
        # Por ejemplo, preguntar si quiere guardar cambios, cerrar sesión, etc.
        
        event.accept()
        
        # Nota: Luego de event.accept(), el flujo del programa regresa al main.py