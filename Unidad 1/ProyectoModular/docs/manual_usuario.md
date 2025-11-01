# 💰 Gestor Simple de Finanzas Personales 

## Propósito del Programa
Este proyecto aplica los principios de **Modularidad, Diseño y Documentación** en Python para crear un sistema básico de gestión de finanzas personales. Su objetivo es demostrar la correcta separación de responsabilidades en tres módulos distintos. 

El diseño mantiene una arquitectura modular simple:
1.  **Control de Flujo/Interfaz** (`main.py`).
2.  **Lógica de Negocio/Modelo** (`modulos/modelo.py`).
3.  **Funciones de Soporte/Utilidades** (`modulos/utilidades.py`).
## Módulos y Funcionalidad


 **`main.py`**  `main()`, `mostrar_menu()`  **Control de Flujo (Vista):** Inicia el gestor, presenta el menú y coordina la interacción del usuario. Usa impresiones básicas para la presentación.
 **`modulos/modelo.py`** `class Transaccion`, `class GestorFinanzas`  **Lógica de Negocio (Modelo):** Define `Transaccion` (datos) y `GestorFinanzas`. El gestor maneja la colección de transacciones y realiza el cálculo del saldo. 
 **`modulos/utilidades.py`**  `formatear_moneda()`  **Funciones Auxiliares (Soporte):** Proporciona la única función de soporte: **`formatear_moneda`**, que se encarga de dar formato monetario a los valores numéricos para su correcta visualización. 

## Cómo Ejecutar el Proyecto

1.  **Requisitos:** Python 3.x instalado.
2.  **Ejecución:** Abre la terminal en la carpeta principal  y ejecuta:
    python main.py

Muestra de la interacción con el menú principal y la visualización del saldo actual.

![Captura del Menú Principal](Unidad 1\ProyectoModular\docs\captura1_Modular.png)
![Captura del Menú Principal](Unidad 1\ProyectoModular\docs\captura2_modular.png)
