from django.shortcuts import render, redirect
from .models import Article
from django.shortcuts import get_object_or_404
from .forms import ArticleForm


def article_list(request):
    articles = Article.objects.select_related('category')
    return render(request, 'blog/article_list.html', {'articles': articles})

    
# pk=pkの部分は左側のpkがArticleモデルのpkで右側のpkが渡ってきたpkである
# それを検索して合致するものの詳細ページに移動する
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'blog/article_detail.html', {'article': article})

# 入力欄のviewを定義
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ArticleForm()
    return render(request, 'blog/article_form.html', {'form': form})
