from django.db import models

# Create your models here.

class Writing(models.Model):
    title = models.CharField(max_length=40)
    text = models.TextField()
    image = models.ImageField(upload_to="", null=True)