from .modelos import Biblioteca, Libro, Usuario
from typing import List

# --- Funciones de Gestión ---

def agregar_libro(biblioteca: Biblioteca, titulo: str, autor: str, anio: int):
    """
    validacion para evitar duplicados
    """
    if titulo in biblioteca.libros:
        print(f" El libro con titulo '{titulo}' ya existe.")
        return

    nuevo_libro = Libro(titulo, autor, anio)
    biblioteca.libros[titulo] = nuevo_libro
    print(f"Libro '{titulo}' agregado.")

def agregar_usuario(biblioteca: Biblioteca, nombre: str):
    """
    se agrega nuevo usuario a la biblioteca
    """
    if nombre in biblioteca.usuarios:
        print(f" El usuario '{nombre}' ya esta registrado.")
        return

    nuevo_usuario = Usuario(nombre)
    biblioteca.usuarios[nombre] = nuevo_usuario
    print(f"Usuario '{nombre}' registrado.")

def mostrar_libros_disponibles(biblioteca: Biblioteca):
    libros_disponibles: List[Libro] = [
        libro for libro in biblioteca.libros.values() if libro.estado == "disponible"
    ]
    
    print("\n--- LIBROS DISPONIBLES PARA PRESTAMO ---")
    if not libros_disponibles:
        print("No hay libros disponibles.")
        return

    for i, libro in enumerate(libros_disponibles, 1):
        print(f"{i}. {libro}")
    print("-" * 40)

def prestar_libro(biblioteca: Biblioteca, titulo_libro: str, nombre_usuario: str):
    """
    prestar un libro, actualizando valores necesarios
    """
    libro = biblioteca.libros.get(titulo_libro)
    usuario = biblioteca.usuarios.get(nombre_usuario)

    if not libro:
        print(f"Libro '{titulo_libro}' no encontrado.")
        return
    if not usuario:
        print(f"Usuario '{nombre_usuario}' no registrado.")
        return
    if libro.estado == "prestado":
        print(f"El libro '{titulo_libro}' ya esta prestado.")
        return
    
    # Realizar el prestamo
    libro.estado = "prestado"
    usuario.libros_prestados.append(libro.titulo)
    
    print(f"'{libro.titulo}' prestado a {usuario.nombre}.")

def devolver_libro(biblioteca: Biblioteca, titulo_libro: str, nombre_usuario: str):
    
    libro = biblioteca.libros.get(titulo_libro)
    usuario = biblioteca.usuarios.get(nombre_usuario)
    """
    devorlver un libro actualizando valores
    """

    if not libro or not usuario:
        print("Libro o Usuario no encontrados.")
        return
    
    if libro.estado == "disponible":
        print(f"'{libro.titulo}' ya estaba disponible.")
        return
    
    if titulo_libro not in usuario.libros_prestados:
        print(f"El libro no estaba registrado como prestado por {usuario.nombre}.")
        return

    # Realizar la devolucion
    usuario.libros_prestados.remove(libro.titulo)
    libro.estado = "disponible"
    print(f"Devolucion exitosa: '{libro.titulo}' ahora esta disponible.")