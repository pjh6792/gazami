from django import forms
from .models import Post, Comment, Ticket

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['show_title', 
         'show_poster' , 'show_date',  'show_time', 'show_place', 
         'ticket_date', 'ticket_price', 
         'ticket_amount', 'bankname', 'account', 
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
        fields = ['count',]