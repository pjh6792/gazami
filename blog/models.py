from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from datetime import date, datetime
from django.conf import settings
from accounts import models as mo
# Create your models here.

class Post(models.Model):
    post_author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    show_title = models.CharField(default = '', max_length=200)
    show_poster = models.ImageField(upload_to='images/', blank=True)
    show_start_date = models.DateField(null=True, blank=True) #2019-07-31 이런식으로 적어야함 
    show_end_date = models.DateField(null=True, blank=True)
    show_time = models.TextField(default = '')
    show_place = models.TextField(default = '')
    ticket_date_1 = models.DateTimeField(null=True, blank=True)
    ticket_date_2 = models.DateTimeField(null=True, blank=True)
    ticket_date_3 = models.DateTimeField(null=True, blank=True)
    ticket_date_4 = models.DateTimeField(null=True, blank=True)
   # ticket_date_5 = models.DateTimeField(null=True, blank=True)

    # ticket_date = ArrayField(models.DateField(blank=True), default = list)
    # ticket_date = models.TextField(default = '')    
    ticket_price_1 = models.BigIntegerField(null=True, blank=True)
    ticket_price_2 = models.BigIntegerField(null=True, blank=True)
    #ticket_price_3 = models.BigIntegerField(default = '')
    ticket_price_3 = models.BigIntegerField(null=True, blank=True)
    ticket_price_4 = models.BigIntegerField(null=True, blank=True)
   # ticket_price_5 = models.BigIntegerField(default = '')
    #ticket_price_5 = models.BigIntegerField(default = '')
   # ticket_price_5 = models.BigIntegerField(default='')
    ticket_amount_1 = models.BigIntegerField(null=True, blank=True)
    ticket_amount_2 = models.BigIntegerField(null=True, blank=True)
    ticket_amount_3 = models.BigIntegerField(null=True, blank=True)
    ticket_amount_4 = models.BigIntegerField(null=True, blank=True)
   # ticket_amount_5 = models.BigIntegerField(default = '')

    
    bankname = models.CharField(default = '', max_length=200)
    account = models.BigIntegerField()
    opendate = models.DateField(null=True, blank=True)
    closedate = models.DateField(null=True, blank=True)
    canceldate = models.DateField(null=True, blank=True)
    show_info_text = models.TextField(default = '', null=True, blank=True)
    show_info_image = models.ImageField(upload_to='images/', blank=True)

    approve = models.BooleanField(default="False") #관리자승인용 False:미승인 True:승인
    # like_user_set = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='like_user_set')
    
    # def like_count(self):
    #     return self.like_user_set.count()
    
class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)




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
    T1 = 'ticket1'
    T2 = 'ticket2'
    T3 = 'ticket3'
    T4 = 'ticket4'
    TICKET_CHOICES = [
        (T1, 'c1'),
        (T2, 'c2'),
        (T3, 'c3'),
        (T4, 'c4'),
    ]
    t_choice = models.CharField(
        max_length=100,
        choices=TICKET_CHOICES,
        default=T1,
    )

class CanceledTicket(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) #예매한 공연정보
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) #예매자정보
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE) #취소 티켓정보
    refund_bank = models.CharField(default = '', max_length=200) #환불계좌은행
    refund_account = models.BigIntegerField() #환불계좌번호
