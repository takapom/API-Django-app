from django.shortcuts import render
from .models import Article
from django.shortcuts import get_object_or_404


def article_list(request):
    articles = Article.objects.select_related('category')
    return render(request, 'blog/article_list.html', {'articles': articles})

    
# pk=pkの部分は左側のpkがArticleモデルのpkで右側のpkが渡ってきたpkである
# それを検索して合致するものの詳細ページに移動する
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'blog/article_detail.html', {'article': article})




