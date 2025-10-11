from producto import Producto

class Inventario:

    def __init__(self):
            self.__productos = {} 

    def agregar_producto(self, producto, cantidad=0):
        
        nombre_clave = producto.nombre.lower()
        
        if nombre_clave in self.__productos:
            self.__productos[nombre_clave].stock += cantidad
            print(f"Stock de '{producto.nombre}' actualizado en {cantidad}.")
        else:
            
            producto.stock = cantidad 
            self.__productos[nombre_clave] = producto
            print(f"Producto '{producto.nombre}' agregado con stock inicial de {cantidad}.")

    def buscar_producto(self, nombre):
        
        nombre_clave = nombre.lower()
        return self.__productos.get(nombre_clave) 

    def total_valor_inventario(self):
        
        valor_total = 0
        for producto in self.__productos.values():
            valor_total += producto.precio * producto.stock
        return valor_total

    def __len__(self):
        
        return len(self.__productos)

    def __str__(self):
        
        if not self.__productos:
            return "El inventario está vacío."

        s = f"Inventario ({len(self)} productos):\n"
        for producto in self.__productos.values():
            s += f"  - {producto}\n"
        s += f" Valor Total: ${self.total_valor_inventario():.2f}"
        return s