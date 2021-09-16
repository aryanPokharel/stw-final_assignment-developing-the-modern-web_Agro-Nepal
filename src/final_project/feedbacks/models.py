from django.db import models
from django import forms

REMARKS_CHOICES = [
    ("Epic", "Epic"),
    ("Good", "Good"),
    ("Fine", "Fine"),
    ("Bad", "Bad"),
    ("Pathetic", "Pathetic"),

]


# Create your models here.
class Feedback(models.Model):
    email = models.EmailField(max_length=100, null=False)
    name = models.CharField(max_length=100, null=True)
    message = models.TextField(max_length=250, null=False)

    remarks = models.CharField(
         max_length=40,
         choices=REMARKS_CHOICES,
         default='Good',
     )
    # remarks = forms.RadioSelect(choices=REMARKS_CHOICES, )
