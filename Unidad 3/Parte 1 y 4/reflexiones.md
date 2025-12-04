# Parte 1: Identificación y Análisis

## Función A: calcular_promedio
**Estado:** Pura.

**Por qué:** Es determinists porque con la misma entrada siempre devuelve la misma salida y no modifica nada mas 

## Función B: siguiente_id
**Estado:** Impura.

**Por qué:** Utiliza y modifica una variable global ,cambia el estado del programa fuera de su propio ámbito, es no determinista porque si la llamas dos veces seguidas sin pasarle argumentos, devuelve resultados diferentes ("ID-1", "ID-2")

Cómo convertirla a Pura: Hay qur pasar el estado actual como argumento y devolver el nuevo estado

Python

def siguiente_id_pura(contador_actual):
    nuevo_contador = contador_actual + 1
    return f"ID-{nuevo_contador}"

## Función C: agregar_fecha
**Estado:** Impura.

**Por qué:** Es no determinista porque usa datetime.now() y su resultado cambia cada vez que lo ejecutas
Tambien modifica el diccionario registro que recibe como argumento 

Cómo convertirla a Pura: Hay que pasar la fecha como argumento  y crear una copia del diccionario en lugar de modificar el original

Python

def agregar_fecha_pura(registro, fecha_iso):
    nuevo_registro = registro.copy()
    nuevo_registro['fecha'] = fecha_iso
    return nuevo_registro

## Función D: filtrar_positivos
**Estado:** Pura.

**Por qué:** Es determinista

## Función E: mezclar_lista
**Estado:** Impura.

**Por qué:** Es no determinista porque usa random

Tambien random.shuffle(lista) mezcla la lista in-place 

Cómo convertirla a Pura: Arreglar la mutacion

Python

import random
def mezclar_lista_pura(lista):
    # random.sample crea una nueva lista mezclada
    # sin tocar la original
    return random.sample(lista, len(lista))

# Parte 4

**1. ¿Qué significa que una función sea "pura"?**

 Una función pura es la que opera bajo un determinismo, si recibe los mismos datos de entrada, siempre devolverá exactamente el mismo resultado, sin importar el momento o el contexto. Tambien no modifica variables externas, no imprime en consola ni altera el estado del sistema fuera de ella misma; es un proceso totalmente contenido. Esto elimina cualquier incertidumbre en el código, ya que nunca se tiene que estar pendiente ni considerar que los resultados vayan a cambiar.Un ejemplo cotidiano que se me ocurre son las leyes de la fisica, ya que son constantes y si se llegan a aplicar a situaciones identicas de alguna manera en teoria deben producir el mismo resultado, ejemplo si dejas caer un lapiz la gravedad va a actuar siempre sobre este objeto haciendo que caiga, como el experimento donde se deja caer 2 objetos diferentes que caen a misma velocidad cuando no hay resistencia del aire

**2. En la Parte 3, ¿por qué `crear_transformador` retorna una función en lugar de aplicar directamente la transformación? ¿Qué ventaja ofrece este diseño?**
Este diseño separa la configuración de la ejecución, esto nos ayuda a crear funciones personalizadas en lugar de realizar la tarea de una. Al retornar una función, ganamos la ventaja de la reutilización y modularidad porque definimos la lógica una sola vez y podemos aplicar esa herramienta generada en múltiples listas distintas sin reescribir código. Esto es importante para la composición de funciones, ya que nos permite encadenar operaciones pequeñas en un "pipeline" de procesamiento limpio y legible. Si la función transformara los datos directamente, perderíamos la capacidad de conectar estos bloques de construcción de manera flexible y tendríamos que gestionar bucles manuales repetitivamente

**3. ¿Qué dificultades encontraste al convertir el código imperativo a funcional en la Parte 2? ¿Qué parte fue más difícil y cómo la resolviste?** 
Pues se tiene que cambiar el pensamiento a la hora de scribir el codigo para pasar de usar instrucciones secuenciales y usar mas flujos de datos. Cambiar de bucles for con contadores por ejemplo y cambiar el paradigma. El implementar la funcion de  crear_reductor tuve que pensar cómo acumular un resultado sin usar una variable externa visible. Lo aplique comprendiendo cómo las funciones internas pueden retener y pasar el estado del acumulador como argumento en cada paso, haciendo el proceso como un flujo de datos y no asignando variable por varieble.

**4. Si tuvieras que explicar la diferencia entre programación imperativa y funcional a alguien que no programa, ¿qué analogía usarías?** 
Usaria la analogia de comparacion entre una calculadora y las funciones de Excel ya que la programación imperativa funciona como una calculadora estándar donde debes introducir numeros y operaciones para que vaya camiando el resultado paso por paso. Aquí te enfocas en el como,cambiando manuelmente el resultado cada vez que quieras realzar una operacion. La programación funcional actúa como una fórmula de Excel, donde solo defines **que** es el resultado que buscas en relación con otras celdas sin preocuparte por el orden de ejecución, la fórmula no altera los datos de las celdas de origen, las funciones simplemente toman valores de entrada y devuelven uno nuevo sin cambiar en el resto de la hoja.

