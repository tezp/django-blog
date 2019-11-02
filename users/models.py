from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(default='default.jpg', upload_to='Profile_Pics')

    def __str__(self):
        return "{} profile".format(self.user.username)

    def save(self):
        super().save()

        profile_pic = Image.open(self.img.path)
        if profile_pic.height > 300 or profile_pic.width > 300:
            size = (300, 300)
            profile_pic.thumbnail(size)
            profile_pic.save(self.img.path)
