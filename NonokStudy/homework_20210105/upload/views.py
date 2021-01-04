from django.shortcuts import render

from rest_framework import viewsets
from .serializers import WritingSerializer
from .models import Writing

class WritingViewset(viewsets.ModelViewSet):
    queryset = Writing.objects.all()
    serializer_class = WritingSerializer