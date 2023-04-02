from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from basicResponse.serializers import AnswerSerializer
import openai

openai.organization = "org-k7JJucHwkXScCNUznzVQ7oet"
openai_api_key='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'
        

# Create your views here.
@api_view(['POST'])
def asking_to_gpt(request):

    if request.method == 'POST':
        
        serializer = AnswerSerializer(data=request.data)
        
        if serializer.is_valid():
            print(serializer.validated_data)
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

