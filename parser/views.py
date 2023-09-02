from rest_framework import generics

from parser.models import Problem
from parser.serializers import ProblemCreateSerializer, ProblemListSerializer, ProblemDetailSerializer


class ProblemCreateAPIView(generics.CreateAPIView):
    """View to create a problem."""
    serializer_class = ProblemCreateSerializer


class ProblemListAPIView(generics.ListAPIView):
    """View to get a list of problems."""
    serializer_class = ProblemListSerializer
    queryset = Problem.objects.all()


class ProblemDetailAPIView(generics.RetrieveAPIView):
    """View to get a particular problem by its id."""
    serializer_class = ProblemDetailSerializer
    queryset = Problem.objects.all()
