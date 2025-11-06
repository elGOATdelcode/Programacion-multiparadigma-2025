"""
Modulo datos.py:
funciones para cargar y guardar datos, se usa formatio json
"""

from .modelos import Biblioteca, Libro, Usuario
import json
import os

ARCHIVO_DATOS = "datos_biblioteca.json"

def guardar_datos(biblioteca: Biblioteca):
    datos_a_guardar = {
        "libros": [
            {
                "titulo": libro.titulo,
                "autor": libro.autor,
                "anio": libro.anio,
                "estado": libro.estado 
            }
            for libro in biblioteca.libros.values()
        ],
        "usuarios": [
            {
                "nombre": usuario.nombre,
                "libros_prestados": usuario.libros_prestados 
            }
            for usuario in biblioteca.usuarios.values()
        ]
    }
    
    try:
        with open(ARCHIVO_DATOS, 'w', encoding='utf-8') as f:
            json.dump(datos_a_guardar, f, indent=4)
        print(f"\nDatos guardados exitosamente en '{ARCHIVO_DATOS}'.")
    except Exception as e:
        print(f"\n Error al intentar guardar los datos: {e}")


def cargar_datos() -> Biblioteca:
    """
    carga los datos de la biblioteca desde un archivo json
    devuelve una instancia de Biblioteca 
    """
    biblioteca = Biblioteca()
    
    if not os.path.exists(ARCHIVO_DATOS):
        print(f"Archivo '{ARCHIVO_DATOS}' no encontrado. Iniciando biblioteca vacia.")
        return biblioteca
    
    try:
        with open(ARCHIVO_DATOS, 'r', encoding='utf-8') as f:
            datos_cargados = json.load(f)
            
            # Carga y reconstruye objetos Libro
            for l_data in datos_cargados.get("libros", []):
                nuevo_libro = Libro(
                    titulo=l_data["titulo"],
                    autor=l_data["autor"],
                    anio=l_data["anio"]
                )
                # Restaura el estado
                nuevo_libro.estado = l_data.get("estado", "disponible")
                biblioteca.libros[nuevo_libro.titulo] = nuevo_libro
                
            # Carga y reconstruye objetos Usuario
            for u_data in datos_cargados.get("usuarios", []):
                nuevo_usuario = Usuario(nombre=u_data["nombre"])
                nuevo_usuario.libros_prestados = u_data.get("libros_prestados", [])
                biblioteca.usuarios[nuevo_usuario.nombre] = nuevo_usuario
                
        print(f"Datos cargados exitosamente desde '{ARCHIVO_DATOS}'.")
        return biblioteca
        
    except json.JSONDecodeError:
        print(f"Error: El archivo '{ARCHIVO_DATOS}' tiene un formato JSON invaido. Iniciando vacio.")
    except Exception as e:
        print(f"Error desconocido al cargar datos: {e}. Iniciando vacio.")
        
    return Biblioteca()