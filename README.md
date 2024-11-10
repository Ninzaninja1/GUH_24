# Career Compass

In this day and age, time is the most valuable currency. Everyone always has something to do, and would be willing to use a product that can cut down time wastage, and to increase our efficiency in day-to-day tasks. People need convenience, to have everything done by the click of a button. 

University students are especially a key demographic of this growing problem. In between assignments, projects, societies, coursework, internship search and everything beyond, we present a solution to bridge the hap and overcome a key barrier when it comes to their career. We eliminate the element of unknown, save their valuable time, and create a time machine: to let them travel into the future and envision a career path tailored just for them.

# The Solution

Users just have to submit their CV, age and dream career via our frontend interface and we will handle the rest of the job. We will draw a personalised career map for them, detailing what they can expect for each career stage. For each individual stage, we present to the user their ideal goals and the recommended strategies to achieve them, technical skills they need and how they can gain them, internships or jobs that can enhance their learning experience and how they can obtain them, along with the pros and cons at each stage of their career.

This is an impactful solution as we target a wide range of audience. With 3 million university students in the UK (according to the UK parliament) and around 254 million university students across the globe (according to UNESCO), we are saving the most valuable resource - time - of the uprising generation. On an individual level, this increases the convenience of students who are unsure of what they want in their future career, or are not sure on what to do to achieve their career goals, and on a global level, we increase the overall productivity of our future pillars of society.

# Description of Use of AI Agents

Utilising the API key for Open AI, we integrated Open AI's API to produce this personalised career map for each user. We first collected the PDF the user sent via the frontend interface and converted it into text. This text is then fed into the prompt of Open AI's API. On top of this information, we crafted a prompt that is trialed and tested with a wide range of user inputs to produce a detailed career map based on the user's CV and not just tell the user what to expect, but also specifically tell them what they can do to achieve their dream career. We collect the data generated by Open Ai's API and presented it in a clear, concise and user-friendly format, to resonate with our mission to maximise efficiency, comfort and convenience for our user.

# How to run our project

## Setting up the Python virtual environment

This documentation assumes the use of a `bash` terminal.

Initialise a virtual environment where we can install packages locally, to the folder `.venv` which we will create:

```python
python -m venv .venv
```

In order to use the packages located in `.venv`, execute the commands located in `.venv/bin/activate`:

```python
source .venv/bin/activate
```
## Activate Open AI's API Key
Append to this file to set the environment variable for the OpenAI key, and resource the `activate` file:

```
export OPENAI_API_KEY="your_api_key_here"
```

## Installing Packages

Install the necessary packages:

```python
pip install openai
pip install streamlit
pip install pypdf2
```

## Run the code

Run the following code to launch our frontend interface in your web browser:
```
python -m streamlit run .\main_page.py 
```

# User interface

Our product is designed to maximise convenience, so that the input from the user's end is clear and minimal. Type in your age, upload your CV, and type your dream career. Upload the information and a personalised career map will be generated for you.
