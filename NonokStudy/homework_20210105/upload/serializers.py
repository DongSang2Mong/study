from rest_framework import serializers
from .models import Writing

class WritingSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Writing
        fields = ('title', 'text', 'image')