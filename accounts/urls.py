from django.urls import path
from . import views

urlpatterns = [
    path('c_signup/', views.c_signup, name='c_signup'),
    path('p_signup/', views.p_signup, name='p_signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout,  name='logout'),    
]