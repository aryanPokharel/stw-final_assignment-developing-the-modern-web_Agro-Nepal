# Generated by Django 2.1.5 on 2021-09-11 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0002_auto_20210910_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='rate',
            field=models.FloatField(default=10.1, null=True),
        ),
    ]
