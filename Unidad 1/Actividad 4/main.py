
class Libro:

    
    biblioteca = "Biblioteca Central"

#metodos de la clase 
    def __init__(self, titulo, autor, anio_publicacion):

        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.prestado = False  

    def prestar(self):

        if not self.prestado:
            self.prestado = True
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' ya se encuentra prestado.")

    def devolver(self):

        if self.prestado:
            self.prestado = False
            print(f"El libro '{self.titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{self.titulo}' ya estaba disponible.")

    def mostrar_estado(self):

        print("\n========== FICHA DEL LIBRO ==========")
        print(f"  Biblioteca: {Libro.biblioteca}")
        print(f"  Titulo: {self.titulo}")
        print(f"  Autor: {self.autor}")
        print(f"  Año: {self.anio_publicacion}")
        estado = "Prestado" if self.prestado else "Disponible"
        print(f"  Estado: {estado}")
        print("=====================================")


if __name__ == "__main__":
    

    libro1 = Libro("Las 48 Leyes del Poder", "Robert Greene", 1998)
    libro2 = Libro("La Metamorfosis", "Franz Kafka", 1915)
    libro3 = Libro("Klara y el Sol", "Kazuo Ishiguro", 2021)

#realizar e imprimir operaciones
    print("-Operaciones-\n")
    libro1.prestar()   
    libro2.prestar()
    libro3.prestar()    
    libro1.devolver()
    libro3.devolver()  
    print("\n-Fin de operaciones-\n")


    libro1.mostrar_estado()
    libro2.mostrar_estado()
    libro3.mostrar_estado()