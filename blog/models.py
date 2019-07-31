from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    show_title = models.CharField(default = '', max_length=200)
    show_poster = models.ImageField(upload_to='images/', blank=True)
    show_date = models.DateField(default = '')
    show_time = models.TextField(default = '')
    show_place = models.TextField(default = '')
    post_author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    ticket_date = models.TextField(default = '')
    ticket_price = models.BigIntegerField()
 #   ticket_price = models.DecimalField(default = 0, max_digits=6, decimal_places=0)
    ticket_amount = models.BigIntegerField()
    bankname = models.CharField(default = '', max_length=200)
 #   account = models.DecimalField(default = 0, max_digits=20, decimal_places=0)
    account = models.BigIntegerField()
    opendate = models.DateTimeField(default = '')
    closedate = models.DateTimeField(default = '')
    canceldate = models.DateTimeField(default = '')
    show_info_text = models.TextField(default = '')
    show_info_image = models.ImageField(upload_to='images/', blank=True)
