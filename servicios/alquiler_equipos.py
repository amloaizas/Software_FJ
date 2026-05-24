# Importamos Servicio
from modelos.servicio import Servicio

# Importamos excepciones
from excepciones.excepciones import (
    ServicioNoDisponibleError,
    CostoInvalidoError
)


# =========================================================
# Clase AlquilerEquipos
# =========================================================
class AlquilerEquipos(Servicio):

    # =====================================================
    # Constructor
    # =====================================================
    def __init__(
        self,
        tipo_equipo,
        precio_dia
    ):

        # Llamamos al constructor padre
        super().__init__("Alquiler de Equipos")

        # Validamos precio
        if precio_dia <= 0:
            raise CostoInvalidoError(
                "El precio por día debe ser válido"
            )

        # Atributos
        self.tipo_equipo = tipo_equipo
        self.precio_dia = precio_dia

    # =====================================================
    # Método sobrescrito calcular costo
    # =====================================================
    def calcular_costo(
        self,
        dias,
        impuesto=0,
        descuento=0
    ):

        # Validamos días
        if dias <= 0:
            raise CostoInvalidoError(
                "Los días deben ser mayores que cero"
            )

        # Calculamos costo
        total = self.precio_dia * dias

        # Impuesto
        total += total * impuesto

        # Descuento
        total -= descuento

        return total

    # =====================================================
    # Método descripción
    # =====================================================
    def descripcion(self):

        return (
            f"Equipo: {self.tipo_equipo}\n"
            f"Precio por día: {self.precio_dia}"
        )

    # =====================================================
    # Método validar servicio
    # =====================================================
    def validar_servicio(self):

        if not self.tipo_equipo:
            raise ServicioNoDisponibleError(
                "El tipo de equipo es inválido"
            )

        return True