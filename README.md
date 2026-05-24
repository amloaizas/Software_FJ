# Sistema Integral de Gestión de Clientes, Servicios y Reservas
## Empresa: Software FJ

---

## Descripción del Proyecto

El presente proyecto consiste en el desarrollo de un sistema integral orientado a objetos para la empresa ficticia Software FJ, dedicada a ofrecer servicios de:

- Reservas de salas
- Alquiler de equipos tecnológicos
- Asesorías especializadas

La aplicación fue desarrollada en Python sin utilizar bases de datos, implementando almacenamiento mediante objetos, listas y archivos de logs.

El sistema incorpora principios fundamentales de Programación Orientada a Objetos (POO), incluyendo:

- Abstracción
- Herencia
- Polimorfismo
- Encapsulación
- Manejo avanzado de excepciones

Además, se implementa un sistema robusto de manejo de errores que permite mantener la aplicación estable y funcional aun cuando ocurren fallos durante su ejecución.

---

# Objetivos

## Objetivo General

Desarrollar un sistema orientado a objetos robusto y modular que permita gestionar clientes, servicios y reservas, implementando manejo avanzado de excepciones y garantizando estabilidad en la ejecución.

---

## Objetivos Específicos

- Implementar clases abstractas y clases derivadas.
- Aplicar encapsulación y validaciones robustas.
- Desarrollar métodos polimórficos y sobrecargados.
- Implementar manejo avanzado de excepciones.
- Registrar eventos y errores en archivos logs.
- Simular operaciones válidas e inválidas.
- Garantizar continuidad del sistema ante errores.

---

# Tecnologías Utilizadas

- Python 3
- Programación Orientada a Objetos
- Manejo de archivos
- Excepciones personalizadas

---

# Estructura del Proyecto

ProyectoSoftwareFJ/

│── main.py
│── logs.txt
│── README.md

├── modelos/
├── servicios/
├── excepciones/
├── utilidades/

---

# Funcionalidades Principales

- Registro de clientes
- Validación de datos
- Gestión de servicios
- Procesamiento de reservas
- Cálculo de costos
- Confirmación y cancelación de reservas
- Manejo de excepciones
- Registro automático de logs

---

# Principios POO Aplicados

| Principio | Implementación |
|---|---|
| Abstracción | Clases Entidad y Servicio |
| Herencia | Servicios especializados |
| Polimorfismo | calcular_costo() |
| Encapsulación | atributos privados |

---

# Manejo de Excepciones

El sistema implementa:

- try / except
- try / except / else
- try / finally
- Excepciones personalizadas
- Encadenamiento de excepciones

---

# Ejecución del Proyecto

1. Abrir terminal.
2. Ubicarse en la carpeta del proyecto.
3. Ejecutar:

```bash
python main.py