from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['show_title', 'show_poster' , 'show_date', 
        'show_time', 'show_place', 'post_author', 'ticket_date',
        'ticket_price', 'ticket_amount', 'bankname', 'account', 
        'opendate', 'closedate', 'canceldate', 'show_info_text', 'show_info_image',
        ]