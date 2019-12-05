from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Artist(models.Model):
    user = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
