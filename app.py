import streamlit as st

from registro import formulario_gastos

from calculos import (
    calcular_total,
    calcular_promedio,
    obtener_gasto_mayor,
    calcular_totales_categoria
)
from historial import (
    guardar_gastos,
    cargar_gastos,
    mostrar_historial,
    mostrar_graficas
)

st.title("Calculadora de Gastos Personales")

st.write("Bienvenido. Aquí puedes registrar tus gastos, ver estadísticas y analizar tus hábitos de consumo.")

if "gastos" not in st.session_state:
    st.session_state.gastos = cargar_gastos()

st.header("Registro de Gastos")

nuevo_gasto = formulario_gastos()

if nuevo_gasto is not None:
    st.session_state.gastos.append(nuevo_gasto)
    guardar_gastos(st.session_state.gastos)
    st.rerun()

gastos = st.session_state.gastos

st.header("Resumen de Gastos")

if len(gastos) > 0:
    total = calcular_total(gastos)
    promedio = calcular_promedio(gastos)
    mayor = obtener_gasto_mayor(gastos)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total gastado", f"${total:.2f}")
    with col2:
        st.metric("Promedio", f"${promedio:.2f}")

    st.subheader("Gasto de mayor cantidad")
    st.write(mayor)

    st.subheader("Gastos por categoria")
    st.write(calcular_totales_categoria(gastos))


    st.header("Historial de gastos")

    mostrar_historial(gastos)


    st.header("Graficas de gastos")

    mostrar_graficas(gastos)

else:
    st.info("No hay gastos registrados aún. Por favor, registra un gasto para ver el resumen y las estadísticas.")