import csv
import streamlit as st
import matplotlib.pyplot as plt


from pathlib import Path

import csv
from pathlib import Path

# Ubicacion del archivo CSV
ARCHIVO_CSV = Path(__file__).parent / "gastos.csv"

# Columnas que tpython3 -m pip install matplotlibendra nuestro archivo
COLUMNAS = [
    "fecha",
    "concepto",
    "categoria",
    "cantidad",
    "descripcion"
    ]
def guardar_gastos(gastos):
    with open(ARCHIVO_CSV, "w", newline="", encoding="utf-8") as archivo:
        
        
        escritor = csv.DictWriter(
            archivo,
            fieldnames=COLUMNAS
        )
        
        escritor.writeheader()
        escritor.writerows(gastos)
        
        
def cargar_gastos():
    
    gastos = []
    
    if not ARCHIVO_CSV.exists():
        return gastos 
    
    with open(ARCHIVO_CSV,"r", newline="", encoding="utf-8") as archivo:
        
        lector = csv.DictReader(archivo)
        
        for fila in lector:
            
            fila["cantidad"] = float(fila["cantidad"])
            
            gastos.append(fila)
            
    return gastos


import streamlit as st



def mostrar_historial(gastos):
    
    
    st.subheader("Historial de gastos")
    
    
    if not gastos:
        st.info("Todavia no hay gastos registrados.")
        return
    
    st.dataframe(
        gastos,
        use_container_width=True
    )
    
import streamlit as st



def mostrar_historial(gastos):
    
    st.subheader("Historial de gastos")
    
    
    if not gastos:
        st.info("Todavia no hay gastos resgistrados.")
        return
    
    st.dataframe(
        gastos,
        use_container_width=True  
    )
    
    eje.pie(
        totales_categoria.values(),
        labels=totales_categoria.keys(),
        autopct="%1.1f%%"
    )
    
    eje.set_title("Porcentaje de gastos por categoria")
    
    
    st.pyplot(figura)
    
    
    plt.close(figura)