from django.shortcuts import render
from .models import Items

# それぞれのアイテムを表示させる処理
def item_list(request):
    items = Items.objects.all()
    return render(
        request, 'store/item_list.html', context={
            'items':items
        }
    )

# 詳細ページを表示させる処理
def item_detail(request, id):
    item = Items.objects.get(pk=id)
    return render(request, 'store/item_detail.html', context={
        'item':item
    })