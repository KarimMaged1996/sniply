# Generated by Django 4.2.7 on 2023-11-17 12:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import snippets.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.UUIDField(default=snippets.models.short_uuid, primary_key=True, serialize=False, unique=True)),
                ('language', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]