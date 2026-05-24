# Importamos ABC y abstractmethod
from abc import ABC, abstractmethod


# =========================================================
# Clase abstracta Servicio
# =========================================================
class Servicio(ABC):

    # =====================================================
    # Constructor
    # =====================================================
    def __init__(self, nombre_servicio):

        self.nombre_servicio = nombre_servicio

    # =====================================================
    # Método abstracto calcular costo
    # =====================================================
    @abstractmethod
    def calcular_costo(self, tiempo, impuesto=0, descuento=0):
        pass

    # =====================================================
    # Método abstracto descripción
    # =====================================================
    @abstractmethod
    def descripcion(self):
        pass

    # =====================================================
    # Método abstracto validar servicio
    # =====================================================
    @abstractmethod
    def validar_servicio(self):
        pass