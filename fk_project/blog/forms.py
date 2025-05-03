# fk_project/blog/forms.py

from django import forms
from .models import Article, Post

# フォームを簡単に表示させるものを定義
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'category']

# ModelFormの練習用
class PostModelForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
        
