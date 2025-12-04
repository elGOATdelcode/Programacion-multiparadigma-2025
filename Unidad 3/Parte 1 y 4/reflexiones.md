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