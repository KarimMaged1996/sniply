from django.db import models
from django.contrib.auth.models import AbstractUser
from config import settings


# Create your models here.
class CustomUser(AbstractUser):
    profile_image = models.ImageField(upload_to="images/profile_pictures")

    def append_full_url(self):
        if self.profile_image:
            return f"{settings.MEDIA_URL}{self.profile_image.url}"
