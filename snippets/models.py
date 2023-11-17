from django.db import models
from users.models import CustomUser
import uuid


def short_uuid():
    full_uuid = uuid.uuid4()
    short_uuid = str(full_uuid)[:6]
    return short_uuid


# Create your models here.
class Snippet(models.Model):
    id = models.CharField(
        primary_key=True, unique=True, default=short_uuid, max_length=6
    )
    language = models.CharField(max_length=100)
    body = models.TextField()
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # ensure that id is unique
        if not self.id:
            self.id = short_uuid()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.id} - {self.language}"
