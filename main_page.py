#!/usr/bin/env python3

import streamlit as st
import streamlit.components.v1 as components
import PyPDF2
from openai import OpenAI

# Disable the sidebar
st.set_option("client.showSidebarNavigation", False)

# Page title
st.title("Have a goal? We will get you there.")

# Making Page Background
st.markdown (
    '''
    <style>
    .stApp {
    background-image: url("https://img.freepik.com/free-vector/gradient-colored-wavy-background_23-2148397558.jpg?t=st=1731200427~exp=1731204027~hmac=5508c8b49539ac9e21d3eea90e47fbbf57b15e0f3e37fb4f52c5a8b5953beb7b&w=900")!important;
    background-size: cover!important;    
    }
    </style>
    ''',
    unsafe_allow_html=True
)

# File uploader for user to upload PDF files
uploaded_files = st.file_uploader(
    "Upload your CV and/or LinkedIn export",
    type=['pdf'],
    accept_multiple_files=True
)

# Initialize the OpenAI client
client = OpenAI()

# Function to extract text from an uploaded PDF file
def extract_pdf_text(uploaded_file):
    text = ""
    if uploaded_file is not None:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text

# name = st.text_input("I want to be a...", placeholder="Software Engineer"

html_file = 'myhtml.html'

with open(html_file, 'r') as file:
    html_contents = file.read()

components.html(html_contents)

pdf_text = ""
if st.button("Get your career path!") and uploaded_files:
    for file in uploaded_files:
        pdf_text += extract_pdf_text(file)

    # Create the completion with the PDF content embedded in the message
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": f"Print the content of this document:\n\n{pdf_text}"
            }
        ]
    )

    # Save in a shared variable between pages
    st.session_state['data'] = completion.choices[0].message