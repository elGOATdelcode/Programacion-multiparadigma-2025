import json 

class Tarea:
    def __init__(self, titulo, descripcion):
        self.__titulo = titulo
        self.__descripcion = descripcion
        self.__completada = False

    def marcar_completada(self): self.__completada = True
    def get_titulo(self): return self.__titulo
    def get_descripcion(self): return self.__descripcion
    def esta_completada(self): return self.__completada

    def mostrar_info(self):
        estado = "Completada" if self.__completada else "Pendiente"
        print(f"Tarea: {self.__titulo} ({estado})")
        print(f"  Descripción: {self.__descripcion}")

    def a_dict(self):
        return {
            "tipo": "base",
            "titulo": self.__titulo,
            "descripcion": self.__descripcion,
            "completada": self.__completada
        }

class TareaUrgente(Tarea):
    def __init__(self, titulo, descripcion, prioridad):
        super().__init__(titulo, descripcion)
        self.__prioridad = prioridad

    def get_prioridad(self): return self.__prioridad

    def mostrar_info(self):
        estado = "Completada" if self.esta_completada() else "Pendiente"
        print(f"TAREA URGENTE: {self.get_titulo()} ({estado})")
        print(f"  Descripción: {self.get_descripcion()}")
        print(f"  Prioridad: {self.__prioridad}") 

    def a_dict(self):
        datos = super().a_dict()
        datos["tipo"] = "urgente" 
        datos["prioridad"] = self.__prioridad
        return datos

class GestorTareas:
    def __init__(self, archivo="tareas.json"):
        self.__lista_tareas = [] 
        self.__archivo = archivo 

    def agregar_tarea(self, tarea):
        self.__lista_tareas.append(tarea)
        print("Tarea agregada correctamente.")

    def listar_tareas(self):
        if not self.__lista_tareas:
            print("\nNo hay tareas registradas.")
            return
        print("\n--- Lista de Tareas ---")
        for i, tarea in enumerate(self.__lista_tareas):
            print(f"[{i + 1}] ", end="") 
            tarea.mostrar_info()
        print("-----------------------\n")

    def marcar_tarea_completada(self, indice):
        try:
            tarea = self.__lista_tareas[indice - 1]
            tarea.marcar_completada()
            print(f"Tarea '{tarea.get_titulo()}' marcada como completada")
        except IndexError:
            print("Error: Ese número de tarea no existe.")

    def eliminar_tarea(self, indice):
        try:
            tarea_eliminada = self.__lista_tareas.pop(indice - 1)
            print(f"Tarea '{tarea_eliminada.get_titulo()}' eliminada.")
        except IndexError:
            print("Error: Ese numero de tarea no existe.")

    def guardar_tareas(self):
        lista_para_guardar = [t.a_dict() for t in self.__lista_tareas]
        with open(self.__archivo, "w", encoding="utf-8") as f:
            json.dump(lista_para_guardar, f, indent=4)
        print(f"Tareas guardadas en '{self.__archivo}'.")

    def cargar_tareas(self):
        try:
            with open(self.__archivo, "r", encoding="utf-8") as f:
                lista_de_datos = json.load(f)
            self.__lista_tareas = [] 
            for datos in lista_de_datos:
                if datos.get("tipo") == "urgente":
                    tarea = TareaUrgente(datos["titulo"], datos["descripcion"], datos["prioridad"])
                else: 
                    tarea = Tarea(datos["titulo"], datos["descripcion"])
                if datos["completada"]:
                    tarea.marcar_completada()
                self.__lista_tareas.append(tarea)
            print(f"Se cargaron {len(self.__lista_tareas)} tareas.")
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"Error al cargar: {e}")

def mostrar_menu():
    print("\n===== GESTOR DE TAREAS =====")
    print("1. Agregar nueva tarea")
    print("2. Listar tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir y guardar")
    return input("Elige una opcion (1-5): ")

def main():
    mi_gestor = GestorTareas("mis_tareas.json")
    mi_gestor.cargar_tareas()

    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            tipo = input("Tipo (1: Normal, 2: Urgente): ")
            titulo = input("Título: ")
            desc = input("Descripcion: ")
            if tipo == "2":
                prioridad = input("Prioridad: ")
                nueva_tarea = TareaUrgente(titulo, desc, prioridad)
            else:
                nueva_tarea = Tarea(titulo, desc)
            mi_gestor.agregar_tarea(nueva_tarea)

        elif opcion == "2":
            mi_gestor.listar_tareas()

        elif opcion == "3":
            mi_gestor.listar_tareas() 
            try:
                idx = int(input("Numero de la tarea a completar: "))
                mi_gestor.marcar_tarea_completada(idx)
            except ValueError:
                print("Error: Debes ingresar un numero.")

        elif opcion == "4":
            mi_gestor.listar_tareas() 
            try:
                idx = int(input("Numero de la tarea a eliminar: "))
                mi_gestor.eliminar_tarea(idx)
            except ValueError:
                print("Error: Debes ingresar un numero.")

        elif opcion == "5":
            mi_gestor.guardar_tareas()
            print("Tareas guardadas.")
            break 
        
        else:
            print("Opcion no valida.")

if __name__ == "__main__":
    main()