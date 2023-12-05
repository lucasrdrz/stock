import streamlit as st
import pandas as pd 
import random
from datetime import date
import datetime
from template import *

st.set_page_config(page_title='Dashboard', page_icon=None, layout='wide', initial_sidebar_state='auto')
st.markdown("##")

UI()
st.markdown("##")

todayDate = datetime.date.today()
#currentYear = date.today().year
rondomNumber=(random.randint(0,10000))

#load excel file
df=pd.read_excel('stock.xlsx', sheet_name='Hoja1')




#form
st.sidebar.header("Add New Product")
options_form=st.sidebar.form("Option Form")
product_name=options_form.text_input("name")
product_type=options_form.selectbox("Type",{"New","Used"})
category=options_form.selectbox("Type",{"Soap","Perfume","Lotion","Other"})
serial_number=options_form.text_input("Product ID",value=rondomNumber,disabled=True)
date_added=options_form.text_input("Registered",value=todayDate,disabled=True)
purchasing_price=options_form.number_input("Purchasing price")
selling_price=options_form.number_input("Selling Price")
add_data=options_form.form_submit_button(label="Add new record")

#when button is clicked
if add_data:
 if product_name  !="":
     df = pd.concat([df, pd.DataFrame.from_records([{ 
         'producto': product_name,
         'tipo':product_type,
         'tipo':category,
         'PK':serial_number,
         }])])
     try:
        df.to_excel("stock.xlsx",index=False)
     except:
        st.warning("Unable to write, Please close your dataset !!")
 else:
    st.sidebar.error("product name required")

with st.expander("Records"):
  shwdata = st.multiselect('Filter :', df.columns, default=['PK','producto','Tipo','Cantidad Actual','Cantidad Utilizada','Cantidad Total','Precio'])
  st.dataframe(df[shwdata],use_container_width=True)

