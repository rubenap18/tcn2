from dao.index_dao import IndexDAO

class ControladorIndex:
    def __init__(self, index_dao):
        self.index_dao = index_dao

    def obtener_pasajeros_dashboard(self):
        
        try:
            return self.index_dao.cargar_pasajeros_dashboard()
        except Exception as e:
            print(f"Error en ControladorIndex.obtener_pasajeros_dashboard: {e}")
            return []

    def obtener_corridas_dashboard(self):
        
        try:
            corridas_data = self.index_dao.cargar_corridas_dashboard()
            return corridas_data
        except Exception as e:
            print(f"Error en ControladorIndex.obtener_corridas_dashboard: {e}")
            return []

    def obtener_operadores_con_corridas_dashboard(self):
        
        try:
            return self.index_dao.cargar_operadores_con_corridas_dashboard()
        except Exception as e:
            print(f"Error en ControladorIndex.obtener_operadores_con_corridas_dashboard: {e}")
            return []

    def obtener_pasajeros_por_corrida(self, corrida_id):
        
        try:
            return self.index_dao.cargar_pasajeros_por_corrida(corrida_id)
        except Exception as e:
            print(f"Error en ControladorIndex.obtener_pasajeros_por_corrida: {e}")
            return []
        
    
    def obtener_todas_las_corridas_detalladas(self, operator_id):
        try:
            return self.index_dao.obtener_todas_las_corridas_detalladas(operator_id)
        except Exception as e:
            print(f"Error en ControladorIndex.obtener_todas_las_corridas_detalladas: {e}")
            return []        
        