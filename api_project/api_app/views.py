# ビューセットはCRUD操作のまとめをしている
from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer

# ModelViewSetのおかげでNext.js側でPOSTやDELETEをmethodにするだけでCRUD操作ができるようになる
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    