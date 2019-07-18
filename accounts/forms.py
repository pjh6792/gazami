from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models

class c_RegisterForm(UserCreationForm):
    c_name = forms.CharField()
    c_email = forms.EmailField()
    c_phone = forms.CharField()

    class Meta:
        model = User
        fields = ['c_name', 'username', 'password1', 'password2', 
        'c_phone', 'c_email', ]

class p_RegisterForm(UserCreationForm):
    p_name = forms.CharField()
    p_email = forms.EmailField()
    p_phone = forms.CharField()
   # p_image = forms.ImageField()
   # p_information = forms.CharField(widget=forms.Textarea)
    
    class Meta:
        model = User
        fields = ['p_name', 'username', 'password1', 'password2',
        'p_phone', 'p_email', 
        #'p_image', 'p_information',
        ]

