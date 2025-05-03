from django.shortcuts import render, redirect
from .models import Memo
from .models import MemoForm

# リクエストがあった時の処理
def memo_view(request):
    if request.method == "POST":
        form = MemoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MemoForm()

    memos = Memo.objects.all()
    return render(request, 'forign_key_app/forign.html', {'form': form, 'memos': memos})

