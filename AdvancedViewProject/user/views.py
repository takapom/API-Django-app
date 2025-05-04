from django.shortcuts import render
from .forms import UserForm
# 以下はDjangoのデフォのバリデーション処理
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

def user_list(request):
    return render(request, 'user/user_list.html'
    )

def regist(request):
    user_form = UserForm(request.POST or None)
    if user_form.is_valid():
        # commit=Falseとしているのはハッシュ化してから保存したため！
        user = user_form.save(commit=False)
        password = user_form.cleaned_data.get('password', '')
        try:
             validate_password(password)
        except ValidationError as e:
            user_form.add_error('password', e)
        user.set_password(password)
        user.save()
    return render(request, 'user/registration.html', context={
        'user_form': user_form,
    })