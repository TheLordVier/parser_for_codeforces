from rest_framework import serializers

from parser.models import Problem
from parser.services import problem_data_create


class ProblemCreateSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        problem_data_create()
        return Problem.objects.all()

    class Meta:
        model = Problem
        fields = ()


class ProblemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ('problem_name', 'rating',)


class ProblemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ('problem_name', 'rating', 'themes', 'number_solutions', 'number',)
