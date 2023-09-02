from django.urls import path

from parser.views import ProblemCreateAPIView, ProblemListAPIView, ProblemDetailAPIView

app_name = 'parser'

urlpatterns = [
    path('add_problems/', ProblemCreateAPIView.as_view(), name='add_problems'),
    path('problems/', ProblemListAPIView.as_view(), name='problems'),
    path('problems/<int:pk>/', ProblemDetailAPIView.as_view(), name='problem'),
]
