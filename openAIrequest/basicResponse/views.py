from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from basicResponse.serializers import AnswerSerializer
from pathlib import Path
import openai

BASE_DIR = Path(__file__).resolve().parent.parent
openai.organization = "org-k7JJucHwkXScCNUznzVQ7oet"
with open(BASE_DIR / 'etc' / 'OPENAI_KEY.txt') as f:
    openai_api_key = f.read().strip()
        

# Create your views here.
@api_view(['POST'])
def asking_to_gpt(request):

    if request.method == 'POST':
        
        serializer = AnswerSerializer(data=request.data)
        
        if serializer.is_valid():
            openai.api_key = openai_api_key
            openaiResponse = openai.Completion.create(
                        model="text-davinci-003",
                        prompt=serializer.validated_data['question'],
                        max_tokens=1000,
                        temperature=0
                    )
            answer = serializer.save()
            serializer = AnswerSerializer(answer, data={'AIanswer': openaiResponse['choices'][0]['text']}, partial=True)
            serializer.is_valid()
            serializer.save()
            
            #print(serializer.data)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse('only POST requests')

