class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __str__(self):
        return f'この本のタイトルは{self.name}、著者は{self.author}です！'
    
book1 = Book('たかぽんの冒険', 'たかぽん')
book2 = Book('Python入門', 'たかぽん先生')
book3 = Book('未来への扉', 'ゆうき先生')

print(book1)
print(book2)
print(book3)
