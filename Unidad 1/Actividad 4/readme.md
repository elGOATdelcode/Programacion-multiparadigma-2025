# Clase Simple: Libro en Python 
La actividad 4 es la realizacion de una clase simple de libro, con sus metodos y atributos necesarios para gestionar los prestamos

## Diseño de la Clase `Libro`

La clase `Libro` se diseñó siguiendo los principios fundamentales de la **POO**.

###  Atributos

**"Biblioteca Central"**. Atributo compartido ya que todos los libros son de la misma libreria.

El titulo del libro y autor del libro  es un string
El atributo del año de publicacion es entero
El atributo prestamo es booleano que inicializa en false
Estos atributos se implementarion porque abordan la informacion mas relevante de un libro

###  Métodos

Metodo constructor que  inicializa los atributos de instancia principales y establece `prestado` en `False`

 `prestar()` y `devolver()` , para cumplir con la funcion fundamental de operaciones de la biblioteca, simplemente cambiando el valor del atributo prestamo e imprimiendo la informacion.
 
 `mostrar_estado()`  Imprime de forma formateada toda la información del libro, incluyendo la biblioteca de clase y su estado actual.

 Estos metodos se eligieron asi ya que es fundamental para cumplir los requerimientos de la clase. 


## Ejecución del Script

El script principal (el bloque `if __name__ == "__main__":`) realiza lo siguiente:
1.  Crea 3 instancias de la clase `Libro`.
2.  Llama a los métodos `prestar()` y `devolver()` para simular operaciones.
3.  Utiliza `mostrar_estado()` en cada objeto para verificar los cambios de estado.

En el resultado de la ejecucion de este script se puede ver las operaciones que realiza la biblioteca y el resultado final de los libros

[Resultado de la ejecución](capturas/capturabiblioteca.png)