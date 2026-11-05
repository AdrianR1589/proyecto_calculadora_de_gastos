import streamlit as st
def formulario_gastos():

    categorias = [
        "Alimentación",
        "Transporte",
        "Entretenimiento",
        "Servicios",
        "Salud",
        "Otros"
    ]
    with st.form("formulario_registro"):
        st.subheader("Registrar un nuevo gasto")
        fecha = st.date_input("Fecha del gasto")
        concepto = st.text_input("Concepto del gasto")
        categoria = st.selectbox(
            "Categoría del gasto",
            categorias
            )
        cantidad = st.number_input(
            "Cantidad gastada", 
            min_value=0.01,
            step=0.01
            )
        descripción = st.text_input(
            "Descripción del gasto (opcional)"
            )
        boton = st.form_submit_button("Registrar gasto")
    if boton:
        if concepto.strip() == "":
            st.error("Debes ingresar un concepto para el gasto.")
        else:
            gasto = {
                "fecha": fecha.strftime("%d-%m-%Y"),
                "concepto": concepto,
                "categoria": categoria,
                "cantidad": cantidad,
                "descripción": descripción
            }
            st.success("Gasto registrado exitosamente.")
            return gasto
    return None
