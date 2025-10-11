class Producto:

    def __init__(self, nombre: str, precio: float):
        
        self.nombre = nombre 
        self.__stock = 0      
        self._precio = 0.0    
  
        self.precio = precio

    @property
    def stock(self) -> int:
        return self.__stock

    @stock.setter
    def stock(self, nuevo_stock: int):
        if nuevo_stock < 0:
            raise ValueError("El stock no puede ser negativo.")
        self.__stock = nuevo_stock

    @property
    def precio(self) -> float:
     
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio: float):
    
        if nuevo_precio <= 0:
            raise ValueError("El precio debe ser un valor positivo.")
        self._precio = nuevo_precio

    def __str__(self) -> str:
       
        return f"Nombre: {self.nombre}, Precio: ${self.precio:.2f}, Stock: {self.stock}"

    def __eq__(self, other) -> bool:
        
        if isinstance(other, Producto):
            return self.nombre.lower() == other.nombre.lower()
        return False