# Generated by Django 2.1.5 on 2021-09-20 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('item_type', models.CharField(max_length=200)),
                ('item_name', models.CharField(max_length=200)),
                ('customer_name', models.CharField(max_length=200)),
                ('order_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]