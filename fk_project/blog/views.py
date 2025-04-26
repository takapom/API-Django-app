from django.shortcuts import render, redirect
from .models import Article, Reminder
from django.shortcuts import get_object_or_404
from .forms import ArticleForm


def article_list(request):
    articles = Article.objects.select_related('category')
    return render(request, 'blog/article_list.html', {'articles': articles})

    
# pk=pkの部分は左側のpkがArticleモデルのpkで右側のpkが渡ってきたpkである
# それを検索して合致するものの詳細ページに移動する
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)

    try:
        reminder = Reminder.objects.get(memo=article)
    except Reminder.DoesNotExist:
        reminder = None

    return render(request, 'blog/article_detail.html', {
        'article': article,
        'reminder': reminder,
        })

# 入力欄のviewを定義
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ArticleForm()
    return render(request, 'blog/article_form.html', {'form': form})


# 削除処理を定義
def article_delete(request, pk):
    article = get_object_or_404(Article ,pk=pk)
    article.delete()
    return redirect('article_list') #トップページへ遷移

