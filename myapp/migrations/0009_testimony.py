# Generated by Django 3.2.8 on 2021-10-18 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_portfolio_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimony',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/img')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.TextField()),
            ],
        ),
    ]
