# Importamos excepciones personalizadas
from excepciones.excepciones import (
    ReservaError,
    DuracionInvalidaError
)

# Importamos logger
from utilidades.logger import registrar_log


# =========================================================
# Clase Reserva
# =========================================================
class Reserva:

    # =====================================================
    # Constructor
    # =====================================================
    def __init__(self, cliente, servicio, duracion):

        # Validamos duración
        if duracion <= 0:
            raise DuracionInvalidaError(
                "La duración debe ser mayor que cero"
            )

        # Guardamos objetos
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion

        # Estado inicial
        self.estado = "Pendiente"

    # =====================================================
    # Método confirmar reserva
    # =====================================================
    def confirmar(self):

        self.estado = "Confirmada"

        registrar_log(
            f"Reserva confirmada para "
            f"{self.cliente.get_nombre()}"
        )

    # =====================================================
    # Método cancelar reserva
    # =====================================================
    def cancelar(self):

        self.estado = "Cancelada"

        registrar_log(
            f"Reserva cancelada para "
            f"{self.cliente.get_nombre()}"
        )

    # =====================================================
    # Método procesar reserva
    # =====================================================
    def procesar_reserva(
        self,
        impuesto=0,
        descuento=0
    ):

        try:

            # Validamos servicio
            self.servicio.validar_servicio()

            # Calculamos costo
            total = self.servicio.calcular_costo(
                self.duracion,
                impuesto,
                descuento
            )

        # Manejo específico de errores
        except Exception as e:

            registrar_log(
                f"Error procesando reserva: {str(e)}"
            )

            # Encadenamiento de excepción
            raise ReservaError(
                "No fue posible procesar la reserva"
            ) from e

        else:

            registrar_log(
                f"Reserva procesada correctamente "
                f"Total: {total}"
            )

            return total

        finally:

            registrar_log(
                "Finalizó el proceso de reserva"
            )

    # =====================================================
    # Mostrar información
    # =====================================================
    def mostrar_reserva(self):

        return (
            f"\n===== RESERVA =====\n"
            f"Cliente: {self.cliente.get_nombre()}\n"
            f"Servicio: {self.servicio.nombre_servicio}\n"
            f"Duración: {self.duracion}\n"
            f"Estado: {self.estado}"
        )