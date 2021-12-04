from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Главная страница")

def group_posts(request):
    return HttpResponse("Тут будем выкладывать посты, ожидайте...")

def group_posts_slug(request, slug):
    return HttpResponse("Да выложим мы посты, выложим!!!")

