# Generated by Django 3.2.8 on 2021-10-17 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('car_1', models.CharField(max_length=50)),
                ('car_2', models.CharField(max_length=50)),
                ('car_3', models.CharField(blank=True, max_length=50)),
                ('car_4', models.CharField(blank=True, max_length=50)),
                ('image_field', models.ImageField(upload_to='')),
            ],
        ),
    ]
