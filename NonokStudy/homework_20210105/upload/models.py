from django.db import models

# Create your models here.

class Writing(models.Model):
    title = models.CharField(max_length=40)
    text = models.TextField()
    image = models.ImageField(upload_to="", blank=True, null=True)

class Diary(models.Model):
    title = models.CharField(max_length=40)
    #writer = models.ForeignKey('User', on_delete=models.SET_NULL, null=False)
    writtenDate = models.DateField(null=True, blank=True)

    contents = models.TextField(max_length=1000)
    #image = models.ImageField(upload_to="", blank=True, null=True)

    openPoint = models.IntegerField(default=0)
    numViews = models.IntegerField(default=0)
    numLikes = models.IntegerField(default=0)

class DiaryImage(models.Model):
    Diary = models.ForeignKey(Diary, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="", blank=True, null=True)

