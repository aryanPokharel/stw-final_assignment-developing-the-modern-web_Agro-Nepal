from django.db import models

STATUS_CHOICES = (
    ("available", "available"),
    ("unavailable", "unavailable"),

)

# Create your models here.
class Worker(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=150)
    rate = models.FloatField(default=10.10)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='available'
    )


