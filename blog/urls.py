from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main, name = 'main'),
    path('new_performance/', views.new_performance, name = 'new_performance'),
    path('performance/<int:index>',views.performance, name='performance'),
    path('pay/<int:index>',views.pay, name='pay'),
    path('p_detail/<int:index>',views.p_detail, name='p_detail'),
    path('c_mypage/',views.c_mypage, name='c_mypage'),
    path('p_mypage/',views.p_mypage, name='p_mypage'),
    # path('performance/<pk>/likes/', views.like, name='likes'),
    path('performance/<int:index>/like', views.post_like, name = 'post_like'),
]