from django import forms #Djangoのフォーム用の機能を読み込む
from .models import Memo #同じアプリ内のMemoモデルを読み込む

# モデルに基づいたフォームを作るクラスを定義
# これがないとビューやテンプレートでフォームとして使えないため
class MemoForm(forms.ModelForm):
    class Meta:
        model = Memo
        fields = ['content']


