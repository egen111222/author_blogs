from .models import Article
from django.shortcuts import render


def check_articles(get_response): # перевірка наявності статтей ()приймає відпоаівдь
    def middleware(request):              # дія яка є фільтром
        if len(Article.objects.all()) > 0:
            response = get_response(request)  # виконати дію з файлу views.py
        else:
            return render(request,'sorry.html')
        return response
    return middleware













