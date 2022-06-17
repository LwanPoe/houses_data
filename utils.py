import streamlit as st
import pandas as pd
from urllib.error import URLError

def read_file():
    file_path = "house.csv"
    df = pd.read_csv(file_path)
    df = df.dropna()
    return df
        
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
