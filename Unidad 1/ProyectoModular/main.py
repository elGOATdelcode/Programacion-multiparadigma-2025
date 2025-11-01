"""
Modulo principal de la aplicación de gestion de finanzas personales.

Controla el flujo del programa, el menu de usuario y la interaccion con el gestor
de finanzas, utilizando la modularidad de Python.
"""

from Modulos.modelo import Transaccion, GestorFinanzas
from Modulos.utilidades import formatear_moneda

def mostrar_menu():
    """
    Imprime el menu de opciones para el usuario y captura su seleccion.

    Returns:
        str: La opcion seleccionada por el usuario.
    """
    print("\n--- MENU DE FINANZAS PERSONALES ---")
    print("1. Agregar Ingreso (I)")
    print("2. Agregar Egreso (E)")
    print("3. Ver Resumen Detallado")
    print("4. Ver Saldo Actual")
    print("5. Salir")
    print("-" * 35)
    return input("Seleccione una opcion: ")

def agregar_nueva_transaccion(gestor: GestorFinanzas, tipo_transaccion: str):
    """
    Pide al usuario los datos necesarios y agrega una nueva transaccion al gestor.

    Args:
        gestor (GestorFinanzas): La instancia del gestor donde se añadira la transaccion.
        tipo_transaccion (str): El tipo de transaccion ('I' o 'E').
    """
    print(f"\n--- AGREGAR {'INGRESO' if tipo_transaccion == 'I' else 'EGRESO'} ---")
    
    while True:
        try:
            descripcion = input("Descripcion (máx 30 caracteres): ")[:30] 
            monto = float(input("Monto: "))
            
            if monto <= 0:
                print("El monto debe ser un numero positivo.")
                continue
            break
        except ValueError:
            print("Entrada invalida. Asegurese de ingresar un numero para el monto.")
            continue

    nueva_transaccion = Transaccion(descripcion, monto, tipo_transaccion)
    gestor.agregar_transaccion(nueva_transaccion)
    print(f"\n Transaccion agregada: {nueva_transaccion}")

def mostrar_resumen(gestor: GestorFinanzas):
    """
    Muestra las transacciones separadas por tipo (Ingresos y Egresos).
    """
    ingresos = gestor.obtener_transacciones_por_tipo('I')
    egresos = gestor.obtener_transacciones_por_tipo('E')
    
    print("\n--- RESUMEN DE TRANSACCIONES ---")

    # Ingresos
    print("\n--- INGRESOS ---")
    if ingresos:
        for i, t in enumerate(ingresos, 1):
            print(f"{i}. {t}")
    else:
        print("No hay ingresos registrados.")

    # Egresos
    print("\n--- EGRESOS ---")
    if egresos:
        for i, t in enumerate(egresos, 1):
            print(f"{i}. {t}")
    else:
        print("No hay egresos registrados.")
    print("-" * 40)


def main():
    """
    Funcion principal que inicializa el sistema y ejecuta el ciclo de la aplicacion.
    """
    gestor = GestorFinanzas()
    
    # Datos iniciales de ejemplo
    gestor.agregar_transaccion(Transaccion("Sueldo Mensual", 2500.55, 'I'))
    gestor.agregar_transaccion(Transaccion("Venta extra", 100.00, 'I'))
    gestor.agregar_transaccion(Transaccion("Compra de mandado", 150.50, 'E'))
    gestor.agregar_transaccion(Transaccion("Pago de Servicios", 85.00, 'E'))
    
    while True:
        opcion = mostrar_menu()

        if opcion == '1':
            agregar_nueva_transaccion(gestor, 'I')
        elif opcion == '2':
            agregar_nueva_transaccion(gestor, 'E')
        elif opcion == '3':
            mostrar_resumen(gestor)
        elif opcion == '4':
            saldo = gestor.calcular_saldo()
            print(f"\n--- SALDO ACTUAL: {formatear_moneda(saldo)} ---")
        elif opcion == '5':
            print("\n Saliendo.")
            break
        else:
            print("\nOpcion no valida. Intente de nuevo.")

if __name__ == "__main__":
    main()