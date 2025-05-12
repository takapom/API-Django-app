# バリデーションの手順
# ①user_form.is_valid():でバリデーションチェックが入る
# 具体的にはclean_メソッド名()やclean()、基本的なバリデーションを確認
# ②もしTrueならその後の処理を実行する

from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm, UserLoginForm, RequestPasswordResetForm, SetNewPasswordForm
# 以下はDjangoのデフォのバリデーション処理
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
# ↓↓これはDjangoのデフォルトで搭載されている、パスワードを確認かつ、再入力欄を表示してくれる
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import PasswordResetToken
import uuid

# ユーザー一覧ページを表示させる✅
def user_list(request):
    return render(request, 'user/user_list.html'
    )

# ユーザー登録処理✅
def regist(request):
    user_form = UserCreationForm(request.POST or None)
    if user_form.is_valid():
        user_form.save()
    return render(request, 'user/registration.html', context={
        'user_form': user_form,
    })

#　ログイン処理✅
def login_view(request):
    login_form = UserLoginForm(request.POST or None)
    if login_form.is_valid():
        #usernameとpassword1のバリデーション後の値を代入
        username = login_form.cleaned_data.get(('username'))
        password = login_form.cleaned_data.get("password1")
        #authenticateはDjangoのデフォルトの関数
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
    return render(request, 'user/login.html', context={
        'login_form': login_form,
    })

#ログイン後のユーザーのページに遷移処理✅
@login_required
def info(request):
    print(request.user)
    return render(request, 'user/info.html')

#ログアウト処理✅
@login_required
def logout_view(request):
    logout(request)
    return redirect('user:login')

#ログアウト後のページ表示✅
def index(request):
    print(request.user)
    return render(request, 'user/index.html')

# パスワードリセットのリクエストを処理する関数
def request_password_reset(request):
    # RequestPasswordResetFormはパスワードリセットのリクエストを処理や
    # リセットメールの送信を行う
    form = PasswordResetForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data['email']
        #Userはデータベースからemailが一致するユーザーが欲しい(userの検索)
        user = get_object_or_404(User, email=email)
        # 新しいトークンを作成
        # createdがtrueの場合、そのユーザーが初めてパスワードリセットを要求したと言うこと
        #createdがfalseの場合、そのユーザーが以前パスワードをリセットしたと言うこと→if文入り、以前のトークンを更新する処理
        password_reset_token, created = PasswordResetToken.objects.get_or_create(user=user)
        if not created:
            password_reset_token.token = uuid.uuid4()
            password_reset_token.used = False
            password_reset_token.save()
        user.is_active = False
        user.save()
        print(password_reset_token.token)
    return render(request, 'user/password_reset_form.html', context={
        'reset_form': form,
    })

# リセットトークンのURLに対してviewの定義
def reset_password(request, token):
    password_reset_token = get_object_or_404(
        PasswordResetToken,
        token=token,
        used=False,
    )

    form = SetNewPasswordForm(request.POST or None
                              )
    return render(request, 'user/password_reset_confirm.html')








# 以下はバリデーションの内部の仕組み

# フォーム送信
# ↓
# is_valid()が呼ばれる
# ↓
# 基本的なバリデーション（メールアドレスの形式など）
# ↓
# cleaned_dataが生成される
# ↓
# clean_email()が呼ばれる
# ↓
# 追加のバリデーション