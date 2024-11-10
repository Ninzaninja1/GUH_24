this will where our great awesome idea will come to life :D

# Setting up the Python virtual environment

This documentation assumes the use of a `bash` terminal.

Initialise a virtual environment where we can install packages locally, to the folder `.venv` which we will create:

```python
python -m venv .venv
```

In order to use the packages located in `.venv`, execute the commands located in `.venv/bin/activate`:

```python
source .venv/bin/activate
```

Append to this file to set the environment variable for the OpenAI key, and resource the `activate` file:

```
export OPENAI_API_KEY=""
```

Install the necessary packages:

```python
pip install openai
pip install streamlit
pip install pypdf2
```
