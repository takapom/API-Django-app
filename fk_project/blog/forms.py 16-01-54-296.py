from django import forms
from .models import Article

# フォームのモデル作成
class ArticleForm(forms.ModelForm):
     class Meta:
          model = Article
          fields = ['title', 'content', 'category']

