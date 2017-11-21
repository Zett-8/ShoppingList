from django.db import models


class Stuff(models.Model):
    title = models.CharField(max_length=100)


