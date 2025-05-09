# バリデーションの手順
# ①user_form.is_valid():でバリデーションチェックが入る
# 具体的にはclean_メソッド名()やclean()、基本的なバリデーションを確認
# ②もしTrueならその後の処理を実行する

from django.shortcuts import render
from .forms import UserForm
# 以下はDjangoのデフォのバリデーション処理
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
# ↓↓これはDjangoのデフォルトで搭載されている、パスワードを確認かつ、再入力欄を表示してくれる
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, 

def user_list(request):
    return render(request, 'user/user_list.html'
    )

# ユーザー登録処理
def regist(request):
    # user_form = UserForm(request.POST or None)
    # if user_form.is_valid():
    #     # commit=Falseとしているのはハッシュ化してから保存したため！
    #     user = user_form.save(commit=False)
    #     password = user_form.cleaned_data.get('password', '')
    #     try:
    #          validate_password(password)
    #     except ValidationError as e:
    #         user_form.add_error('password', e)
    #     #パスワードをハッシュ化
    #     user.set_password(password)
    #     user.save()
    user_form = UserCreationForm(request.POST or None)
    if user_form.is_valid():
        user_form.save()
    return render(request, 'user/registration.html', context={
        'user_form': user_form,
    })

# ユーザーが入力した後のパスワードの処理
def login_view(request):
    login_view = UserLoginForm
    #Udemyの201の途中から！！！！！！！！！