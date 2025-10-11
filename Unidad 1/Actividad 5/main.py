from producto import Producto
from inventario import Inventario

def main():
    """Ejecutar la demostracion del sistema de inventario."""
    
    print("--- DEMOSTRACIoN DE INVENTARIO CON ENCAPSULACIÓN ---")

    mi_inventario = Inventario()
    print("\n[Inicializando Inventario...]")

    laptop = Producto("Laptop", 9200.00)
    mouse = Producto("Mouse", 95.50)
    teclado = Producto("Teclado", 325.00)
    monitor = Producto("Monitor", 1350.00)

    mi_inventario.agregar_producto(laptop, 19)
    mi_inventario.agregar_producto(mouse, 48)
    mi_inventario.agregar_producto(teclado, 12)
    mi_inventario.agregar_producto(monitor, 8)

    print(f"\nNumero de productos distintos: {len(mi_inventario)}")
    print("\n--- Estado Inicial del Inventario ---")
    print(mi_inventario)

    print("\n--- Modificacion de Stock y Precios ---")
    
    raton = mi_inventario.buscar_producto("Mouse")
    if raton:
        print(f"Stock anterior de Mouse: {raton.stock}")
        raton.stock -= 10
        print(f"Nuevo stock de Mouse: {raton.stock}")


    laptop_inv = mi_inventario.buscar_producto("Laptop")
    if laptop_inv:
        print(f"Precio anterior de Laptop: ${laptop_inv.precio}")
        laptop_inv.precio = 1150.99
        print(f"Nuevo precio de Laptop: ${laptop_inv.precio}")
        
    mi_inventario.agregar_producto(Producto("mouse", 28.00), 5) 

    print("\n--- Valor Total del Inventario (Actualizado) ---")
    print(mi_inventario) 

    print("\n--- Busqueda de Producto ---")
    buscado = mi_inventario.buscar_producto("Teclado")
    if buscado:
        print(f"Resultado de búsqueda: {buscado}")


    print("\n--- Comparacion de Productos  ---")
    producto_a = Producto("Cable USB", 5.00)
    producto_b = Producto("cable usb", 8.00)
    
    print(f"'{producto_a.nombre}' == '{producto_b.nombre}': {producto_a == producto_b}")

if __name__ == "__main__":
    main()