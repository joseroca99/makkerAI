from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from basicResponse.serializers import AnswerSerializer, PersonalInfoSerializer
from pathlib import Path
import openai

BASE_DIR = Path(__file__).resolve().parent.parent
openai.organization = "org-k7JJucHwkXScCNUznzVQ7oet"
with open(BASE_DIR / 'etc' / 'OPENAI_KEY.py') as f:
    openai_api_key = f.read().strip()
        

# Create your views here.
@api_view(['POST'])
def asking_to_gpt(request):
    if request.method == 'POST':
        
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer_data=serializer.validated_data
            
            openai.api_key = openai_api_key
            openaiResponse = openai.Completion.create(
                model="text-davinci-003",
                prompt=serializer_data['question'],
                max_tokens=1000,
                temperature=0
            )
            serializer_data['AIanswer'] = openaiResponse['choices'][0]['text']
            serializer = AnswerSerializer(data=serializer_data)
            serializer.is_valid()
            return Response(serializer.validated_data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse('only POST requests')
    
@api_view(['POST'])
def write_general_bio(request):
    if request.method == 'POST':
        
        serializer = PersonalInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer_data=serializer.validated_data
            #building prompt for AI
            prompt= 'Write cover letter with the next information:\n'\
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
            if len(serializer_data['example']) > 0:
                prompt = '\n'.join([prompt,
                                   ('Use the next bio as an example:\n{}'
                                    .format(serializer_data['example']))])

            #sending prompt to openai and reading response
            openai.api_key = openai_api_key
            openaiResponse = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                max_tokens=3500,
                temperature=0
            )
            serializer_data['biography'] = openaiResponse['choices'][0]['text']
            serializer = PersonalInfoSerializer(data=serializer_data)
            serializer.is_valid()
            return Response(serializer.validated_data.get('biography'))
        else:
            print(serializer.errors)
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse('only POST requests')

