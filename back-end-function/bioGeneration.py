import openai
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
openai.organization = "org-k7JJucHwkXScCNUznzVQ7oet"
with open(BASE_DIR / 'openAIrequest' / 'etc' / 'OPENAI_KEY.py') as f:
    openai_api_key = f.read().strip()

def bioWriting(**serializer_data):

    #building prompt for AI
    prompt= 'Write bio with the next information:\n'\
        'first name: {}\n'\
        'last name: {}\n'\
        'date of birth: {}\n'\
        'phone number: {}\n'\
        'adress line: {}\n'\
        'email: {}\n'\
        'The bio must have a {} tone and emphatize on {}.'.format(
            serializer_data['first_name'],
            serializer_data['last_name'],
            serializer_data['date_of_birth'],
            serializer_data['phone_number'],
            serializer_data['address_line'],
            serializer_data['email_address'],
            serializer_data['tone'],
            serializer_data['strength']
        )
    try:
        prompt = '\n'.join([prompt,
                            ('Use the next bio as an example:\n{}'
                            .format(serializer_data['example']))])
    except KeyError:
        print('No bio example, OK!')

    #sending prompt to openai and reading response
    openai.api_key = openai_api_key
    openaiResponse = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=3500,
        temperature=0
    )
    return openaiResponse['choices'][0]['text']

#EXAMPLE HOW TO USE:
bio = bioWriting(first_name = 'Jhon', 
                 last_name = 'Smith', 
                 date_of_birth = '1992-01-02', 
                 phone_number ='+3 142-948-1846', 
                 address_line = '123 Baker St', 
                 email_address = 'jhon@gmail.com', 
                 tone = 'hard', 
                 strength = 'pacience',)
print(bio)