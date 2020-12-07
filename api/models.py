from django.db import models
from django.conf import settings

class InceptionImageModel(models.Model):

    image = models.ImageField(upload_to = 'images/') 