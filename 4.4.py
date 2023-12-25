# -*- coding: utf-8 -*-

class Book:
    BOOK_TYPES = ("твердый переплет", "мягкая обложка")


    def __init__(self, title, author, pages, book_type):
        self.title = title
        self.author = author
        self.pages = pages
        if book_type in Book.BOOK_TYPES:
            self.book_type = book_type
        else:
            raise ValueError("Неправильный тип книги")


    def get_book_info(self):
        return f"{self.title} - {self.author}, {self.pages} страниц, {self.book_type}"


    @staticmethod
    def validate_isbn(isbn):

        if len(isbn) == 10 or len(isbn) == 13:
            return True
        else:
            return False


    @classmethod
    def get_hardcover_book(cls, title, author, pages):
        return cls(title, author, pages, cls.BOOK_TYPES[0])



book1 = Book("Война и мир", "Лев Толстой", 1225, "тврдый переплет")
book2 = Book.get_hardcover_book("451 градус по Фаренгейту", "Рэй Брэдбери", 256)

print(book1.get_book_info())
print(book2.get_book_info())
print(Book.validate_isbn("1234567890"))