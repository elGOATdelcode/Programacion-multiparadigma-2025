def crear_transformador(funcion):
    def transformador(lista):
        return [funcion(x) for x in lista]
    return transformador

def crear_filtro(predicado):
    def filtro(lista):
        return [x for x in lista if predicado(x)]
    return filtro

def crear_reductor(funcion, valor_inicial):
    def reductor(lista):
        acumulado = valor_inicial
        for elemento in lista:
            acumulado = funcion(acumulado, elemento)
        return acumulado
    return reductor

def componer(*funciones):
    def pipeline(data):
        resultado = data
        for f in funciones:
            resultado = f(resultado)
        return resultado
    return pipeline

# Pruebas
numeros = [1, -2, 3, -4, 5, -6, 7, 8, -9, 10]


pipeline = componer(
    crear_filtro(lambda x: x > 0),             
    crear_transformador(lambda x: x ** 2),     
    crear_reductor(lambda acc, x: acc + x, 0)  )


resultado = pipeline(numeros)

print(f"Lista original: {numeros}")
print(f"Resultado final: {resultado}") 
