this will where our great awesome idea will come to life :D

# Setting up the Python virtual environment

This documentation assumes the use of a `bash` terminal.

Initialise a virtual environment where we can install packages locally, to the folder `.venv` which we will create below.

```python
python -m venv .venv
```

In order to use the packages located in `.venv`, we need to execute the commands located in `.venv/bin/activate`.

```python
source .venv/bin/activate
```

We will then install the necessary packages.

```python
pip install openai
pip install streamlit
```
