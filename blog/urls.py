from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main, name = 'main'),
    path('new_performance/', views.new_performance, name = 'new_performance'),

]