 Sistema de Gestión de Parqueadero

Proyecto desarrollado con Django*para administrar los procesos de un parqueadero urbano, incluyendo usuarios, vehículos, espacios, tarifas, sesiones de parqueo y pagos.  
Este sistema permite gestionar de forma centralizada la entrada y salida de vehículos, el cálculo automático de tarifas, la asignación de espacios y el registro de pagos.

---
Descripción del problema

En muchos parqueaderos urbanos, los procesos de registro de vehículos, control de espacios y cobro de tarifas se realizan de forma manual o con herramientas poco integradas.  
Esto genera errores frecuentes, pérdida de información y dificultad para calcular correctamente los valores a cobrar.

El sistema propuesto automatiza la gestión del parqueadero, permitiendo:
- Registrar usuarios (administradores, empleados y clientes)
- Asociar vehículos a clientes
- Controlar los espacios de estacionamiento
- Registrar entradas y salidas
- Calcular el valor a pagar según el tipo de vehículo y tiempo de uso
- Registrar los pagos de cada sesión

---

Objetivos del sistema

 Objetivo general
Diseñar e implementar un sistema web que permita gestionar de forma eficiente un parqueadero urbano, controlando usuarios, vehículos, espacios, tarifas y pagos.

 Objetivos específicos
- Implementar un modelo de datos relacional en Django con las entidades del sistema.  
- Permitir la administración de registros desde el panel de Django Admin.  
- Establecer relaciones entre las entidades (1–N, N–N, 1–1) de forma coherente.  
- Aplicar restricciones de integridad y validación de datos.  
- Facilitar el control y seguimiento de sesiones de parqueo y pagos asociados.  

---

 Arquitectura del sistema

El sistema está compuesto por seis aplicaciones (apps) principales:

| App | Descripción |
|-----|--------------|
| `usuarios` | Gestión de usuarios del sistema (administradores, empleados, clientes). |
| `vehiculos` | Registro de vehículos y relación con los clientes. |
| `espacios` | Control de los espacios físicos disponibles en el parqueadero. |
| `tarifas` | Administración de las tarifas según tipo de vehículo o tiempo. |
| `sesiones` | Control de entrada/salida de vehículos y cálculo del total a pagar. |
| `pagos` | Registro de pagos realizados por las sesiones de parqueo. |

---

 Modelo entidad–relación (resumen lógico)

Usuario (1) ───< Vehículo (N)
Vehículo (1) ───< SesiónParqueo (N)
Espacio (1) ───< SesiónParqueo (N)
Tarifa (1) ───< SesiónParqueo (N)
SesiónParqueo (1) ──── (1) Pago

 Tecnologías utilizadas

Python 3.13
Django 5.2.1
SQLite
HTML / CSS (panel Django Admin)
PowerShell / Visual Studio Code para desarrollo

Activar el entorno virtual

.\venv\Scripts\Activate.ps1

Pegar la caerpeta 

 cd "C:\Users\Windows 11\Documents\sistemadeGestionParqueadero"

Ejecutar el servidor
python manage.py runserver

Autores 
Juan venancio ruiz marin
Junior javier borrego de castro