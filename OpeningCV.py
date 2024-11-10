from openai import OpenAI
import PyPDF2

# Initialize the OpenAI client
client = OpenAI()

# Path to the PDF file
pdf_path = "Alessandro-Sica-CV.pdf"

# Extract text from the PDF
pdf_text = ""
with open(pdf_path, "rb") as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    for page in pdf_reader.pages:
        pdf_text += page.extract_text()

# Create the completion with the PDF content embedded in the message
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": f"Summarize the content of this file\n\n{pdf_text}"
        }
    ]
)

# Print the response
print(completion.choices[0].message)
