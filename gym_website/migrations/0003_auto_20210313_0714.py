# Generated by Django 3.1.7 on 2021-03-13 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_website', '0002_freetrial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freetrial',
            name='photo',
            field=models.ImageField(blank=True, upload_to='media/trialPhoto/'),
        ),
    ]
