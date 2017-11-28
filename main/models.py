from django.db import models
from django.contrib.auth.models import User


class Stuff(models.Model):
    title = models.CharField(max_length=100)
    user = models.CharField(default=User, max_length=100)

    def __str__(self):
        return self.title
