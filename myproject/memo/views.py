from django.shortcuts import render, redirect, get_object_or_404 #HTMLを表示する道具
from .models import Memo
from .forms import MemoForm

# 保存ボタンを押された時の処理
def memo_view(request):
    if request.method == 'POST':
        form = MemoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('memo')
    else:
        form = MemoForm()

    memos = Memo.objects.all()
    return render(request, 'memo/memo.html', {'form': form, 'memos': memos})

# 削除の処理を定義
def delete_memo(request, memo_id):
    memo = get_object_or_404(Memo, id=memo_id)
    memo.delete()
    return redirect('memo') #memoはurls.pyで書いたトップページのこと(nameで定義している)

