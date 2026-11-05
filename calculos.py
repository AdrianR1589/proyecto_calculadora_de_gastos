# Funcion 1: Calcular el total de gastos
def calcular_total(gastos):

    total= 0

    for gasto in gastos:
        total += gasto["cantidad"]

    return total


# Funcion 2: Calcular el promedio de gastos
def calcular_promedio(gastos):

    if len(gastos) == 0:
        return 0
    
    total = calcular_total(gastos)

    promedio = total / len(gastos)

    return promedio


# Funcion 3: Obtener el gasto de mayor cantidad
def obtener_gasto_mayor(gastos):

    if len(gastos) == 0:
        return None
    
    gasto_mayor = gastos[0]

    for gasto in gastos:

        if gasto["cantidad"] > gasto_mayor["cantidad"]:
            gasto_mayor = gasto

    return gasto_mayor


# Funcion 4: Calcular los totales por categoria
def calcular_totales_categoria(gastos):

    totales = {}

    for gasto in gastos:

        categoria = gasto["categoria"]
        cantidad = gasto["cantidad"]

        if categoria in totales:
            totales[categoria] += cantidad

        else:
            totales[categoria] = cantidad

    return totales
