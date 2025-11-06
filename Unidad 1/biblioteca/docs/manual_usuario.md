# Aplicacion para gestionar biblioteca

Proyecto de un sistema simple de gestión de biblioteca utilizando Python y POO

## Caracteristicas

Clase: LIbro , usuario que hereda de persona y biblioteca, persona
Modularidad con codigo dividido en varios modulos
Documentacion con uso de docstrings y manual de usuario
Aplicacion funcional: Agregar, listar, prestar, devolver, guardar/cargar. 

## Estructura del Código

biblioteca/ ├── main.py # Punto de entrada y menú de usuario. ├── modelos.py # Definición de clases (Libro, Persona, Usuario, Biblioteca). ├── operaciones.py # Lógica de negocio (agregar, prestar, devolver, listar). ├── datos.py # Funciones de almacenamiento (guardar/cargar en JSON). └── README.md # Documentacion

## Instrucciones para Ejecutar el Programa

1.  **Organización:** Tener la estructura de carpeta `biblioteca/` con todos los archivos dentro.
2.  **Entorno:** Debe tener Python instalado.
3.  **Ejecución:** Abra la terminal en el directorio **superior** a `biblioteca` y ejecute el siguiente comando.

    ```bash
    python -m biblioteca.main
    ```

4.  **Interactuar con el programa con las opciones que ofrece el menu**

**Demostracion de funcionalidad de la aplicacion**

-Agregar libro
![agregar libro](docs/agregarlibro.png)

-Ver lista de usuarios
![listausuarios](docs/listausuarios.png)

-Prestar uno de los libros
![Prestarlibro](docs/Prestarlibro.png)
