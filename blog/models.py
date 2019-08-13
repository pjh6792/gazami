from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Post(models.Model):
    post_author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    show_title = models.CharField(default = '', max_length=200)
    show_poster = models.ImageField(upload_to='images/', blank=True)
    show_start_date = models.DateField(null=True, blank=True) #2019-07-31 이런식으로 적어야함 
    show_end_date = models.DateField(null=True, blank=True)
  # show_date = models.DateField(null=True, blank=True)
    show_time = models.TextField(default = '')
    show_place = models.TextField(default = '')
    ticket_date_1 = models.DateTimeField(null=True, blank=True)
    ticket_date_2 = models.DateTimeField(null=True, blank=True)
    ticket_date_3 = models.DateTimeField(null=True, blank=True)
    ticket_date_4 = models.DateTimeField(null=True, blank=True)
   # ticket_date_5 = models.DateTimeField(null=True, blank=True)

    # ticket_date = ArrayField(models.DateField(blank=True), default = list)
    # ticket_date = models.TextField(default = '')    
    ticket_price_1 = models.BigIntegerField(default = '')
    ticket_price_2 = models.BigIntegerField(default = '')
    #ticket_price_3 = models.BigIntegerField(default = '')
    ticket_price_3 = models.BigIntegerField(default = '')
    ticket_price_4 = models.BigIntegerField(default = '')
   # ticket_price_5 = models.BigIntegerField(default = '')
    #ticket_price_5 = models.BigIntegerField(default = '')
   # ticket_price_5 = models.BigIntegerField(default='')
    ticket_amount_1 = models.BigIntegerField(default = '')
    ticket_amount_2 = models.BigIntegerField(default = '')
    ticket_amount_3 = models.BigIntegerField(default = '')
    ticket_amount_4 = models.BigIntegerField(default = '')
   # ticket_amount_5 = models.BigIntegerField(default = '')

    
    bankname = models.CharField(default = '', max_length=200)
    account = models.BigIntegerField(default = '')
    opendate = models.DateField(null=True, blank=True)
    closedate = models.DateField(null=True, blank=True)
    canceldate = models.DateField(null=True, blank=True)
    show_info_text = models.TextField(default = '')
    show_info_image = models.ImageField(upload_to='images/', blank=True)




class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    content = models.CharField(max_length=300)
    timestamp = models.DateTimeField(default=timezone.now)

class Ticket(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) #예매하는 공연정보
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) #예매자정보
    count = models.IntegerField(default = '1') #티켓 매수
    timestamp = models.DateTimeField(default=timezone.now)
    T1 = 'Post.ticket_date_1'
    T2 = 'Ticket2'
    TICKET_CHOICES = [
        (T1,'c1'),
        (T2, 'Sophomore'),
    ]
    t_choice = models.CharField(
        max_length=100,
        choices=TICKET_CHOICES,
        default=T1,
    )