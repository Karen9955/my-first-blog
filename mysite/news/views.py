from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from.models import News


def index(request):
    news = News.objects.order_by('-created_at')
    return render(request, 'news/index2.html', {'news': news, 'title': 'Список новостей'})

