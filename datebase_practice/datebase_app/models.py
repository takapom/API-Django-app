from django.db import models

# 著者のデータベースのモデルを定義
class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

# 本のデータベースのモデルを定義
class Book(models.Model):
    title = models.CharField(max_length=50)
    publish_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



