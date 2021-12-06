from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Post, Group

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

def group_posts(request,slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context) 

def group_posts_slug(request, slug):
    return HttpResponse("Да выложим мы посты, выложим!!!")

