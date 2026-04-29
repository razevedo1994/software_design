from book import Book
from attributes import Attributes


class Catalogue:
    def __init__(self):
        self._booklist = []

    def add(self, attrs):
        self._booklist.append(Book(attrs))

    def find(self, target_attrs):
        return [
            book for book in self._booklist if book.attributes.is_match(target_attrs)
        ]
