from django.db import models

# カテゴリモデル処理を定義
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# 1対1の練習のため、リマインダー機能の処理を定義
class Reminder(models.Model):
    memo = models.OneToOneField(Article ,on_delete=models.CASCADE)
    remind_at = models.DateTimeField()

    def __str__(self):
        return f'{self.memo.content}を{self.remind_at}にリマインド'

# ModelsFormの勉強用
class Post(models.Model):
    name = models.CharField(max_length=10)
    title = models.CharField(max_length=255)
    memo = models.CharField(max_length=255)