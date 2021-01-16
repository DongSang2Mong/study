from django.shortcuts import render
from rest_framework import viewsets

from .serializers import DiarySerializer
from .models import Diary

# Create your views here.

class DiaryViewset(viewsets.ModelViewSet):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer