import os
import openai
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
with open(BASE_DIR / 'OPENAI_KEY.py') as f:
    SECRET_KEY = f.read().strip()


openai.api_key = SECRET_KEY
model_engine = "text-davinci-003"


def completionQuery():
  print('completQuery')
  prompt = ('Write me a bio (a text introduction about myself) using multiple inputs:/n The tone of voice to use./n Some personal information:/n - My full name/n - My education level/n - My gender/n Some examples of other bio./n Informations I want to emphasize./n Then, only after my answer, generate the bio./n')

  text_input = ('Tone of voice: professional/n Full name: Manuel Cecere Palazzo/n Education level: Ms student/n Gender: Male/n Bio examples:/n -Creative and Technical ML and Web Development Professional. Effectively provides end-to-end service, collaborates in projects that involve database and building user-facing websites. Proficient working with front and back ends of a website or application. Positive and adaptable, works cooperatively with team members and strives towards achieving a common goal. Demonstrates great interest and passion in learning new programming languages./n Specific information:/n - Passionate for AI for social good/n - Binge reader/n - Extrovert/n')

  prompt += "/n" + text_input

  completion = openai.Completion.create(
                                    engine = model_engine,
                                    prompt = prompt,
                                    max_tokens = 1024,
                                    n = 1,
                                    temperature = 0.1,
                                        )

  print(completion.choices[0].text)


def generateBio(input_values = []):
  messages = [
 {"role": "system", "content" : "You're a kind helpful assistant"}
]
  initial_prompt = ('Write me a bio (a text introduction about myself) using multiple inputs:/n The tone of voice to use./n Some personal information:/n - My full name/n - My education level/n - My gender/n Some examples of other bio(if none, ignore it)./n Informations I want to emphasize./n Then, only after my answer, generate the bio./n')
  
  # just a placeholder
  # input_values = ("Tone of voice: professional/n Full name: Manuel Cecere Palazzo/n Education level: Ms student/n Gender: Male/n Bio examples:/n -Creative and Technical ML and Web Development Professional. Effectively provides end-to-end service, collaborates in projects that involve database and building user-facing websites. Proficient working with front and back ends of a website or application. Positive and adaptable, works cooperatively with team members and strives towards achieving a common goal. Demonstrates great interest and passion in learning new programming languages./n Specific information:/n - Passionate for AI for social good/n - Binge reader/n - Extrovert/n")

  content = initial_prompt + ' '.join(input_values)
  messages.append({"role": "user", "content": content})

  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
    temperature = 0,
  )

  chat_response = completion.choices[0].message.content
  print(f'ChatGPT: {chat_response}')
  messages.append({"role": "assistant", "content": chat_response})
  return completion.choices[0].message.content

def writeShorter(old_bio):

  print("let's write shorter")
  content = ("Rewrite it shorter")
  messages = [{"role": "system", "content" : old_bio},]
  
  messages.append({"role": "user", "content": content})
  
  completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages= messages,temperature = 0,)
  chat_response = completion.choices[0].message.content
  
  print(f'ChatGPT: {chat_response}')
  messages.append({"role": "assistant", "content": chat_response})
  return messages

def generateCL(input_values = []):
  messages = [
  {"role": "system", "content" : "You're a kind helpful assistant"},
  ]
  initial_prompt = ('Write me a Cover Letter with the next information:\n')
  keys = ['\nfirst_name: ','\nlast_name: ','\nemail: ','\ndesired_pos: ','\nexperience years: ','\nskills: ','\nexperience_level: ','\nachievements: ','\ncompany_name: ','\ncompany_representative: ','\ncompany_email: ', '\nwhy I am a good fit (if empty, it iss the AI job): ']
  input_with_keys = [varName+str(varContent) for varName,varContent in zip(keys,input_values)]
  

  content = initial_prompt + ' '.join(input_with_keys)
  print(content)
  messages.append({"role": "user", "content": content})

  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
    temperature = 0,
  )

  chat_response = completion.choices[0].message.content
  print(f'ChatGPT: {chat_response}')
  messages.append({"role": "assistant", "content": chat_response})
  return completion.choices[0].message.content