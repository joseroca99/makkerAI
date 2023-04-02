from rest_framework import serializers
from basicResponse.models import Answer

class AnswerSerializer(serializers.Serializer):
    question = serializers.CharField(max_length=None, trim_whitespace=True)
    AIanswer = serializers.CharField(max_length=None, allow_blank=True)

    def create(self, validated_data):
        return Answer.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.question = validated_data.get('question', instance.question)
        instance.AIanswer = validated_data.get('AIanswer', instance.AIanswer)
        instance.save()
        return instance