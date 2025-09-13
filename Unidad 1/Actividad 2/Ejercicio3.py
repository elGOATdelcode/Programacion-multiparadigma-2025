opcion = ''

while opcion != '3':

    print("--- Menú de Operaciones ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Salir")

    opcion = input("Elige una opción: ")
    
    if opcion == '1':

        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = num1 + num2
        print(f"La suma es: {resultado}")
    elif opcion == '2':

        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = num1 - num2
        print(f"La resta es: {resultado}")
    elif opcion == '3':
        print("Saliendo del programa.")
    else:
        print("Opción no válida. Elige 1, 2 o 3.")
