from openai import OpenAI
import PyPDF2

# Initialize the OpenAI client
client = OpenAI()

# Paths to the two PDF files
pdf_path1 = "Alessandro-Sica-CV.pdf"
pdf_path2 = "Profile.pdf"

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
            "content": f"print the contenct of this document:\n\n{combined_pdf_text}"
        }
    ]
)

# Print the response
print(completion.choices[0].message)
