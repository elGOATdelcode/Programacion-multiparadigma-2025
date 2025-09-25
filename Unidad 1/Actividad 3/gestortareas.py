tareas = tareas = []

def mostrar_menu():
    print("\n" + "="*25)
    print("  GESTOR DE TAREAS ")
    print("1. Agregar nueva tarea")
    print("2. Mostrar todas las tareas (Pendientes y Completadas)")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("-" * 25)
    print("5. Salir del programa")
    print("-" * 25)

def listar_todas_las_tareas(lista_tareas):
    if not lista_tareas:
        print(" No hay tareas en la lista.")
        return
    else:
        print("\n--- Listado Completo de Tareas ---")
        for i, t in enumerate(lista_tareas, 1):
            estado = "[COMPLETADA]" if t['completada'] else "[PENDIENTE]"
            print(f"{i}. {estado} {t['descripcion']}")
        print("-" * 25)

def listar_pendientes_interna(lista_tareas):
    """Devuelve la lista de pendientes para la opción 3 (Completar)."""
    pendientes = [t for t in lista_tareas if not t['completada']]
    if not pendientes:
        print(" No hay tareas pendientes para marcar como completadas.")
        return []
    else:
        print("\n--- Tareas Pendientes para Completar ---")
        for i, t in enumerate(pendientes, 1):
            print(f"{i}. {t['descripcion']}")
        print("-" * 25)
        return pendientes

def agregar_tarea():
    descripcion = input(" Ingrese la descripción de la nueva tarea: ")
    tareas.append({'descripcion': descripcion, 'completada': False})
    print(" Tarea agregada con éxito.")

def completar_o_eliminar(opcion):
    if opcion == '3':
        lista_a_modificar = listar_pendientes_interna(tareas)
        if not lista_a_modificar:
            return 
        accion = "completar"
    else: 
        listar_todas_las_tareas(tareas) 
        if not tareas:
            return
        lista_a_modificar = tareas
        accion = "eliminar"
    
    try:
        if opcion == '3':
            num = int(input(f" Ingrese el número de la tarea a {accion}: ")) - 1
            
            if 0 <= num < len(lista_a_modificar):
                tarea_seleccionada = lista_a_modificar[num]
                tarea_seleccionada['completada'] = True
                print(" Tarea marcada como completada.")
            else:
                print(" Número de tarea no válido.")
        
        elif opcion == '4':
            num = int(input(f" Ingrese el número de la tarea a {accion}: ")) - 1
            
            if 0 <= num < len(tareas):
                tareas.pop(num)
                print(" Tarea eliminada permanentemente.")
            else:
                print(" Número de tarea no válido.")
                
    except ValueError:
        print(" Entrada no válida. Debe ingresar un número.")

# Bucle Principal 
while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-5): ")

    if opcion == '1':
        agregar_tarea()
    elif opcion == '2':
        listar_todas_las_tareas(tareas)
    elif opcion in ['3', '4']:
        completar_o_eliminar(opcion)
    elif opcion == '5':
        print("\n Saliendo del Gestor de Tareas")
        break
    else:
        print(" Opción no válida. Por favor, elija un número del 1 al 5.")