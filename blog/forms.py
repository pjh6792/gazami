from django import forms
from .models import Post, Comment, Ticket

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['show_title', 
         'show_poster' , 'show_start_date', 'show_end_date',  'show_time', 'show_place', 
         'ticket_date_1', 'ticket_date_2', 'ticket_date_3', 'ticket_date_4', 
         #'ticket_date_5',
        'ticket_price_1', 
         'ticket_price_2' ,
   #      'ticket_price_3',
         'ticket_price_3',
         'ticket_price_4', 
    #     'ticket_price_5',
     #   'ticket_price_5',
     #   'ticket_price_5',
         'ticket_amount_1',   'ticket_amount_2',  'ticket_amount_3',  'ticket_amount_4',  
         #'ticket_amount_5',
         'bankname', 'account', 
         'opendate', 
         'closedate', 'canceldate', 
         'show_info_text', 'show_info_image',
        ]
        


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content',]

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['count', 't_choice',]

