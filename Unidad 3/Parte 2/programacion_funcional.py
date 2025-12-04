def venta_valida(venta):
    return venta['monto'] > 100

def transformar_venta(venta):
    return {
        'id': venta['id'],
        'monto_original': venta['monto'],
        'monto_final': venta['monto'] * 1.15
    }

def obtener_monto_final(venta):
    return venta['monto_final']

def procesar_venta(ventas):

    ventas_filtradas = list(filter(venta_valida, ventas))
    resultado = list(map(transformar_venta, ventas_filtradas))
    montos = map(obtener_monto_final, resultado)
    total = sum(montos)
    
    return resultado, total

datos_prueba = [
    {'id': 1, 'monto': 50},
    {'id': 2, 'monto': 150},
    {'id': 3, 'monto': 200},
    {'id': 4, 'monto': 80},
    {'id': 5, 'monto': 300},
]

lista_resultado, total_resultado = procesar_venta(datos_prueba)

print("Lista Resultado:", lista_resultado)
print("Total:", total_resultado)