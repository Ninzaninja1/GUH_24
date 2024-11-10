#!/usr/bin/env python3 

import streamlit as st
import streamlit.components.v1 as components
import PyPDF2
from openai import OpenAI
from datetime import datetime 

# Disable the sidebar
st.set_option("client.showSidebarNavigation", False)

# Custom CSS for button and other styling
st.markdown(
    '''
    <style>
    .stApp {
    background-image: url("https://i.pinimg.com/originals/a9/4a/ee/a94aee835e16cff4f14c83dac8ffbe10.gif")!important;
    background-size: cover!important;    
    }
    .stTextInput label, .stFileUploader label {
        color: white !important;
    }

    .title {
        color: white;
        font-weight: bold;
        font-size: 4em; /* Increase the title size */
        text-align: left;
        margin-top: -0.5em; /* Reduce space between titles */
    }

    /* Button Styling */
    .stButton button {
        background-color: white !important;
        color: black !important;
        border: 1px solid black !important;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
    }

    .stButton button:hover {
        background-color: #f0f0f0 !important;
    }

    .st-emotion-cache-qcpnpn, hr {
        border: 2px solid white !important;
    }
    </style>
    ''',
    unsafe_allow_html=True
)

# Page title with custom class 'title' for styling
st.markdown('<h1 class="title">Have a goal?</h1>', unsafe_allow_html=True)
st.markdown('<h1 class="title">We will get you there.</h1>', unsafe_allow_html=True)

age = st.text_input("Age")
current_datetime = datetime.now()
current_year = current_datetime.year

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

col1, col2 = st.columns([5,3])  # Creates two equal-width columns
with col1:
    components.html(html_contents)
with col2:
    dream_career = st.text_input("Career role", label_visibility="hidden", placeholder="a GUH Hacker!")

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
                "content": f"""Map a career path for this person, aged {age} in the year {current_year}, based on the information provided below (under "Extra Information"), which are their current CV and LinkedIn profile.

Extra information:
{pdf_text}

Take into account the dream career that this person wants to achieve, which is {dream_career}. Map a clear, detailed career path from this person's age to their dream career, with intervals. I want you to heavily utilise and consider their CV and LinkedIn profile above, by analysing their strengths and interests, and take them into serious consideration when mapping out their career path. Start with intervals of 6 months at first, then gradually increase the length of time for each interval, with a maximum of 10 years per interval, until this person can realistically achieve their dream career, and continue until retirement age. Be really careful when linking the age and the year. Use gender neutral pronouns when addressing this person. For each interval, give me this person's age and the year. List me 3 goals that this person needs to achieve during each stage, and what strategy this person needs to adopt to realistically achieve those goals. List me at least 4 technical skills this person needs, and how can this person learn these skills, by giving me specific courses and projects to do. Give me the general and relevant links to each of these courses and projects (the main webpage), but make sure that all the links work. Recommended internships or jobs for this person, and give me resources and advice on how this person can get those internships/jobs, along with the website links for this. Give me the expected salary. Give me at least 3 pros and cons for these career decisions, for every single stage of age. Give me essential career events to attend, and how can these person register for them. I want you to go into detail, a step-by-step analysis on how to achieve career goals and milestones, with it being very specific, detailed and well-explained, with as many important website URLs in the answer. Do not start with an introduction to my prompt.
"""
            }
        ]
    )

    response_text = completion.choices[0].message.content

    # Split the response into different stages based on the word "Age"
    prompt = f"Create an image which shows a group of people (male and female, and from every race) who look professional and whose description matches with the profile specified in the following text file. The description should be based on the career path outlined below (don't include any text in the created image):\n\n{dream_career}"

    # Generate an image based on the career profile described in the last section
    response = client.images.generate(
      model="dall-e-3",
      prompt=prompt,
      size="1024x1024",
      quality="standard",
      n=1,
    )

    # Display the image URL generated by DALL·E
    image_url = response.data[0].url
    st.image(image_url, use_container_width=True)

    container = st.container(border=True)
    container.markdown(response_text)