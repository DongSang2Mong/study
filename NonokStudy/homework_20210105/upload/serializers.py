from rest_framework import serializers
from .models import Writing, Diary, DiaryImage

class WritingSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Writing
        fields = ('title', 'text', 'image')

class DiaryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaryImage
        fields = ('image')

class DiarySerializer(serializers.ModelSerializer):
    images = DiaryImageSerializer(many=True, read_only=True)

    class Meta:
        model = Diary
        fields = ('title', 'writtenDate', 'contents', 'openPoint', 'numViews', 'numLikes', 'images')

    def create(self, validated_data):
        images_data = self.context['request'].FILES
        diary = Diary.objects.create(**validated_data)
        for image_data in images_data.getlist('image'):
            DiaryImage.objects.create(diary=diary, image=image_data)
        return diary