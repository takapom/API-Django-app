from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    complated = models.BooleanField(default=False)

    class  Meta:
        db_table = 'APIの練習テーブル'

    def __str__(self):
        return self.title