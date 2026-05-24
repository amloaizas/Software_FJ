# =========================================================
# Importamos expresiones regulares
import re

# Importamos la clase Entidad
from modelos.entidad import Entidad

# Importamos excepción personalizada
from excepciones.excepciones import ClienteInvalidoError


# =========================================================
# Clase Cliente
# =========================================================
class Cliente(Entidad):

    # =====================================================
    # Constructor
    # =====================================================
    def __init__(self, id_entidad, nombre, correo, telefono):

        # Llamamos al constructor padre
        super().__init__(id_entidad)

        # Validamos el nombre
        if not nombre.strip():
            raise ClienteInvalidoError(
                "El nombre del cliente no puede estar vacío"
            )

        # Validamos el correo
        if not self.validar_correo(correo):
            raise ClienteInvalidoError(
                "El correo electrónico es inválido"
            )

        # Validamos el teléfono
        if not telefono.isdigit():
            raise ClienteInvalidoError(
                "El teléfono solo debe contener números"
            )

        # Encapsulación de atributos
        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

    # =====================================================
    # Método para validar correo
    # =====================================================
    def validar_correo(self, correo):

        # Patrón de validación
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        # Retornamos True o False
        return re.match(patron, correo)

    # =====================================================
    # Getter nombre
    # =====================================================
    def get_nombre(self):
        return self.__nombre

    # =====================================================
    # Setter nombre
    # =====================================================
    def set_nombre(self, nuevo_nombre):

        if not nuevo_nombre.strip():
            raise ClienteInvalidoError(
                "El nombre no puede estar vacío"
            )

        self.__nombre = nuevo_nombre

    # =====================================================
    # Getter correo
    # =====================================================
    def get_correo(self):
        return self.__correo

    # =====================================================
    # Setter correo
    # =====================================================
    def set_correo(self, nuevo_correo):

        if not self.validar_correo(nuevo_correo):
            raise ClienteInvalidoError(
                "Correo inválido"
            )

        self.__correo = nuevo_correo

    # =====================================================
    # Getter teléfono
    # =====================================================
    def get_telefono(self):
        return self.__telefono

    # =====================================================
    # Setter teléfono
    # =====================================================
    def set_telefono(self, nuevo_telefono):

        if not nuevo_telefono.isdigit():
            raise ClienteInvalidoError(
                "El teléfono debe contener solo números"
            )

        self.__telefono = nuevo_telefono

    # =====================================================
    # Método sobrescrito obligatorio
    # =====================================================
    def mostrar_info(self):

        return (
            f"Cliente ID: {self.get_id()}\n"
            f"Nombre: {self.__nombre}\n"
            f"Correo: {self.__correo}\n"
            f"Teléfono: {self.__telefono}"
        )