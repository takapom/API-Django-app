from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# sqliteのauth_userに格納される！
class UserForm(forms.ModelForm):

    class Meta():
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput
        }

# ログイン用の入力フォーム
class UserLoginForm(forms.Form):
    username = forms.CharField(label='ユーザー名' ,max_length=255)
    password1 = forms.CharField(
        label='パスワード', max_length=50, widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label="パスワード(再)", max_length=50, widget=forms.PasswordInput
    )

     #バリデーション
    def clean(self):
        cleaned_date = super().clean()
        password1 = cleaned_date.get('password1')
        password2 = cleaned_date.get('password2')
        if password1 != password2:
            raise ValidationError
        return cleaned_date