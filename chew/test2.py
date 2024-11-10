#!/usr/bin/env python3

import streamlit as st
import streamlit.components.v1 as components
import PyPDF2
from openai import OpenAI
from datetime import datetime 

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

# Variables
age = "20"
dream_career = "Electrical Engineer"
current_datetime = datetime.now()
current_year = current_datetime.year

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
                "content": f"""Map a career path for this person, aged {age}. Start with a brief introduction of what this person does right now, like this person's name, age, current education or work status, and what experiences and technical skills this person has, based on the information provided below (under "Extra Information"), which are their current CV and LinkedIn profile.

Extra information:

{pdf_text}

Here is what I want you to do: take into account the dream career that this person wants to achieve, which is {dream_career}. Map a clear, detailed career path from this person's age to their dream career, with intervals. I want you to heavily utilise and consider their CV and LinkedIn profile above, by analysing their strengths and interests, and take them into serious consideration when mapping out their career path. Start with intervals of 6 months at first, then gradually increase the length of time for each interval, with a maximum of 10 years per interval, until this person can realistically achieve their dream career, and continue until retirement age. Be really careful when linking the age and the year. Use gender neutral pronouns when addressing this person. For each interval, give me this person's age and the year. List me 3 goals that this person needs to achieve during each stage, and what strategy this person needs to adopt to realistically achieve those goals. List me at least 4 technical skills this person needs, and how can this person learn these skills, by giving me specific courses and projects to do. Give me the general and relevant links to each of these courses and projects (the main webpage), but make sure that all the links work. Recommended internships or jobs for this person, and give me resources and advice on how this person can get those internships/jobs, along with the website links for this. Give me the expected salary. Give me at least 3 pros and cons for these career decisions, for every single stage of age. Give me essential career events to attend, and how can these person register for them. I want you to go into detail, a step-by-step analysis on how to achieve career goals and milestones, with it being very specific, detailed and well-explained, with as many important website URLs in the answer.

"""
            }
        ]
    )

# Global white text style
st.markdown(
    """
    <style>
    .stApp {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Extract the response text from the OpenAI API's output
response_text = completion.choices[0].message.content

    # Display the career path on Streamlit
st.header("Career Path Guidance")
st.subheader("Introduction")
st.write(f"This is a career path guide for someone aged {age}, with the dream career of a **{dream_career}**.")

    # Display response text in white
st.subheader("Career Path Output")
st.markdown(f"<p style='color: white;'>{response_text}</p>", unsafe_allow_html=True)