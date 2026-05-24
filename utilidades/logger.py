# Importamos fecha y hora
from datetime import datetime


# =========================================================
# Función registrar log general
# =========================================================
def registrar_log(mensaje):

    try:

        # Abrimos el archivo en modo agregar
        with open(
            "logs.txt",
            "a",
            encoding="utf-8"
        ) as archivo:

            # Creamos fecha y hora actual
            fecha = datetime.now()

            # Escribimos el log
            archivo.write(
                f"{fecha} - INFO - {mensaje}\n"
            )

    except Exception as e:

        # Si falla el log lo mostramos en consola
        print(
            f"Error registrando log: {e}"
        )


# =========================================================
# Función registrar errores
# =========================================================
def registrar_error(error):

    try:

        # Abrimos archivo
        with open(
            "logs.txt",
            "a",
            encoding="utf-8"
        ) as archivo:

            # Fecha actual
            fecha = datetime.now()

            # Guardamos error
            archivo.write(
                f"{fecha} - ERROR - {error}\n"
            )

    except Exception as e:

        # Error secundario
        print(
            f"No se pudo registrar el error: {e}"
        )