import streamlit as st

from data import *
from input import image_input, webcam_input


st.title("Ai Art for NFT Generation")
st.sidebar.title('Input Source:')
method = st.sidebar.radio('Select:', options=['Webcam', 'Image'])
st.sidebar.header('Art Styles Available:')

style_model_name = st.sidebar.selectbox("Select style for transformation: ", style_models_name)
st.header("ahoy")
hide_st_style = """
               <style>
               #MainMenu {visibility: hidden;}
               footer {visibility: hidden;}
               header {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)
if method == 'Image':
    image_input(style_model_name)
else:
    webcam_input(style_model_name)
