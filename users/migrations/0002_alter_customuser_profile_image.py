# Generated by Django 4.2.7 on 2023-11-17 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_image',
            field=models.ImageField(upload_to='images/profile_pictures'),
        ),
    ]