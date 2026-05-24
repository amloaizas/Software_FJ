
# Importamos ABC y abstractmethod para crear clases abstractas
from abc import ABC, abstractmethod


# =========================================================
# Clase abstracta Entidad
# =========================================================
class Entidad(ABC):

    # =====================================================
    # Constructor de la clase
    # =====================================================
    def __init__(self, id_entidad):

        # Encapsulamos el atributo ID
        self._id = id_entidad

    # =====================================================
    # Método getter para obtener el ID
    # =====================================================
    def get_id(self):
        return self._id

    # =====================================================
    # Método setter para modificar el ID
    # =====================================================
    def set_id(self, nuevo_id):

        # Validamos que el ID no esté vacío
        if not nuevo_id:
            raise ValueError("El ID no puede estar vacío")

        self._id = nuevo_id

    # =====================================================
    # Método abstracto obligatorio
    # Cada clase hija debe implementarlo
    # =====================================================
    @abstractmethod
    def mostrar_info(self):
        pass