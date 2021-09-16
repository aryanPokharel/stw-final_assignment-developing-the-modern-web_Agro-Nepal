# Generated by Django 2.1.5 on 2021-09-12 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField(default=100.55, null=True)),
                ('image', models.FileField(null=True, upload_to='static/uploads')),
                ('description', models.TextField(max_length=200, null=True)),
                ('status', models.CharField(choices=[('available', 'available'), ('unavailable', 'unavailable')], default='available', max_length=20)),
            ],
        ),
    ]