from django.db import models

# データベースモデル定義
class Todo(models.Model):
    name = models.CharField(max_length=100)
    complated = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    