# Generated by Django 2.1.5 on 2021-09-16 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('message', models.TextField(max_length=250, null=True)),
            ],
        ),
    ]