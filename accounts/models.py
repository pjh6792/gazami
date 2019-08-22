from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from blog import models as mo

class CUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    check = models.BooleanField(default = True)
    c_phone = models.CharField(max_length=11, default="")
    post = models.ForeignKey(mo.Post , on_delete=models.CASCADE, null=True, blank=True)

class PUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    check = models.BooleanField(default = False)
    p_phone = models.CharField(max_length=11, default="")
   # p_image = forms.ImageField()
   # p_information = forms.CharField(widget=forms.Textarea)
    


