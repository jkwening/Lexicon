from django.db import models

# Create your models here.
class Dictionary(models.Model):
  word = models.CharField(max_length=50)
  definition = models.TextField()
  part_of_speech = models.CharField(max_length=50)
