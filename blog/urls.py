from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main, name = 'main'),
    path('new_performance/', views.new_performance, name = 'new_performance'),
    path('c_mypage/',views.c_mypage, name='c_mypage'),
    path('p_mypage/',views.p_mypage, name='p_mypage'),
]