# Generated by Django 2.1.5 on 2021-09-19 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insiders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='insider',
            name='password',
            field=models.CharField(default=12345, max_length=100),
            preserve_default=False,
        ),
    ]