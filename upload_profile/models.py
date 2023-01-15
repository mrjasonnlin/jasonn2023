from django.db import models
from django.utils import timezone


# Create your models here.

class Photo(models.Model):
    user_name = models.CharField(max_length=30)
    user_image = models.ImageField(upload_to='image/', blank=False, null=False)
    upload_date = models.DateField(default=timezone.now)
    introduce = models.FileField(upload_to='introduce/')

    def __str__(self):
        return self.user_name
