import streamlit as st
import pandas as pd
import utils as ul
from urllib.error import URLError
st.subheader("Data Visualization with Table 📝")

# read data from csv  

def draw_table(df):
    df.rename(columns = {'Number' : 'Number of Burned Down Houses' }, inplace = True)
    total_houses = 0

    #description
    st.markdown('''<br>
    The following data illustrates the estimation of burned down houses in each village.
    <br><br>
    ''', unsafe_allow_html = True)

    rslt_df = ul.select_condition(df)
    if rslt_df.empty :
        st.markdown("The corresponding data does not exist. Please choose at least one condition.")

    else:
        st.write(rslt_df[['Name', 'Number of Burned Down Houses', 'Date', 'Region']])
        for index, row in rslt_df.iterrows():
            total_houses += row['Number of Burned Down Houses']
        st.write("Total Burned down houses (estimate) :  " + str(total_houses))     
        
try:
    df = ul.read_file()
    draw_table(df)        
        
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
    draw_table(df)
