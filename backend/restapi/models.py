from django.db import models

# Create your models here.

class Todo(models.Model):
    id = models.IntegerField(primary_key = True)
    title = models.CharField(max_length=30)
    complete = models.BooleanField()
