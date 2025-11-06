from typing import List, Dict

class Persona:

    def __init__(self, nombre: str):
        """
        Senicializa una nueva Persona
        tomando como argumento el nombre

        """
        self.nombre = nombre

    def __str__(self) -> str:
        return self.nombre

class Usuario(Persona):

    def __init__(self, nombre: str):

        super().__init__(nombre)
        # Lista de títulos de libros prestados
        self.libros_prestados: List[str] = []

    def __str__(self) -> str:
        return f"Usuario: {self.nombre} (Libros Prestados: {len(self.libros_prestados)})"

class Libro:
    def __init__(self, titulo: str, autor: str, anio: int):
        """
        Al inicializar un nuevo libro los argumentos son su informacion relevante
        """
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        #  disponible o prestado
        self.estado = "disponible"

    def __str__(self) -> str:
        return f"'{self.titulo}' por {self.autor} ({self.anio}) - Estado: {self.estado.capitalize()}"

class Biblioteca:
    
    def __init__(self):
        """
       Uso de diccionarios para mejor acceso

        """
        self.libros: Dict[str, Libro] = {}
        
        self.usuarios: Dict[str, Usuario] = {}

    def __str__(self) -> str:
     
        return (f"Resumen de Biblioteca:\n"
                f"Total de Libros: {len(self.libros)}\n"
                f"Total de Usuarios: {len(self.usuarios)}")