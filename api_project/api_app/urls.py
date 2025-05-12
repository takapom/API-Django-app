from django.urls import path, include
from rest_framework import routers
from .views import TodoViewSet

router = routers.DefaultRouter()
router.register('todos', TodoViewSet)

#router.urlsとすると /todos/ のようなURLにアクセスしたときに、自動で TodoViewSet が呼び出されるようになります。
urlpatterns = [
    path('', include(router.urls))
]
