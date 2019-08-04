from django.urls import path
from . import views

urlpatterns = [
    path('c_signup/', views.c_signup, name='c_signup'),
    path('p_signup/', views.p_signup, name='p_signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout,  name='logout'),    
    path('c_update/',views.c_update, name='c_update'),
    path('p_update/',views.p_update, name='p_update'),
]