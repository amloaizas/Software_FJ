# Importamos la clase abstracta Servicio
from modelos.servicio import Servicio

# Importamos excepción personalizada
from excepciones.excepciones import (
    ServicioNoDisponibleError,
    CostoInvalidoError
)


# =========================================================
# Clase ReservaSala
# =========================================================
class ReservaSala(Servicio):

    # =====================================================
    # Constructor
    # =====================================================
    def __init__(
        self,
        nombre_sala,
        capacidad,
        precio_hora
    ):

        # Llamamos al constructor padre
        super().__init__("Reserva de Sala")

        # Validaciones
        if capacidad <= 0:
            raise ServicioNoDisponibleError(
                "La capacidad de la sala debe ser mayor a cero"
            )

        if precio_hora <= 0:
            raise CostoInvalidoError(
                "El precio por hora es inválido"
            )

        # Atributos
        self.nombre_sala = nombre_sala
        self.capacidad = capacidad
        self.precio_hora = precio_hora

    # =====================================================
    # Método sobrescrito calcular costo
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
                "Las horas deben ser mayores a cero"
            )

        # Calculamos subtotal
        subtotal = self.precio_hora * horas

        # Aplicamos impuesto
        subtotal += subtotal * impuesto

        # Aplicamos descuento
        subtotal -= descuento

        return subtotal

    # =====================================================
    # Método sobrescrito descripción
    # =====================================================
    def descripcion(self):

        return (
            f"Sala: {self.nombre_sala}\n"
            f"Capacidad: {self.capacidad}\n"
            f"Precio por hora: {self.precio_hora}"
        )

    # =====================================================
    # Método sobrescrito validar servicio
    # =====================================================
    def validar_servicio(self):

        if not self.nombre_sala:
            raise ServicioNoDisponibleError(
                "La sala no tiene nombre válido"
            )

        return True