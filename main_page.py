#!/usr/bin/env python3

import streamlit as st
import streamlit.components.v1 as components
import PyPDF2
from openai import OpenAI
import base64

def load_font_as_base64(font_path):
    with open(font_path, "rb") as font_file:
        return base64.b64encode(font_file.read()).decode()

# Path to your local font file
font_base64 = load_font_as_base64("fonts/Kola-Regular.ttf")

# Disable the sidebar
st.set_option("client.showSidebarNavigation", False)

# Page title
st.title("Have a goal? We will get you there.")

<<<<<<< HEAD
# File uploader +
=======
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

<<<<<<< HEAD
# File uploader for user to upload PDF files
=======
# File uploader +
# r user to upload PDF files
>>>>>>> 3ae02f904ed12636252531573c781c1240187839
>>>>>>> b60ff4beb3909f65335574bb7c56ae61501434ce
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

html_file = 'myhtml.html'

with open(html_file, 'r') as file:
    html_contents = file.read()

<<<<<<< HEAD
components.html(html_contents)
 
=======
# Create two columns
col1, col2 = st.columns(2)  # Creates two equal-width columns

# first column
with col1:
    components.html(html_contents)

# second column
with col2:
    st.text_input("______")


>>>>>>> 3ae02f904ed12636252531573c781c1240187839
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

container = st.container(border=True)
container.markdown("# 1st Step Date")
container.markdown("Hear from experts and peers, gain new ideas, and share experiences together.")

container2 = st.container(border=True)
container2.markdown("# 2nd Step Date")
container2.markdown("Hear stories, get fresh ideas, and walk away with motivation to tackle challenges.")