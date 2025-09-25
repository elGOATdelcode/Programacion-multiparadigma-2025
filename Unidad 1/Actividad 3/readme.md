# Gestor de Tareas Personales en Python

## Descripción del Programa

Este programa es un gestor de tareas personale básico implementado en Python. Permite al usuario administrar sus tareas mediante un **menú interactivo** en la consola.

Las tareas se almacenan en una lista de diccionarios en memoria durante la ejecución del programa. Cada tarea tiene dos atributo principales:
1. Descripción: El texto de la tarea (string).
2. Completada: El estado de la tarea (`True` para completada, `False` para pendiente).

El sistema soporta las funcionalidaes esenciales de un gestor de tareas: agregar, listar, marcar como completada, y eliminar tareas.

##  Instrucciones 

Para poner en marcha el gestor de tareas, seguir los siguientes pasos:

1.  **Requisitos**: Asegurarse de tener Python 3 instalado en su sistema operativo.Copie el código proporcionado y guárdelo en un archivo 
2.  **Ejecutar**: Abra su terminal o símbolo del sistema, navegue hasta el directorio donde guardó el archivo y ejecute el programa con el siguiente comando: python gestor_tareas.py


## Ejemplo de Uso

A continuación, se muestra un flujo de interacción típico con el programa:

### 1. Inicio y Menú Principal

Al ejecutar el script, aparecerá el menú:

=========================
GESTOR DE TAREAS

Agregar nueva tarea

Mostrar todas las tareas (Pendientes y Completadas)

Marcar tarea como completada

Eliminar tarea

Salir del programa

Elige una opción (1-5):


### 2. Agregar una Tarea (Opción 1)

El usuario elige '1' e ingresa la descripción:

Elige una opción (1-5): 1
Ingrese la descripción de la nueva tarea: Preparar el informe mensual
Tarea agregada con éxito.


### 3. Agregar otra Tarea y Listar (Opciones 1 y 2)

Agregamos otra y luego listamos todas las tareas para verificar (Opción 2):

Elige una opción (1-5): 1
Ingrese la descripción de la nueva tarea: Comprar víveres
Tarea agregada con éxito.

Elige una opción (1-5): 2

--- Listado Completo de Tareas ---

[PENDIENTE] Preparar el informe mensual

[PENDIENTE] Comprar víveres


### 4. Marcar Tarea como Completada (Opción 3)

Elegimos '3', seleccionamos la tarea a completar (en este caso, la número **1** de la lista de pendientes):

Elige una opción (1-5): 3

--- Tareas Pendientes para Completar ---

Preparar el informe mensual

Comprar víveres

Ingrese el número de la tarea a completar: 1
Tarea marcada como completada.

Verificamos el cambio con la Opción 2:
Elige una opción (1-5): 2

--- Listado Completo de Tareas ---

[COMPLETADA] Preparar el informe mensual

[PENDIENTE] Comprar víveres


### 5. Salir del Programa (Opción 5)

Elige una opción (1-5): 5

Saliendo del Gestor de Tareas

El programa finaliza su ejecución.