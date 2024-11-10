from openai import OpenAI
import PyPDF2
import json
import re
import streamlit as st

# Initialize the OpenAI client
client = OpenAI()

# Paths to the two PDF files
pdf_path1 = "YuXuanChew_Siemens_Healthineers_CV.pdf"
pdf_path2 = "Profile.pdf"

# Collect user input
age = "20"
dream_career = "Electrical Engineer"

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
            "content": f"""Map a career path for this person, aged {age}. Start with a brief introduction of what this person does right now, like this person's name, age, current education or work status, and what experiences and technical skills this person has, based on the information provided below (under "Extra Information"), which are their current CV and LinkedIn profile.

Then, take into account the dream career that this person wants to achieve, which is {dream_career}. Map a clear, detailed career path from this person's age to their dream career, with intervals. Start with intervals of 6 months at first, then gradually increase the length of time for each interval, until this person can realistically achieve their dream career, and continue until retirement age. Use gender neutral pronouns when addressing this person. For each interval, give me this person's age, the year, skills this person needs, recommended internships or jobs, expected salary, pros and cons, and essential career events to attend.

Extra information:

{combined_pdf_text}"""
        }
    ]
)

# Extract the response text from the OpenAI API's output
response_text = completion.choices[0].message.content

# Save the response text into a user-friendly text file
with open("career_path_output.txt", "w", encoding="utf-8") as file:
    file.write(response_text)

st.write("The career path has been saved to 'career_path_output.txt'.")

# Read the text file content
with open("career_path_output.txt", "r", encoding="utf-8") as file:
    content = file.read()

# Split the content into paragraphs
paragraphs = content.split('\n\n')  # Assuming paragraphs are separated by two newlines

# Streamlit page title
st.title("Career Path Mapping")

# Display each paragraph as a separate bubble
for para in paragraphs:
    # Styling each paragraph as a bubble
    st.markdown(f"""
    <div style="background-color: #e0f7fa; padding: 10px; margin: 5px; border-radius: 15px; border: 1px solid #26c6da;">
        <p style="font-size: 16px; color: #00796b;">{para}</p>
    </div>
    """, unsafe_allow_html=True)

# Print the response
# print(completion.choices[0].message)



