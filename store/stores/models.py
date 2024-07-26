from django.db import models

class DocModel(models.Model):
    name = models.CharField(max_length=255)
    doc = models.FileField(upload_to='docs/')
