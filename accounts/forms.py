from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import models
from .models import CUser


class c_RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', #ID, 
        'first_name', 'last_name', 'email', 'password1', 'password2'
        ]

        
class cuserForm(forms.ModelForm):
    class Meta:
        model = CUser
        fields = ['check',]

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

class c_updateForm(UserChangeForm):
    c_name = forms.CharField()
    c_email = forms.EmailField()
    c_phone = forms.CharField()

    class Meta:
        model = User
        fields = ['c_name', 'c_phone', 'c_email', 
        # 'c_image',
        ]

class p_updateForm(UserChangeForm):
    p_name = forms.CharField()
    p_email = forms.EmailField()
    p_phone = forms.CharField()
   # p_image = forms.ImageField()
   # p_information = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User
        fields = ['p_name', 'p_phone', 'p_email', 
        #'p_image', 'p_information',
        ]

