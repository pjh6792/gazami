from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class CUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    check = models.BooleanField(default = True)

class PUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    check = models.BooleanField(default = False)

