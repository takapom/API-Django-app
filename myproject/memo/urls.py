from django.urls import path 
from . import views

urlpatterns = [
    # 「/」にアクセスしたらmemo_listに表示
    path('', views.memo_view, name='memo'), 
    path('delete/<int:memo_id>', views.delete_memo, name='delete_memo'),
]
