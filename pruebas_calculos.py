
# Importamos las funciones de nuestro modulo
from calculos import (
    calcular_total,
    calcular_promedio,
    obtener_gasto_mayor,
    calcular_totales_categoria
)

# Creamos algunos gastos de prueba
gastos = [

    {
        "fecha": "04/11/2026",
        "concepto": "Comida",
        "categoria": "Alimentacion",
        "cantidad": 200.00,
        "descripcion": "Comida del dia"
    },

    {
        "fecha": "04/11/2026",
        "concepto": "Gasolina",
        "categoria": "Transporte",
        "cantidad": 300.00,
        "descripcion": "Carga de gasolina"
    },

    {
        "fecha": "04/11/2026",
        "concepto": "Cine",
        "categoria": "Entretenimiento",
        "cantidad": 150.00,
        "descripcion": "Entrada al cine"
    },

    {
        "fecha": "04/11/2026",
        "concepto": "Supermercado",
        "categoria": "Alimentacion",
        "cantidad": 250.00,
        "descripcion": "Compra de alimentos"
    }
]

# Probamos las funciones

print("TOTAL DE GASTOS:")
print(calcular_total(gastos))

print("\nPROMEDIO DE GASTOS:")
print(calcular_promedio(gastos))

print("\nGASTO MAS ALTO:")
print(obtener_gasto_mayor(gastos))

print("\nGASTOS POR CATEGORIA:")
print(calcular_totales_categoria(gastos))
