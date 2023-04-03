from rest_framework import serializers
from basicResponse.models import Answer

class AnswerSerializer(serializers.Serializer):
    question = serializers.CharField(max_length=None, trim_whitespace=True)
    AIanswer = serializers.CharField(max_length=None, allow_blank=True)

    def create(self, validated_data):
        return Answer.objects.create(**validated_data)
    
    
class PersonalInfoSerializer(serializers.Serializer):
    first_name= serializers.CharField(max_length=30)
    last_name= serializers.CharField(max_length=30)
    date_of_birth= serializers.DateField()
    phone_number = serializers.CharField(max_length=20)
    address_line = serializers.CharField(max_length=None)
    email_address = serializers.EmailField()
    tone = serializers.CharField(max_length=20)
    strength = serializers.CharField(max_length=20)
    example = serializers.CharField(max_length=None, allow_blank=True)
    biography = serializers.CharField(max_length=None, allow_blank=True)

    def create(self, validated_data):
        return Answer.objects.create(**validated_data)