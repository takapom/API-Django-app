# fk_project/blog/forms.py

from django import forms
from .models import Article

# フォームを簡単に表示させるものを定義
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'category']