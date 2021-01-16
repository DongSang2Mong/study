from django.shortcuts import render

from rest_framework import viewsets
from .serializers import WritingSerializer, DiarySerializer
from .models import Writing, Diary

class WritingViewset(viewsets.ModelViewSet):
    queryset = Writing.objects.all()
    serializer_class = WritingSerializer

class DiaryViewset(viewsets.ModelViewSet):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer