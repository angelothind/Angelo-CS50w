class Book():
    def __init__(self, genre, author, title):
        self.genre = genre
        self.author = author
        self.title = title

book1 = Book("Horror","Stephen King", "The Shining")

print(book1.author)
print(book1.title)