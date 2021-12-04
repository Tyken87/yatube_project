from django.urls import path

from . import views

urlpattern = [
    path('', views.index),
    #path('group/', views.group_posts),
]