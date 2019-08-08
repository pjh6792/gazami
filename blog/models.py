from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    post_author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    show_title = models.CharField(default = '', max_length=200)
    show_poster = models.ImageField(upload_to='images/', blank=True)
    #show_date = models.DateField(null=True, blank=True) #2019-07-31 이런식으로 적어야함
    show_start_date = models.TextField(default='')
    show_end_date = models.TextField(default='')
    show_time = models.TextField(default = '')
    show_place = models.TextField(default = '')
    #ticket_date = models.TextField(default = '')
    ticket_start_date = models.TextField(default='')
    ticket_end_date = models.TextField(default='')
    ticket_price = models.BigIntegerField(default = '')
    ticket_amount = models.BigIntegerField(default = '')
    bankname = models.CharField(default = '', max_length=200)
    account = models.BigIntegerField(default = '')
    opendate = models.DateField(null=True, blank=True)
    closedate = models.DateField(null=True, blank=True)
    canceldate = models.DateField(null=True, blank=True)
    show_info_text = models.TextField(default = '', blank=True)
    show_info_image = models.ImageField(upload_to='images/', blank=True)

#Class Ticket(models.Model):
#    ticket_start_date = models.CharField(default = '', max_length=100)
#    ticket_end_date = models.CharFIeld(default = '', max_length=100)
#    ticket_price = models.BigIntegerField(default = '')
    