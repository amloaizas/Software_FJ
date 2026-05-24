# Importamos clases del sistema
from modelos.cliente import Cliente
from modelos.reserva import Reserva

# Importamos servicios
from servicios.reserva_sala import ReservaSala
from servicios.alquiler_equipos import AlquilerEquipos
from servicios.asesoria_especializada import (
    AsesoriaEspecializada
)

# Importamos logger
from utilidades.logger import (
    registrar_log,
    registrar_error
)

# Importamos excepciones
from excepciones.excepciones import (
    ClienteInvalidoError,
    ServicioNoDisponibleError,
    ReservaError,
    DuracionInvalidaError,
    CostoInvalidoError
)

# =========================================================
# LISTAS DEL SISTEMA
# =========================================================

# Lista de clientes
clientes = []

# Lista de servicios
servicios = []

# Lista de reservas
reservas = []


# =========================================================
# FUNCIÓN AUXILIAR PARA MOSTRAR TÍTULOS
# =========================================================
def mostrar_titulo(texto):

    print("\n")
    print("=" * 60)
    print(texto)
    print("=" * 60)


# =========================================================
# PRUEBA 1
# CLIENTE VÁLIDO
# =========================================================

mostrar_titulo("PRUEBA 1 - CLIENTE VÁLIDO")

try:

    cliente1 = Cliente(
        1,
        "Carlos Ramirez",
        "carlos@gmail.com",
        "3001234567"
    )

    clientes.append(cliente1)

    print(cliente1.mostrar_info())

    registrar_log(
        "Cliente válido registrado correctamente"
    )

except Exception as e:

    registrar_error(str(e))

    print(e)


# =========================================================
# PRUEBA 1B
# OTRO CLIENTE VÁLIDO
# =========================================================

mostrar_titulo("PRUEBA 1B - OTRO CLIENTE VÁLIDO")

try:

    cliente4 = Cliente(
        4,
        "Luisa Gómez",
        "luisa@gmail.com",
        "3105553344"
    )

    clientes.append(cliente4)

    print(cliente4.mostrar_info())

    registrar_log(
        "Segundo cliente válido registrado correctamente"
    )

except Exception as e:

    registrar_error(str(e))

    print(e)


# =========================================================
# PRUEBA 2
# CLIENTE CON NOMBRE VACÍO
# =========================================================

mostrar_titulo("PRUEBA 2 - CLIENTE INVÁLIDO")

try:

    cliente2 = Cliente(
        2,
        "",
        "maria@gmail.com",
        "3009998888"
    )

    clientes.append(cliente2)

except ClienteInvalidoError as e:

    registrar_error(str(e))

    print(f"ERROR CONTROLADO: {e}")


# =========================================================
# PRUEBA 2B
# CLIENTE CON TELÉFONO INVÁLIDO
# =========================================================

mostrar_titulo("PRUEBA 2B - CLIENTE CON TELÉFONO INVÁLIDO")

try:

    cliente5 = Cliente(
        5,
        "Ana Torres",
        "ana@gmail.com",
        "300abc7777"
    )

    clientes.append(cliente5)

except ClienteInvalidoError as e:

    registrar_error(str(e))

    print(f"ERROR CONTROLADO: {e}")


# =========================================================
# PRUEBA 3
# CLIENTE CON CORREO INVÁLIDO
# =========================================================

mostrar_titulo("PRUEBA 3 - CORREO INVÁLIDO")

try:

    cliente3 = Cliente(
        3,
        "Andres",
        "correo_mal",
        "123456"
    )

    clientes.append(cliente3)

except ClienteInvalidoError as e:

    registrar_error(str(e))

    print(f"ERROR CONTROLADO: {e}")


# =========================================================
# PRUEBA 3B
# CLIENTE CON CORREO VACÍO
# =========================================================

mostrar_titulo("PRUEBA 3B - CLIENTE CON CORREO VACÍO")

try:

    cliente6 = Cliente(
        6,
        "Miguel López",
        "",
        "3017778888"
    )

    clientes.append(cliente6)

except ClienteInvalidoError as e:

    registrar_error(str(e))

    print(f"ERROR CONTROLADO: {e}")


# =========================================================
# PRUEBA 4
# SERVICIO VÁLIDO
# =========================================================

mostrar_titulo("PRUEBA 4 - SERVICIO SALA")

try:

    sala1 = ReservaSala(
        "Sala Empresarial",
        15,
        50000
    )

    servicios.append(sala1)

    print(sala1.descripcion())

    registrar_log(
        "Servicio de sala creado correctamente"
    )

except Exception as e:

    registrar_error(str(e))

    print(e)


# =========================================================
# PRUEBA 4B
# OTRA SALA VÁLIDA
# =========================================================

mostrar_titulo("PRUEBA 4B - OTRA SALA VÁLIDA")

try:

    sala2 = ReservaSala(
        "Sala Creativa",
        20,
        75000
    )

    servicios.append(sala2)

    print(sala2.descripcion())

    registrar_log(
        "Segunda sala creada correctamente"
    )

except Exception as e:

    registrar_error(str(e))

    print(e)


# =========================================================
# PRUEBA 5
# SERVICIO CON PRECIO INVÁLIDO
# =========================================================

mostrar_titulo("PRUEBA 5 - SERVICIO INVÁLIDO")

try:

    equipo1 = AlquilerEquipos(
        "Portátil Gamer",
        -1000
    )

    servicios.append(equipo1)

except CostoInvalidoError as e:

    registrar_error(str(e))

    print(f"ERROR CONTROLADO: {e}")


# =========================================================
# PRUEBA 5B
# SERVICIO CON PRECIO CERO
# =========================================================

mostrar_titulo("PRUEBA 5B - SERVICIO CON PRECIO CERO")

try:

    equipo2 = AlquilerEquipos(
        "Impresora 3D",
        0
    )

    servicios.append(equipo2)

except CostoInvalidoError as e:

    registrar_error(str(e))

    print(f"ERROR CONTROLADO: {e}")


# =========================================================
# PRUEBA 6
# SERVICIO DE ASESORÍA
# =========================================================

mostrar_titulo("PRUEBA 6 - ASESORÍA")

try:

    asesoria1 = AsesoriaEspecializada(
        "Ingeniero de Software",
        120000
    )

    servicios.append(asesoria1)

    print(asesoria1.descripcion())

    registrar_log(
        "Asesoría creada correctamente"
    )

except Exception as e:

    registrar_error(str(e))

    print(e)


# =========================================================
# PRUEBA 6B
# OTRA ASESORÍA
# =========================================================

mostrar_titulo("PRUEBA 6B - OTRA ASESORÍA")

try:

    asesoria2 = AsesoriaEspecializada(
        "Consultor Financiero",
        90000
    )

    servicios.append(asesoria2)

    print(asesoria2.descripcion())

    registrar_log(
        "Segunda asesoría creada correctamente"
    )

except Exception as e:

    registrar_error(str(e))

    print(e)


# =========================================================
# PRUEBA 7
# RESERVA EXITOSA
# =========================================================

mostrar_titulo("PRUEBA 7 - RESERVA EXITOSA")

try:

    reserva1 = Reserva(
        cliente1,
        sala1,
        5
    )

    reservas.append(reserva1)

    total = reserva1.procesar_reserva(
        impuesto=0.19,
        descuento=10000
    )

    reserva1.confirmar()

    print(reserva1.mostrar_reserva())

    print(f"TOTAL A PAGAR: {total}")

except (
    ReservaError,
    DuracionInvalidaError
) as e:

    registrar_error(str(e))

    print(f"ERROR CONTROLADO: {e}")


# =========================================================
# PRUEBA 8
# RESERVA CON DURACIÓN INVÁLIDA
# =========================================================

mostrar_titulo(
    "PRUEBA 8 - DURACIÓN INVÁLIDA"
)

try:

    reserva2 = Reserva(
        cliente1,
        sala1,
        -5
    )

    reservas.append(reserva2)

except DuracionInvalidaError as e:

    registrar_error(str(e))

    print(f"ERROR CONTROLADO: {e}")


# =========================================================
# PRUEBA 9
# CÁLCULO INCORRECTO
# =========================================================

mostrar_titulo(
    "PRUEBA 9 - ERROR DE CÁLCULO"
)

try:

    total_error = sala1.calcular_costo(
        -3
    )

    print(total_error)

except CostoInvalidoError as e:

    registrar_error(str(e))

    print(f"ERROR CONTROLADO: {e}")


# =========================================================
# PRUEBA 10
# CANCELACIÓN DE RESERVA
# =========================================================

mostrar_titulo(
    "PRUEBA 10 - CANCELACIÓN"
)

try:

    reserva1.cancelar()

    print(
        "Reserva cancelada correctamente"
    )

    print(reserva1.mostrar_reserva())

except Exception as e:

    registrar_error(str(e))

    print(e)


# =========================================================
# PRUEBA 11
# TRY - EXCEPT - ELSE
# =========================================================

mostrar_titulo(
    "PRUEBA 11 - TRY EXCEPT ELSE"
)

try:

    total = asesoria1.calcular_costo(
        2
    )

except Exception as e:

    registrar_error(str(e))

    print(e)

else:

    print(
        f"Cálculo realizado correctamente: {total}"
    )

    registrar_log(
        "Cálculo exitoso usando ELSE"
    )


# =========================================================
# FINAL DEL SISTEMA
# =========================================================

mostrar_titulo(
    "SISTEMA FINALIZADO"
)

print(
    "El sistema continúa funcionando "
    "aunque existan errores."
)

print(
    f"\nClientes registrados: {len(clientes)}"
)

print(
    f"Servicios registrados: {len(servicios)}"
)

print(
    f"Reservas registradas: {len(reservas)}"
)