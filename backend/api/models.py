from django.db import models

# Create your models here.
class Dictionary(models.Model):
  word = models.CharField(max_length=50, primary_key=True)
  definition = models.TextField()
  part_of_speech = models.CharField(max_length=50)

  class Meta:
    db_table = 'dictionary' # override database table name
