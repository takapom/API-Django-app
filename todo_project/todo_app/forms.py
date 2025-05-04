from django import forms
from .models import Todo
from django.core.exceptions import ValidationError

# 数字禁止のバリを定義
# valueはフォームで入力された値が入ってくる
def no_digits(value):
    if any(char.isdigit() for char in value):
        raise ValidationError("数字は含めないでね！")
    
# フォームモデルを定義
class TodoForm(forms.ModelForm):
    title = forms.CharField(
        max_length=100,
        validators=[no_digits],
        label='タスク名'
    )

    class Meta:
        model = Todo
        fields = '__all__'