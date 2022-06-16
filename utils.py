import streamlit as st
import pandas as pd
from urllib.error import URLError

def read_file():
    file_path = "house.csv"
    df = pd.read_csv(file_path)
    df = df.dropna()
    return df

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

        
def read_local_data():
    data = {
        "Name" : ['Zaw Chaung', 'A Lal Khone', 'Shaw Phyu Kone', 'Kyun Kone', 'Kine Ma', 'Sar Gyin', 
                  'Hnaw Kone', 'In Pin', 'Chan Thar', 'Se Sone', 'Than Te', 'Mone Tai Pin'],
        "Number" : [89, 164, 148, 4, 11, 6, 50, 12, 21, 7, 2, 29],
        "Date" : [ '6/8/22', '6/8/22', '6/6/22', '6/6/22', '6/5/22', '5/14/22', '6/6/22', '5/7/22', '5/7/22',
                 '5/10/22', '5/7/22', '5/10/22'],
        "Region" : ['Kanbalu', 'Kanbalu', 'Kanbalu', 'Kanbalu', 'Kanbalu', 'Kanbalu', 
                    'Ye U', 'Ye U', 'Ye U', 'Ye U', 'Ye U', 'Ye U']
    }
    df = pd.DataFrame(data)
    df = df.dropna()
    return df.rename(columns = {'Name' : 'index'}).set_index('index')