from django import template
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.
def index(request):
    template = 'posts/index.html'
    return render(request, template)

def group_list(request):
    template = 'posts/group_list.html'
    return render(request, template)

def group_posts(request):
    return HttpResponse("Тут будем выкладывать посты, ожидайте...")

def group_posts_slug(request, slug):
    return HttpResponse("Да выложим мы посты, выложим!!!")

