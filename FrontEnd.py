#!/usr/bin/env python3

import streamlit as st
import PyPDF2
from openai import OpenAI

st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)
with open("Timeline1.html", "r") as file:
    html_content = file.read()

# Render the HTML content
st.components.v1.html(html_content, height=800, scrolling=True)