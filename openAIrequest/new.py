import os
import openai
openai.api_key = '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'

completion = openai.Completion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Tell the world about the ChatGPT API in the style of a pirate."}
  ]
)

print(completion.choices[0].message.content)