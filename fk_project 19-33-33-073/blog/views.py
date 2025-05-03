from django.shortcuts import render
from .models import Article

def article_list(request):
    articles = Article.objects.select_related('category')
    return render(request, 'blog/article_list', {'articles': articles})

