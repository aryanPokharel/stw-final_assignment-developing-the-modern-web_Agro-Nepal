from django.db import models

REMARKS_CHOICES = (
    ("Epic", "Epic"),
    ("Good", "Good"),
    ("Fine", "Fine"),
    ("Bad", "Bad"),
    ("Pathetic", "Pathetic"),

)


# Create your models here.
class Feedback(models.Model):
    email = models.EmailField(max_length=100, null=False)
    name = models.CharField(max_length=100, null=False)
    message = models.TextField(max_length=250, null=True)

    remarks = models.CharField(
        max_length=20,
        choices=REMARKS_CHOICES,
        default='Good',
    )