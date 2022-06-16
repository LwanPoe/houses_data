import streamlit as st
import utils as ul

st.subheader("Loss of houses after burning down")
'''The residents lost storehouses full of crops and food for animals as well as their homes, built over generations.'''

#https://s3-us-west-2.amazonaws.com/uw-s3-cdn/wp-content/uploads/sites/6/2017/11/04133712/waterfall.jpg
img1 = "image/image1.jpg"
img2 = "image/image2.jpg"
img3 = "image/image3.jpg"

img_arr = [img1, img2, img3] 

col1, col2, col3 = st.columns(3)

with col1:
    st.image(img1, caption = "Ref : facebook pages")

with col2:
    st.image(img2, caption = "Ref : facebook pages")

with col3:
    st.image(img3, caption = "Ref : facebook pages")
