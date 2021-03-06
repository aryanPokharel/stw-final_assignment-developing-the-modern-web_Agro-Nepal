# Generated by Django 2.1.5 on 2021-09-10 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=150)),
                ('rate', models.FloatField(default=10.1)),
                ('status', models.CharField(choices=[('available', 'available'), ('unavailable', 'unavailable')], default='1', max_length=20)),
            ],
        ),
    ]
