from rest_framework import serializers

from quiz.models import Quiz


class QuizFetchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


