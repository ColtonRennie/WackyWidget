from django.db import models
from django.urls import reverse

class Widget(models.Model):
 description = models.CharField(max_length = 30)
 quantity = models.IntegerField()

 def __str__(self):
  return self.description
