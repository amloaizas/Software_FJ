# Importamos Servicio
from modelos.servicio import Servicio

# Importamos excepciones
from excepciones.excepciones import (
    ServicioNoDisponibleError,
    CostoInvalidoError
)


# =========================================================
# Clase AsesoriaEspecializada
# =========================================================
class AsesoriaEspecializada(Servicio):

    # =====================================================
    # Constructor
    # =====================================================
    def __init__(
        self,
        especialista,
        tarifa_hora
    ):

        # Constructor padre
        super().__init__("Asesoría Especializada")

        # Validamos tarifa
        if tarifa_hora <= 0:
            raise CostoInvalidoError(
                "La tarifa por hora es inválida"
            )

        # Atributos
        self.especialista = especialista
        self.tarifa_hora = tarifa_hora

    # =====================================================
    # Método calcular costo
    # =====================================================
    def calcular_costo(
        self,
        horas,
        impuesto=0,
        descuento=0
    ):

        # Validamos horas
        if horas <= 0:
            raise CostoInvalidoError(
                "Las horas deben ser válidas"
            )

        # Subtotal
        subtotal = self.tarifa_hora * horas

        # Impuesto
        subtotal += subtotal * impuesto

        # Descuento
        subtotal -= descuento

        return subtotal

    # =====================================================
    # Método descripción
    # =====================================================
    def descripcion(self):

        return (
            f"Especialista: {self.especialista}\n"
            f"Tarifa por hora: {self.tarifa_hora}"
        )

    # =====================================================
    # Método validar servicio
    # =====================================================
    def validar_servicio(self):

        if not self.especialista:
            raise ServicioNoDisponibleError(
                "El especialista no es válido"
            )

        return True