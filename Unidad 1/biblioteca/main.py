"""
main.py:
menu y ciclo del progrma
"""

from .modelos import Biblioteca
from .operaciones import (
    agregar_libro,
    agregar_usuario,
    mostrar_libros_disponibles,
    prestar_libro,
    devolver_libro
)
from .datos import cargar_datos, guardar_datos

# funciones para la interfaz del usuario

def mostrar_menu():
   #menu
    print("\n--- SISTEMA DE GESTION DE BIBLIOTECA ---")
    print("1. Agregar libro")
    print("2. Agregar usuario")
    print("3. Mostrar libros disponibles")
    print("4. Prestar libro")
    print("5. Devolver libro")
    print("6. Mostrar usuarios y prestamos")
    print("7. Guardar y Salir")
    print("-" * 40)
    return input("Seleccione una opcion: ")

def mostrar_usuarios_y_prestamos(biblioteca: Biblioteca):
    """Mostrar lista de usuarios y sus libros"""
    print("\n--- LISTA DE USUARIOS ---")
    if not biblioteca.usuarios:
        print("No hay usuarios registrados.")
        return
    for usuario in biblioteca.usuarios.values():
        print(usuario)
        if usuario.libros_prestados:
            print(f"  > Titulos: {', '.join(usuario.libros_prestados)}")
        else:
            print("  > Sin prestamos activos.")
    print("-" * 40)

def ejecutar_opcion(opcion: str, biblioteca: Biblioteca) -> bool:
    """
   ejecuta la opcion seleccionada y regresa booleano si va a seguir o no
    """
    if opcion == '1':
        print("\n--- AGREGAR LIBRO ---")
        titulo = input("Titulo: ")
        autor = input("Autor: ")
        try:
            anio = int(input("Año de Publicacion: "))
            agregar_libro(biblioteca, titulo, autor, anio)
        except ValueError:
            print("El año debe ser un numero valido.")
            
    elif opcion == '2':
        print("\n--- AGREGAR USUARIO ---")
        nombre = input("Nombre del usuario: ")
        agregar_usuario(biblioteca, nombre)
        
    elif opcion == '3':
        mostrar_libros_disponibles(biblioteca)

    elif opcion == '4':
        print("\n--- PRESTAR LIBRO ---")
        titulo = input("Titulo del libro a prestar: ")
        usuario = input("Nombre del usuario: ")
        prestar_libro(biblioteca, titulo, usuario)

    elif opcion == '5':
        print("\n--- DEVOLVER LIBRO ---")
        titulo = input("Titulo del libro a devolver: ")
        usuario = input("Nombre del usuario: ")
        devolver_libro(biblioteca, titulo, usuario)
        
    elif opcion == '6':
        mostrar_usuarios_y_prestamos(biblioteca)

    elif opcion == '7':
        guardar_datos(biblioteca)
        print("Finalizado.")
        return False

    else:
        print("Opcion no valida. Intentar de nuevo.")
        
    return True

# funcion principal

def main():
   
    biblioteca = cargar_datos()

    # ejemplos
    if not biblioteca.libros and not biblioteca.usuarios:
        print("Inicializando con datos de ejemplo...")
        agregar_libro(biblioteca, "Zero to one", "Peter Thiel", 2014)
        agregar_libro(biblioteca, "A New Earth", "Eckhart Tolle", 2008)
        agregar_libro(biblioteca, "Sangre de Campeon", "Carlos Cuauhtémoc Sánchez", 2001)
        agregar_usuario(biblioteca, "Angel Madrid")
        agregar_usuario(biblioteca, "Roberto Martinez")
        
    print("\n" + "=" * 40)
    print("Aplicacion iniciada")
    print(biblioteca)
    print("=" * 40)

    # ciclo principal
    while True:
        if not ejecutar_opcion(mostrar_menu(), biblioteca):
            break

if __name__ == "__main__":
    main()