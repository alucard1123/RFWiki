from django.db import models


class Settings(models.Model):
    name = models.CharField(max_length=20)
