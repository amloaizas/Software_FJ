# =========================================================
# Excepción para clientes inválidos
# =========================================================
class ClienteInvalidoError(Exception):

    # Constructor
    def __init__(self, mensaje):

        # Llamamos al constructor padre
        super().__init__(mensaje)


# =========================================================
# Excepción para servicios no disponibles
# =========================================================
class ServicioNoDisponibleError(Exception):

    # Constructor
    def __init__(self, mensaje):

        # Constructor padre
        super().__init__(mensaje)


# =========================================================
# Excepción general de reservas
# =========================================================
class ReservaError(Exception):

    # Constructor
    def __init__(self, mensaje):

        # Constructor padre
        super().__init__(mensaje)


# =========================================================
# Excepción para duración inválida
# =========================================================
class DuracionInvalidaError(Exception):

    # Constructor
    def __init__(self, mensaje):

        # Constructor padre
        super().__init__(mensaje)


# =========================================================
# Excepción para costos inválidos
# =========================================================
class CostoInvalidoError(Exception):

    # Constructor
    def __init__(self, mensaje):

        # Constructor padre
        super().__init__(mensaje)