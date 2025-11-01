"""
Modulo de utilidades para el manejo de finanzas personales.
Con funcion auxiliar para maneajar los datos
"""

def formatear_moneda(monto: float) -> str:
    """
    Args:
        monto (float): El valor numerico a formatear.

    Returns:
        str: El valor formateado con el simbolo '$' y separador de miles y dos decimales.
    """
    return f"${monto:,.2f}"