from django.db import models

STATUS_CHOICES = (
    ("available", "available"),
    ("unavailable", "unavailable"),

)


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100, null=False)
    username = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=100, null=False)
