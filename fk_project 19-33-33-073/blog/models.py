from django.db import models

# モデル作成
class Category(models.Model):
    name = models.TextField(max_length=100)

    def __str__(self):
        return self.name
    
# 記事のモデル作成
class Article(models.Model):
    title = models.TextField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title