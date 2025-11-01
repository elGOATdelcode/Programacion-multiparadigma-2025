"""
Modulo principal del modelo de datos para la aplicacion de finanzas personales.
"""

# Se importa la utilidad de formato desde el mismo paquete
from .utilidades import formatear_moneda
from typing import List

class Transaccion:

    def __init__(self, descripcion: str, monto: float, tipo: str):
        """
        Inicializa una nueva transaccion.

        Args:
            descripcion (str): Breve descripción de la transaccion (ej. "Sueldo").
            monto (float): La cantidad de dinero asociada.
            tipo (str): El tipo de transaccion ('I' para Ingreso, 'E' para Egreso).
        """
        self.descripcion = descripcion
        self.monto = abs(monto)  
        self.tipo = tipo.upper()

    def __str__(self) -> str:

        signo = "+" if self.tipo == 'I' else "-"
        monto_formateado = formatear_moneda(self.monto)
        return f"[{self.tipo}] {self.descripcion:<30} {signo}{monto_formateado}"


class GestorFinanzas:
    """
    Gestiona una coleccion de objetos Transaccion y proporciona metodos
    para manipular y calcular el saldo financiero.
    """
    def __init__(self):
        self.transacciones: List[Transaccion] = []

    def agregar_transaccion(self, transaccion: Transaccion):
        
        self.transacciones.append(transaccion)

    def calcular_saldo(self) -> float:
        """
        Calcula el saldo total sumando todos los ingresos y restando todos los egresos.

        Returns:
            float: El saldo financiero actual.
        """
        saldo = 0.0
        for t in self.transacciones:
            if t.tipo == 'I':
                saldo += t.monto
            elif t.tipo == 'E':
                saldo -= t.monto
        return saldo

    def obtener_transacciones_por_tipo(self, tipo: str) -> List[Transaccion]:
        tipo = tipo.upper()
        return [t for t in self.transacciones if t.tipo == tipo]