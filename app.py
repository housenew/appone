import streamlit as st
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            <a href="javascript:document.getElementsByClassName('css-cuz8q9 edgvbvh5')[1].click();">
            <p><img src="https://www.freeiconspng.com/uploads/arrow-icon--myiconfinder-23.png" alt="Options" width="50" height="50" style="float:left">Show options</p>
             </a>
            """

from data import *
from input import image_input, webcam_input

st.markdown(hide_st_style, unsafe_allow_html=True)
st.title("Ai Art for NFT Generation")
st.sidebar.title('Input Source:')
method = st.sidebar.radio('Select:', options=['Webcam', 'Image'])
st.sidebar.header('Art Styles Available:')

style_model_name = st.sidebar.selectbox("Select style for transformation: ", style_models_name)



if method == 'Image':
    image_input(style_model_name)
else:
    webcam_input(style_model_name)
