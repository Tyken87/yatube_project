from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Главная страница")

def group_posts(request):
    return HttpResponse("Тут будем выкладывать посты, ожидайте...")

