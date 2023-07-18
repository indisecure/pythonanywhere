from django.db import models

class File(models.Model):
    file=models.FileField()
    class Meta:
        ordering=['id']
