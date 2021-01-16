from django.db import models
import uuid

# Create your models here.

from uuid import uuid4
from datetime import datetime

def get_file_path(instance, filename):
    ymd_path = datetime.now().strftime('%Y%m%d') 
    uuid_name = uuid4().hex
    return '/'.join([ymd_path, uuid_name])

class Diary(models.Model):

    ##FIELDS##

    diaryKey = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    title = models.CharField(max_length=40)
    content = models.TextField(max_length=2000)

    testImage = models.ImageField(upload_to=get_file_path, null=True)

    writtenDate = models.DateField(auto_now_add=True, null=True)
    openPoint = models.IntegerField()
    numView = models.IntegerField(default=0)
    numLike = models.IntegerField(default=0)

    ##METHOD##

    def __str__ (self):
        return self.diaryKey

