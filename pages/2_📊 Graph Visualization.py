import streamlit as st
import pandas as pd
import utils as ul
from urllib.error import URLError


def select_condition(df):
    #Month mapping
    mm = { 1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May',
          6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October',
          11: 'November', 12: 'December' }
    df['Month'] = pd.DatetimeIndex(df['Date']).month.map(mm)
    col1, col2 = st.columns(2)
    with col1:
        #Choose Region
        slct_rgn = st.multiselect("Choose Region:", list(df.Region.unique()), [df.Region.unique()[0]])
        rslt_df = df[df['Region'].isin(slct_rgn)]
     
    with col2:
        #Choose Month        
        slct_mnt = st.multiselect("Choose Month:", list(df.Month.unique()), [df.Month.unique()[0]])
        if rslt_df.empty:
            rslt_df = df[df['Month'].isin(slct_mnt)]
        else:
            rslt_df = rslt_df[rslt_df['Month'].isin(slct_mnt)]
            if rslt_df.empty:
                rslt_df = df[df['Region'].isin(slct_rgn)]
                
    return  rslt_df

def draw_graph(df):
    st.markdown('''<br>
    The following data illustrates the estimation of burned down houses in each village.
    <br><br>
    ''', unsafe_allow_html = True)
    rslt_df = select_condition(df)
    if rslt_df.empty :
        st.markdown("The corresponding data does not exist. Please choose at least one condition.")

    else:
        st.bar_chart(rslt_df.Number)
    
st.subheader("Data Visualization with Chart")

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

