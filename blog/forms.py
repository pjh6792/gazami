from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['show_title', 
         'show_poster' , 'show_start_date', 'show_end_date',  'show_time', 'show_place', 
         'ticket_start_date','ticket_end_date' ,'ticket_price', 
         'ticket_amount', 'bankname', 'account', 
         'opendate', 
         'closedate', 'canceldate', 
         'show_info_text', 'show_info_image',
        ]