from django.db import models
from datetime import date
from django.utils.timezone import now


# Create your models here.
class Order(models.Model):
    now = now()

    order_id = models.BigAutoField(primary_key=True)
    item_type = models.CharField(max_length=200, null=False)
    item_name = models.CharField(max_length=200)
    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField(max_length=200)
    order_date = models.DateField(auto_now_add=True)
    total_price = models.FloatField(default=0)
    quantity = models.IntegerField(default=1)
    remarks = models.TextField(max_length=250, null=True)
