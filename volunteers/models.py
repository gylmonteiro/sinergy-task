from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class VoluntaryUser(AbstractUser):
    type = models.CharField(max_length=255, verbose_name='tipo', blank=True, null=True)

    def __str__(self):
        return self.username
    

