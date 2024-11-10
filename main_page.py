#!/usr/bin/env python3

import streamlit as st
import PyPDF2
from openai import OpenAI

# Page title
st.markdown("# Main Page Woohooo")

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

name = st.text_input("What is your future career?")

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

    # Display the response in the Streamlit app
    # st.write(completion.choices[0].message)

    
else:
    st.write("Please upload a PDF file to continue.")