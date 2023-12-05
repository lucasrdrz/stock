import streamlit as st
import pandas as pd 
import random
from datetime import date
import datetime
from template import *

todayDate = datetime.date.today()
#currentYear = date.today().year
rondomNumber=(random.randint(0,10000))

#load excel file
df=pd.read_excel('stock.xlsx', sheet_name='Hoja1')


# Crear una lista de productos únicos para la selección
productos = df['producto'].unique()

# Crear una interfaz de usuario con Streamlit
st.title('Gestor de Stock')

# Multiselección de productos
selected_productos = st.multiselect('Selecciona productos:', productos)

# Mostrar la información de los productos seleccionados
if selected_productos:
    st.write('Información de productos seleccionados:')
    st.write(df[df['producto'].isin(selected_productos)])

    # Agregar campos de entrada para la cantidad manual
    cantidad_manuales = {}
    for producto in selected_productos:
        cantidad_manuales[producto] = st.number_input(f'Ingresa la cantidad para {producto}:', key=producto)

    # Actualizar el DataFrame con las cantidades manuales
    for producto, cantidad_manual in cantidad_manuales.items():
        df.loc[df['producto'] == producto, 'Cantidad Utilizada'] = cantidad_manual

    # Botón para exportar a un nuevo archivo Excel
    if st.button('Exportar a Excel'):
        df[df['producto'].isin(selected_productos)].to_excel('stock_seleccionado.xlsx', index=False)
        st.success('Se exportó la selección a stock_seleccionado.xlsx')
else:
    st.warning('Por favor, selecciona al menos un producto.')

