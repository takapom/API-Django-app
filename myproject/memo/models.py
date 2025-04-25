from django.db import models

#データベースの構造を定義
class Memo(models.Model):
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)