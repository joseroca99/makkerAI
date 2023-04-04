import os
import openai
openai.api_key = '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'
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
  initial_prompt = ('Write me a bio (a text introduction about myself) using multiple inputs:/n The tone of voice to use./n Some personal information:/n - My full name/n - My education level/n - My gender/n Some examples of other bio./n Informations I want to emphasize./n Then, only after my answer, generate the bio./n')
  
  # just a placeholder
  # input_values = ("Tone of voice: professional/n Full name: Manuel Cecere Palazzo/n Education level: Ms student/n Gender: Male/n Bio examples:/n -Creative and Technical ML and Web Development Professional. Effectively provides end-to-end service, collaborates in projects that involve database and building user-facing websites. Proficient working with front and back ends of a website or application. Positive and adaptable, works cooperatively with team members and strives towards achieving a common goal. Demonstrates great interest and passion in learning new programming languages./n Specific information:/n - Passionate for AI for social good/n - Binge reader/n - Extrovert/n")

  content = initial_prompt + ' '.join(input_values)
  messages.append({"role": "user", "content": content})

  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
  )

  chat_response = completion.choices[0].message.content
  print(f'ChatGPT: {chat_response}')
  messages.append({"role": "assistant", "content": chat_response})
  return completion.choices[0].message.content

def writeShorter(messages):

  print("let's write shorter")
  content = ("Rewrite it shorter")
  
  messages.append({"role": "user", "content": content})
  
  completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages= messages)
  chat_response = completion.choices[0].message.content
  
  print(f'ChatGPT: {chat_response}')
  messages.append({"role": "assistant", "content": chat_response})
  return messages
