from book import Book


class Catalogue:
    @staticmethod
    def _equal_ignore_case(targe_str: str, other_str: str):
        if len(targe_str) == 0:
            return True
        else:
            return targe_str.casefold() == other_str.casefold()

    def __init__(self):
        self._booklist = []

    def add(self, title: str, last: str, first: str):
        book = Book(title, last, first)
        self._booklist.append(book)

    def _is_match(self, book, target):
        return (
            Catalogue._equal_ignore_case(target.title, book.title)
            and Catalogue._equal_ignore_case(target.last, book.last)
            and Catalogue._equal_ignore_case(target.first, book.first)
        )

    def find(self, target):
        return [book for book in self._booklist if self._is_match(book, target)]
