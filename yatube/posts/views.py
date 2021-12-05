from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'title': 'Главная страница',
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)

def group_list(request):
    template = 'posts/group_list.html'
    return render(request, template)

def group_posts(request):
    template = 'posts/index.html'
    text = "Здесь будет информация о группах проекта Yatube"
    context = {
        'title': 'Информация о группах',
        'text' : text,
    }
    return render(request, template, context)

def group_posts_slug(request, slug):
    return HttpResponse("Да выложим мы посты, выложим!!!")

