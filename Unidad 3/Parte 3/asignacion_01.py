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


