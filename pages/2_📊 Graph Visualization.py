import tkinter
import streamlit as st
import pandas as pd
import utils as ul
from urllib.error import URLError


def draw_graph(df):
    st.markdown('''<br>
    The following data illustrates the estimation of burned down houses in each village.
    <br><br>
    ''', unsafe_allow_html = True)
    rslt_df = ul.select_condition(df)
    if rslt_df.empty :
        st.markdown("The corresponding data does not exist. Please choose at least one condition.")

    else:
        st.bar_chart(rslt_df.Number)
    
st.subheader("Data Visualization with Chart 📊")
#file_path = "C:\\Users\\Nwe Ni\\Desktop\\Python\\house.csv" 
try:
    df = ul.read_file().rename(columns = {'Name' : 'index'}).set_index('index') 
    draw_graph(df)
except URLError as e:
    st.error(
        """
        **This demo requires internet access.**
        Connection error: ...
        The updated data cannot be shown
    """
        
    )
    df = ul.read_local_data()
    #st.write(df)
    draw_graph(df)

