from rest_framework import serializers
from .models import Diary

class DiarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Diary
        fields = ['diaryKey', 'title', 'content', 'testImage', 'writtenDate', 'openPoint', 'numView', 'numLike']
