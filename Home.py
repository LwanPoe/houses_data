import streamlit as st

#This is the first app created using streamlit
st.set_page_config(
    page_title="Houses Data",
    page_icon="🔥",
)

st.header("Burned Down Houses in Myanmar 🔥")
st.markdown("**(_Sagaing Division_)**")
st.markdown('''
    This app will show the data of houses that are burned down by Military since May 2022 in Sagaing Region.<br>
    The data may be a little difference from ground information.<br><br><br>
    Referrence : facebook pages
    
''', unsafe_allow_html=True)