from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index),
    path('group/', views.group_posts),
    path('group/<slug:slug>/', views.group_posts_slug),
    path('group_list/', views.group_list),
]