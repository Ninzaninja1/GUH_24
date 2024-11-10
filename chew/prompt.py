from openai import OpenAI
import PyPDF2
import json
import re
import streamlit as st
from datetime import datetime 

# Initialize the OpenAI client
client = OpenAI()

# Paths to the two PDF files
pdf_path1 = "YuXuanChew_Siemens_Healthineers_CV.pdf"
pdf_path2 = "Profile.pdf"

# Collect user input
age = input("Enter your age: ")
dream_career = input("Enter your dream career: ")
current_datetime = datetime.now()
current_year = current_datetime.year

# Function to extract text from a PDF
def extract_pdf_text(pdf_path):
    text = ""
    with open(pdf_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# Extract text from both PDFs
pdf_text1 = extract_pdf_text(pdf_path1)
pdf_text2 = extract_pdf_text(pdf_path2)

# Combine the text from both PDFs
combined_pdf_text = f"First Document Content:\n\n{pdf_text1}\n\nSecond Document Content:\n\n{pdf_text2}"

# Create the completion with both PDF contents embedded in the message
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": f"""Map a career path for this person, aged {age} in the year {current_year}. Start with a brief introduction of what this person does right now, like this person's name, age, current education or work status, and what experiences and technical skills this person has, based on the information provided below (under "Extra Information"), which are their current CV and LinkedIn profile.

Extra information:

{combined_pdf_text}

Here is what I want you to do: take into account the dream career that this person wants to achieve, which is {dream_career}. Map a clear, detailed career path from this person's age to their dream career, with intervals. I want you to heavily utilise and consider their CV and LinkedIn profile above, by analysing their strengths and interests, and take them into serious consideration when mapping out their career path. Start with intervals of 6 months at first, then gradually increase the length of time for each interval, with a maximum of 10 years per interval, until this person can realistically achieve their dream career, and continue until retirement age. Be really careful when linking the age and the year. Use gender neutral pronouns when addressing this person. For each interval, give me this person's age and the year. List me 3 goals that this person needs to achieve during each stage, and what strategy this person needs to adopt to realistically achieve those goals. List me at least 4 technical skills this person needs, and how can this person learn these skills, by giving me specific courses and projects to do. Recommended internships or jobs for this person, and give me resources and advice on how this person can get those internships/jobs. Give me the expected salary. List me at least 3 pros and cons for these career decisions, for every single stage of age. List me essential career events to attend, and how can these person register for them. I want you to go into detail, a step-by-step analysis on how to achieve career goals and milestones, with it being very specific, detailed and well-explained.

"""
        }
    ]
)

# Extract the response text from the OpenAI API's output
response_text = completion.choices[0].message.content

# Save the response text into a user-friendly text file
with open("career_path_output.txt", "w", encoding="utf-8") as file:
    file.write(response_text)

st.write("The career path has been saved to 'career_path_output.txt'.")