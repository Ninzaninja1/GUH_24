from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
    {
      "role": "system",
      "content":"You are a helpful assistant that only answers how to get to future careers"
    },
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "In the future I want to be a Software Enineer, What would my progression be in 6 steps from highschool"
        }
    ]
)

print(completion.choices[0].message)
