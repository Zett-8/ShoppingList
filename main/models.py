from django.db import models
from django.contrib.auth.models import User


class Stuff(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.user
