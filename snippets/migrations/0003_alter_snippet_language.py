# Generated by Django 4.2.7 on 2023-11-17 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_alter_snippet_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='language',
            field=models.CharField(choices=[('javascript', 'JavaScript'), ('python', 'Python'), ('java', 'Java'), ('c', 'C'), ('c++', 'C++'), ('c#', 'C#')], max_length=100),
        ),
    ]
