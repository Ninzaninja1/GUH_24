#!/usr/bin/env python3

import streamlit as st
import streamlit.components.v1 as components
import PyPDF2
from openai import OpenAI

# Disable the sidebar
st.set_option("client.showSidebarNavigation", False)

# Page title
st.title("Have a goal? We will get you there.")

age = st.text_input("Age:")

# Array with file objects
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

# Starting of embedded html for fancy textbox
html_file = 'myhtml.html'
with open(html_file, 'r') as file:
    html_contents = file.read()
col1, col2 = st.columns(2)  # Creates two equal-width columns
with col1:
    components.html(html_contents)
with col2:
    dream_career = st.text_input("______")
    st.text_input("be an GUH Hacker!",label_visibility="hidden")


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

    response_text = completion.choices[0].message.content

    container = st.container(border=True)
    container.markdown(completion.choices[0].message.content)

# Function to split and save each interval as a variable
def split_and_save_intervals(response_text):
    # Split the response into different stages based on the word "Interval"
    stages = response_text.split("Interval")
    
    # Remove any empty sections that may appear after splitting
    stages = [stage.strip() for stage in stages if stage.strip()]
    
    # Create a dictionary to store each stage as a variable
    stages_dict = {}
    
    # Assign each stage to a separate variable in the dictionary
    for i, stage in enumerate(stages):
        stages_dict[f"interval_{i+1}"] = stage
    
    return stages_dict

# Function to display the saved variables in separate boxes
def display_stages(stages_dict):
    # Loop through each stage variable and display it inside a box
    for key, stage in stages_dict.items():
        # HTML for the box style
        html = f"""
        <div style="background-color: #f9f9f9; padding: 15px; margin: 10px 0; border: 1px solid #ddd; border-radius: 8px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
            <h4 style="color: #333; font-size: 1.2em; font-weight: bold;">{key}</h4>
            <p style="color: #555; line-height: 1.6;">{stage}</p>
        </div>
        """
        # Display the HTML content in the Streamlit app
        components.html(html, height=300)